# Hospital Simulation Results


## Empty Initial Condition with 20 Target Healed Patients

```

Event Trace for First 20 Events:
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|   Event# |   Time | Event Type                |   PatientID |   Triage Queue |   Busy Nurses |   Occupied Beds |   Total Patients |   Total Healed |
+==========+========+===========================+=============+================+===============+=================+==================+================+
|        1 | 0.4288 | Arrival                   |             |              0 |             1 |               0 |                1 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        2 | 2.0863 | DepartureTriage           |           1 |              0 |             0 |               1 |                1 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        3 | 2.8529 | Arrival                   |             |              0 |             1 |               1 |                2 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        4 | 3.4432 | Arrival                   |             |              0 |             2 |               1 |                3 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        5 | 3.6712 | Arrival                   |             |              0 |             3 |               1 |                4 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        6 | 3.8913 | Arrival                   |             |              0 |             4 |               1 |                5 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        7 | 4.0048 | Arrival                   |             |              1 |             4 |               1 |                6 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        8 | 4.0516 | DepartureTriage           |           2 |              0 |             4 |               2 |                6 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        9 | 4.553  | Arrival                   |             |              1 |             4 |               2 |                7 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       10 | 4.7522 | DepartureTriage           |           5 |              0 |             4 |               2 |                7 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       11 | 5.2254 | DepartureTriage           |           6 |              0 |             3 |               3 |                7 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       12 | 5.2288 | DepartureTriage           |           4 |              0 |             2 |               4 |                7 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       13 | 5.5275 | DepartureTriage           |           3 |              0 |             1 |               5 |                7 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       14 | 5.6627 | HomeHealingCompletion     |           5 |              0 |             1 |               5 |                7 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       15 | 5.8335 | Arrival                   |             |              0 |             2 |               5 |                8 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       16 | 6.4636 | HospitalHealingCompletion |           4 |              0 |             2 |               4 |                8 |              2 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       17 | 6.7665 | Arrival                   |             |              0 |             3 |               4 |                9 |              2 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       18 | 7.0864 | DepartureTriage           |           9 |              0 |             2 |               5 |                9 |              2 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       19 | 7.276  | HospitalHealingCompletion |           2 |              0 |             2 |               4 |                9 |              3 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       20 | 7.4522 | Arrival                   |             |              0 |             3 |               4 |               10 |              3 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+

Future Event Lists:
After Event 1: [(2.0863, 'DepartureTriage', 1), (2.8529, 'Arrival', None)]
After Event 2: [(2.8529, 'Arrival', None), (7.944, 'HospitalHealingCompletion', 1)]
After Event 3: [(3.4432, 'Arrival', None), (7.944, 'HospitalHealingCompletion', 1), (4.0516, 'DepartureTriage', 2)]
After Event 4: [(3.6712, 'Arrival', None), (5.5275, 'DepartureTriage', 3), (4.0516, 'DepartureTriage', 2), (7.944, 'HospitalHealingCompletion', 1)]
After Event 5: [(3.8913, 'Arrival', None), (4.0516, 'DepartureTriage', 2), (7.944, 'HospitalHealingCompletion', 1), (5.5275, 'DepartureTriage', 3), (5.2288, 'DepartureTriage', 4)]
After Event 6: [(4.0048, 'Arrival', None), (4.0516, 'DepartureTriage', 2), (4.7522, 'DepartureTriage', 5), (5.5275, 'DepartureTriage', 3), (5.2288, 'DepartureTriage', 4), (7.944, 'HospitalHealingCompletion', 1)]
After Event 7: [(4.0516, 'DepartureTriage', 2), (5.2288, 'DepartureTriage', 4), (4.553, 'Arrival', None), (5.5275, 'DepartureTriage', 3), (7.944, 'HospitalHealingCompletion', 1), (4.7522, 'DepartureTriage', 5)]
After Event 8: [(4.553, 'Arrival', None), (5.2288, 'DepartureTriage', 4), (4.7522, 'DepartureTriage', 5), (5.5275, 'DepartureTriage', 3), (7.944, 'HospitalHealingCompletion', 1), (7.276, 'HospitalHealingCompletion', 2), (5.2254, 'DepartureTriage', 6)]
After Event 9: [(4.7522, 'DepartureTriage', 5), (5.2288, 'DepartureTriage', 4), (5.2254, 'DepartureTriage', 6), (5.5275, 'DepartureTriage', 3), (7.944, 'HospitalHealingCompletion', 1), (7.276, 'HospitalHealingCompletion', 2), (5.8335, 'Arrival', None)]
After Event 10: [(5.2254, 'DepartureTriage', 6), (5.2288, 'DepartureTriage', 4), (5.6627, 'HomeHealingCompletion', 5), (5.5275, 'DepartureTriage', 3), (7.944, 'HospitalHealingCompletion', 1), (7.276, 'HospitalHealingCompletion', 2), (5.8335, 'Arrival', None), (12.0669, 'DepartureTriage', 7)]
After Event 11: [(5.2288, 'DepartureTriage', 4), (5.5275, 'DepartureTriage', 3), (5.6627, 'HomeHealingCompletion', 5), (12.0669, 'DepartureTriage', 7), (7.944, 'HospitalHealingCompletion', 1), (7.276, 'HospitalHealingCompletion', 2), (5.8335, 'Arrival', None), (12.9382, 'HospitalHealingCompletion', 6)]
After Event 12: [(5.5275, 'DepartureTriage', 3), (6.4636, 'HospitalHealingCompletion', 4), (5.6627, 'HomeHealingCompletion', 5), (7.944, 'HospitalHealingCompletion', 1), (12.9382, 'HospitalHealingCompletion', 6), (7.276, 'HospitalHealingCompletion', 2), (5.8335, 'Arrival', None), (12.0669, 'DepartureTriage', 7)]
After Event 13: [(5.6627, 'HomeHealingCompletion', 5), (6.4636, 'HospitalHealingCompletion', 4), (5.8335, 'Arrival', None), (7.6068, 'HospitalHealingCompletion', 3), (12.9382, 'HospitalHealingCompletion', 6), (7.276, 'HospitalHealingCompletion', 2), (12.0669, 'DepartureTriage', 7), (7.944, 'HospitalHealingCompletion', 1)]
After Event 14: [(5.8335, 'Arrival', None), (6.4636, 'HospitalHealingCompletion', 4), (7.276, 'HospitalHealingCompletion', 2), (7.6068, 'HospitalHealingCompletion', 3), (12.9382, 'HospitalHealingCompletion', 6), (7.944, 'HospitalHealingCompletion', 1), (12.0669, 'DepartureTriage', 7)]
After Event 15: [(6.4636, 'HospitalHealingCompletion', 4), (7.6068, 'HospitalHealingCompletion', 3), (6.7665, 'Arrival', None), (8.4842, 'DepartureTriage', 8), (12.9382, 'HospitalHealingCompletion', 6), (7.944, 'HospitalHealingCompletion', 1), (7.276, 'HospitalHealingCompletion', 2), (12.0669, 'DepartureTriage', 7)]
After Event 16: [(6.7665, 'Arrival', None), (7.6068, 'HospitalHealingCompletion', 3), (7.276, 'HospitalHealingCompletion', 2), (8.4842, 'DepartureTriage', 8), (12.9382, 'HospitalHealingCompletion', 6), (7.944, 'HospitalHealingCompletion', 1), (12.0669, 'DepartureTriage', 7)]
After Event 17: [(7.0864, 'DepartureTriage', 9), (7.276, 'HospitalHealingCompletion', 2), (7.4522, 'Arrival', None), (7.6068, 'HospitalHealingCompletion', 3), (12.9382, 'HospitalHealingCompletion', 6), (12.0669, 'DepartureTriage', 7), (7.944, 'HospitalHealingCompletion', 1), (8.4842, 'DepartureTriage', 8)]
After Event 18: [(7.276, 'HospitalHealingCompletion', 2), (7.6068, 'HospitalHealingCompletion', 3), (7.4522, 'Arrival', None), (8.4842, 'DepartureTriage', 8), (12.9382, 'HospitalHealingCompletion', 6), (12.0669, 'DepartureTriage', 7), (7.944, 'HospitalHealingCompletion', 1), (8.5655, 'HospitalHealingCompletion', 9)]
After Event 19: [(7.4522, 'Arrival', None), (7.6068, 'HospitalHealingCompletion', 3), (7.944, 'HospitalHealingCompletion', 1), (8.4842, 'DepartureTriage', 8), (12.9382, 'HospitalHealingCompletion', 6), (12.0669, 'DepartureTriage', 7), (8.5655, 'HospitalHealingCompletion', 9)]
After Event 20: [(7.6068, 'HospitalHealingCompletion', 3), (8.146, 'DepartureTriage', 10), (7.944, 'HospitalHealingCompletion', 1), (8.4842, 'DepartureTriage', 8), (12.9382, 'HospitalHealingCompletion', 6), (12.0669, 'DepartureTriage', 7), (10.0805, 'Arrival', None), (8.5655, 'HospitalHealingCompletion', 9)]

Results for empty initial condition, 20 healed patients:
SimulationLength: 33.149206
TotalPatientsArrived: 34.000000
TotalPatientsHealed: 20.000000
ProbabilityTriageEmpty: 0.056214
ProbabilityBedsEmpty: 0.012936
ProbabilityBothEmpty: 0.000000
RejectionProbability: 0.280000
AverageNurseUtilization: 0.657306
AverageOccupiedBeds: 4.584726
ProportionHomeTreated: 0.550000
AverageHealingTime: 8.321741
```

## Empty Initial Condition with 200 Target Healed Patients

