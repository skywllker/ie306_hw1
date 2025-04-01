import random
import math
import heapq # Using heapq for efficient priority queue (FEL)

# --- Parameters (Group 36 and Context) ---
LAMBDA = 1.0  # Arrival rate (patients/hour)
MU_T = 1.0 / 3.0  # Triage nurse service rate (patients/hour)
MU_S = 0.16  # Stable patient home healing rate (patients/hour)
MU_CB = 0.153061224  # Critical patient hospital healing rate (patients/hour)
ALPHA_MIN = 1.25 # Min value for alpha uniform distribution
ALPHA_MAX = 1.75 # Max value for alpha uniform distribution
P1 = 0.25 # Probability of stable condition
P2 = 1.0 - P1 # Probability of critical condition
S = 4 # Number of triage nurses
K = 7 # Number of hospital beds

# --- Random Variable Generation Functions (Part 1.2 Requirement) ---

def GenerateInterarrival():
  """Generates exponential interarrival times for patients."""
  u = 0
  while u == 0: u = random.random()
  return -math.log(u) / LAMBDA

def GenerateNurseServiceTime():
  """Generates exponential service times for triage nurses."""
  u = 0
  while u == 0: u = random.random()
  return -math.log(u) / MU_T

def GenerateHospitalHealingTime():
  """Generates exponential healing times for patients in hospital beds."""
  u = 0
  while u == 0: u = random.random()
  return -math.log(u) / MU_CB

def GenerateHomeHealingTime(condition):
  """Generates exponential healing times for patients healing at home."""
  u = 0
  while u == 0: u = random.random()
  if condition == 's':
    return -math.log(u) / MU_S
  elif condition == 'c':
    alpha = random.uniform(ALPHA_MIN, ALPHA_MAX)
    mu_ch_effective = MU_CB / alpha
    return -math.log(u) / mu_ch_effective
  else:
    raise ValueError("Condition must be 's' (stable) or 'c' (critical)")

# --- Process Function Definitions (Part 1.2 Requirement) ---
# These functions contain the core logic for each process.
# They assume access to a simulation state object/dictionary (sim_state)
# and an event scheduling function (ScheduleEvent) which would be
# part of the main simulation algorithm developed in Part 2.

def Arrival(sim_state, ScheduleEvent):
  """
  Executes the arrival process logic.
  Assumes sim_state contains: Clock, BusyNurses, TriageQueue, NextPatientID, Patients (dict)
  Assumes ScheduleEvent(time, event_type, patient_id=None) exists.
  """
  print(f"DEBUG: Arrival at time {sim_state['Clock']:.4f}")
  sim_state['TotalPatientsArrived'] += 1
  patient_id = sim_state['NextPatientID']
  sim_state['NextPatientID'] += 1
  sim_state['Patients'][patient_id] = {'ArrivalTime': sim_state['Clock'], 'Status': 'Arrived'}

  # Schedule next arrival
  next_arrival_time = sim_state['Clock'] + GenerateInterarrival()
  ScheduleEvent(next_arrival_time, "Arrival") # No patient ID needed for general arrival

  # Check nurse availability
  if sim_state['BusyNurses'] < S:
    sim_state['BusyNurses'] += 1
    sim_state['Patients'][patient_id]['Status'] = 'InTriage'
    sim_state['Patients'][patient_id]['TriageStartTime'] = sim_state['Clock']
    service_time = GenerateNurseServiceTime()
    print(f"DEBUG: Patient {patient_id} starts triage. Duration: {service_time:.4f}")
    ScheduleEvent(sim_state['Clock'] + service_time, "DepartureTriage", patient_id)
  else:
    sim_state['TriageQueue'].append(patient_id)
    sim_state['Patients'][patient_id]['Status'] = 'WaitingTriage'
    sim_state['Patients'][patient_id]['TriageQueueEntryTime'] = sim_state['Clock']
    print(f"DEBUG: Patient {patient_id} added to triage queue.")

