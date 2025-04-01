import random
import math
import heapq
import numpy as np
import pandas as pd
from tabulate import tabulate  # For nice table output
import matplotlib.pyplot as plt
from collections import defaultdict

# --- Parameters (Group 36 from parameter values document) ---
LAMBDA = 1.0  # Arrival rate (patients/hour) - fixed for all groups
MU_T = 1.0 / 3.0  # Triage nurse service rate (patients/hour)
MU_S = 0.16  # Stable patient home healing rate (patients/hour) - fixed for all groups
MU_CB = 0.153061224  # Critical patient hospital healing rate (patients/hour)
ALPHA_MIN = 1.25  # Min value for alpha uniform distribution
ALPHA_MAX = 1.75  # Max value for alpha uniform distribution
P1 = 0.25  # Probability of stable condition
P2 = 1.0 - P1  # Probability of critical condition
S = 4  # Number of triage nurses
K = 7  # Number of hospital beds

# Group ID sum for random seed
GROUP_SEED = 123456789  # Replace with actual sum of your group members' IDs

# --- Import functions from part1_2_functions.py ---
# Assuming these functions are available from the previous part
from part1_2_functions import (
    GenerateInterarrival, GenerateNurseServiceTime, 
    GenerateHospitalHealingTime, GenerateHomeHealingTime
)