```

Event Trace for First 20 Events:
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|   Event# |   Time | Event Type                |   PatientID |   Triage Queue |   Busy Nurses |   Occupied Beds |   Total Patients |   Total Healed |
+==========+========+===========================+=============+================+===============+=================+==================+================+
|        1 | 0.4288 | Arrival                   |             |              0 |             1 |               0 |                1 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        2 | 2.0863 | DepartureTriage           |           1 |              0 |             0 |               1 |                1 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        3 | 2.8529 | Arrival                   |             |              0 |             1 |               1 |                2 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        4 | 3.4432 | Arrival                   |             |              0 |             2 |               1 |                3 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        5 | 3.6712 | Arrival                   |             |              0 |             3 |               1 |                4 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        6 | 3.8913 | Arrival                   |             |              0 |             4 |               1 |                5 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        7 | 4.0048 | Arrival                   |             |              1 |             4 |               1 |                6 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        8 | 4.0516 | DepartureTriage           |           2 |              0 |             4 |               2 |                6 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        9 | 4.553  | Arrival                   |             |              1 |             4 |               2 |                7 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       10 | 4.7522 | DepartureTriage           |           5 |              0 |             4 |               2 |                7 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       11 | 5.2254 | DepartureTriage           |           6 |              0 |             3 |               3 |                7 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       12 | 5.2288 | DepartureTriage           |           4 |              0 |             2 |               4 |                7 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       13 | 5.5275 | DepartureTriage           |           3 |              0 |             1 |               5 |                7 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       14 | 5.6627 | HomeHealingCompletion     |           5 |              0 |             1 |               5 |                7 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       15 | 5.8335 | Arrival                   |             |              0 |             2 |               5 |                8 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       16 | 6.4636 | HospitalHealingCompletion |           4 |              0 |             2 |               4 |                8 |              2 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       17 | 6.7665 | Arrival                   |             |              0 |             3 |               4 |                9 |              2 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       18 | 7.0864 | DepartureTriage           |           9 |              0 |             2 |               5 |                9 |              2 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       19 | 7.276  | HospitalHealingCompletion |           2 |              0 |             2 |               4 |                9 |              3 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       20 | 7.4522 | Arrival                   |             |              0 |             3 |               4 |               10 |              3 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+

Future Event Lists:
After Event 1: [(2.0863, 'DepartureTriage', 1), (2.8529, 'Arrival', None)]
After Event 2: [(2.8529, 'Arrival', None), (7.944, 'HospitalHealingCompletion', 1)]
After Event 3: [(3.4432, 'Arrival', None), (7.944, 'HospitalHealingCompletion', 1), (4.0516, 'DepartureTriage', 2)]
After Event 4: [(3.6712, 'Arrival', None), (5.5275, 'DepartureTriage', 3), (4.0516, 'DepartureTriage', 2), (7.944, 'HospitalHealingCompletion', 1)]
After Event 5: [(3.8913, 'Arrival', None), (4.0516, 'DepartureTriage', 2), (7.944, 'HospitalHealingCompletion', 1), (5.5275, 'DepartureTriage', 3), (5.2288, 'DepartureTriage', 4)]
After Event 6: [(4.0048, 'Arrival', None), (4.0516, 'DepartureTriage', 2), (4.7522, 'DepartureTriage', 5), (5.5275, 'DepartureTriage', 3), (5.2288, 'DepartureTriage', 4), (7.944, 'HospitalHealingCompletion', 1)]
After Event 7: [(4.0516, 'DepartureTriage', 2), (5.2288, 'DepartureTriage', 4), (4.553, 'Arrival', None), (5.5275, 'DepartureTriage', 3), (7.944, 'HospitalHealingCompletion', 1), (4.7522, 'DepartureTriage', 5)]
After Event 8: [(4.553, 'Arrival', None), (5.2288, 'DepartureTriage', 4), (4.7522, 'DepartureTriage', 5), (5.5275, 'DepartureTriage', 3), (7.944, 'HospitalHealingCompletion', 1), (7.276, 'HospitalHealingCompletion', 2), (5.2254, 'DepartureTriage', 6)]
After Event 9: [(4.7522, 'DepartureTriage', 5), (5.2288, 'DepartureTriage', 4), (5.2254, 'DepartureTriage', 6), (5.5275, 'DepartureTriage', 3), (7.944, 'HospitalHealingCompletion', 1), (7.276, 'HospitalHealingCompletion', 2), (5.8335, 'Arrival', None)]
After Event 10: [(5.2254, 'DepartureTriage', 6), (5.2288, 'DepartureTriage', 4), (5.6627, 'HomeHealingCompletion', 5), (5.5275, 'DepartureTriage', 3), (7.944, 'HospitalHealingCompletion', 1), (7.276, 'HospitalHealingCompletion', 2), (5.8335, 'Arrival', None), (12.0669, 'DepartureTriage', 7)]
After Event 11: [(5.2288, 'DepartureTriage', 4), (5.5275, 'DepartureTriage', 3), (5.6627, 'HomeHealingCompletion', 5), (12.0669, 'DepartureTriage', 7), (7.944, 'HospitalHealingCompletion', 1), (7.276, 'HospitalHealingCompletion', 2), (5.8335, 'Arrival', None), (12.9382, 'HospitalHealingCompletion', 6)]
After Event 12: [(5.5275, 'DepartureTriage', 3), (6.4636, 'HospitalHealingCompletion', 4), (5.6627, 'HomeHealingCompletion', 5), (7.944, 'HospitalHealingCompletion', 1), (12.9382, 'HospitalHealingCompletion', 6), (7.276, 'HospitalHealingCompletion', 2), (5.8335, 'Arrival', None), (12.0669, 'DepartureTriage', 7)]
After Event 13: [(5.6627, 'HomeHealingCompletion', 5), (6.4636, 'HospitalHealingCompletion', 4), (5.8335, 'Arrival', None), (7.6068, 'HospitalHealingCompletion', 3), (12.9382, 'HospitalHealingCompletion', 6), (7.276, 'HospitalHealingCompletion', 2), (12.0669, 'DepartureTriage', 7), (7.944, 'HospitalHealingCompletion', 1)]
After Event 14: [(5.8335, 'Arrival', None), (6.4636, 'HospitalHealingCompletion', 4), (7.276, 'HospitalHealingCompletion', 2), (7.6068, 'HospitalHealingCompletion', 3), (12.9382, 'HospitalHealingCompletion', 6), (7.944, 'HospitalHealingCompletion', 1), (12.0669, 'DepartureTriage', 7)]
After Event 15: [(6.4636, 'HospitalHealingCompletion', 4), (7.6068, 'HospitalHealingCompletion', 3), (6.7665, 'Arrival', None), (8.4842, 'DepartureTriage', 8), (12.9382, 'HospitalHealingCompletion', 6), (7.944, 'HospitalHealingCompletion', 1), (7.276, 'HospitalHealingCompletion', 2), (12.0669, 'DepartureTriage', 7)]
After Event 16: [(6.7665, 'Arrival', None), (7.6068, 'HospitalHealingCompletion', 3), (7.276, 'HospitalHealingCompletion', 2), (8.4842, 'DepartureTriage', 8), (12.9382, 'HospitalHealingCompletion', 6), (7.944, 'HospitalHealingCompletion', 1), (12.0669, 'DepartureTriage', 7)]
After Event 17: [(7.0864, 'DepartureTriage', 9), (7.276, 'HospitalHealingCompletion', 2), (7.4522, 'Arrival', None), (7.6068, 'HospitalHealingCompletion', 3), (12.9382, 'HospitalHealingCompletion', 6), (12.0669, 'DepartureTriage', 7), (7.944, 'HospitalHealingCompletion', 1), (8.4842, 'DepartureTriage', 8)]
After Event 18: [(7.276, 'HospitalHealingCompletion', 2), (7.6068, 'HospitalHealingCompletion', 3), (7.4522, 'Arrival', None), (8.4842, 'DepartureTriage', 8), (12.9382, 'HospitalHealingCompletion', 6), (12.0669, 'DepartureTriage', 7), (7.944, 'HospitalHealingCompletion', 1), (8.5655, 'HospitalHealingCompletion', 9)]
After Event 19: [(7.4522, 'Arrival', None), (7.6068, 'HospitalHealingCompletion', 3), (7.944, 'HospitalHealingCompletion', 1), (8.4842, 'DepartureTriage', 8), (12.9382, 'HospitalHealingCompletion', 6), (12.0669, 'DepartureTriage', 7), (8.5655, 'HospitalHealingCompletion', 9)]
After Event 20: [(7.6068, 'HospitalHealingCompletion', 3), (8.146, 'DepartureTriage', 10), (7.944, 'HospitalHealingCompletion', 1), (8.4842, 'DepartureTriage', 8), (12.9382, 'HospitalHealingCompletion', 6), (12.0669, 'DepartureTriage', 7), (10.0805, 'Arrival', None), (8.5655, 'HospitalHealingCompletion', 9)]

Results for empty initial condition, 200 healed patients:
SimulationLength: 207.862931
TotalPatientsArrived: 211.000000
TotalPatientsHealed: 200.000000
ProbabilityTriageEmpty: 0.059809
ProbabilityBedsEmpty: 0.002063
ProbabilityBothEmpty: 0.000000
RejectionProbability: 0.126582
AverageNurseUtilization: 0.727236
AverageOccupiedBeds: 4.390007
ProportionHomeTreated: 0.345000
AverageHealingTime: 10.726018
```

## Empty Initial Condition with 1000 Target Healed Patients

```

Event Trace for First 20 Events:
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|   Event# |   Time | Event Type                |   PatientID |   Triage Queue |   Busy Nurses |   Occupied Beds |   Total Patients |   Total Healed |
+==========+========+===========================+=============+================+===============+=================+==================+================+
|        1 | 0.4288 | Arrival                   |             |              0 |             1 |               0 |                1 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        2 | 2.0863 | DepartureTriage           |           1 |              0 |             0 |               1 |                1 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        3 | 2.8529 | Arrival                   |             |              0 |             1 |               1 |                2 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        4 | 3.4432 | Arrival                   |             |              0 |             2 |               1 |                3 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        5 | 3.6712 | Arrival                   |             |              0 |             3 |               1 |                4 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        6 | 3.8913 | Arrival                   |             |              0 |             4 |               1 |                5 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        7 | 4.0048 | Arrival                   |             |              1 |             4 |               1 |                6 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        8 | 4.0516 | DepartureTriage           |           2 |              0 |             4 |               2 |                6 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        9 | 4.553  | Arrival                   |             |              1 |             4 |               2 |                7 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       10 | 4.7522 | DepartureTriage           |           5 |              0 |             4 |               2 |                7 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       11 | 5.2254 | DepartureTriage           |           6 |              0 |             3 |               3 |                7 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       12 | 5.2288 | DepartureTriage           |           4 |              0 |             2 |               4 |                7 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       13 | 5.5275 | DepartureTriage           |           3 |              0 |             1 |               5 |                7 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       14 | 5.6627 | HomeHealingCompletion     |           5 |              0 |             1 |               5 |                7 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       15 | 5.8335 | Arrival                   |             |              0 |             2 |               5 |                8 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       16 | 6.4636 | HospitalHealingCompletion |           4 |              0 |             2 |               4 |                8 |              2 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       17 | 6.7665 | Arrival                   |             |              0 |             3 |               4 |                9 |              2 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       18 | 7.0864 | DepartureTriage           |           9 |              0 |             2 |               5 |                9 |              2 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       19 | 7.276  | HospitalHealingCompletion |           2 |              0 |             2 |               4 |                9 |              3 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       20 | 7.4522 | Arrival                   |             |              0 |             3 |               4 |               10 |              3 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+

Future Event Lists:
After Event 1: [(2.0863, 'DepartureTriage', 1), (2.8529, 'Arrival', None)]
After Event 2: [(2.8529, 'Arrival', None), (7.944, 'HospitalHealingCompletion', 1)]
After Event 3: [(3.4432, 'Arrival', None), (7.944, 'HospitalHealingCompletion', 1), (4.0516, 'DepartureTriage', 2)]
After Event 4: [(3.6712, 'Arrival', None), (5.5275, 'DepartureTriage', 3), (4.0516, 'DepartureTriage', 2), (7.944, 'HospitalHealingCompletion', 1)]
After Event 5: [(3.8913, 'Arrival', None), (4.0516, 'DepartureTriage', 2), (7.944, 'HospitalHealingCompletion', 1), (5.5275, 'DepartureTriage', 3), (5.2288, 'DepartureTriage', 4)]
After Event 6: [(4.0048, 'Arrival', None), (4.0516, 'DepartureTriage', 2), (4.7522, 'DepartureTriage', 5), (5.5275, 'DepartureTriage', 3), (5.2288, 'DepartureTriage', 4), (7.944, 'HospitalHealingCompletion', 1)]
After Event 7: [(4.0516, 'DepartureTriage', 2), (5.2288, 'DepartureTriage', 4), (4.553, 'Arrival', None), (5.5275, 'DepartureTriage', 3), (7.944, 'HospitalHealingCompletion', 1), (4.7522, 'DepartureTriage', 5)]
After Event 8: [(4.553, 'Arrival', None), (5.2288, 'DepartureTriage', 4), (4.7522, 'DepartureTriage', 5), (5.5275, 'DepartureTriage', 3), (7.944, 'HospitalHealingCompletion', 1), (7.276, 'HospitalHealingCompletion', 2), (5.2254, 'DepartureTriage', 6)]
After Event 9: [(4.7522, 'DepartureTriage', 5), (5.2288, 'DepartureTriage', 4), (5.2254, 'DepartureTriage', 6), (5.5275, 'DepartureTriage', 3), (7.944, 'HospitalHealingCompletion', 1), (7.276, 'HospitalHealingCompletion', 2), (5.8335, 'Arrival', None)]
After Event 10: [(5.2254, 'DepartureTriage', 6), (5.2288, 'DepartureTriage', 4), (5.6627, 'HomeHealingCompletion', 5), (5.5275, 'DepartureTriage', 3), (7.944, 'HospitalHealingCompletion', 1), (7.276, 'HospitalHealingCompletion', 2), (5.8335, 'Arrival', None), (12.0669, 'DepartureTriage', 7)]
After Event 11: [(5.2288, 'DepartureTriage', 4), (5.5275, 'DepartureTriage', 3), (5.6627, 'HomeHealingCompletion', 5), (12.0669, 'DepartureTriage', 7), (7.944, 'HospitalHealingCompletion', 1), (7.276, 'HospitalHealingCompletion', 2), (5.8335, 'Arrival', None), (12.9382, 'HospitalHealingCompletion', 6)]
After Event 12: [(5.5275, 'DepartureTriage', 3), (6.4636, 'HospitalHealingCompletion', 4), (5.6627, 'HomeHealingCompletion', 5), (7.944, 'HospitalHealingCompletion', 1), (12.9382, 'HospitalHealingCompletion', 6), (7.276, 'HospitalHealingCompletion', 2), (5.8335, 'Arrival', None), (12.0669, 'DepartureTriage', 7)]
After Event 13: [(5.6627, 'HomeHealingCompletion', 5), (6.4636, 'HospitalHealingCompletion', 4), (5.8335, 'Arrival', None), (7.6068, 'HospitalHealingCompletion', 3), (12.9382, 'HospitalHealingCompletion', 6), (7.276, 'HospitalHealingCompletion', 2), (12.0669, 'DepartureTriage', 7), (7.944, 'HospitalHealingCompletion', 1)]
After Event 14: [(5.8335, 'Arrival', None), (6.4636, 'HospitalHealingCompletion', 4), (7.276, 'HospitalHealingCompletion', 2), (7.6068, 'HospitalHealingCompletion', 3), (12.9382, 'HospitalHealingCompletion', 6), (7.944, 'HospitalHealingCompletion', 1), (12.0669, 'DepartureTriage', 7)]
After Event 15: [(6.4636, 'HospitalHealingCompletion', 4), (7.6068, 'HospitalHealingCompletion', 3), (6.7665, 'Arrival', None), (8.4842, 'DepartureTriage', 8), (12.9382, 'HospitalHealingCompletion', 6), (7.944, 'HospitalHealingCompletion', 1), (7.276, 'HospitalHealingCompletion', 2), (12.0669, 'DepartureTriage', 7)]
After Event 16: [(6.7665, 'Arrival', None), (7.6068, 'HospitalHealingCompletion', 3), (7.276, 'HospitalHealingCompletion', 2), (8.4842, 'DepartureTriage', 8), (12.9382, 'HospitalHealingCompletion', 6), (7.944, 'HospitalHealingCompletion', 1), (12.0669, 'DepartureTriage', 7)]
After Event 17: [(7.0864, 'DepartureTriage', 9), (7.276, 'HospitalHealingCompletion', 2), (7.4522, 'Arrival', None), (7.6068, 'HospitalHealingCompletion', 3), (12.9382, 'HospitalHealingCompletion', 6), (12.0669, 'DepartureTriage', 7), (7.944, 'HospitalHealingCompletion', 1), (8.4842, 'DepartureTriage', 8)]
After Event 18: [(7.276, 'HospitalHealingCompletion', 2), (7.6068, 'HospitalHealingCompletion', 3), (7.4522, 'Arrival', None), (8.4842, 'DepartureTriage', 8), (12.9382, 'HospitalHealingCompletion', 6), (12.0669, 'DepartureTriage', 7), (7.944, 'HospitalHealingCompletion', 1), (8.5655, 'HospitalHealingCompletion', 9)]
After Event 19: [(7.4522, 'Arrival', None), (7.6068, 'HospitalHealingCompletion', 3), (7.944, 'HospitalHealingCompletion', 1), (8.4842, 'DepartureTriage', 8), (12.9382, 'HospitalHealingCompletion', 6), (12.0669, 'DepartureTriage', 7), (8.5655, 'HospitalHealingCompletion', 9)]
After Event 20: [(7.6068, 'HospitalHealingCompletion', 3), (8.146, 'DepartureTriage', 10), (7.944, 'HospitalHealingCompletion', 1), (8.4842, 'DepartureTriage', 8), (12.9382, 'HospitalHealingCompletion', 6), (12.0669, 'DepartureTriage', 7), (10.0805, 'Arrival', None), (8.5655, 'HospitalHealingCompletion', 9)]

Results for empty initial condition, 1000 healed patients:
SimulationLength: 1000.116047
TotalPatientsArrived: 1016.000000
TotalPatientsHealed: 1000.000000
ProbabilityTriageEmpty: 0.028079
ProbabilityBedsEmpty: 0.005183
ProbabilityBothEmpty: 0.000000
RejectionProbability: 0.143045
AverageNurseUtilization: 0.769814
AverageOccupiedBeds: 4.471325
ProportionHomeTreated: 0.350000
AverageHealingTime: 11.458152
```