def DepartureTriage(sim_state, ScheduleEvent, patient_id):
  """
  Executes the departure from triage logic.
  Assumes sim_state contains: Clock, BusyNurses, OccupiedBeds, TriageQueue, Patients
  Assumes ScheduleEvent(time, event_type, patient_id) exists.
  """
  print(f"DEBUG: DepartureTriage for Patient {patient_id} at time {sim_state['Clock']:.4f}")
  sim_state['BusyNurses'] -= 1
  sim_state['Patients'][patient_id]['TriageEndTime'] = sim_state['Clock']

  # Determine condition
  if random.random() < P1: # Stable condition
    sim_state['Patients'][patient_id]['Condition'] = 'Stable'
    sim_state['Patients'][patient_id]['Status'] = 'HomeHealing'
    sim_state['Patients'][patient_id]['TreatmentLocation'] = 'Home'
    sim_state['Patients'][patient_id]['TreatmentStartTime'] = sim_state['Clock']
    healing_time = GenerateHomeHealingTime('s')
    print(f"DEBUG: Patient {patient_id} is Stable. Home healing duration: {healing_time:.4f}")
    ScheduleEvent(sim_state['Clock'] + healing_time, "HomeHealingCompletion", patient_id)
    sim_state['TotalHomeTreated'] += 1
  else: # Critical condition
    sim_state['Patients'][patient_id]['Condition'] = 'Critical'
    # Check bed availability
    if sim_state['OccupiedBeds'] < K:
      sim_state['OccupiedBeds'] += 1
      sim_state['Patients'][patient_id]['Status'] = 'HospitalHealing'
      sim_state['Patients'][patient_id]['TreatmentLocation'] = 'Hospital'
      sim_state['Patients'][patient_id]['TreatmentStartTime'] = sim_state['Clock']
      healing_time = GenerateHospitalHealingTime()
      print(f"DEBUG: Patient {patient_id} is Critical. Bed assigned. Hospital healing duration: {healing_time:.4f}")
      ScheduleEvent(sim_state['Clock'] + healing_time, "HospitalHealingCompletion", patient_id)
    else: # No beds available
      sim_state['Patients'][patient_id]['Status'] = 'HomeHealingRejected'
      sim_state['Patients'][patient_id]['TreatmentLocation'] = 'HomeRejected'
      sim_state['Patients'][patient_id]['TreatmentStartTime'] = sim_state['Clock']
      sim_state['Patients'][patient_id]['WasRejected'] = True
      sim_state['TotalPatientsRejected'] += 1
      healing_time = GenerateHomeHealingTime('c')
      print(f"DEBUG: Patient {patient_id} is Critical. No bed! Rejected. Home healing duration: {healing_time:.4f}")
      ScheduleEvent(sim_state['Clock'] + healing_time, "HomeHealingCompletion", patient_id)
      sim_state['TotalHomeTreated'] += 1

  # Check triage queue
  if len(sim_state['TriageQueue']) > 0:
    next_patient_id = sim_state['TriageQueue'].pop(0)
    sim_state['BusyNurses'] += 1
    # Calculate waiting time (optional for stats)
    wait_time = sim_state['Clock'] - sim_state['Patients'][next_patient_id]['TriageQueueEntryTime']
    sim_state['TotalTriageWaitingTime'] += wait_time
    # Start service
    sim_state['Patients'][next_patient_id]['Status'] = 'InTriage'
    sim_state['Patients'][next_patient_id]['TriageStartTime'] = sim_state['Clock']
    service_time = GenerateNurseServiceTime()
    print(f"DEBUG: Patient {next_patient_id} starts triage from queue (waited {wait_time:.4f}). Duration: {service_time:.4f}")
    ScheduleEvent(sim_state['Clock'] + service_time, "DepartureTriage", next_patient_id)

def TreatedatHospital(sim_state, ScheduleEvent, patient_id):
  """
  Executes the discharge from hospital bed logic.
  Assumes sim_state contains: Clock, OccupiedBeds, Patients
  """
  print(f"DEBUG: TreatedatHospital for Patient {patient_id} at time {sim_state['Clock']:.4f}")
  sim_state['OccupiedBeds'] -= 1
  sim_state['Patients'][patient_id]['Status'] = 'Healed'
  sim_state['Patients'][patient_id]['TreatmentEndTime'] = sim_state['Clock']
  sim_state['TotalPatientsHealed'] += 1
  # Calculate total system time (optional for stats)
  total_time = sim_state['Clock'] - sim_state['Patients'][patient_id]['ArrivalTime']
  sim_state['TotalSystemTime'] += total_time
  print(f"DEBUG: Patient {patient_id} healed in hospital. Total time: {total_time:.4f}")

def HomeHealingCompletion(sim_state, ScheduleEvent, patient_id):
    """
    Executes the completion of home healing logic.
    Assumes sim_state contains: Clock, Patients
    """
    print(f"DEBUG: HomeHealingCompletion for Patient {patient_id} at time {sim_state['Clock']:.4f}")
    sim_state['Patients'][patient_id]['Status'] = 'Healed'
    sim_state['Patients'][patient_id]['TreatmentEndTime'] = sim_state['Clock']
    sim_state['TotalPatientsHealed'] += 1
    # Calculate total system time (optional for stats)
    total_time = sim_state['Clock'] - sim_state['Patients'][patient_id]['ArrivalTime']
    sim_state['TotalSystemTime'] += total_time
    print(f"DEBUG: Patient {patient_id} healed at home. Total time: {total_time:.4f}")


# --- Simulation Engine Related Functions (Part 1.2 Requirement) ---
# These represent the control flow aspects, typically part of the main loop in Part 2.

