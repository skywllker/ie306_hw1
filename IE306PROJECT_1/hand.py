import random
import math
import heapq
import pandas as pd
from IPython.display import display, HTML

# Set the group-specific parameters
LAMBDA = 1.0  # Arrival rate (patients/hour)
MU_T = 1.0/3.0  # Triage nurse service rate = 0.333333333 (patients/hour)
MU_S = 0.16  # Stable patient home healing rate (patients/hour)
MU_CB = 0.153061224  # Critical patient hospital healing rate (patients/hour)
ALPHA_MIN = 1.25  # Min value for alpha uniform distribution
ALPHA_MAX = 1.75  # Max value for alpha uniform distribution
P1 = 0.25  # Probability of stable condition
P2 = 1.0 - P1  # Probability of critical condition
S = 4  # Number of triage nurses (Group 36)
K = 7  # Number of hospital beds (Group 36)

# Set the group-specific random seed
GROUP_SEED = 4040800288  # Sum of group members' student IDs
random.seed(GROUP_SEED)

# --- Random Variable Generation Functions ---

def GenerateInterarrival():
    """Generates exponential interarrival times for patients."""
    u = random.random()
    return -math.log(u) / LAMBDA

def GenerateNurseServiceTime():
    """Generates exponential service times for triage nurses."""
    u = random.random()
    return -math.log(u) / MU_T

def GenerateHospitalHealingTime():
    """Generates exponential healing times for patients in hospital beds."""
    u = random.random()
    return -math.log(u) / MU_CB

def GenerateHomeHealingTime(condition):
    """Generates exponential healing times for patients healing at home."""
    u = random.random()
    if condition == 's':
        return -math.log(u) / MU_S
    elif condition == 'c':
        alpha = random.uniform(ALPHA_MIN, ALPHA_MAX)
        mu_ch_effective = MU_CB / alpha
        return -math.log(u) / mu_ch_effective
    else:
        raise ValueError("Condition must be 's' (stable) or 'c' (critical)")

# --- State Tracking ---
sim_state = {
    'Clock': 0.0,
    'FEL': [],  # Future Event List (Priority Queue)
    'TriageQueue': [],
    'BusyNurses': 0,
    'OccupiedBeds': 0,
    'NextPatientID': 1,
    'Patients': {},  # Dictionary to store patient data
    # Stats Accumulators
    'TotalPatientsArrived': 0,
    'TotalPatientsHealed': 0,
    'TotalPatientsRejected': 0,
    'TotalHomeTreated': 0,
}

def ScheduleEvent(time, event_type, patient_id=None):
    """Adds an event to the Future Event List (FEL)."""
    heapq.heappush(sim_state['FEL'], (time, event_type, patient_id))

# --- Initialize the simulation ---
# Schedule the first arrival
first_arrival_time = GenerateInterarrival()
ScheduleEvent(first_arrival_time, "Arrival")

# --- Hand Simulation Table Setup ---
simulation_records = []

# --- Helper functions for hand simulation ---
def get_fel_info():
    """Format the FEL for display in the table"""
    if not sim_state['FEL']:
        return "Empty"
    fel_info = []
    for time, event_type, patient_id in sorted(sim_state['FEL']):
        if patient_id is None:
            fel_info.append(f"{event_type} at {time:.4f}")
        else:
            fel_info.append(f"{event_type} (Patient {patient_id}) at {time:.4f}")
    return fel_info

def record_state(event_description):
    """Record the current simulation state to our records table"""
    record = {
        'Time': sim_state['Clock'],
        'Event': event_description,
        'FEL': get_fel_info(),
        'Triage Queue': len(sim_state['TriageQueue']),
        'Busy Nurses': sim_state['BusyNurses'],
        'Occupied Beds': sim_state['OccupiedBeds'],
        'Healed Patients': sim_state['TotalPatientsHealed'],
        'Status': get_patient_statuses()
    }
    simulation_records.append(record)