## Half_full Initial Condition with 20 Target Healed Patients

```

Event Trace for First 20 Events:
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|   Event# |   Time | Event Type                |   PatientID |   Triage Queue |   Busy Nurses |   Occupied Beds |   Total Patients |   Total Healed |
+==========+========+===========================+=============+================+===============+=================+==================+================+
|        1 | 0.5903 | Arrival                   |             |              0 |             3 |               3 |                1 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        2 | 0.9899 | Arrival                   |             |              0 |             4 |               3 |                2 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        3 | 1.2742 | DepartureTriage           |           6 |              0 |             3 |               4 |                2 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        4 | 1.2865 | DepartureTriage           |           1 |              0 |             2 |               5 |                2 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        5 | 1.6501 | DepartureTriage           |           7 |              0 |             1 |               6 |                2 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        6 | 1.6846 | Arrival                   |             |              0 |             2 |               6 |                3 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        7 | 2.0155 | HospitalHealingCompletion |           6 |              0 |             2 |               5 |                3 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        8 | 2.0759 | Arrival                   |             |              0 |             3 |               5 |                4 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        9 | 2.5129 | DepartureTriage           |           9 |              0 |             2 |               5 |                4 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       10 | 3.6095 | HospitalHealingCompletion |           3 |              0 |             2 |               4 |                4 |              2 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       11 | 4.8685 | HospitalHealingCompletion |           1 |              0 |             2 |               3 |                4 |              3 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       12 | 4.8745 | HospitalHealingCompletion |           7 |              0 |             2 |               2 |                4 |              4 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       13 | 5.5261 | DepartureTriage           |           8 |              0 |             1 |               3 |                4 |              4 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       14 | 5.8578 | HospitalHealingCompletion |           5 |              0 |             1 |               2 |                4 |              5 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       15 | 6.7418 | HomeHealingCompletion     |           9 |              0 |             1 |               2 |                4 |              6 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       16 | 6.9641 | HospitalHealingCompletion |           4 |              0 |             1 |               1 |                4 |              7 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       17 | 7.2723 | DepartureTriage           |           2 |              0 |             0 |               2 |                4 |              7 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       18 | 8.0542 | Arrival                   |             |              0 |             1 |               2 |                5 |              7 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       19 | 8.3724 | Arrival                   |             |              0 |             2 |               2 |                6 |              7 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       20 | 9.256  | Arrival                   |             |              0 |             3 |               2 |                7 |              7 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+

Future Event Lists:
After Event 1: [(0.9899, 'Arrival', None), (5.8578, 'HospitalHealingCompletion', 5), (1.2742, 'DepartureTriage', 6), (7.2723, 'DepartureTriage', 2), (6.9641, 'HospitalHealingCompletion', 4), (3.6095, 'HospitalHealingCompletion', 3), (1.2865, 'DepartureTriage', 1)]
After Event 2: [(1.2742, 'DepartureTriage', 6), (1.6501, 'DepartureTriage', 7), (1.2865, 'DepartureTriage', 1), (5.8578, 'HospitalHealingCompletion', 5), (6.9641, 'HospitalHealingCompletion', 4), (3.6095, 'HospitalHealingCompletion', 3), (1.6846, 'Arrival', None), (7.2723, 'DepartureTriage', 2)]
After Event 3: [(1.2865, 'DepartureTriage', 1), (1.6501, 'DepartureTriage', 7), (1.6846, 'Arrival', None), (2.0155, 'HospitalHealingCompletion', 6), (6.9641, 'HospitalHealingCompletion', 4), (3.6095, 'HospitalHealingCompletion', 3), (7.2723, 'DepartureTriage', 2), (5.8578, 'HospitalHealingCompletion', 5)]
After Event 4: [(1.6501, 'DepartureTriage', 7), (2.0155, 'HospitalHealingCompletion', 6), (1.6846, 'Arrival', None), (4.8685, 'HospitalHealingCompletion', 1), (6.9641, 'HospitalHealingCompletion', 4), (3.6095, 'HospitalHealingCompletion', 3), (7.2723, 'DepartureTriage', 2), (5.8578, 'HospitalHealingCompletion', 5)]
After Event 5: [(1.6846, 'Arrival', None), (2.0155, 'HospitalHealingCompletion', 6), (3.6095, 'HospitalHealingCompletion', 3), (4.8685, 'HospitalHealingCompletion', 1), (6.9641, 'HospitalHealingCompletion', 4), (5.8578, 'HospitalHealingCompletion', 5), (7.2723, 'DepartureTriage', 2), (4.8745, 'HospitalHealingCompletion', 7)]
After Event 6: [(2.0155, 'HospitalHealingCompletion', 6), (2.0759, 'Arrival', None), (3.6095, 'HospitalHealingCompletion', 3), (4.8685, 'HospitalHealingCompletion', 1), (6.9641, 'HospitalHealingCompletion', 4), (5.8578, 'HospitalHealingCompletion', 5), (7.2723, 'DepartureTriage', 2), (4.8745, 'HospitalHealingCompletion', 7), (5.5261, 'DepartureTriage', 8)]
After Event 7: [(2.0759, 'Arrival', None), (4.8685, 'HospitalHealingCompletion', 1), (3.6095, 'HospitalHealingCompletion', 3), (4.8745, 'HospitalHealingCompletion', 7), (6.9641, 'HospitalHealingCompletion', 4), (5.8578, 'HospitalHealingCompletion', 5), (7.2723, 'DepartureTriage', 2), (5.5261, 'DepartureTriage', 8)]
After Event 8: [(2.5129, 'DepartureTriage', 9), (3.6095, 'HospitalHealingCompletion', 3), (5.5261, 'DepartureTriage', 8), (4.8685, 'HospitalHealingCompletion', 1), (6.9641, 'HospitalHealingCompletion', 4), (5.8578, 'HospitalHealingCompletion', 5), (7.2723, 'DepartureTriage', 2), (8.0542, 'Arrival', None), (4.8745, 'HospitalHealingCompletion', 7)]
After Event 9: [(3.6095, 'HospitalHealingCompletion', 3), (4.8685, 'HospitalHealingCompletion', 1), (5.5261, 'DepartureTriage', 8), (4.8745, 'HospitalHealingCompletion', 7), (6.9641, 'HospitalHealingCompletion', 4), (5.8578, 'HospitalHealingCompletion', 5), (7.2723, 'DepartureTriage', 2), (8.0542, 'Arrival', None), (6.7418, 'HomeHealingCompletion', 9)]
After Event 10: [(4.8685, 'HospitalHealingCompletion', 1), (4.8745, 'HospitalHealingCompletion', 7), (5.5261, 'DepartureTriage', 8), (6.7418, 'HomeHealingCompletion', 9), (6.9641, 'HospitalHealingCompletion', 4), (5.8578, 'HospitalHealingCompletion', 5), (7.2723, 'DepartureTriage', 2), (8.0542, 'Arrival', None)]
After Event 11: [(4.8745, 'HospitalHealingCompletion', 7), (6.7418, 'HomeHealingCompletion', 9), (5.5261, 'DepartureTriage', 8), (8.0542, 'Arrival', None), (6.9641, 'HospitalHealingCompletion', 4), (5.8578, 'HospitalHealingCompletion', 5), (7.2723, 'DepartureTriage', 2)]
After Event 12: [(5.5261, 'DepartureTriage', 8), (6.7418, 'HomeHealingCompletion', 9), (5.8578, 'HospitalHealingCompletion', 5), (8.0542, 'Arrival', None), (6.9641, 'HospitalHealingCompletion', 4), (7.2723, 'DepartureTriage', 2)]
After Event 13: [(5.8578, 'HospitalHealingCompletion', 5), (6.7418, 'HomeHealingCompletion', 9), (7.2723, 'DepartureTriage', 2), (8.0542, 'Arrival', None), (6.9641, 'HospitalHealingCompletion', 4), (13.4244, 'HospitalHealingCompletion', 8)]
After Event 14: [(6.7418, 'HomeHealingCompletion', 9), (6.9641, 'HospitalHealingCompletion', 4), (7.2723, 'DepartureTriage', 2), (8.0542, 'Arrival', None), (13.4244, 'HospitalHealingCompletion', 8)]
After Event 15: [(6.9641, 'HospitalHealingCompletion', 4), (8.0542, 'Arrival', None), (7.2723, 'DepartureTriage', 2), (13.4244, 'HospitalHealingCompletion', 8)]
After Event 16: [(7.2723, 'DepartureTriage', 2), (8.0542, 'Arrival', None), (13.4244, 'HospitalHealingCompletion', 8)]
After Event 17: [(8.0542, 'Arrival', None), (13.4244, 'HospitalHealingCompletion', 8), (10.2741, 'HospitalHealingCompletion', 2)]
After Event 18: [(8.3724, 'Arrival', None), (10.8532, 'DepartureTriage', 10), (10.2741, 'HospitalHealingCompletion', 2), (13.4244, 'HospitalHealingCompletion', 8)]
After Event 19: [(9.256, 'Arrival', None), (10.2741, 'HospitalHealingCompletion', 2), (13.4244, 'HospitalHealingCompletion', 8), (10.8532, 'DepartureTriage', 10), (10.4295, 'DepartureTriage', 11)]
After Event 20: [(9.3626, 'Arrival', None), (10.2741, 'HospitalHealingCompletion', 2), (10.4336, 'DepartureTriage', 12), (10.8532, 'DepartureTriage', 10), (10.4295, 'DepartureTriage', 11), (13.4244, 'HospitalHealingCompletion', 8)]

Results for half_full initial condition, 20 healed patients:
SimulationLength: 24.265025
TotalPatientsArrived: 20.000000
TotalPatientsHealed: 20.000000
ProbabilityTriageEmpty: 0.059158
ProbabilityBedsEmpty: 0.153646
ProbabilityBothEmpty: 0.000000
RejectionProbability: 0.000000
AverageNurseUtilization: 0.558979
AverageOccupiedBeds: 2.256665
ProportionHomeTreated: 0.300000
AverageHealingTime: 6.353242
```

## Half_full Initial Condition with 200 Target Healed Patients