def AdvanceTime(sim_state):
  """
  Advances the simulation clock to the time of the next event in the FEL.
  Assumes sim_state contains: Clock, FEL (heapq priority queue)
  Returns:
      tuple: (event_time, event_type, patient_id) or None if FEL is empty
  """
  if len(sim_state['FEL']) > 0:
      # heapq stores tuples, get the smallest (earliest time)
      next_event_time, event_type, patient_id = sim_state['FEL'][0] # Peek
      # Update clock only if moving forward
      if next_event_time >= sim_state['Clock']:
          # --- Statistics Update Hook (Example) ---
          # In a full simulation (Part 2), you'd update time-integral stats here
          # based on the time difference (next_event_time - sim_state['Clock'])
          # and the current state (BusyNurses, OccupiedBeds).
          time_interval = next_event_time - sim_state['Clock']
          sim_state['TotalNurseBusyTime'] += sim_state['BusyNurses'] * time_interval
          sim_state['TotalBedOccupancyTime'] += sim_state['OccupiedBeds'] * time_interval
          # --- End Statistics Update Hook ---
          sim_state['Clock'] = next_event_time
          print(f"DEBUG: Advancing time to {sim_state['Clock']:.4f}")
          return True # Indicate time advanced
      else:
          # This case (next event time < current clock) shouldn't happen
          # in a correctly managed FEL, but handle defensively.
          print(f"WARNING: Next event time {next_event_time} is before current clock {sim_state['Clock']}. Removing event.")
          heapq.heappop(sim_state['FEL']) # Remove the problematic event
          return AdvanceTime(sim_state) # Try advancing again
  else:
      print("DEBUG: FEL is empty. Cannot advance time.")
      return False # Indicate FEL is empty

def ExecuteEvent(sim_state, ScheduleEvent):
  """
  Retrieves the next event from FEL and calls the appropriate process function.
  Assumes sim_state contains: FEL
  Assumes ScheduleEvent exists.
  """
  if len(sim_state['FEL']) > 0:
      # Get the next event (remove from FEL)
      event_time, event_type, patient_id = heapq.heappop(sim_state['FEL'])
      print(f"DEBUG: Executing Event: {event_type} at {event_time:.4f} (Patient: {patient_id})")

      # Call the corresponding process function
      if event_type == "Arrival":
          Arrival(sim_state, ScheduleEvent)
      elif event_type == "DepartureTriage":
          DepartureTriage(sim_state, ScheduleEvent, patient_id)
      elif event_type == "HospitalHealingCompletion":
          TreatedatHospital(sim_state, ScheduleEvent, patient_id)
      elif event_type == "HomeHealingCompletion":
          HomeHealingCompletion(sim_state, ScheduleEvent, patient_id)
      else:
          print(f"ERROR: Unknown event type '{event_type}'")
  else:
      print("DEBUG: FEL is empty. No event to execute.")


# --- Helper for Scheduling Events ---
# This function would typically be part of the main simulation class/module in Part 2

def ScheduleEvent_Helper(fel_heap, time, event_type, patient_id=None):
    """Adds an event to the Future Event List (FEL)."""
    heapq.heappush(fel_heap, (time, event_type, patient_id))
    # print(f"DEBUG: Scheduled {event_type} at {time:.4f} for Patient {patient_id}")


# --- Example Initialization and Loop (Illustrative - Belongs in Part 2) ---
if __name__ == '__main__':
    print("--- Running Illustrative Simulation Snippet (Part 1.2 Functions) ---")

    # Basic state initialization (more comprehensive in Part 2)
    sim_state = {
        'Clock': 0.0,
        'FEL': [],  # Future Event List (Priority Queue)
        'TriageQueue': [],
        'BusyNurses': 0,
        'OccupiedBeds': 0,
        'NextPatientID': 1,
        'Patients': {}, # Dictionary to store patient data
        # Stats Accumulators
        'TotalPatientsArrived': 0,
        'TotalPatientsHealed': 0,
        'TotalPatientsRejected': 0,
        'TotalTriageWaitingTime': 0.0,
        'TotalNurseBusyTime': 0.0,
        'TotalBedOccupancyTime': 0.0,
        'TotalSystemTime': 0.0,
        'TotalHomeTreated': 0
    }

    # Seed for reproducibility (Use your group seed in Part 2)
    # random.seed(12345)

    # Schedule the first arrival
    first_arrival_time = GenerateInterarrival()
    ScheduleEvent_Helper(sim_state['FEL'], first_arrival_time, "Arrival")

    # Simple illustrative loop (Part 2 would have proper termination)
    max_events = 15 # Limit for this example
    event_count = 0
    while len(sim_state['FEL']) > 0 and event_count < max_events:
        if AdvanceTime(sim_state): # Advances clock to next event time
             ExecuteEvent(sim_state, lambda t, et, pid=None: ScheduleEvent_Helper(sim_state['FEL'], t, et, pid))
             event_count += 1
        else:
            break # Stop if FEL becomes empty

    print("\n--- End of Illustrative Snippet ---")
    print(f"Final Clock: {sim_state['Clock']:.4f}")
    print(f"Total Arrivals: {sim_state['TotalPatientsArrived']}")
    print(f"Total Healed: {sim_state['TotalPatientsHealed']}")
    print(f"Total Rejected: {sim_state['TotalPatientsRejected']}")
    print(f"Final Triage Queue Length: {len(sim_state['TriageQueue'])}")
    print(f"Final Busy Nurses: {sim_state['BusyNurses']}")
    print(f"Final Occupied Beds: {sim_state['OccupiedBeds']}")