def get_patient_statuses():
    """Get a summary of all patients and their statuses"""
    statuses = {}
    for pid, data in sim_state['Patients'].items():
        statuses[f"P{pid}"] = data.get('Status', 'Unknown')
    return statuses

# --- Hand simulation for the first 5 healings ---

def perform_hand_simulation():
    # Continue until we have 5 healed patients
    while sim_state['TotalPatientsHealed'] < 5:
        # Get the next event from FEL
        if not sim_state['FEL']:
            break
        
        event_time, event_type, patient_id = heapq.heappop(sim_state['FEL'])
        sim_state['Clock'] = event_time
        
        # Process the event
        if event_type == "Arrival":
            # Record state before processing
            record_state(f"Arrival")
            
            # Process arrival
            sim_state['TotalPatientsArrived'] += 1
            patient_id = sim_state['NextPatientID']
            sim_state['NextPatientID'] += 1
            sim_state['Patients'][patient_id] = {'ArrivalTime': sim_state['Clock'], 'Status': 'Arrived'}
            
            # Schedule next arrival
            next_arrival_time = sim_state['Clock'] + GenerateInterarrival()
            ScheduleEvent(next_arrival_time, "Arrival")
            
            # Check nurse availability
            if sim_state['BusyNurses'] < S:
                sim_state['BusyNurses'] += 1
                sim_state['Patients'][patient_id]['Status'] = 'InTriage'
                service_time = GenerateNurseServiceTime()
                ScheduleEvent(sim_state['Clock'] + service_time, "DepartureTriage", patient_id)
            else:
                sim_state['TriageQueue'].append(patient_id)
                sim_state['Patients'][patient_id]['Status'] = 'WaitingTriage'
        
        elif event_type == "DepartureTriage":
            # Record state before processing
            record_state(f"DepartureTriage (Patient {patient_id})")
            
            # Process triage departure
            sim_state['BusyNurses'] -= 1
            
            # Determine patient condition
            condition_rand = random.random()
            if condition_rand < P1:  # Stable condition
                sim_state['Patients'][patient_id]['Condition'] = 'Stable'
                sim_state['Patients'][patient_id]['Status'] = 'HomeHealing'
                sim_state['Patients'][patient_id]['TreatmentLocation'] = 'Home'
                healing_time = GenerateHomeHealingTime('s')
                ScheduleEvent(sim_state['Clock'] + healing_time, "HomeHealingCompletion", patient_id)
                sim_state['TotalHomeTreated'] += 1
            else:  # Critical condition
                sim_state['Patients'][patient_id]['Condition'] = 'Critical'
                # Check bed availability
                if sim_state['OccupiedBeds'] < K:
                    sim_state['OccupiedBeds'] += 1
                    sim_state['Patients'][patient_id]['Status'] = 'HospitalHealing'
                    sim_state['Patients'][patient_id]['TreatmentLocation'] = 'Hospital'
                    healing_time = GenerateHospitalHealingTime()
                    ScheduleEvent(sim_state['Clock'] + healing_time, "HospitalHealingCompletion", patient_id)
                else:  # No beds available
                    sim_state['Patients'][patient_id]['Status'] = 'HomeHealingRejected'
                    sim_state['Patients'][patient_id]['TreatmentLocation'] = 'HomeRejected'
                    sim_state['TotalPatientsRejected'] += 1
                    healing_time = GenerateHomeHealingTime('c')
                    ScheduleEvent(sim_state['Clock'] + healing_time, "HomeHealingCompletion", patient_id)
                    sim_state['TotalHomeTreated'] += 1
            
            # Check triage queue
            if sim_state['TriageQueue']:
                next_patient_id = sim_state['TriageQueue'].pop(0)
                sim_state['BusyNurses'] += 1
                sim_state['Patients'][next_patient_id]['Status'] = 'InTriage'
                service_time = GenerateNurseServiceTime()
                ScheduleEvent(sim_state['Clock'] + service_time, "DepartureTriage", next_patient_id)
        
        elif event_type == "HospitalHealingCompletion":
            # Record state before processing
            record_state(f"HospitalHealingCompletion (Patient {patient_id})")
            
            # Process hospital healing completion
            sim_state['OccupiedBeds'] -= 1
            sim_state['Patients'][patient_id]['Status'] = 'Healed'
            sim_state['TotalPatientsHealed'] += 1
        
        elif event_type == "HomeHealingCompletion":
            # Record state before processing
            record_state(f"HomeHealingCompletion (Patient {patient_id})")
            
            # Process home healing completion
            sim_state['Patients'][patient_id]['Status'] = 'Healed'
            sim_state['TotalPatientsHealed'] += 1
        
        else:
            print(f"ERROR: Unknown event type '{event_type}'")