class HospitalSimulation:
    def __init__(self, seed=GROUP_SEED, initial_condition="empty"):
        """
        Initialize the hospital simulation with given parameters.
        
        Args:
            seed: Random seed for reproducibility
            initial_condition: One of "empty", "half_full", or "full"
        """
        # Set random seed
        random.seed(seed)
        np.random.seed(seed)
        
        # Initialize simulation state
        self.sim_state = {
            'Clock': 0.0,
            'FEL': [],  # Future Event List (Priority Queue)
            'TriageQueue': [],
            'BusyNurses': 0,
            'OccupiedBeds': 0,
            'NextPatientID': 1,
            'Patients': {},  # Dictionary to store patient data
            
            # Statistics accumulators
            'TotalPatientsArrived': 0,
            'TotalPatientsHealed': 0,
            'TotalPatientsRejected': 0,
            'TotalHomeTreated': 0,
            'TotalCriticalPatients': 0,
            
            # Time-weighted statistics
            'LastUpdateTime': 0.0,
            'CumTriageEmpty': 0.0,
            'CumBedsEmpty': 0.0,
            'CumBothEmpty': 0.0,
            'CumNurseBusyTime': 0.0,
            'CumBedOccupancyTime': 0.0,
            'TotalSystemTime': 0.0,
            'TotalTriageWaitingTime': 0.0,
            'SimulationLength': 0.0,
            
            # Event count for reporting
            'EventCount': 0,
            
            # Event trace table for first 20 events
            'EventTrace': []
        }
        
        # Set initial conditions based on parameter
        self._set_initial_condition(initial_condition)
        
        # Schedule the first arrival
        first_arrival_time = GenerateInterarrival()
        self.schedule_event(first_arrival_time, "Arrival")
        
    def _set_initial_condition(self, condition):
        """Sets the initial state of the system based on condition."""
        if condition == "empty":
            # Default values already set in init
            pass
        elif condition == "half_full":
            # Set half of nurses and beds as busy/occupied
            half_nurses = S // 2
            half_beds = K // 2
            
            for i in range(half_nurses):
                patient_id = self.sim_state['NextPatientID']
                self.sim_state['NextPatientID'] += 1
                self.sim_state['BusyNurses'] += 1
                self.sim_state['Patients'][patient_id] = {
                    'ArrivalTime': 0.0,
                    'Status': 'InTriage',
                    'TriageStartTime': 0.0
                }
                service_time = GenerateNurseServiceTime()
                self.schedule_event(service_time, "DepartureTriage", patient_id)
            
            for i in range(half_beds):
                patient_id = self.sim_state['NextPatientID']
                self.sim_state['NextPatientID'] += 1
                self.sim_state['OccupiedBeds'] += 1
                self.sim_state['Patients'][patient_id] = {
                    'ArrivalTime': 0.0,
                    'Status': 'HospitalHealing',
                    'Condition': 'Critical',
                    'TreatmentLocation': 'Hospital',
                    'TreatmentStartTime': 0.0
                }
                healing_time = GenerateHospitalHealingTime()
                self.schedule_event(healing_time, "HospitalHealingCompletion", patient_id)
                
        elif condition == "full":
            # Set all nurses and beds as busy/occupied
            for i in range(S):
                patient_id = self.sim_state['NextPatientID']
                self.sim_state['NextPatientID'] += 1
                self.sim_state['BusyNurses'] += 1
                self.sim_state['Patients'][patient_id] = {
                    'ArrivalTime': 0.0,
                    'Status': 'InTriage',
                    'TriageStartTime': 0.0
                }
                service_time = GenerateNurseServiceTime()
                self.schedule_event(service_time, "DepartureTriage", patient_id)
            
            for i in range(K):
                patient_id = self.sim_state['NextPatientID']
                self.sim_state['NextPatientID'] += 1
                self.sim_state['OccupiedBeds'] += 1
                self.sim_state['Patients'][patient_id] = {
                    'ArrivalTime': 0.0,
                    'Status': 'HospitalHealing',
                    'Condition': 'Critical',
                    'TreatmentLocation': 'Hospital',
                    'TreatmentStartTime': 0.0
                }
                healing_time = GenerateHospitalHealingTime()
                self.schedule_event(healing_time, "HospitalHealingCompletion", patient_id)
        else:
            raise ValueError(f"Unknown initial condition: {condition}")
    
    def schedule_event(self, time, event_type, patient_id=None):
        """Schedule an event in the future event list."""
        event_time = self.sim_state['Clock'] + time
        heapq.heappush(self.sim_state['FEL'], (event_time, event_type, patient_id))
        return event_time
    
    def update_time_weighted_stats(self):
        """Update time-weighted statistics before advancing the clock."""
        elapsed = self.sim_state['Clock'] - self.sim_state['LastUpdateTime']
        
        # Update time-weighted statistics
        if self.sim_state['BusyNurses'] == 0:
            self.sim_state['CumTriageEmpty'] += elapsed
        
        if self.sim_state['OccupiedBeds'] == 0:
            self.sim_state['CumBedsEmpty'] += elapsed
        
        if self.sim_state['BusyNurses'] == 0 and self.sim_state['OccupiedBeds'] == 0:
            self.sim_state['CumBothEmpty'] += elapsed
        
        # Update resource utilization statistics
        self.sim_state['CumNurseBusyTime'] += self.sim_state['BusyNurses'] * elapsed
        self.sim_state['CumBedOccupancyTime'] += self.sim_state['OccupiedBeds'] * elapsed
        
        # Update last update time
        self.sim_state['LastUpdateTime'] = self.sim_state['Clock']
    
    def advance_time(self):
        """Advance the simulation clock to the next event time."""
        if len(self.sim_state['FEL']) > 0:
            # Update time-weighted statistics
            self.update_time_weighted_stats()
            
            # Get the next event time (peek without removing)
            next_event_time, _, _ = self.sim_state['FEL'][0]
            self.sim_state['Clock'] = next_event_time
            return True
        return False
    
    def process_arrival(self):
        """Process an arrival event."""
        self.sim_state['TotalPatientsArrived'] += 1
        patient_id = self.sim_state['NextPatientID']
        self.sim_state['NextPatientID'] += 1
        
        # Create patient record
        self.sim_state['Patients'][patient_id] = {
            'ArrivalTime': self.sim_state['Clock'],
            'Status': 'Arrived'
        }
        
        # Schedule next arrival
        next_arrival = GenerateInterarrival()
        self.schedule_event(next_arrival, "Arrival")
        
        # Check if a triage nurse is available
        if self.sim_state['BusyNurses'] < S:
            # Start triage immediately
            self.sim_state['BusyNurses'] += 1
            self.sim_state['Patients'][patient_id]['Status'] = 'InTriage'
            self.sim_state['Patients'][patient_id]['TriageStartTime'] = self.sim_state['Clock']
            
            # Schedule departure from triage
            triage_time = GenerateNurseServiceTime()
            self.schedule_event(triage_time, "DepartureTriage", patient_id)
        else:
            # Join triage queue
            self.sim_state['TriageQueue'].append(patient_id)
            self.sim_state['Patients'][patient_id]['Status'] = 'WaitingTriage'
            self.sim_state['Patients'][patient_id]['TriageQueueEntryTime'] = self.sim_state['Clock']
    
    def process_departure_triage(self, patient_id):
        """Process a departure from triage event."""
        # Free up the nurse
        self.sim_state['BusyNurses'] -= 1
        
        # Update patient status
        self.sim_state['Patients'][patient_id]['TriageEndTime'] = self.sim_state['Clock']
        
        # Determine patient condition (stable vs critical)
        is_stable = random.random() < P1
        
        if is_stable:  # Stable condition - send home
            self.sim_state['Patients'][patient_id]['Condition'] = 'Stable'
            self.sim_state['Patients'][patient_id]['Status'] = 'HomeHealing'
            self.sim_state['Patients'][patient_id]['TreatmentLocation'] = 'Home'
            self.sim_state['Patients'][patient_id]['TreatmentStartTime'] = self.sim_state['Clock']
            
            # Schedule healing completion
            healing_time = GenerateHomeHealingTime('s')
            self.schedule_event(healing_time, "HomeHealingCompletion", patient_id)
            
            self.sim_state['TotalHomeTreated'] += 1
        else:  # Critical condition
            self.sim_state['Patients'][patient_id]['Condition'] = 'Critical'
            self.sim_state['TotalCriticalPatients'] += 1
            
            # Check if there's an available bed
            if self.sim_state['OccupiedBeds'] < K:
                # Admit to hospital
                self.sim_state['OccupiedBeds'] += 1
                self.sim_state['Patients'][patient_id]['Status'] = 'HospitalHealing'
                self.sim_state['Patients'][patient_id]['TreatmentLocation'] = 'Hospital'
                self.sim_state['Patients'][patient_id]['TreatmentStartTime'] = self.sim_state['Clock']
                
                # Schedule hospital healing completion
                healing_time = GenerateHospitalHealingTime()
                self.schedule_event(healing_time, "HospitalHealingCompletion", patient_id)
            else:
                # No beds available - send home for care
                self.sim_state['Patients'][patient_id]['Status'] = 'HomeHealingRejected'
                self.sim_state['Patients'][patient_id]['TreatmentLocation'] = 'HomeRejected'
                self.sim_state['Patients'][patient_id]['TreatmentStartTime'] = self.sim_state['Clock']
                self.sim_state['Patients'][patient_id]['WasRejected'] = True
                
                # Schedule home healing completion
                healing_time = GenerateHomeHealingTime('c')
                self.schedule_event(healing_time, "HomeHealingCompletion", patient_id)
                
                self.sim_state['TotalPatientsRejected'] += 1
                self.sim_state['TotalHomeTreated'] += 1
        
        # Check triage queue for next patient
        if len(self.sim_state['TriageQueue']) > 0:
            next_patient_id = self.sim_state['TriageQueue'].pop(0)
            
            # Calculate waiting time
            wait_time = self.sim_state['Clock'] - self.sim_state['Patients'][next_patient_id]['TriageQueueEntryTime']
            self.sim_state['TotalTriageWaitingTime'] += wait_time
            
            # Start triage for next patient
            self.sim_state['BusyNurses'] += 1
            self.sim_state['Patients'][next_patient_id]['Status'] = 'InTriage'
            self.sim_state['Patients'][next_patient_id]['TriageStartTime'] = self.sim_state['Clock']
            
            # Schedule departure from triage
            triage_time = GenerateNurseServiceTime()
            self.schedule_event(triage_time, "DepartureTriage", next_patient_id)
    
    def process_hospital_healing_completion(self, patient_id):
        """Process a hospital healing completion event."""
        # Free up the bed
        self.sim_state['OccupiedBeds'] -= 1
        
        # Update patient status
        self.sim_state['Patients'][patient_id]['Status'] = 'Healed'
        self.sim_state['Patients'][patient_id]['TreatmentEndTime'] = self.sim_state['Clock']
        
        # Calculate total system time
        total_time = self.sim_state['Clock'] - self.sim_state['Patients'][patient_id]['ArrivalTime']
        self.sim_state['TotalSystemTime'] += total_time
        
        # Increment healed counter
        self.sim_state['TotalPatientsHealed'] += 1
    
    def process_home_healing_completion(self, patient_id):
        """Process a home healing completion event."""
        # Update patient status
        self.sim_state['Patients'][patient_id]['Status'] = 'Healed'
        self.sim_state['Patients'][patient_id]['TreatmentEndTime'] = self.sim_state['Clock']
        
        # Calculate total system time
        total_time = self.sim_state['Clock'] - self.sim_state['Patients'][patient_id]['ArrivalTime']
        self.sim_state['TotalSystemTime'] += total_time
        
        # Increment healed counter
        self.sim_state['TotalPatientsHealed'] += 1
    
    def execute_next_event(self):
        """Execute the next event from the future event list."""
        if len(self.sim_state['FEL']) > 0:
            # Get the next event (remove from FEL)
            event_time, event_type, patient_id = heapq.heappop(self.sim_state['FEL'])
            
            # Process the event
            if event_type == "Arrival":
                self.process_arrival()
            elif event_type == "DepartureTriage":
                self.process_departure_triage(patient_id)
            elif event_type == "HospitalHealingCompletion":
                self.process_hospital_healing_completion(patient_id)
            elif event_type == "HomeHealingCompletion":
                self.process_home_healing_completion(patient_id)
            else:
                raise ValueError(f"Unknown event type: {event_type}")
            
            # For the first 20 events, record detailed state information
            if self.sim_state['EventCount'] < 20:
                # Create a snapshot of the system state
                event_record = {
                    'EventNumber': self.sim_state['EventCount'] + 1,
                    'EventTime': round(self.sim_state['Clock'], 4),
                    'EventType': event_type,
                    'PatientID': patient_id,
                    'TriageQueueLength': len(self.sim_state['TriageQueue']),
                    'BusyNurses': self.sim_state['BusyNurses'],
                    'OccupiedBeds': self.sim_state['OccupiedBeds'],
                    'TotalPatients': self.sim_state['TotalPatientsArrived'],
                    'TotalHealed': self.sim_state['TotalPatientsHealed'],
                    'FutureEventList': [(round(t, 4), et, pid) for t, et, pid in self.sim_state['FEL']]
                }
                self.sim_state['EventTrace'].append(event_record)
            
            # Increment event counter
            self.sim_state['EventCount'] += 1
            
            return True
        return False
    
    def run_until_healed(self, target_healed):
        """Run the simulation until the specified number of patients are healed."""
        while self.sim_state['TotalPatientsHealed'] < target_healed:
            if self.advance_time():
                self.execute_next_event()
            else:
                # No more events to process
                break
        
        # Update the simulation length
        self.sim_state['SimulationLength'] = self.sim_state['Clock']
        return self.collect_statistics()
    
    def collect_statistics(self):
        """Calculate and return key statistics from the simulation run."""
        sim_length = self.sim_state['SimulationLength']
        
        # Calculate probabilities and utilization
        if sim_length > 0:
            p_triage_empty = self.sim_state['CumTriageEmpty'] / sim_length
            p_beds_empty = self.sim_state['CumBedsEmpty'] / sim_length
            p_both_empty = self.sim_state['CumBothEmpty'] / sim_length
            avg_nurse_utilization = self.sim_state['CumNurseBusyTime'] / (S * sim_length)
            avg_occupied_beds = self.sim_state['CumBedOccupancyTime'] / sim_length
        else:
            p_triage_empty = p_beds_empty = p_both_empty = avg_nurse_utilization = avg_occupied_beds = 0
        
        # Calculate rejection probability
        total_critical = self.sim_state['TotalCriticalPatients']
        rejection_prob = self.sim_state['TotalPatientsRejected'] / total_critical if total_critical > 0 else 0
        
        # Calculate proportion treated at home
        total_patients = self.sim_state['TotalPatientsHealed']
        prop_home_treated = self.sim_state['TotalHomeTreated'] / total_patients if total_patients > 0 else 0
        
        # Calculate average healing time
        avg_healing_time = self.sim_state['TotalSystemTime'] / total_patients if total_patients > 0 else 0
        
        # Return all statistics as a dictionary
        return {
            'SimulationLength': sim_length,
            'TotalPatientsArrived': self.sim_state['TotalPatientsArrived'],
            'TotalPatientsHealed': self.sim_state['TotalPatientsHealed'],
            'ProbabilityTriageEmpty': p_triage_empty,
            'ProbabilityBedsEmpty': p_beds_empty,
            'ProbabilityBothEmpty': p_both_empty,
            'RejectionProbability': rejection_prob,
            'AverageNurseUtilization': avg_nurse_utilization,
            'AverageOccupiedBeds': avg_occupied_beds,
            'ProportionHomeTreated': prop_home_treated,
            'AverageHealingTime': avg_healing_time
        }
    
    def print_event_trace(self):
        """Print the trace of events for the first 20 events."""
        headers = ['Event#', 'Time', 'Event Type', 'PatientID', 'Triage Queue', 'Busy Nurses', 'Occupied Beds', 'Total Patients', 'Total Healed']
        data = [[
            event['EventNumber'],
            f"{event['EventTime']:.4f}",
            event['EventType'],
            event['PatientID'],
            event['TriageQueueLength'],
            event['BusyNurses'],
            event['OccupiedBeds'],
            event['TotalPatients'],
            event['TotalHealed']
        ] for event in self.sim_state['EventTrace']]
        
        print("\nEvent Trace for First 20 Events:")
        print(tabulate(data, headers=headers, tablefmt='grid'))
        print("\nFuture Event Lists:")
        for i, event in enumerate(self.sim_state['EventTrace']):
            print(f"After Event {i+1}: {event['FutureEventList']}")