```

Event Trace for First 20 Events:
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|   Event# |   Time | Event Type                |   PatientID |   Triage Queue |   Busy Nurses |   Occupied Beds |   Total Patients |   Total Healed |
+==========+========+===========================+=============+================+===============+=================+==================+================+
|        1 | 0.5903 | Arrival                   |             |              0 |             3 |               3 |                1 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        2 | 0.9899 | Arrival                   |             |              0 |             4 |               3 |                2 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        3 | 1.2742 | DepartureTriage           |           6 |              0 |             3 |               4 |                2 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        4 | 1.2865 | DepartureTriage           |           1 |              0 |             2 |               5 |                2 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        5 | 1.6501 | DepartureTriage           |           7 |              0 |             1 |               6 |                2 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        6 | 1.6846 | Arrival                   |             |              0 |             2 |               6 |                3 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        7 | 2.0155 | HospitalHealingCompletion |           6 |              0 |             2 |               5 |                3 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        8 | 2.0759 | Arrival                   |             |              0 |             3 |               5 |                4 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        9 | 2.5129 | DepartureTriage           |           9 |              0 |             2 |               5 |                4 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       10 | 3.6095 | HospitalHealingCompletion |           3 |              0 |             2 |               4 |                4 |              2 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       11 | 4.8685 | HospitalHealingCompletion |           1 |              0 |             2 |               3 |                4 |              3 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       12 | 4.8745 | HospitalHealingCompletion |           7 |              0 |             2 |               2 |                4 |              4 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       13 | 5.5261 | DepartureTriage           |           8 |              0 |             1 |               3 |                4 |              4 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       14 | 5.8578 | HospitalHealingCompletion |           5 |              0 |             1 |               2 |                4 |              5 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       15 | 6.7418 | HomeHealingCompletion     |           9 |              0 |             1 |               2 |                4 |              6 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       16 | 6.9641 | HospitalHealingCompletion |           4 |              0 |             1 |               1 |                4 |              7 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       17 | 7.2723 | DepartureTriage           |           2 |              0 |             0 |               2 |                4 |              7 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       18 | 8.0542 | Arrival                   |             |              0 |             1 |               2 |                5 |              7 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       19 | 8.3724 | Arrival                   |             |              0 |             2 |               2 |                6 |              7 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       20 | 9.256  | Arrival                   |             |              0 |             3 |               2 |                7 |              7 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+

Future Event Lists:
After Event 1: [(0.9899, 'Arrival', None), (5.8578, 'HospitalHealingCompletion', 5), (1.2742, 'DepartureTriage', 6), (7.2723, 'DepartureTriage', 2), (6.9641, 'HospitalHealingCompletion', 4), (3.6095, 'HospitalHealingCompletion', 3), (1.2865, 'DepartureTriage', 1)]
After Event 2: [(1.2742, 'DepartureTriage', 6), (1.6501, 'DepartureTriage', 7), (1.2865, 'DepartureTriage', 1), (5.8578, 'HospitalHealingCompletion', 5), (6.9641, 'HospitalHealingCompletion', 4), (3.6095, 'HospitalHealingCompletion', 3), (1.6846, 'Arrival', None), (7.2723, 'DepartureTriage', 2)]
After Event 3: [(1.2865, 'DepartureTriage', 1), (1.6501, 'DepartureTriage', 7), (1.6846, 'Arrival', None), (2.0155, 'HospitalHealingCompletion', 6), (6.9641, 'HospitalHealingCompletion', 4), (3.6095, 'HospitalHealingCompletion', 3), (7.2723, 'DepartureTriage', 2), (5.8578, 'HospitalHealingCompletion', 5)]
After Event 4: [(1.6501, 'DepartureTriage', 7), (2.0155, 'HospitalHealingCompletion', 6), (1.6846, 'Arrival', None), (4.8685, 'HospitalHealingCompletion', 1), (6.9641, 'HospitalHealingCompletion', 4), (3.6095, 'HospitalHealingCompletion', 3), (7.2723, 'DepartureTriage', 2), (5.8578, 'HospitalHealingCompletion', 5)]
After Event 5: [(1.6846, 'Arrival', None), (2.0155, 'HospitalHealingCompletion', 6), (3.6095, 'HospitalHealingCompletion', 3), (4.8685, 'HospitalHealingCompletion', 1), (6.9641, 'HospitalHealingCompletion', 4), (5.8578, 'HospitalHealingCompletion', 5), (7.2723, 'DepartureTriage', 2), (4.8745, 'HospitalHealingCompletion', 7)]
After Event 6: [(2.0155, 'HospitalHealingCompletion', 6), (2.0759, 'Arrival', None), (3.6095, 'HospitalHealingCompletion', 3), (4.8685, 'HospitalHealingCompletion', 1), (6.9641, 'HospitalHealingCompletion', 4), (5.8578, 'HospitalHealingCompletion', 5), (7.2723, 'DepartureTriage', 2), (4.8745, 'HospitalHealingCompletion', 7), (5.5261, 'DepartureTriage', 8)]
After Event 7: [(2.0759, 'Arrival', None), (4.8685, 'HospitalHealingCompletion', 1), (3.6095, 'HospitalHealingCompletion', 3), (4.8745, 'HospitalHealingCompletion', 7), (6.9641, 'HospitalHealingCompletion', 4), (5.8578, 'HospitalHealingCompletion', 5), (7.2723, 'DepartureTriage', 2), (5.5261, 'DepartureTriage', 8)]
After Event 8: [(2.5129, 'DepartureTriage', 9), (3.6095, 'HospitalHealingCompletion', 3), (5.5261, 'DepartureTriage', 8), (4.8685, 'HospitalHealingCompletion', 1), (6.9641, 'HospitalHealingCompletion', 4), (5.8578, 'HospitalHealingCompletion', 5), (7.2723, 'DepartureTriage', 2), (8.0542, 'Arrival', None), (4.8745, 'HospitalHealingCompletion', 7)]
After Event 9: [(3.6095, 'HospitalHealingCompletion', 3), (4.8685, 'HospitalHealingCompletion', 1), (5.5261, 'DepartureTriage', 8), (4.8745, 'HospitalHealingCompletion', 7), (6.9641, 'HospitalHealingCompletion', 4), (5.8578, 'HospitalHealingCompletion', 5), (7.2723, 'DepartureTriage', 2), (8.0542, 'Arrival', None), (6.7418, 'HomeHealingCompletion', 9)]
After Event 10: [(4.8685, 'HospitalHealingCompletion', 1), (4.8745, 'HospitalHealingCompletion', 7), (5.5261, 'DepartureTriage', 8), (6.7418, 'HomeHealingCompletion', 9), (6.9641, 'HospitalHealingCompletion', 4), (5.8578, 'HospitalHealingCompletion', 5), (7.2723, 'DepartureTriage', 2), (8.0542, 'Arrival', None)]
After Event 11: [(4.8745, 'HospitalHealingCompletion', 7), (6.7418, 'HomeHealingCompletion', 9), (5.5261, 'DepartureTriage', 8), (8.0542, 'Arrival', None), (6.9641, 'HospitalHealingCompletion', 4), (5.8578, 'HospitalHealingCompletion', 5), (7.2723, 'DepartureTriage', 2)]
After Event 12: [(5.5261, 'DepartureTriage', 8), (6.7418, 'HomeHealingCompletion', 9), (5.8578, 'HospitalHealingCompletion', 5), (8.0542, 'Arrival', None), (6.9641, 'HospitalHealingCompletion', 4), (7.2723, 'DepartureTriage', 2)]
After Event 13: [(5.8578, 'HospitalHealingCompletion', 5), (6.7418, 'HomeHealingCompletion', 9), (7.2723, 'DepartureTriage', 2), (8.0542, 'Arrival', None), (6.9641, 'HospitalHealingCompletion', 4), (13.4244, 'HospitalHealingCompletion', 8)]
After Event 14: [(6.7418, 'HomeHealingCompletion', 9), (6.9641, 'HospitalHealingCompletion', 4), (7.2723, 'DepartureTriage', 2), (8.0542, 'Arrival', None), (13.4244, 'HospitalHealingCompletion', 8)]
After Event 15: [(6.9641, 'HospitalHealingCompletion', 4), (8.0542, 'Arrival', None), (7.2723, 'DepartureTriage', 2), (13.4244, 'HospitalHealingCompletion', 8)]
After Event 16: [(7.2723, 'DepartureTriage', 2), (8.0542, 'Arrival', None), (13.4244, 'HospitalHealingCompletion', 8)]
After Event 17: [(8.0542, 'Arrival', None), (13.4244, 'HospitalHealingCompletion', 8), (10.2741, 'HospitalHealingCompletion', 2)]
After Event 18: [(8.3724, 'Arrival', None), (10.8532, 'DepartureTriage', 10), (10.2741, 'HospitalHealingCompletion', 2), (13.4244, 'HospitalHealingCompletion', 8)]
After Event 19: [(9.256, 'Arrival', None), (10.2741, 'HospitalHealingCompletion', 2), (13.4244, 'HospitalHealingCompletion', 8), (10.8532, 'DepartureTriage', 10), (10.4295, 'DepartureTriage', 11)]
After Event 20: [(9.3626, 'Arrival', None), (10.2741, 'HospitalHealingCompletion', 2), (10.4336, 'DepartureTriage', 12), (10.8532, 'DepartureTriage', 10), (10.4295, 'DepartureTriage', 11), (13.4244, 'HospitalHealingCompletion', 8)]

Results for half_full initial condition, 200 healed patients:
SimulationLength: 223.178273
TotalPatientsArrived: 200.000000
TotalPatientsHealed: 200.000000
ProbabilityTriageEmpty: 0.093693
ProbabilityBedsEmpty: 0.016705
ProbabilityBothEmpty: 0.000000
RejectionProbability: 0.130435
AverageNurseUtilization: 0.626643
AverageOccupiedBeds: 4.678713
ProportionHomeTreated: 0.310000
AverageHealingTime: 10.711956
```

## Half_full Initial Condition with 1000 Target Healed Patients

```

Event Trace for First 20 Events:
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|   Event# |   Time | Event Type                |   PatientID |   Triage Queue |   Busy Nurses |   Occupied Beds |   Total Patients |   Total Healed |
+==========+========+===========================+=============+================+===============+=================+==================+================+
|        1 | 0.5903 | Arrival                   |             |              0 |             3 |               3 |                1 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        2 | 0.9899 | Arrival                   |             |              0 |             4 |               3 |                2 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        3 | 1.2742 | DepartureTriage           |           6 |              0 |             3 |               4 |                2 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        4 | 1.2865 | DepartureTriage           |           1 |              0 |             2 |               5 |                2 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        5 | 1.6501 | DepartureTriage           |           7 |              0 |             1 |               6 |                2 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        6 | 1.6846 | Arrival                   |             |              0 |             2 |               6 |                3 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        7 | 2.0155 | HospitalHealingCompletion |           6 |              0 |             2 |               5 |                3 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        8 | 2.0759 | Arrival                   |             |              0 |             3 |               5 |                4 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        9 | 2.5129 | DepartureTriage           |           9 |              0 |             2 |               5 |                4 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       10 | 3.6095 | HospitalHealingCompletion |           3 |              0 |             2 |               4 |                4 |              2 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       11 | 4.8685 | HospitalHealingCompletion |           1 |              0 |             2 |               3 |                4 |              3 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       12 | 4.8745 | HospitalHealingCompletion |           7 |              0 |             2 |               2 |                4 |              4 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       13 | 5.5261 | DepartureTriage           |           8 |              0 |             1 |               3 |                4 |              4 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       14 | 5.8578 | HospitalHealingCompletion |           5 |              0 |             1 |               2 |                4 |              5 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       15 | 6.7418 | HomeHealingCompletion     |           9 |              0 |             1 |               2 |                4 |              6 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       16 | 6.9641 | HospitalHealingCompletion |           4 |              0 |             1 |               1 |                4 |              7 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       17 | 7.2723 | DepartureTriage           |           2 |              0 |             0 |               2 |                4 |              7 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       18 | 8.0542 | Arrival                   |             |              0 |             1 |               2 |                5 |              7 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       19 | 8.3724 | Arrival                   |             |              0 |             2 |               2 |                6 |              7 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       20 | 9.256  | Arrival                   |             |              0 |             3 |               2 |                7 |              7 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+

Future Event Lists:
After Event 1: [(0.9899, 'Arrival', None), (5.8578, 'HospitalHealingCompletion', 5), (1.2742, 'DepartureTriage', 6), (7.2723, 'DepartureTriage', 2), (6.9641, 'HospitalHealingCompletion', 4), (3.6095, 'HospitalHealingCompletion', 3), (1.2865, 'DepartureTriage', 1)]
After Event 2: [(1.2742, 'DepartureTriage', 6), (1.6501, 'DepartureTriage', 7), (1.2865, 'DepartureTriage', 1), (5.8578, 'HospitalHealingCompletion', 5), (6.9641, 'HospitalHealingCompletion', 4), (3.6095, 'HospitalHealingCompletion', 3), (1.6846, 'Arrival', None), (7.2723, 'DepartureTriage', 2)]
After Event 3: [(1.2865, 'DepartureTriage', 1), (1.6501, 'DepartureTriage', 7), (1.6846, 'Arrival', None), (2.0155, 'HospitalHealingCompletion', 6), (6.9641, 'HospitalHealingCompletion', 4), (3.6095, 'HospitalHealingCompletion', 3), (7.2723, 'DepartureTriage', 2), (5.8578, 'HospitalHealingCompletion', 5)]
After Event 4: [(1.6501, 'DepartureTriage', 7), (2.0155, 'HospitalHealingCompletion', 6), (1.6846, 'Arrival', None), (4.8685, 'HospitalHealingCompletion', 1), (6.9641, 'HospitalHealingCompletion', 4), (3.6095, 'HospitalHealingCompletion', 3), (7.2723, 'DepartureTriage', 2), (5.8578, 'HospitalHealingCompletion', 5)]
After Event 5: [(1.6846, 'Arrival', None), (2.0155, 'HospitalHealingCompletion', 6), (3.6095, 'HospitalHealingCompletion', 3), (4.8685, 'HospitalHealingCompletion', 1), (6.9641, 'HospitalHealingCompletion', 4), (5.8578, 'HospitalHealingCompletion', 5), (7.2723, 'DepartureTriage', 2), (4.8745, 'HospitalHealingCompletion', 7)]
After Event 6: [(2.0155, 'HospitalHealingCompletion', 6), (2.0759, 'Arrival', None), (3.6095, 'HospitalHealingCompletion', 3), (4.8685, 'HospitalHealingCompletion', 1), (6.9641, 'HospitalHealingCompletion', 4), (5.8578, 'HospitalHealingCompletion', 5), (7.2723, 'DepartureTriage', 2), (4.8745, 'HospitalHealingCompletion', 7), (5.5261, 'DepartureTriage', 8)]
After Event 7: [(2.0759, 'Arrival', None), (4.8685, 'HospitalHealingCompletion', 1), (3.6095, 'HospitalHealingCompletion', 3), (4.8745, 'HospitalHealingCompletion', 7), (6.9641, 'HospitalHealingCompletion', 4), (5.8578, 'HospitalHealingCompletion', 5), (7.2723, 'DepartureTriage', 2), (5.5261, 'DepartureTriage', 8)]
After Event 8: [(2.5129, 'DepartureTriage', 9), (3.6095, 'HospitalHealingCompletion', 3), (5.5261, 'DepartureTriage', 8), (4.8685, 'HospitalHealingCompletion', 1), (6.9641, 'HospitalHealingCompletion', 4), (5.8578, 'HospitalHealingCompletion', 5), (7.2723, 'DepartureTriage', 2), (8.0542, 'Arrival', None), (4.8745, 'HospitalHealingCompletion', 7)]
After Event 9: [(3.6095, 'HospitalHealingCompletion', 3), (4.8685, 'HospitalHealingCompletion', 1), (5.5261, 'DepartureTriage', 8), (4.8745, 'HospitalHealingCompletion', 7), (6.9641, 'HospitalHealingCompletion', 4), (5.8578, 'HospitalHealingCompletion', 5), (7.2723, 'DepartureTriage', 2), (8.0542, 'Arrival', None), (6.7418, 'HomeHealingCompletion', 9)]
After Event 10: [(4.8685, 'HospitalHealingCompletion', 1), (4.8745, 'HospitalHealingCompletion', 7), (5.5261, 'DepartureTriage', 8), (6.7418, 'HomeHealingCompletion', 9), (6.9641, 'HospitalHealingCompletion', 4), (5.8578, 'HospitalHealingCompletion', 5), (7.2723, 'DepartureTriage', 2), (8.0542, 'Arrival', None)]
After Event 11: [(4.8745, 'HospitalHealingCompletion', 7), (6.7418, 'HomeHealingCompletion', 9), (5.5261, 'DepartureTriage', 8), (8.0542, 'Arrival', None), (6.9641, 'HospitalHealingCompletion', 4), (5.8578, 'HospitalHealingCompletion', 5), (7.2723, 'DepartureTriage', 2)]
After Event 12: [(5.5261, 'DepartureTriage', 8), (6.7418, 'HomeHealingCompletion', 9), (5.8578, 'HospitalHealingCompletion', 5), (8.0542, 'Arrival', None), (6.9641, 'HospitalHealingCompletion', 4), (7.2723, 'DepartureTriage', 2)]
After Event 13: [(5.8578, 'HospitalHealingCompletion', 5), (6.7418, 'HomeHealingCompletion', 9), (7.2723, 'DepartureTriage', 2), (8.0542, 'Arrival', None), (6.9641, 'HospitalHealingCompletion', 4), (13.4244, 'HospitalHealingCompletion', 8)]
After Event 14: [(6.7418, 'HomeHealingCompletion', 9), (6.9641, 'HospitalHealingCompletion', 4), (7.2723, 'DepartureTriage', 2), (8.0542, 'Arrival', None), (13.4244, 'HospitalHealingCompletion', 8)]
After Event 15: [(6.9641, 'HospitalHealingCompletion', 4), (8.0542, 'Arrival', None), (7.2723, 'DepartureTriage', 2), (13.4244, 'HospitalHealingCompletion', 8)]
After Event 16: [(7.2723, 'DepartureTriage', 2), (8.0542, 'Arrival', None), (13.4244, 'HospitalHealingCompletion', 8)]
After Event 17: [(8.0542, 'Arrival', None), (13.4244, 'HospitalHealingCompletion', 8), (10.2741, 'HospitalHealingCompletion', 2)]
After Event 18: [(8.3724, 'Arrival', None), (10.8532, 'DepartureTriage', 10), (10.2741, 'HospitalHealingCompletion', 2), (13.4244, 'HospitalHealingCompletion', 8)]
After Event 19: [(9.256, 'Arrival', None), (10.2741, 'HospitalHealingCompletion', 2), (13.4244, 'HospitalHealingCompletion', 8), (10.8532, 'DepartureTriage', 10), (10.4295, 'DepartureTriage', 11)]
After Event 20: [(9.3626, 'Arrival', None), (10.2741, 'HospitalHealingCompletion', 2), (10.4336, 'DepartureTriage', 12), (10.8532, 'DepartureTriage', 10), (10.4295, 'DepartureTriage', 11), (13.4244, 'HospitalHealingCompletion', 8)]

Results for half_full initial condition, 1000 healed patients:
SimulationLength: 1039.520770
TotalPatientsArrived: 1012.000000
TotalPatientsHealed: 1000.000000
ProbabilityTriageEmpty: 0.042439
ProbabilityBedsEmpty: 0.017336
ProbabilityBothEmpty: 0.000000
RejectionProbability: 0.149485
AverageNurseUtilization: 0.724040
AverageOccupiedBeds: 4.508593
ProportionHomeTreated: 0.340000
AverageHealingTime: 11.428489
```