# Run the hand simulation
perform_hand_simulation()

# Create a DataFrame from the recorded simulation states
df = pd.DataFrame(simulation_records)

# Display the hand simulation table
print("Hand Simulation Table - First 5 Healings")
display(df)

# Generate the markdown content
markdown_content = """# Part 2.1: Hand Simulation Results

## Simulation Parameters
- Group: 36
- Number of Triage Nurses (S): 4
- Triage Service Rate (μ_t): 0.333333333 patients/hour
- Probability of Stable Condition (p₁): 0.25
- Number of Hospital Beds (K): 7
- Hospital Healing Rate (μ_cb): 0.153061224 patients/hour
- Random Seed: 4040800288

## Hand Simulation Table
"""

# Convert DataFrame to markdown table
markdown_content += df.to_markdown(index=False) + "\n\n"

# Add analysis
markdown_content += """
## Analysis of Hand Simulation Results

1. **Total patients arrived:** {}
2. **Total patients healed:** {}
3. **Total patients rejected due to bed unavailability:** {}
4. **Total patients treated at home:** {}
5. **Final state:** {} patients in triage queue, {} busy nurses, {} occupied beds

## Patient Journey Details
""".format(
    sim_state['TotalPatientsArrived'],
    sim_state['TotalPatientsHealed'],
    sim_state['TotalPatientsRejected'],
    sim_state['TotalHomeTreated'],
    len(sim_state['TriageQueue']),
    sim_state['BusyNurses'],
    sim_state['OccupiedBeds']
)

# Add patient details
markdown_content += "\n"
for pid, data in sorted(sim_state['Patients'].items()):
    markdown_content += "- Patient {}: {}, Condition: {}, Treatment: {}\n".format(
        pid,
        data.get('Status', 'Unknown'),
        data.get('Condition', 'Unknown'),
        data.get('TreatmentLocation', 'Unknown')
    )

# Add explanation
markdown_content += """
## Explanation of Hand Simulation Results

1. **Event Processing:** The simulation follows a discrete event model where time jumps from one event to the next, with 
   no changes occurring between events.

2. **Patient Flow:** Each patient goes through a sequence of states - arrival, waiting or direct entry to triage, 
   assessment by a nurse, then either hospital or home care depending on condition and bed availability.

3. **Rejection Dynamics:** Critical patients are rejected from hospital care when all beds are occupied, forcing them 
   to undergo home care with longer healing times.

4. **Resource Utilization:** The simulation tracks the utilization of nurses and beds throughout the process, showing 
   how resource constraints affect patient flow.

5. **Random Variables:** All service times and healing times follow exponential distributions with the specified rates, 
   creating variability in patient experiences.

This hand simulation provides a foundation for understanding how the full simulation works and validates the 
conceptual model before proceeding to the complete computational implementation.
"""

# Save to markdown file
with open('part2_1_hand.md', 'w') as f:
    f.write(markdown_content)

print("\nResults saved to part2_1_hand.md")