def run_single_simulation(initial_condition, target_healed, seed=GROUP_SEED):
    """Run a single simulation with the specified parameters."""
    sim = HospitalSimulation(seed=seed, initial_condition=initial_condition)
    results = sim.run_until_healed(target_healed)
    
    # Print detailed trace for first 20 events
    if target_healed >= 20:
        sim.print_event_trace()
    
    # Print summarized results
    print(f"\nResults for {initial_condition} initial condition, {target_healed} healed patients:")
    for key, value in results.items():
        print(f"{key}: {value:.6f}")
    
    return results

def run_replications(initial_condition, num_replications=20, target_healed=200, base_seed=GROUP_SEED):
    """Run multiple replications and calculate confidence intervals."""
    results_list = []
    
    for rep in range(num_replications):
        # Use a different seed for each replication
        seed = base_seed + rep
        sim = HospitalSimulation(seed=seed, initial_condition=initial_condition)
        results = sim.run_until_healed(target_healed)
        results_list.append(results)
    
    # Calculate means and confidence intervals
    stats = {}
    for key in results_list[0].keys():
        values = [r[key] for r in results_list]
        mean = np.mean(values)
        std = np.std(values, ddof=1)  # Sample standard deviation
        half_width = 1.96 * std / np.sqrt(num_replications)  # 95% confidence interval
        stats[key] = {
            'mean': mean,
            'lower': mean - half_width,
            'upper': mean + half_width
        }
    
    # Print results with confidence intervals
    print(f"\nResults for {initial_condition} with {num_replications} replications:")
    for key, value in stats.items():
        print(f"{key}: {value['mean']:.6f} [95% CI: {value['lower']:.6f}, {value['upper']:.6f}]")
    
    return stats