## Full Initial Condition with 20 Target Healed Patients

```

Event Trace for First 20 Events:
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|   Event# |   Time | Event Type                |   PatientID |   Triage Queue |   Busy Nurses |   Occupied Beds |   Total Patients |   Total Healed |
+==========+========+===========================+=============+================+===============+=================+==================+================+
|        1 | 0.1135 | Arrival                   |             |              1 |             4 |               7 |                1 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        2 | 0.4004 | Arrival                   |             |              2 |             4 |               7 |                2 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        3 | 0.9487 | Arrival                   |             |              3 |             4 |               7 |                3 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        4 | 0.9673 | Arrival                   |             |              4 |             4 |               7 |                4 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        5 | 1.2865 | DepartureTriage           |           1 |              3 |             4 |               7 |                4 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        6 | 1.4379 | HospitalHealingCompletion |          10 |              3 |             4 |               6 |                4 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        7 | 1.4608 | Arrival                   |             |              4 |             4 |               6 |                5 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        8 | 1.4893 | HospitalHealingCompletion |           8 |              4 |             4 |               5 |                5 |              2 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        9 | 1.6574 | DepartureTriage           |           3 |              3 |             4 |               6 |                5 |              2 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       10 | 1.7235 | DepartureTriage           |          12 |              2 |             4 |               7 |                5 |              2 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       11 | 2.6104 | HospitalHealingCompletion |           7 |              2 |             4 |               6 |                5 |              3 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       12 | 2.6783 | DepartureTriage           |          14 |              1 |             4 |               7 |                5 |              3 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       13 | 3.1978 | DepartureTriage           |           4 |              0 |             4 |               7 |                5 |              3 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       14 | 3.3922 | HospitalHealingCompletion |          11 |              0 |             4 |               6 |                5 |              4 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       15 | 3.8567 | HospitalHealingCompletion |           6 |              0 |             4 |               5 |                5 |              5 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       16 | 3.899  | Arrival                   |             |              1 |             4 |               5 |                6 |              5 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       17 | 4.1303 | Arrival                   |             |              2 |             4 |               5 |                7 |              5 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       18 | 4.539  | HospitalHealingCompletion |           9 |              2 |             4 |               4 |                7 |              6 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       19 | 4.7254 | HospitalHealingCompletion |          12 |              2 |             4 |               3 |                7 |              7 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       20 | 4.7353 | DepartureTriage           |          15 |              1 |             4 |               3 |                7 |              7 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+

Future Event Lists:
After Event 1: [(0.4004, 'Arrival', None), (1.4379, 'HospitalHealingCompletion', 10), (1.2865, 'DepartureTriage', 1), (3.1978, 'DepartureTriage', 4), (1.4893, 'HospitalHealingCompletion', 8), (1.6574, 'DepartureTriage', 3), (2.6104, 'HospitalHealingCompletion', 7), (7.2723, 'DepartureTriage', 2), (4.539, 'HospitalHealingCompletion', 9), (5.8578, 'HospitalHealingCompletion', 5), (3.3922, 'HospitalHealingCompletion', 11), (3.8567, 'HospitalHealingCompletion', 6)]
After Event 2: [(0.9487, 'Arrival', None), (1.4379, 'HospitalHealingCompletion', 10), (1.2865, 'DepartureTriage', 1), (3.1978, 'DepartureTriage', 4), (1.4893, 'HospitalHealingCompletion', 8), (1.6574, 'DepartureTriage', 3), (2.6104, 'HospitalHealingCompletion', 7), (7.2723, 'DepartureTriage', 2), (4.539, 'HospitalHealingCompletion', 9), (5.8578, 'HospitalHealingCompletion', 5), (3.3922, 'HospitalHealingCompletion', 11), (3.8567, 'HospitalHealingCompletion', 6)]
After Event 3: [(0.9673, 'Arrival', None), (1.4379, 'HospitalHealingCompletion', 10), (1.2865, 'DepartureTriage', 1), (3.1978, 'DepartureTriage', 4), (1.4893, 'HospitalHealingCompletion', 8), (1.6574, 'DepartureTriage', 3), (2.6104, 'HospitalHealingCompletion', 7), (7.2723, 'DepartureTriage', 2), (4.539, 'HospitalHealingCompletion', 9), (5.8578, 'HospitalHealingCompletion', 5), (3.3922, 'HospitalHealingCompletion', 11), (3.8567, 'HospitalHealingCompletion', 6)]
After Event 4: [(1.2865, 'DepartureTriage', 1), (1.4379, 'HospitalHealingCompletion', 10), (1.4608, 'Arrival', None), (3.1978, 'DepartureTriage', 4), (1.4893, 'HospitalHealingCompletion', 8), (1.6574, 'DepartureTriage', 3), (2.6104, 'HospitalHealingCompletion', 7), (7.2723, 'DepartureTriage', 2), (4.539, 'HospitalHealingCompletion', 9), (5.8578, 'HospitalHealingCompletion', 5), (3.3922, 'HospitalHealingCompletion', 11), (3.8567, 'HospitalHealingCompletion', 6)]
After Event 5: [(1.4379, 'HospitalHealingCompletion', 10), (1.4893, 'HospitalHealingCompletion', 8), (1.4608, 'Arrival', None), (3.1978, 'DepartureTriage', 4), (3.3922, 'HospitalHealingCompletion', 11), (1.6574, 'DepartureTriage', 3), (2.6104, 'HospitalHealingCompletion', 7), (7.2723, 'DepartureTriage', 2), (4.539, 'HospitalHealingCompletion', 9), (5.8578, 'HospitalHealingCompletion', 5), (3.8567, 'HospitalHealingCompletion', 6), (11.7543, 'HomeHealingCompletion', 1), (1.7235, 'DepartureTriage', 12)]
After Event 6: [(1.4608, 'Arrival', None), (1.4893, 'HospitalHealingCompletion', 8), (1.6574, 'DepartureTriage', 3), (3.1978, 'DepartureTriage', 4), (3.3922, 'HospitalHealingCompletion', 11), (1.7235, 'DepartureTriage', 12), (2.6104, 'HospitalHealingCompletion', 7), (7.2723, 'DepartureTriage', 2), (4.539, 'HospitalHealingCompletion', 9), (5.8578, 'HospitalHealingCompletion', 5), (3.8567, 'HospitalHealingCompletion', 6), (11.7543, 'HomeHealingCompletion', 1)]
After Event 7: [(1.4893, 'HospitalHealingCompletion', 8), (3.1978, 'DepartureTriage', 4), (1.6574, 'DepartureTriage', 3), (4.539, 'HospitalHealingCompletion', 9), (3.3922, 'HospitalHealingCompletion', 11), (1.7235, 'DepartureTriage', 12), (2.6104, 'HospitalHealingCompletion', 7), (7.2723, 'DepartureTriage', 2), (11.7543, 'HomeHealingCompletion', 1), (5.8578, 'HospitalHealingCompletion', 5), (3.8567, 'HospitalHealingCompletion', 6), (3.899, 'Arrival', None)]
After Event 8: [(1.6574, 'DepartureTriage', 3), (3.1978, 'DepartureTriage', 4), (1.7235, 'DepartureTriage', 12), (4.539, 'HospitalHealingCompletion', 9), (3.3922, 'HospitalHealingCompletion', 11), (3.899, 'Arrival', None), (2.6104, 'HospitalHealingCompletion', 7), (7.2723, 'DepartureTriage', 2), (11.7543, 'HomeHealingCompletion', 1), (5.8578, 'HospitalHealingCompletion', 5), (3.8567, 'HospitalHealingCompletion', 6)]
After Event 9: [(1.7235, 'DepartureTriage', 12), (3.1978, 'DepartureTriage', 4), (2.6104, 'HospitalHealingCompletion', 7), (4.539, 'HospitalHealingCompletion', 9), (3.3922, 'HospitalHealingCompletion', 11), (3.899, 'Arrival', None), (3.8567, 'HospitalHealingCompletion', 6), (7.2723, 'DepartureTriage', 2), (11.7543, 'HomeHealingCompletion', 1), (5.8578, 'HospitalHealingCompletion', 5), (9.3703, 'HospitalHealingCompletion', 3), (5.2843, 'DepartureTriage', 13)]
After Event 10: [(2.6104, 'HospitalHealingCompletion', 7), (3.1978, 'DepartureTriage', 4), (2.6783, 'DepartureTriage', 14), (4.539, 'HospitalHealingCompletion', 9), (3.3922, 'HospitalHealingCompletion', 11), (3.8567, 'HospitalHealingCompletion', 6), (5.2843, 'DepartureTriage', 13), (7.2723, 'DepartureTriage', 2), (11.7543, 'HomeHealingCompletion', 1), (5.8578, 'HospitalHealingCompletion', 5), (9.3703, 'HospitalHealingCompletion', 3), (4.7254, 'HospitalHealingCompletion', 12), (3.899, 'Arrival', None)]
After Event 11: [(2.6783, 'DepartureTriage', 14), (3.1978, 'DepartureTriage', 4), (3.8567, 'HospitalHealingCompletion', 6), (4.539, 'HospitalHealingCompletion', 9), (3.3922, 'HospitalHealingCompletion', 11), (3.899, 'Arrival', None), (5.2843, 'DepartureTriage', 13), (7.2723, 'DepartureTriage', 2), (11.7543, 'HomeHealingCompletion', 1), (5.8578, 'HospitalHealingCompletion', 5), (9.3703, 'HospitalHealingCompletion', 3), (4.7254, 'HospitalHealingCompletion', 12)]
After Event 12: [(3.1978, 'DepartureTriage', 4), (3.3922, 'HospitalHealingCompletion', 11), (3.8567, 'HospitalHealingCompletion', 6), (4.539, 'HospitalHealingCompletion', 9), (4.7254, 'HospitalHealingCompletion', 12), (3.899, 'Arrival', None), (5.2843, 'DepartureTriage', 13), (7.2723, 'DepartureTriage', 2), (11.7543, 'HomeHealingCompletion', 1), (5.8578, 'HospitalHealingCompletion', 5), (9.3703, 'HospitalHealingCompletion', 3), (8.451, 'HospitalHealingCompletion', 14), (4.7353, 'DepartureTriage', 15)]
After Event 13: [(3.3922, 'HospitalHealingCompletion', 11), (4.539, 'HospitalHealingCompletion', 9), (3.8567, 'HospitalHealingCompletion', 6), (4.7353, 'DepartureTriage', 15), (4.7254, 'HospitalHealingCompletion', 12), (3.899, 'Arrival', None), (5.2843, 'DepartureTriage', 13), (7.2723, 'DepartureTriage', 2), (11.7543, 'HomeHealingCompletion', 1), (5.8578, 'HospitalHealingCompletion', 5), (9.3703, 'HospitalHealingCompletion', 3), (8.451, 'HospitalHealingCompletion', 14), (7.426, 'HomeHealingCompletion', 4), (11.0828, 'DepartureTriage', 16)]
After Event 14: [(3.8567, 'HospitalHealingCompletion', 6), (4.539, 'HospitalHealingCompletion', 9), (3.899, 'Arrival', None), (4.7353, 'DepartureTriage', 15), (4.7254, 'HospitalHealingCompletion', 12), (7.426, 'HomeHealingCompletion', 4), (5.2843, 'DepartureTriage', 13), (7.2723, 'DepartureTriage', 2), (11.7543, 'HomeHealingCompletion', 1), (5.8578, 'HospitalHealingCompletion', 5), (9.3703, 'HospitalHealingCompletion', 3), (8.451, 'HospitalHealingCompletion', 14), (11.0828, 'DepartureTriage', 16)]
After Event 15: [(3.899, 'Arrival', None), (4.539, 'HospitalHealingCompletion', 9), (5.2843, 'DepartureTriage', 13), (4.7353, 'DepartureTriage', 15), (4.7254, 'HospitalHealingCompletion', 12), (7.426, 'HomeHealingCompletion', 4), (11.0828, 'DepartureTriage', 16), (7.2723, 'DepartureTriage', 2), (11.7543, 'HomeHealingCompletion', 1), (5.8578, 'HospitalHealingCompletion', 5), (9.3703, 'HospitalHealingCompletion', 3), (8.451, 'HospitalHealingCompletion', 14)]
After Event 16: [(4.1303, 'Arrival', None), (4.7254, 'HospitalHealingCompletion', 12), (4.539, 'HospitalHealingCompletion', 9), (4.7353, 'DepartureTriage', 15), (5.8578, 'HospitalHealingCompletion', 5), (5.2843, 'DepartureTriage', 13), (11.0828, 'DepartureTriage', 16), (7.2723, 'DepartureTriage', 2), (11.7543, 'HomeHealingCompletion', 1), (8.451, 'HospitalHealingCompletion', 14), (9.3703, 'HospitalHealingCompletion', 3), (7.426, 'HomeHealingCompletion', 4)]
After Event 17: [(4.539, 'HospitalHealingCompletion', 9), (4.7254, 'HospitalHealingCompletion', 12), (5.2071, 'Arrival', None), (4.7353, 'DepartureTriage', 15), (5.8578, 'HospitalHealingCompletion', 5), (5.2843, 'DepartureTriage', 13), (11.0828, 'DepartureTriage', 16), (7.2723, 'DepartureTriage', 2), (11.7543, 'HomeHealingCompletion', 1), (8.451, 'HospitalHealingCompletion', 14), (9.3703, 'HospitalHealingCompletion', 3), (7.426, 'HomeHealingCompletion', 4)]
After Event 18: [(4.7254, 'HospitalHealingCompletion', 12), (4.7353, 'DepartureTriage', 15), (5.2071, 'Arrival', None), (7.2723, 'DepartureTriage', 2), (5.8578, 'HospitalHealingCompletion', 5), (5.2843, 'DepartureTriage', 13), (11.0828, 'DepartureTriage', 16), (7.426, 'HomeHealingCompletion', 4), (11.7543, 'HomeHealingCompletion', 1), (8.451, 'HospitalHealingCompletion', 14), (9.3703, 'HospitalHealingCompletion', 3)]
After Event 19: [(4.7353, 'DepartureTriage', 15), (5.8578, 'HospitalHealingCompletion', 5), (5.2071, 'Arrival', None), (7.2723, 'DepartureTriage', 2), (8.451, 'HospitalHealingCompletion', 14), (5.2843, 'DepartureTriage', 13), (11.0828, 'DepartureTriage', 16), (7.426, 'HomeHealingCompletion', 4), (11.7543, 'HomeHealingCompletion', 1), (9.3703, 'HospitalHealingCompletion', 3)]
After Event 20: [(5.2071, 'Arrival', None), (5.8578, 'HospitalHealingCompletion', 5), (5.2843, 'DepartureTriage', 13), (7.2723, 'DepartureTriage', 2), (6.4817, 'DepartureTriage', 17), (9.3703, 'HospitalHealingCompletion', 3), (11.0828, 'DepartureTriage', 16), (7.426, 'HomeHealingCompletion', 4), (11.7543, 'HomeHealingCompletion', 1), (13.5047, 'HomeHealingCompletion', 15), (8.451, 'HospitalHealingCompletion', 14)]

Results for full initial condition, 20 healed patients:
SimulationLength: 16.500198
TotalPatientsArrived: 13.000000
TotalPatientsHealed: 20.000000
ProbabilityTriageEmpty: 0.025613
ProbabilityBedsEmpty: 0.000000
ProbabilityBothEmpty: 0.000000
RejectionProbability: 0.153846
AverageNurseUtilization: 0.678716
AverageOccupiedBeds: 3.706623
ProportionHomeTreated: 0.300000
AverageHealingTime: 5.990347
```

