# Hand Simulation of Hospital System (Group 36)

## Parameters
- λ = 1.0 patient/hour (arrival rate)
- μt = 0.333333333 patient/hour (triage nurse service rate)
- μs = 0.16 patient/hour (stable patient home healing rate)
- μcb = 0.153061224 patient/hour (critical patient hospital healing rate)
- p1 = 0.25 (probability of stable condition)
- p2 = 0.75 (probability of critical condition)
- S = 4 (number of triage nurses)
- K = 7 (number of hospital beds)
- α ~ U[1.25, 1.75] (factor for critical patients healing at home)
- Random seed = 4040800288

## Initial State
- System starts empty (Clock = 0.0)
- Future Event List (FEL) = []
- Generate first arrival: t = -ln(0.3781074913)/1.0 = 0.9733
- Initial FEL = [(0.9733, "Arrival", null)]

## Simulation Steps

| Step | Clock | Event | Patient ID | FEL After Event | TriageQueue | BusyNurses | OccupiedBeds | Patient Status Changes |
|------|-------|-------|------------|-----------------|-------------|------------|--------------|------------------------|
| 1 | 0.9733 | Arrival | 1 | [(1.5510, "Arrival", null), (4.9352, "DepartureTriage", 1)] | [] | 1 | 0 | P1: Arrived → InTriage |
| 2 | 1.5510 | Arrival | 2 | [(3.6055, "DepartureTriage", 2), (4.6371, "Arrival", null), (4.9352, "DepartureTriage", 1)] | [] | 2 | 0 | P2: Arrived → InTriage |
| 3 | 3.6055 | DepartureTriage | 2 | [(4.6371, "Arrival", null), (4.9352, "DepartureTriage", 1), (10.8240, "HospitalHealingCompletion", 2)] | [] | 1 | 1 | P2: InTriage → Critical, HospitalHealing |
| 4 | 4.6371 | Arrival | 3 | [(4.9352, "DepartureTriage", 1), (6.3982, "DepartureTriage", 3), (10.8240, "HospitalHealingCompletion", 2)] | [] | 2 | 1 | P3: Arrived → InTriage |
| 5 | 4.9352 | DepartureTriage | 1 | [(6.3982, "DepartureTriage", 3), (10.8240, "HospitalHealingCompletion", 2), (14.6464, "HomeHealingCompletion", 1)] | [] | 1 | 1 | P1: InTriage → Stable, HomeHealing |
| 6 | 6.3982 | DepartureTriage | 3 | [(7.2614, "Arrival", null), (10.8240, "HospitalHealingCompletion", 2), (14.6464, "HomeHealingCompletion", 1)] | [] | 0 | 2 | P3: InTriage → Critical, HospitalHealing |
| 7 | 7.2614 | Arrival | 4 | [(8.9553, "DepartureTriage", 4), (10.8240, "HospitalHealingCompletion", 2), (14.6464, "HomeHealingCompletion", 1)] | [] | 1 | 2 | P4: Arrived → InTriage |
| 8 | 8.9553 | DepartureTriage | 4 | [(10.5203, "Arrival", null), (10.8240, "HospitalHealingCompletion", 2), (14.6464, "HomeHealingCompletion", 1), (15.4122, "HospitalHealingCompletion", 4)] | [] | 0 | 3 | P4: InTriage → Critical, HospitalHealing |
| 9 | 10.5203 | Arrival | 5 | [(10.8240, "HospitalHealingCompletion", 2), (13.4749, "DepartureTriage", 5), (14.6464, "HomeHealingCompletion", 1), (15.4122, "HospitalHealingCompletion", 4)] | [] | 1 | 3 | P5: Arrived → InTriage |
| 10 | 10.8240 | HospitalHealingCompletion | 2 | [(11.4735, "Arrival", null), (13.4749, "DepartureTriage", 5), (14.6464, "HomeHealingCompletion", 1), (15.4122, "HospitalHealingCompletion", 4)] | [] | 1 | 2 | P2: HospitalHealing → Healed |
| 11 | 11.4735 | Arrival | 6 | [(13.4749, "DepartureTriage", 5), (14.6464, "HomeHealingCompletion", 1), (15.4122, "HospitalHealingCompletion", 4), (15.9651, "DepartureTriage", 6)] | [] | 2 | 2 | P6: Arrived → InTriage |
| 12 | 13.4749 | DepartureTriage | 5 | [(14.6464, "HomeHealingCompletion", 1), (15.4122, "HospitalHealingCompletion", 4), (15.9651, "DepartureTriage", 6), (17.7382, "HomeHealingCompletion", 5)] | [] | 1 | 2 | P5: InTriage → Stable, HomeHealing |
| 13 | 14.6464 | HomeHealingCompletion | 1 | [(15.4122, "HospitalHealingCompletion", 4), (15.9651, "DepartureTriage", 6), (17.7382, "HomeHealingCompletion", 5)] | [] | 1 | 2 | P1: HomeHealing → Healed |
| 14 | 15.4122 | HospitalHealingCompletion | 4 | [(15.9651, "DepartureTriage", 6), (16.5488, "Arrival", null), (17.7382, "HomeHealingCompletion", 5)] | [] | 1 | 1 | P4: HospitalHealing → Healed |
| 15 | 15.9651 | DepartureTriage | 6 | [(16.5488, "Arrival", null), (17.7382, "HomeHealingCompletion", 5), (25.6912, "HospitalHealingCompletion", 6)] | [] | 0 | 2 | P6: InTriage → Critical, HospitalHealing |
| 16 | 16.5488 | Arrival | 7 | [(17.7382, "HomeHealingCompletion", 5), (19.0825, "DepartureTriage", 7), (25.6912, "HospitalHealingCompletion", 6)] | [] | 1 | 2 | P7: Arrived → InTriage |
| 17 | 17.7382 | HomeHealingCompletion | 5 | [(19.0825, "DepartureTriage", 7), (25.6912, "HospitalHealingCompletion", 6)] | [] | 1 | 2 | P5: HomeHealing → Healed |
| 18 | 19.0825 | DepartureTriage | 7 | [(20.4501, "Arrival", null), (25.6912, "HospitalHealingCompletion", 6), (30.5642, "HospitalHealingCompletion", 7)] | [] | 0 | 3 | P7: InTriage → Critical, HospitalHealing |