def run_all_simulations():
    """Run all required simulations based on the assignment specifications and save results to a file."""
    # Create and open output file
    with open('results.md', 'w') as f:
        f.write("# Hospital Simulation Results\n\n")
        
        # List of initial conditions to test
        initial_conditions = ["empty", "half_full", "full"]
        
        # List of target healed patients to test
        target_healed_list = [20, 200, 1000]
        
        # Run single simulations for each combination
        results = {}
        for condition in initial_conditions:
            condition_results = {}
            for target in target_healed_list:
                header = f"\n## {condition.capitalize()} Initial Condition with {target} Target Healed Patients\n\n"
                f.write(header)
                f.write("```\n")  # Start code block
                
                # Redirect print output to file by capturing it
                from io import StringIO
                import sys
                original_stdout = sys.stdout
                captured_output = StringIO()
                sys.stdout = captured_output
                
                # Run the simulation
                condition_results[target] = run_single_simulation(condition, target)
                
                # Restore stdout and write captured output to file
                sys.stdout = original_stdout
                f.write(captured_output.getvalue())
                f.write("```\n")  # End code block
                
            results[condition] = condition_results
        
        # Run replications for each initial condition
        replication_results = {}
        for condition in initial_conditions:
            header = f"\n## {condition.capitalize()} Initial Condition - 20 Replications\n\n"
            f.write(header)
            f.write("```\n")  # Start code block
            
            # Capture output
            from io import StringIO
            import sys
            original_stdout = sys.stdout
            captured_output = StringIO()
            sys.stdout = captured_output
            
            # Run replications
            replication_results[condition] = run_replications(condition)
            
            # Restore stdout and write captured output
            sys.stdout = original_stdout
            f.write(captured_output.getvalue())
            f.write("```\n")  # End code block
        
        # Add comparison section
        f.write("\n## Comparison of Results\n\n")
        f.write("```\n")  # Start code block
        
        # Capture comparison output
        from io import StringIO
        import sys
        original_stdout = sys.stdout
        captured_output = StringIO()
        sys.stdout = captured_output
        
        # Compare results
        compare_results(results)
        
        # Restore stdout and write captured output
        sys.stdout = original_stdout
        f.write(captured_output.getvalue())
        f.write("```\n")  # End code block
        
    print(f"Results saved to results.md")
    
    return results, replication_results