## Full Initial Condition with 200 Target Healed Patients

```

Event Trace for First 20 Events:
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|   Event# |   Time | Event Type                |   PatientID |   Triage Queue |   Busy Nurses |   Occupied Beds |   Total Patients |   Total Healed |
+==========+========+===========================+=============+================+===============+=================+==================+================+
|        1 | 0.1135 | Arrival                   |             |              1 |             4 |               7 |                1 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        2 | 0.4004 | Arrival                   |             |              2 |             4 |               7 |                2 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        3 | 0.9487 | Arrival                   |             |              3 |             4 |               7 |                3 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        4 | 0.9673 | Arrival                   |             |              4 |             4 |               7 |                4 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        5 | 1.2865 | DepartureTriage           |           1 |              3 |             4 |               7 |                4 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        6 | 1.4379 | HospitalHealingCompletion |          10 |              3 |             4 |               6 |                4 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        7 | 1.4608 | Arrival                   |             |              4 |             4 |               6 |                5 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        8 | 1.4893 | HospitalHealingCompletion |           8 |              4 |             4 |               5 |                5 |              2 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        9 | 1.6574 | DepartureTriage           |           3 |              3 |             4 |               6 |                5 |              2 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       10 | 1.7235 | DepartureTriage           |          12 |              2 |             4 |               7 |                5 |              2 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       11 | 2.6104 | HospitalHealingCompletion |           7 |              2 |             4 |               6 |                5 |              3 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       12 | 2.6783 | DepartureTriage           |          14 |              1 |             4 |               7 |                5 |              3 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       13 | 3.1978 | DepartureTriage           |           4 |              0 |             4 |               7 |                5 |              3 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       14 | 3.3922 | HospitalHealingCompletion |          11 |              0 |             4 |               6 |                5 |              4 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       15 | 3.8567 | HospitalHealingCompletion |           6 |              0 |             4 |               5 |                5 |              5 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       16 | 3.899  | Arrival                   |             |              1 |             4 |               5 |                6 |              5 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       17 | 4.1303 | Arrival                   |             |              2 |             4 |               5 |                7 |              5 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       18 | 4.539  | HospitalHealingCompletion |           9 |              2 |             4 |               4 |                7 |              6 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       19 | 4.7254 | HospitalHealingCompletion |          12 |              2 |             4 |               3 |                7 |              7 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       20 | 4.7353 | DepartureTriage           |          15 |              1 |             4 |               3 |                7 |              7 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+

Future Event Lists:
After Event 1: [(0.4004, 'Arrival', None), (1.4379, 'HospitalHealingCompletion', 10), (1.2865, 'DepartureTriage', 1), (3.1978, 'DepartureTriage', 4), (1.4893, 'HospitalHealingCompletion', 8), (1.6574, 'DepartureTriage', 3), (2.6104, 'HospitalHealingCompletion', 7), (7.2723, 'DepartureTriage', 2), (4.539, 'HospitalHealingCompletion', 9), (5.8578, 'HospitalHealingCompletion', 5), (3.3922, 'HospitalHealingCompletion', 11), (3.8567, 'HospitalHealingCompletion', 6)]
After Event 2: [(0.9487, 'Arrival', None), (1.4379, 'HospitalHealingCompletion', 10), (1.2865, 'DepartureTriage', 1), (3.1978, 'DepartureTriage', 4), (1.4893, 'HospitalHealingCompletion', 8), (1.6574, 'DepartureTriage', 3), (2.6104, 'HospitalHealingCompletion', 7), (7.2723, 'DepartureTriage', 2), (4.539, 'HospitalHealingCompletion', 9), (5.8578, 'HospitalHealingCompletion', 5), (3.3922, 'HospitalHealingCompletion', 11), (3.8567, 'HospitalHealingCompletion', 6)]
After Event 3: [(0.9673, 'Arrival', None), (1.4379, 'HospitalHealingCompletion', 10), (1.2865, 'DepartureTriage', 1), (3.1978, 'DepartureTriage', 4), (1.4893, 'HospitalHealingCompletion', 8), (1.6574, 'DepartureTriage', 3), (2.6104, 'HospitalHealingCompletion', 7), (7.2723, 'DepartureTriage', 2), (4.539, 'HospitalHealingCompletion', 9), (5.8578, 'HospitalHealingCompletion', 5), (3.3922, 'HospitalHealingCompletion', 11), (3.8567, 'HospitalHealingCompletion', 6)]
After Event 4: [(1.2865, 'DepartureTriage', 1), (1.4379, 'HospitalHealingCompletion', 10), (1.4608, 'Arrival', None), (3.1978, 'DepartureTriage', 4), (1.4893, 'HospitalHealingCompletion', 8), (1.6574, 'DepartureTriage', 3), (2.6104, 'HospitalHealingCompletion', 7), (7.2723, 'DepartureTriage', 2), (4.539, 'HospitalHealingCompletion', 9), (5.8578, 'HospitalHealingCompletion', 5), (3.3922, 'HospitalHealingCompletion', 11), (3.8567, 'HospitalHealingCompletion', 6)]
After Event 5: [(1.4379, 'HospitalHealingCompletion', 10), (1.4893, 'HospitalHealingCompletion', 8), (1.4608, 'Arrival', None), (3.1978, 'DepartureTriage', 4), (3.3922, 'HospitalHealingCompletion', 11), (1.6574, 'DepartureTriage', 3), (2.6104, 'HospitalHealingCompletion', 7), (7.2723, 'DepartureTriage', 2), (4.539, 'HospitalHealingCompletion', 9), (5.8578, 'HospitalHealingCompletion', 5), (3.8567, 'HospitalHealingCompletion', 6), (11.7543, 'HomeHealingCompletion', 1), (1.7235, 'DepartureTriage', 12)]
After Event 6: [(1.4608, 'Arrival', None), (1.4893, 'HospitalHealingCompletion', 8), (1.6574, 'DepartureTriage', 3), (3.1978, 'DepartureTriage', 4), (3.3922, 'HospitalHealingCompletion', 11), (1.7235, 'DepartureTriage', 12), (2.6104, 'HospitalHealingCompletion', 7), (7.2723, 'DepartureTriage', 2), (4.539, 'HospitalHealingCompletion', 9), (5.8578, 'HospitalHealingCompletion', 5), (3.8567, 'HospitalHealingCompletion', 6), (11.7543, 'HomeHealingCompletion', 1)]
After Event 7: [(1.4893, 'HospitalHealingCompletion', 8), (3.1978, 'DepartureTriage', 4), (1.6574, 'DepartureTriage', 3), (4.539, 'HospitalHealingCompletion', 9), (3.3922, 'HospitalHealingCompletion', 11), (1.7235, 'DepartureTriage', 12), (2.6104, 'HospitalHealingCompletion', 7), (7.2723, 'DepartureTriage', 2), (11.7543, 'HomeHealingCompletion', 1), (5.8578, 'HospitalHealingCompletion', 5), (3.8567, 'HospitalHealingCompletion', 6), (3.899, 'Arrival', None)]
After Event 8: [(1.6574, 'DepartureTriage', 3), (3.1978, 'DepartureTriage', 4), (1.7235, 'DepartureTriage', 12), (4.539, 'HospitalHealingCompletion', 9), (3.3922, 'HospitalHealingCompletion', 11), (3.899, 'Arrival', None), (2.6104, 'HospitalHealingCompletion', 7), (7.2723, 'DepartureTriage', 2), (11.7543, 'HomeHealingCompletion', 1), (5.8578, 'HospitalHealingCompletion', 5), (3.8567, 'HospitalHealingCompletion', 6)]
After Event 9: [(1.7235, 'DepartureTriage', 12), (3.1978, 'DepartureTriage', 4), (2.6104, 'HospitalHealingCompletion', 7), (4.539, 'HospitalHealingCompletion', 9), (3.3922, 'HospitalHealingCompletion', 11), (3.899, 'Arrival', None), (3.8567, 'HospitalHealingCompletion', 6), (7.2723, 'DepartureTriage', 2), (11.7543, 'HomeHealingCompletion', 1), (5.8578, 'HospitalHealingCompletion', 5), (9.3703, 'HospitalHealingCompletion', 3), (5.2843, 'DepartureTriage', 13)]
After Event 10: [(2.6104, 'HospitalHealingCompletion', 7), (3.1978, 'DepartureTriage', 4), (2.6783, 'DepartureTriage', 14), (4.539, 'HospitalHealingCompletion', 9), (3.3922, 'HospitalHealingCompletion', 11), (3.8567, 'HospitalHealingCompletion', 6), (5.2843, 'DepartureTriage', 13), (7.2723, 'DepartureTriage', 2), (11.7543, 'HomeHealingCompletion', 1), (5.8578, 'HospitalHealingCompletion', 5), (9.3703, 'HospitalHealingCompletion', 3), (4.7254, 'HospitalHealingCompletion', 12), (3.899, 'Arrival', None)]
After Event 11: [(2.6783, 'DepartureTriage', 14), (3.1978, 'DepartureTriage', 4), (3.8567, 'HospitalHealingCompletion', 6), (4.539, 'HospitalHealingCompletion', 9), (3.3922, 'HospitalHealingCompletion', 11), (3.899, 'Arrival', None), (5.2843, 'DepartureTriage', 13), (7.2723, 'DepartureTriage', 2), (11.7543, 'HomeHealingCompletion', 1), (5.8578, 'HospitalHealingCompletion', 5), (9.3703, 'HospitalHealingCompletion', 3), (4.7254, 'HospitalHealingCompletion', 12)]
After Event 12: [(3.1978, 'DepartureTriage', 4), (3.3922, 'HospitalHealingCompletion', 11), (3.8567, 'HospitalHealingCompletion', 6), (4.539, 'HospitalHealingCompletion', 9), (4.7254, 'HospitalHealingCompletion', 12), (3.899, 'Arrival', None), (5.2843, 'DepartureTriage', 13), (7.2723, 'DepartureTriage', 2), (11.7543, 'HomeHealingCompletion', 1), (5.8578, 'HospitalHealingCompletion', 5), (9.3703, 'HospitalHealingCompletion', 3), (8.451, 'HospitalHealingCompletion', 14), (4.7353, 'DepartureTriage', 15)]
After Event 13: [(3.3922, 'HospitalHealingCompletion', 11), (4.539, 'HospitalHealingCompletion', 9), (3.8567, 'HospitalHealingCompletion', 6), (4.7353, 'DepartureTriage', 15), (4.7254, 'HospitalHealingCompletion', 12), (3.899, 'Arrival', None), (5.2843, 'DepartureTriage', 13), (7.2723, 'DepartureTriage', 2), (11.7543, 'HomeHealingCompletion', 1), (5.8578, 'HospitalHealingCompletion', 5), (9.3703, 'HospitalHealingCompletion', 3), (8.451, 'HospitalHealingCompletion', 14), (7.426, 'HomeHealingCompletion', 4), (11.0828, 'DepartureTriage', 16)]
After Event 14: [(3.8567, 'HospitalHealingCompletion', 6), (4.539, 'HospitalHealingCompletion', 9), (3.899, 'Arrival', None), (4.7353, 'DepartureTriage', 15), (4.7254, 'HospitalHealingCompletion', 12), (7.426, 'HomeHealingCompletion', 4), (5.2843, 'DepartureTriage', 13), (7.2723, 'DepartureTriage', 2), (11.7543, 'HomeHealingCompletion', 1), (5.8578, 'HospitalHealingCompletion', 5), (9.3703, 'HospitalHealingCompletion', 3), (8.451, 'HospitalHealingCompletion', 14), (11.0828, 'DepartureTriage', 16)]
After Event 15: [(3.899, 'Arrival', None), (4.539, 'HospitalHealingCompletion', 9), (5.2843, 'DepartureTriage', 13), (4.7353, 'DepartureTriage', 15), (4.7254, 'HospitalHealingCompletion', 12), (7.426, 'HomeHealingCompletion', 4), (11.0828, 'DepartureTriage', 16), (7.2723, 'DepartureTriage', 2), (11.7543, 'HomeHealingCompletion', 1), (5.8578, 'HospitalHealingCompletion', 5), (9.3703, 'HospitalHealingCompletion', 3), (8.451, 'HospitalHealingCompletion', 14)]
After Event 16: [(4.1303, 'Arrival', None), (4.7254, 'HospitalHealingCompletion', 12), (4.539, 'HospitalHealingCompletion', 9), (4.7353, 'DepartureTriage', 15), (5.8578, 'HospitalHealingCompletion', 5), (5.2843, 'DepartureTriage', 13), (11.0828, 'DepartureTriage', 16), (7.2723, 'DepartureTriage', 2), (11.7543, 'HomeHealingCompletion', 1), (8.451, 'HospitalHealingCompletion', 14), (9.3703, 'HospitalHealingCompletion', 3), (7.426, 'HomeHealingCompletion', 4)]
After Event 17: [(4.539, 'HospitalHealingCompletion', 9), (4.7254, 'HospitalHealingCompletion', 12), (5.2071, 'Arrival', None), (4.7353, 'DepartureTriage', 15), (5.8578, 'HospitalHealingCompletion', 5), (5.2843, 'DepartureTriage', 13), (11.0828, 'DepartureTriage', 16), (7.2723, 'DepartureTriage', 2), (11.7543, 'HomeHealingCompletion', 1), (8.451, 'HospitalHealingCompletion', 14), (9.3703, 'HospitalHealingCompletion', 3), (7.426, 'HomeHealingCompletion', 4)]
After Event 18: [(4.7254, 'HospitalHealingCompletion', 12), (4.7353, 'DepartureTriage', 15), (5.2071, 'Arrival', None), (7.2723, 'DepartureTriage', 2), (5.8578, 'HospitalHealingCompletion', 5), (5.2843, 'DepartureTriage', 13), (11.0828, 'DepartureTriage', 16), (7.426, 'HomeHealingCompletion', 4), (11.7543, 'HomeHealingCompletion', 1), (8.451, 'HospitalHealingCompletion', 14), (9.3703, 'HospitalHealingCompletion', 3)]
After Event 19: [(4.7353, 'DepartureTriage', 15), (5.8578, 'HospitalHealingCompletion', 5), (5.2071, 'Arrival', None), (7.2723, 'DepartureTriage', 2), (8.451, 'HospitalHealingCompletion', 14), (5.2843, 'DepartureTriage', 13), (11.0828, 'DepartureTriage', 16), (7.426, 'HomeHealingCompletion', 4), (11.7543, 'HomeHealingCompletion', 1), (9.3703, 'HospitalHealingCompletion', 3)]
After Event 20: [(5.2071, 'Arrival', None), (5.8578, 'HospitalHealingCompletion', 5), (5.2843, 'DepartureTriage', 13), (7.2723, 'DepartureTriage', 2), (6.4817, 'DepartureTriage', 17), (9.3703, 'HospitalHealingCompletion', 3), (11.0828, 'DepartureTriage', 16), (7.426, 'HomeHealingCompletion', 4), (11.7543, 'HomeHealingCompletion', 1), (13.5047, 'HomeHealingCompletion', 15), (8.451, 'HospitalHealingCompletion', 14)]

Results for full initial condition, 200 healed patients:
SimulationLength: 212.565076
TotalPatientsArrived: 204.000000
TotalPatientsHealed: 200.000000
ProbabilityTriageEmpty: 0.068743
ProbabilityBedsEmpty: 0.000000
ProbabilityBothEmpty: 0.000000
RejectionProbability: 0.086667
AverageNurseUtilization: 0.670338
AverageOccupiedBeds: 4.313736
ProportionHomeTreated: 0.320000
AverageHealingTime: 9.229651
```