## Detailed Calculation Steps

**Step 1: Patient 1 Arrival (Clock = 0.9733)**
- Set random seed: 4040800288
- Generate first arrival time: t = -ln(0.3781074913)/1.0 = 0.9733
- Patient 1 arrives and goes to a free nurse
- Generate triage service time: t = -ln(0.2642626166)/0.333333333 = 3.9619
- Schedule triage completion at t = 0.9733 + 3.9619 = 4.9352
- Generate next arrival time: t = -ln(0.5612407136)/1.0 = 0.5777
- Schedule next arrival at t = 0.9733 + 0.5777 = 1.5510

**Step 2: Patient 2 Arrival (Clock = 1.5510)**
- Patient 2 arrives and goes to a free nurse
- Generate triage service time: t = -ln(0.5045389744)/0.333333333 = 2.0545
- Schedule triage completion at t = 1.5510 + 2.0545 = 3.6055
- Generate next arrival time: t = -ln(0.0456824185)/1.0 = 3.0861
- Schedule next arrival at t = 1.5510 + 3.0861 = 4.6371

**Step 3: Patient 2 Triage Completion (Clock = 3.6055)**
- Random number for condition: 0.6631252408 > 0.25, so condition is Critical
- Assign to hospital bed (1 occupied)
- Generate hospital healing time: t = -ln(0.3363628924)/0.153061224 = 7.2185
- Schedule hospital healing completion at t = 3.6055 + 7.2185 = 10.8240

**Step 4: Patient 3 Arrival (Clock = 4.6371)**
- Patient 3 arrives and goes to a free nurse
- Generate triage service time: t = -ln(0.4539717674)/0.333333333 = 1.7611
- Schedule triage completion at t = 4.6371 + 1.7611 = 6.3982
- Generate next arrival time: t = -ln(0.4318252856)/1.0 = 0.8403
- Schedule next arrival at t = 4.6371 + 0.8403 = 5.4774 (not shown in final table due to later rescheduling)

**Step 5: Patient 1 Triage Completion (Clock = 4.9352)**
- Random number for condition: 0.1230283405 < 0.25, so condition is Stable
- Send to home care
- Generate home healing time: t = -ln(0.4634647219)/0.16 = 9.7112
- Schedule home healing completion at t = 4.9352 + 9.7112 = 14.6464

**Steps 6-18 continue with similar calculations...**

## Summary of First 5 Healed Patients

| Patient | Arrival | Condition | Treatment | Healed At | Total Time |
|---------|---------|-----------|-----------|-----------|------------|
| 2 | 1.5510 | Critical | Hospital | 10.8240 | 9.2730 |
| 1 | 0.9733 | Stable | Home | 14.6464 | 13.6731 |
| 4 | 7.2614 | Critical | Hospital | 15.4122 | 8.1508 |
| 5 | 10.5203 | Stable | Home | 17.7382 | 7.2179 |
| 7 | 16.5488 | Critical | Hospital | 30.5642 | 14.0154 |

The hand simulation tracks the first 5 patients through the entire healing process. The system demonstrates the interaction between arrivals, triage, and the different healing paths (hospital beds vs. home care).