def compare_results(results):
    """Compare and analyze results from different simulation configurations."""
    print("\n" + "="*80)
    print("Comparison of Results Across Initial Conditions and Run Lengths")
    print("="*80)
    
    # Create a dataframe for easier comparison
    rows = []
    for condition in results:
        for target, stats in results[condition].items():
            row = {
                'Initial Condition': condition,
                'Target Healed': target,
                **stats
            }
            rows.append(row)
    
    df = pd.DataFrame(rows)
    
    # Compare across initial conditions for the same target healed
    for target in [20, 200, 1000]:
        print(f"\nComparison for {target} healed patients:")
        subset = df[df['Target Healed'] == target]
        for col in ['ProbabilityTriageEmpty', 'ProbabilityBedsEmpty', 'RejectionProbability', 
                   'AverageNurseUtilization', 'AverageOccupiedBeds', 'ProportionHomeTreated']:
            print(f"\n{col}:")
            for condition in ['empty', 'half_full', 'full']:
                value = subset[subset['Initial Condition'] == condition][col].values[0]
                print(f"  {condition}: {value:.6f}")
    
    # Compare convergence as target healed increases
    print("\n" + "="*80)
    print("Convergence Analysis as Simulation Length Increases")
    print("="*80)
    
    for condition in ['empty', 'half_full', 'full']:
        print(f"\nConvergence for {condition} initial condition:")
        subset = df[df['Initial Condition'] == condition]
        for col in ['ProbabilityTriageEmpty', 'ProbabilityBedsEmpty', 'RejectionProbability', 
                   'AverageNurseUtilization', 'AverageOccupiedBeds', 'ProportionHomeTreated']:
            print(f"\n{col}:")
            for target in [20, 200, 1000]:
                value = subset[subset['Target Healed'] == target][col].values[0]
                print(f"  {target} patients: {value:.6f}")

if __name__ == "__main__":
    # Run all simulations
    results, replication_results = run_all_simulations()
    
    # Compare and analyze results
    compare_results(results)