## Full Initial Condition with 1000 Target Healed Patients

```

Event Trace for First 20 Events:
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|   Event# |   Time | Event Type                |   PatientID |   Triage Queue |   Busy Nurses |   Occupied Beds |   Total Patients |   Total Healed |
+==========+========+===========================+=============+================+===============+=================+==================+================+
|        1 | 0.1135 | Arrival                   |             |              1 |             4 |               7 |                1 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        2 | 0.4004 | Arrival                   |             |              2 |             4 |               7 |                2 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        3 | 0.9487 | Arrival                   |             |              3 |             4 |               7 |                3 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        4 | 0.9673 | Arrival                   |             |              4 |             4 |               7 |                4 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        5 | 1.2865 | DepartureTriage           |           1 |              3 |             4 |               7 |                4 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        6 | 1.4379 | HospitalHealingCompletion |          10 |              3 |             4 |               6 |                4 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        7 | 1.4608 | Arrival                   |             |              4 |             4 |               6 |                5 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        8 | 1.4893 | HospitalHealingCompletion |           8 |              4 |             4 |               5 |                5 |              2 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        9 | 1.6574 | DepartureTriage           |           3 |              3 |             4 |               6 |                5 |              2 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       10 | 1.7235 | DepartureTriage           |          12 |              2 |             4 |               7 |                5 |              2 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       11 | 2.6104 | HospitalHealingCompletion |           7 |              2 |             4 |               6 |                5 |              3 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       12 | 2.6783 | DepartureTriage           |          14 |              1 |             4 |               7 |                5 |              3 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       13 | 3.1978 | DepartureTriage           |           4 |              0 |             4 |               7 |                5 |              3 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       14 | 3.3922 | HospitalHealingCompletion |          11 |              0 |             4 |               6 |                5 |              4 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       15 | 3.8567 | HospitalHealingCompletion |           6 |              0 |             4 |               5 |                5 |              5 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       16 | 3.899  | Arrival                   |             |              1 |             4 |               5 |                6 |              5 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       17 | 4.1303 | Arrival                   |             |              2 |             4 |               5 |                7 |              5 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       18 | 4.539  | HospitalHealingCompletion |           9 |              2 |             4 |               4 |                7 |              6 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       19 | 4.7254 | HospitalHealingCompletion |          12 |              2 |             4 |               3 |                7 |              7 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       20 | 4.7353 | DepartureTriage           |          15 |              1 |             4 |               3 |                7 |              7 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+

Future Event Lists:
After Event 1: [(0.4004, 'Arrival', None), (1.4379, 'HospitalHealingCompletion', 10), (1.2865, 'DepartureTriage', 1), (3.1978, 'DepartureTriage', 4), (1.4893, 'HospitalHealingCompletion', 8), (1.6574, 'DepartureTriage', 3), (2.6104, 'HospitalHealingCompletion', 7), (7.2723, 'DepartureTriage', 2), (4.539, 'HospitalHealingCompletion', 9), (5.8578, 'HospitalHealingCompletion', 5), (3.3922, 'HospitalHealingCompletion', 11), (3.8567, 'HospitalHealingCompletion', 6)]
After Event 2: [(0.9487, 'Arrival', None), (1.4379, 'HospitalHealingCompletion', 10), (1.2865, 'DepartureTriage', 1), (3.1978, 'DepartureTriage', 4), (1.4893, 'HospitalHealingCompletion', 8), (1.6574, 'DepartureTriage', 3), (2.6104, 'HospitalHealingCompletion', 7), (7.2723, 'DepartureTriage', 2), (4.539, 'HospitalHealingCompletion', 9), (5.8578, 'HospitalHealingCompletion', 5), (3.3922, 'HospitalHealingCompletion', 11), (3.8567, 'HospitalHealingCompletion', 6)]
After Event 3: [(0.9673, 'Arrival', None), (1.4379, 'HospitalHealingCompletion', 10), (1.2865, 'DepartureTriage', 1), (3.1978, 'DepartureTriage', 4), (1.4893, 'HospitalHealingCompletion', 8), (1.6574, 'DepartureTriage', 3), (2.6104, 'HospitalHealingCompletion', 7), (7.2723, 'DepartureTriage', 2), (4.539, 'HospitalHealingCompletion', 9), (5.8578, 'HospitalHealingCompletion', 5), (3.3922, 'HospitalHealingCompletion', 11), (3.8567, 'HospitalHealingCompletion', 6)]
After Event 4: [(1.2865, 'DepartureTriage', 1), (1.4379, 'HospitalHealingCompletion', 10), (1.4608, 'Arrival', None), (3.1978, 'DepartureTriage', 4), (1.4893, 'HospitalHealingCompletion', 8), (1.6574, 'DepartureTriage', 3), (2.6104, 'HospitalHealingCompletion', 7), (7.2723, 'DepartureTriage', 2), (4.539, 'HospitalHealingCompletion', 9), (5.8578, 'HospitalHealingCompletion', 5), (3.3922, 'HospitalHealingCompletion', 11), (3.8567, 'HospitalHealingCompletion', 6)]
After Event 5: [(1.4379, 'HospitalHealingCompletion', 10), (1.4893, 'HospitalHealingCompletion', 8), (1.4608, 'Arrival', None), (3.1978, 'DepartureTriage', 4), (3.3922, 'HospitalHealingCompletion', 11), (1.6574, 'DepartureTriage', 3), (2.6104, 'HospitalHealingCompletion', 7), (7.2723, 'DepartureTriage', 2), (4.539, 'HospitalHealingCompletion', 9), (5.8578, 'HospitalHealingCompletion', 5), (3.8567, 'HospitalHealingCompletion', 6), (11.7543, 'HomeHealingCompletion', 1), (1.7235, 'DepartureTriage', 12)]
After Event 6: [(1.4608, 'Arrival', None), (1.4893, 'HospitalHealingCompletion', 8), (1.6574, 'DepartureTriage', 3), (3.1978, 'DepartureTriage', 4), (3.3922, 'HospitalHealingCompletion', 11), (1.7235, 'DepartureTriage', 12), (2.6104, 'HospitalHealingCompletion', 7), (7.2723, 'DepartureTriage', 2), (4.539, 'HospitalHealingCompletion', 9), (5.8578, 'HospitalHealingCompletion', 5), (3.8567, 'HospitalHealingCompletion', 6), (11.7543, 'HomeHealingCompletion', 1)]
After Event 7: [(1.4893, 'HospitalHealingCompletion', 8), (3.1978, 'DepartureTriage', 4), (1.6574, 'DepartureTriage', 3), (4.539, 'HospitalHealingCompletion', 9), (3.3922, 'HospitalHealingCompletion', 11), (1.7235, 'DepartureTriage', 12), (2.6104, 'HospitalHealingCompletion', 7), (7.2723, 'DepartureTriage', 2), (11.7543, 'HomeHealingCompletion', 1), (5.8578, 'HospitalHealingCompletion', 5), (3.8567, 'HospitalHealingCompletion', 6), (3.899, 'Arrival', None)]
After Event 8: [(1.6574, 'DepartureTriage', 3), (3.1978, 'DepartureTriage', 4), (1.7235, 'DepartureTriage', 12), (4.539, 'HospitalHealingCompletion', 9), (3.3922, 'HospitalHealingCompletion', 11), (3.899, 'Arrival', None), (2.6104, 'HospitalHealingCompletion', 7), (7.2723, 'DepartureTriage', 2), (11.7543, 'HomeHealingCompletion', 1), (5.8578, 'HospitalHealingCompletion', 5), (3.8567, 'HospitalHealingCompletion', 6)]
After Event 9: [(1.7235, 'DepartureTriage', 12), (3.1978, 'DepartureTriage', 4), (2.6104, 'HospitalHealingCompletion', 7), (4.539, 'HospitalHealingCompletion', 9), (3.3922, 'HospitalHealingCompletion', 11), (3.899, 'Arrival', None), (3.8567, 'HospitalHealingCompletion', 6), (7.2723, 'DepartureTriage', 2), (11.7543, 'HomeHealingCompletion', 1), (5.8578, 'HospitalHealingCompletion', 5), (9.3703, 'HospitalHealingCompletion', 3), (5.2843, 'DepartureTriage', 13)]
After Event 10: [(2.6104, 'HospitalHealingCompletion', 7), (3.1978, 'DepartureTriage', 4), (2.6783, 'DepartureTriage', 14), (4.539, 'HospitalHealingCompletion', 9), (3.3922, 'HospitalHealingCompletion', 11), (3.8567, 'HospitalHealingCompletion', 6), (5.2843, 'DepartureTriage', 13), (7.2723, 'DepartureTriage', 2), (11.7543, 'HomeHealingCompletion', 1), (5.8578, 'HospitalHealingCompletion', 5), (9.3703, 'HospitalHealingCompletion', 3), (4.7254, 'HospitalHealingCompletion', 12), (3.899, 'Arrival', None)]
After Event 11: [(2.6783, 'DepartureTriage', 14), (3.1978, 'DepartureTriage', 4), (3.8567, 'HospitalHealingCompletion', 6), (4.539, 'HospitalHealingCompletion', 9), (3.3922, 'HospitalHealingCompletion', 11), (3.899, 'Arrival', None), (5.2843, 'DepartureTriage', 13), (7.2723, 'DepartureTriage', 2), (11.7543, 'HomeHealingCompletion', 1), (5.8578, 'HospitalHealingCompletion', 5), (9.3703, 'HospitalHealingCompletion', 3), (4.7254, 'HospitalHealingCompletion', 12)]
After Event 12: [(3.1978, 'DepartureTriage', 4), (3.3922, 'HospitalHealingCompletion', 11), (3.8567, 'HospitalHealingCompletion', 6), (4.539, 'HospitalHealingCompletion', 9), (4.7254, 'HospitalHealingCompletion', 12), (3.899, 'Arrival', None), (5.2843, 'DepartureTriage', 13), (7.2723, 'DepartureTriage', 2), (11.7543, 'HomeHealingCompletion', 1), (5.8578, 'HospitalHealingCompletion', 5), (9.3703, 'HospitalHealingCompletion', 3), (8.451, 'HospitalHealingCompletion', 14), (4.7353, 'DepartureTriage', 15)]
After Event 13: [(3.3922, 'HospitalHealingCompletion', 11), (4.539, 'HospitalHealingCompletion', 9), (3.8567, 'HospitalHealingCompletion', 6), (4.7353, 'DepartureTriage', 15), (4.7254, 'HospitalHealingCompletion', 12), (3.899, 'Arrival', None), (5.2843, 'DepartureTriage', 13), (7.2723, 'DepartureTriage', 2), (11.7543, 'HomeHealingCompletion', 1), (5.8578, 'HospitalHealingCompletion', 5), (9.3703, 'HospitalHealingCompletion', 3), (8.451, 'HospitalHealingCompletion', 14), (7.426, 'HomeHealingCompletion', 4), (11.0828, 'DepartureTriage', 16)]
After Event 14: [(3.8567, 'HospitalHealingCompletion', 6), (4.539, 'HospitalHealingCompletion', 9), (3.899, 'Arrival', None), (4.7353, 'DepartureTriage', 15), (4.7254, 'HospitalHealingCompletion', 12), (7.426, 'HomeHealingCompletion', 4), (5.2843, 'DepartureTriage', 13), (7.2723, 'DepartureTriage', 2), (11.7543, 'HomeHealingCompletion', 1), (5.8578, 'HospitalHealingCompletion', 5), (9.3703, 'HospitalHealingCompletion', 3), (8.451, 'HospitalHealingCompletion', 14), (11.0828, 'DepartureTriage', 16)]
After Event 15: [(3.899, 'Arrival', None), (4.539, 'HospitalHealingCompletion', 9), (5.2843, 'DepartureTriage', 13), (4.7353, 'DepartureTriage', 15), (4.7254, 'HospitalHealingCompletion', 12), (7.426, 'HomeHealingCompletion', 4), (11.0828, 'DepartureTriage', 16), (7.2723, 'DepartureTriage', 2), (11.7543, 'HomeHealingCompletion', 1), (5.8578, 'HospitalHealingCompletion', 5), (9.3703, 'HospitalHealingCompletion', 3), (8.451, 'HospitalHealingCompletion', 14)]
After Event 16: [(4.1303, 'Arrival', None), (4.7254, 'HospitalHealingCompletion', 12), (4.539, 'HospitalHealingCompletion', 9), (4.7353, 'DepartureTriage', 15), (5.8578, 'HospitalHealingCompletion', 5), (5.2843, 'DepartureTriage', 13), (11.0828, 'DepartureTriage', 16), (7.2723, 'DepartureTriage', 2), (11.7543, 'HomeHealingCompletion', 1), (8.451, 'HospitalHealingCompletion', 14), (9.3703, 'HospitalHealingCompletion', 3), (7.426, 'HomeHealingCompletion', 4)]
After Event 17: [(4.539, 'HospitalHealingCompletion', 9), (4.7254, 'HospitalHealingCompletion', 12), (5.2071, 'Arrival', None), (4.7353, 'DepartureTriage', 15), (5.8578, 'HospitalHealingCompletion', 5), (5.2843, 'DepartureTriage', 13), (11.0828, 'DepartureTriage', 16), (7.2723, 'DepartureTriage', 2), (11.7543, 'HomeHealingCompletion', 1), (8.451, 'HospitalHealingCompletion', 14), (9.3703, 'HospitalHealingCompletion', 3), (7.426, 'HomeHealingCompletion', 4)]
After Event 18: [(4.7254, 'HospitalHealingCompletion', 12), (4.7353, 'DepartureTriage', 15), (5.2071, 'Arrival', None), (7.2723, 'DepartureTriage', 2), (5.8578, 'HospitalHealingCompletion', 5), (5.2843, 'DepartureTriage', 13), (11.0828, 'DepartureTriage', 16), (7.426, 'HomeHealingCompletion', 4), (11.7543, 'HomeHealingCompletion', 1), (8.451, 'HospitalHealingCompletion', 14), (9.3703, 'HospitalHealingCompletion', 3)]
After Event 19: [(4.7353, 'DepartureTriage', 15), (5.8578, 'HospitalHealingCompletion', 5), (5.2071, 'Arrival', None), (7.2723, 'DepartureTriage', 2), (8.451, 'HospitalHealingCompletion', 14), (5.2843, 'DepartureTriage', 13), (11.0828, 'DepartureTriage', 16), (7.426, 'HomeHealingCompletion', 4), (11.7543, 'HomeHealingCompletion', 1), (9.3703, 'HospitalHealingCompletion', 3)]
After Event 20: [(5.2071, 'Arrival', None), (5.8578, 'HospitalHealingCompletion', 5), (5.2843, 'DepartureTriage', 13), (7.2723, 'DepartureTriage', 2), (6.4817, 'DepartureTriage', 17), (9.3703, 'HospitalHealingCompletion', 3), (11.0828, 'DepartureTriage', 16), (7.426, 'HomeHealingCompletion', 4), (11.7543, 'HomeHealingCompletion', 1), (13.5047, 'HomeHealingCompletion', 15), (8.451, 'HospitalHealingCompletion', 14)]

Results for full initial condition, 1000 healed patients:
SimulationLength: 1003.682687
TotalPatientsArrived: 999.000000
TotalPatientsHealed: 1000.000000
ProbabilityTriageEmpty: 0.031223
ProbabilityBedsEmpty: 0.005809
ProbabilityBothEmpty: 0.000000
RejectionProbability: 0.144168
AverageNurseUtilization: 0.763804
AverageOccupiedBeds: 4.499492
ProportionHomeTreated: 0.342000
AverageHealingTime: 11.344011
```

## Empty Initial Condition - 20 Replications

```

Results for empty with 20 replications:
SimulationLength: 210.703323 [95% CI: 203.518911, 217.887734]
TotalPatientsArrived: 212.050000 [95% CI: 209.380417, 214.719583]
TotalPatientsHealed: 200.000000 [95% CI: 200.000000, 200.000000]
ProbabilityTriageEmpty: 0.040819 [95% CI: 0.031447, 0.050191]
ProbabilityBedsEmpty: 0.023256 [95% CI: 0.017103, 0.029408]
ProbabilityBothEmpty: 0.000057 [95% CI: -0.000040, 0.000154]
RejectionProbability: 0.090597 [95% CI: 0.074337, 0.106857]
AverageNurseUtilization: 0.734975 [95% CI: 0.705864, 0.764086]
AverageOccupiedBeds: 4.135837 [95% CI: 3.997190, 4.274484]
ProportionHomeTreated: 0.334500 [95% CI: 0.317858, 0.351142]
AverageHealingTime: 10.421544 [95% CI: 9.985666, 10.857422]
```

## Half_full Initial Condition - 20 Replications

```

Results for half_full with 20 replications:
SimulationLength: 205.931396 [95% CI: 199.172779, 212.690013]
TotalPatientsArrived: 205.450000 [95% CI: 203.348254, 207.551746]
TotalPatientsHealed: 200.000000 [95% CI: 200.000000, 200.000000]
ProbabilityTriageEmpty: 0.039849 [95% CI: 0.027072, 0.052626]
ProbabilityBedsEmpty: 0.008781 [95% CI: 0.003751, 0.013810]
ProbabilityBothEmpty: 0.000000 [95% CI: 0.000000, 0.000000]
RejectionProbability: 0.110849 [95% CI: 0.095382, 0.126317]
AverageNurseUtilization: 0.746208 [95% CI: 0.704479, 0.787937]
AverageOccupiedBeds: 4.318754 [95% CI: 4.159729, 4.477779]
ProportionHomeTreated: 0.328500 [95% CI: 0.313266, 0.343734]
AverageHealingTime: 11.647070 [95% CI: 10.280872, 13.013268]
```

## Full Initial Condition - 20 Replications

```

Results for full with 20 replications:
SimulationLength: 199.128732 [95% CI: 192.227411, 206.030053]
TotalPatientsArrived: 202.050000 [95% CI: 198.923443, 205.176557]
TotalPatientsHealed: 200.000000 [95% CI: 200.000000, 200.000000]
ProbabilityTriageEmpty: 0.034732 [95% CI: 0.024163, 0.045300]
ProbabilityBedsEmpty: 0.009114 [95% CI: 0.003946, 0.014283]
ProbabilityBothEmpty: 0.000065 [95% CI: -0.000062, 0.000191]
RejectionProbability: 0.122335 [95% CI: 0.098996, 0.145673]
AverageNurseUtilization: 0.765980 [95% CI: 0.732756, 0.799205]
AverageOccupiedBeds: 4.418974 [95% CI: 4.261763, 4.576186]
ProportionHomeTreated: 0.340750 [95% CI: 0.324533, 0.356967]
AverageHealingTime: 10.743653 [95% CI: 10.042339, 11.444966]
```

## Comparison of Results

```

================================================================================
Comparison of Results Across Initial Conditions and Run Lengths
================================================================================

Comparison for 20 healed patients:

ProbabilityTriageEmpty:
  empty: 0.056214
  half_full: 0.059158
  full: 0.025613

ProbabilityBedsEmpty:
  empty: 0.012936
  half_full: 0.153646
  full: 0.000000

RejectionProbability:
  empty: 0.280000
  half_full: 0.000000
  full: 0.153846

AverageNurseUtilization:
  empty: 0.657306
  half_full: 0.558979
  full: 0.678716

AverageOccupiedBeds:
  empty: 4.584726
  half_full: 2.256665
  full: 3.706623

ProportionHomeTreated:
  empty: 0.550000
  half_full: 0.300000
  full: 0.300000

Comparison for 200 healed patients:

ProbabilityTriageEmpty:
  empty: 0.059809
  half_full: 0.093693
  full: 0.068743

ProbabilityBedsEmpty:
  empty: 0.002063
  half_full: 0.016705
  full: 0.000000

RejectionProbability:
  empty: 0.126582
  half_full: 0.130435
  full: 0.086667

AverageNurseUtilization:
  empty: 0.727236
  half_full: 0.626643
  full: 0.670338

AverageOccupiedBeds:
  empty: 4.390007
  half_full: 4.678713
  full: 4.313736

ProportionHomeTreated:
  empty: 0.345000
  half_full: 0.310000
  full: 0.320000

Comparison for 1000 healed patients:

ProbabilityTriageEmpty:
  empty: 0.028079
  half_full: 0.042439
  full: 0.031223

ProbabilityBedsEmpty:
  empty: 0.005183
  half_full: 0.017336
  full: 0.005809

RejectionProbability:
  empty: 0.143045
  half_full: 0.149485
  full: 0.144168

AverageNurseUtilization:
  empty: 0.769814
  half_full: 0.724040
  full: 0.763804

AverageOccupiedBeds:
  empty: 4.471325
  half_full: 4.508593
  full: 4.499492

ProportionHomeTreated:
  empty: 0.350000
  half_full: 0.340000
  full: 0.342000

================================================================================
Convergence Analysis as Simulation Length Increases
================================================================================

Convergence for empty initial condition:

ProbabilityTriageEmpty:
  20 patients: 0.056214
  200 patients: 0.059809
  1000 patients: 0.028079

ProbabilityBedsEmpty:
  20 patients: 0.012936
  200 patients: 0.002063
  1000 patients: 0.005183

RejectionProbability:
  20 patients: 0.280000
  200 patients: 0.126582
  1000 patients: 0.143045

AverageNurseUtilization:
  20 patients: 0.657306
  200 patients: 0.727236
  1000 patients: 0.769814

AverageOccupiedBeds:
  20 patients: 4.584726
  200 patients: 4.390007
  1000 patients: 4.471325

ProportionHomeTreated:
  20 patients: 0.550000
  200 patients: 0.345000
  1000 patients: 0.350000

Convergence for half_full initial condition:

ProbabilityTriageEmpty:
  20 patients: 0.059158
  200 patients: 0.093693
  1000 patients: 0.042439

ProbabilityBedsEmpty:
  20 patients: 0.153646
  200 patients: 0.016705
  1000 patients: 0.017336

RejectionProbability:
  20 patients: 0.000000
  200 patients: 0.130435
  1000 patients: 0.149485

AverageNurseUtilization:
  20 patients: 0.558979
  200 patients: 0.626643
  1000 patients: 0.724040

AverageOccupiedBeds:
  20 patients: 2.256665
  200 patients: 4.678713
  1000 patients: 4.508593

ProportionHomeTreated:
  20 patients: 0.300000
  200 patients: 0.310000
  1000 patients: 0.340000

Convergence for full initial condition:

ProbabilityTriageEmpty:
  20 patients: 0.025613
  200 patients: 0.068743
  1000 patients: 0.031223

ProbabilityBedsEmpty:
  20 patients: 0.000000
  200 patients: 0.000000
  1000 patients: 0.005809

RejectionProbability:
  20 patients: 0.153846
  200 patients: 0.086667
  1000 patients: 0.144168

AverageNurseUtilization:
  20 patients: 0.678716
  200 patients: 0.670338
  1000 patients: 0.763804

AverageOccupiedBeds:
  20 patients: 3.706623
  200 patients: 4.313736
  1000 patients: 4.499492

ProportionHomeTreated:
  20 patients: 0.300000
  200 patients: 0.320000
  1000 patients: 0.342000
```
