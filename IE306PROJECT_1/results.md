# Hospital Simulation Results


## Empty Initial Condition with 20 Target Healed Patients

```

Event Trace for First 20 Events:
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|   Event# |   Time | Event Type                |   PatientID |   Triage Queue |   Busy Nurses |   Occupied Beds |   Total Patients |   Total Healed |
+==========+========+===========================+=============+================+===============+=================+==================+================+
|        1 | 0.4441 | Arrival                   |             |              0 |             1 |               0 |                1 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        2 | 0.4646 | DepartureTriage           |           1 |              0 |             0 |               1 |                1 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        3 | 1.0562 | Arrival                   |             |              0 |             1 |               1 |                2 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        4 | 1.2512 | DepartureTriage           |           2 |              0 |             0 |               2 |                2 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        5 | 1.8274 | HospitalHealingCompletion |           1 |              0 |             0 |               1 |                2 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        6 | 1.9796 | Arrival                   |             |              0 |             1 |               1 |                3 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        7 | 3.0265 | Arrival                   |             |              0 |             2 |               1 |                4 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        8 | 3.6324 | Arrival                   |             |              0 |             3 |               1 |                5 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        9 | 4.143  | Arrival                   |             |              0 |             4 |               1 |                6 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       10 | 4.635  | Arrival                   |             |              1 |             4 |               1 |                7 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       11 | 4.7315 | DepartureTriage           |           3 |              0 |             4 |               2 |                7 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       12 | 5.1128 | Arrival                   |             |              1 |             4 |               2 |                8 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       13 | 5.6381 | Arrival                   |             |              2 |             4 |               2 |                9 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       14 | 5.8921 | DepartureTriage           |           7 |              1 |             4 |               2 |                9 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       15 | 6.0934 | Arrival                   |             |              2 |             4 |               2 |               10 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       16 | 7.0978 | DepartureTriage           |           8 |              1 |             4 |               2 |               10 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       17 | 7.285  | HospitalHealingCompletion |           2 |              1 |             4 |               1 |               10 |              2 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       18 | 7.7413 | DepartureTriage           |           4 |              0 |             4 |               1 |               10 |              2 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       19 | 8.8477 | DepartureTriage           |           9 |              0 |             3 |               2 |               10 |              2 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       20 | 9.2288 | Arrival                   |             |              0 |             4 |               2 |               11 |              2 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+

Future Event Lists:
After Event 1: [(0.4646, 'DepartureTriage', 1), (1.0562, 'Arrival', None)]
After Event 2: [(1.0562, 'Arrival', None), (1.8274, 'HospitalHealingCompletion', 1)]
After Event 3: [(1.2512, 'DepartureTriage', 2), (1.9796, 'Arrival', None), (1.8274, 'HospitalHealingCompletion', 1)]
After Event 4: [(1.8274, 'HospitalHealingCompletion', 1), (1.9796, 'Arrival', None), (7.285, 'HospitalHealingCompletion', 2)]
After Event 5: [(1.9796, 'Arrival', None), (7.285, 'HospitalHealingCompletion', 2)]
After Event 6: [(3.0265, 'Arrival', None), (7.285, 'HospitalHealingCompletion', 2), (4.7315, 'DepartureTriage', 3)]
After Event 7: [(3.6324, 'Arrival', None), (7.285, 'HospitalHealingCompletion', 2), (4.7315, 'DepartureTriage', 3), (7.7413, 'DepartureTriage', 4)]
After Event 8: [(4.143, 'Arrival', None), (4.7315, 'DepartureTriage', 3), (7.7413, 'DepartureTriage', 4), (7.285, 'HospitalHealingCompletion', 2), (14.8618, 'DepartureTriage', 5)]
After Event 9: [(4.635, 'Arrival', None), (4.7315, 'DepartureTriage', 3), (7.7413, 'DepartureTriage', 4), (14.8618, 'DepartureTriage', 5), (7.285, 'HospitalHealingCompletion', 2), (15.0677, 'DepartureTriage', 6)]
After Event 10: [(4.7315, 'DepartureTriage', 3), (7.285, 'HospitalHealingCompletion', 2), (5.1128, 'Arrival', None), (14.8618, 'DepartureTriage', 5), (15.0677, 'DepartureTriage', 6), (7.7413, 'DepartureTriage', 4)]
After Event 11: [(5.1128, 'Arrival', None), (7.285, 'HospitalHealingCompletion', 2), (5.8921, 'DepartureTriage', 7), (14.8618, 'DepartureTriage', 5), (15.0677, 'DepartureTriage', 6), (12.2969, 'HospitalHealingCompletion', 3), (7.7413, 'DepartureTriage', 4)]
After Event 12: [(5.6381, 'Arrival', None), (7.285, 'HospitalHealingCompletion', 2), (5.8921, 'DepartureTriage', 7), (14.8618, 'DepartureTriage', 5), (15.0677, 'DepartureTriage', 6), (12.2969, 'HospitalHealingCompletion', 3), (7.7413, 'DepartureTriage', 4)]
After Event 13: [(5.8921, 'DepartureTriage', 7), (7.285, 'HospitalHealingCompletion', 2), (6.0934, 'Arrival', None), (14.8618, 'DepartureTriage', 5), (15.0677, 'DepartureTriage', 6), (12.2969, 'HospitalHealingCompletion', 3), (7.7413, 'DepartureTriage', 4)]
After Event 14: [(6.0934, 'Arrival', None), (7.0978, 'DepartureTriage', 8), (7.7413, 'DepartureTriage', 4), (7.285, 'HospitalHealingCompletion', 2), (15.0677, 'DepartureTriage', 6), (12.2969, 'HospitalHealingCompletion', 3), (13.1566, 'HomeHealingCompletion', 7), (14.8618, 'DepartureTriage', 5)]
After Event 15: [(7.0978, 'DepartureTriage', 8), (7.285, 'HospitalHealingCompletion', 2), (7.7413, 'DepartureTriage', 4), (9.2288, 'Arrival', None), (15.0677, 'DepartureTriage', 6), (12.2969, 'HospitalHealingCompletion', 3), (13.1566, 'HomeHealingCompletion', 7), (14.8618, 'DepartureTriage', 5)]
After Event 16: [(7.285, 'HospitalHealingCompletion', 2), (8.8477, 'DepartureTriage', 9), (7.7413, 'DepartureTriage', 4), (9.2288, 'Arrival', None), (15.0677, 'DepartureTriage', 6), (12.2969, 'HospitalHealingCompletion', 3), (13.1566, 'HomeHealingCompletion', 7), (14.8618, 'DepartureTriage', 5), (9.8034, 'HomeHealingCompletion', 8)]
After Event 17: [(7.7413, 'DepartureTriage', 4), (8.8477, 'DepartureTriage', 9), (9.8034, 'HomeHealingCompletion', 8), (9.2288, 'Arrival', None), (15.0677, 'DepartureTriage', 6), (12.2969, 'HospitalHealingCompletion', 3), (13.1566, 'HomeHealingCompletion', 7), (14.8618, 'DepartureTriage', 5)]
After Event 18: [(8.8477, 'DepartureTriage', 9), (9.2288, 'Arrival', None), (9.8034, 'HomeHealingCompletion', 8), (10.1643, 'DepartureTriage', 10), (15.0677, 'DepartureTriage', 6), (12.2969, 'HospitalHealingCompletion', 3), (13.1566, 'HomeHealingCompletion', 7), (14.8618, 'DepartureTriage', 5), (11.8257, 'HomeHealingCompletion', 4)]
After Event 19: [(9.2288, 'Arrival', None), (10.1643, 'DepartureTriage', 10), (9.8034, 'HomeHealingCompletion', 8), (10.7959, 'HospitalHealingCompletion', 9), (15.0677, 'DepartureTriage', 6), (12.2969, 'HospitalHealingCompletion', 3), (13.1566, 'HomeHealingCompletion', 7), (14.8618, 'DepartureTriage', 5), (11.8257, 'HomeHealingCompletion', 4)]
After Event 20: [(9.2953, 'Arrival', None), (9.8034, 'HomeHealingCompletion', 8), (11.8257, 'HomeHealingCompletion', 4), (10.1643, 'DepartureTriage', 10), (13.2638, 'DepartureTriage', 11), (12.2969, 'HospitalHealingCompletion', 3), (13.1566, 'HomeHealingCompletion', 7), (14.8618, 'DepartureTriage', 5), (10.7959, 'HospitalHealingCompletion', 9), (15.0677, 'DepartureTriage', 6)]

Results for empty initial condition, 20 healed patients:
SimulationLength: 24.038185
TotalPatientsArrived: 27.000000
TotalPatientsHealed: 20.000000
ProbabilityTriageEmpty: 0.083793
ProbabilityBedsEmpty: 0.018475
ProbabilityBothEmpty: 0.000000
RejectionProbability: 0.222222
AverageNurseUtilization: 0.714442
AverageOccupiedBeds: 2.650335
ProportionHomeTreated: 0.600000
AverageHealingTime: 7.129253
```

## Empty Initial Condition with 200 Target Healed Patients

```

Event Trace for First 20 Events:
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|   Event# |   Time | Event Type                |   PatientID |   Triage Queue |   Busy Nurses |   Occupied Beds |   Total Patients |   Total Healed |
+==========+========+===========================+=============+================+===============+=================+==================+================+
|        1 | 0.4441 | Arrival                   |             |              0 |             1 |               0 |                1 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        2 | 0.4646 | DepartureTriage           |           1 |              0 |             0 |               1 |                1 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        3 | 1.0562 | Arrival                   |             |              0 |             1 |               1 |                2 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        4 | 1.2512 | DepartureTriage           |           2 |              0 |             0 |               2 |                2 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        5 | 1.8274 | HospitalHealingCompletion |           1 |              0 |             0 |               1 |                2 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        6 | 1.9796 | Arrival                   |             |              0 |             1 |               1 |                3 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        7 | 3.0265 | Arrival                   |             |              0 |             2 |               1 |                4 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        8 | 3.6324 | Arrival                   |             |              0 |             3 |               1 |                5 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        9 | 4.143  | Arrival                   |             |              0 |             4 |               1 |                6 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       10 | 4.635  | Arrival                   |             |              1 |             4 |               1 |                7 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       11 | 4.7315 | DepartureTriage           |           3 |              0 |             4 |               2 |                7 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       12 | 5.1128 | Arrival                   |             |              1 |             4 |               2 |                8 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       13 | 5.6381 | Arrival                   |             |              2 |             4 |               2 |                9 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       14 | 5.8921 | DepartureTriage           |           7 |              1 |             4 |               2 |                9 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       15 | 6.0934 | Arrival                   |             |              2 |             4 |               2 |               10 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       16 | 7.0978 | DepartureTriage           |           8 |              1 |             4 |               2 |               10 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       17 | 7.285  | HospitalHealingCompletion |           2 |              1 |             4 |               1 |               10 |              2 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       18 | 7.7413 | DepartureTriage           |           4 |              0 |             4 |               1 |               10 |              2 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       19 | 8.8477 | DepartureTriage           |           9 |              0 |             3 |               2 |               10 |              2 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       20 | 9.2288 | Arrival                   |             |              0 |             4 |               2 |               11 |              2 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+

Future Event Lists:
After Event 1: [(0.4646, 'DepartureTriage', 1), (1.0562, 'Arrival', None)]
After Event 2: [(1.0562, 'Arrival', None), (1.8274, 'HospitalHealingCompletion', 1)]
After Event 3: [(1.2512, 'DepartureTriage', 2), (1.9796, 'Arrival', None), (1.8274, 'HospitalHealingCompletion', 1)]
After Event 4: [(1.8274, 'HospitalHealingCompletion', 1), (1.9796, 'Arrival', None), (7.285, 'HospitalHealingCompletion', 2)]
After Event 5: [(1.9796, 'Arrival', None), (7.285, 'HospitalHealingCompletion', 2)]
After Event 6: [(3.0265, 'Arrival', None), (7.285, 'HospitalHealingCompletion', 2), (4.7315, 'DepartureTriage', 3)]
After Event 7: [(3.6324, 'Arrival', None), (7.285, 'HospitalHealingCompletion', 2), (4.7315, 'DepartureTriage', 3), (7.7413, 'DepartureTriage', 4)]
After Event 8: [(4.143, 'Arrival', None), (4.7315, 'DepartureTriage', 3), (7.7413, 'DepartureTriage', 4), (7.285, 'HospitalHealingCompletion', 2), (14.8618, 'DepartureTriage', 5)]
After Event 9: [(4.635, 'Arrival', None), (4.7315, 'DepartureTriage', 3), (7.7413, 'DepartureTriage', 4), (14.8618, 'DepartureTriage', 5), (7.285, 'HospitalHealingCompletion', 2), (15.0677, 'DepartureTriage', 6)]
After Event 10: [(4.7315, 'DepartureTriage', 3), (7.285, 'HospitalHealingCompletion', 2), (5.1128, 'Arrival', None), (14.8618, 'DepartureTriage', 5), (15.0677, 'DepartureTriage', 6), (7.7413, 'DepartureTriage', 4)]
After Event 11: [(5.1128, 'Arrival', None), (7.285, 'HospitalHealingCompletion', 2), (5.8921, 'DepartureTriage', 7), (14.8618, 'DepartureTriage', 5), (15.0677, 'DepartureTriage', 6), (12.2969, 'HospitalHealingCompletion', 3), (7.7413, 'DepartureTriage', 4)]
After Event 12: [(5.6381, 'Arrival', None), (7.285, 'HospitalHealingCompletion', 2), (5.8921, 'DepartureTriage', 7), (14.8618, 'DepartureTriage', 5), (15.0677, 'DepartureTriage', 6), (12.2969, 'HospitalHealingCompletion', 3), (7.7413, 'DepartureTriage', 4)]
After Event 13: [(5.8921, 'DepartureTriage', 7), (7.285, 'HospitalHealingCompletion', 2), (6.0934, 'Arrival', None), (14.8618, 'DepartureTriage', 5), (15.0677, 'DepartureTriage', 6), (12.2969, 'HospitalHealingCompletion', 3), (7.7413, 'DepartureTriage', 4)]
After Event 14: [(6.0934, 'Arrival', None), (7.0978, 'DepartureTriage', 8), (7.7413, 'DepartureTriage', 4), (7.285, 'HospitalHealingCompletion', 2), (15.0677, 'DepartureTriage', 6), (12.2969, 'HospitalHealingCompletion', 3), (13.1566, 'HomeHealingCompletion', 7), (14.8618, 'DepartureTriage', 5)]
After Event 15: [(7.0978, 'DepartureTriage', 8), (7.285, 'HospitalHealingCompletion', 2), (7.7413, 'DepartureTriage', 4), (9.2288, 'Arrival', None), (15.0677, 'DepartureTriage', 6), (12.2969, 'HospitalHealingCompletion', 3), (13.1566, 'HomeHealingCompletion', 7), (14.8618, 'DepartureTriage', 5)]
After Event 16: [(7.285, 'HospitalHealingCompletion', 2), (8.8477, 'DepartureTriage', 9), (7.7413, 'DepartureTriage', 4), (9.2288, 'Arrival', None), (15.0677, 'DepartureTriage', 6), (12.2969, 'HospitalHealingCompletion', 3), (13.1566, 'HomeHealingCompletion', 7), (14.8618, 'DepartureTriage', 5), (9.8034, 'HomeHealingCompletion', 8)]
After Event 17: [(7.7413, 'DepartureTriage', 4), (8.8477, 'DepartureTriage', 9), (9.8034, 'HomeHealingCompletion', 8), (9.2288, 'Arrival', None), (15.0677, 'DepartureTriage', 6), (12.2969, 'HospitalHealingCompletion', 3), (13.1566, 'HomeHealingCompletion', 7), (14.8618, 'DepartureTriage', 5)]
After Event 18: [(8.8477, 'DepartureTriage', 9), (9.2288, 'Arrival', None), (9.8034, 'HomeHealingCompletion', 8), (10.1643, 'DepartureTriage', 10), (15.0677, 'DepartureTriage', 6), (12.2969, 'HospitalHealingCompletion', 3), (13.1566, 'HomeHealingCompletion', 7), (14.8618, 'DepartureTriage', 5), (11.8257, 'HomeHealingCompletion', 4)]
After Event 19: [(9.2288, 'Arrival', None), (10.1643, 'DepartureTriage', 10), (9.8034, 'HomeHealingCompletion', 8), (10.7959, 'HospitalHealingCompletion', 9), (15.0677, 'DepartureTriage', 6), (12.2969, 'HospitalHealingCompletion', 3), (13.1566, 'HomeHealingCompletion', 7), (14.8618, 'DepartureTriage', 5), (11.8257, 'HomeHealingCompletion', 4)]
After Event 20: [(9.2953, 'Arrival', None), (9.8034, 'HomeHealingCompletion', 8), (11.8257, 'HomeHealingCompletion', 4), (10.1643, 'DepartureTriage', 10), (13.2638, 'DepartureTriage', 11), (12.2969, 'HospitalHealingCompletion', 3), (13.1566, 'HomeHealingCompletion', 7), (14.8618, 'DepartureTriage', 5), (10.7959, 'HospitalHealingCompletion', 9), (15.0677, 'DepartureTriage', 6)]

Results for empty initial condition, 200 healed patients:
SimulationLength: 228.701384
TotalPatientsArrived: 209.000000
TotalPatientsHealed: 200.000000
ProbabilityTriageEmpty: 0.038114
ProbabilityBedsEmpty: 0.002001
ProbabilityBothEmpty: 0.000000
RejectionProbability: 0.173077
AverageNurseUtilization: 0.665023
AverageOccupiedBeds: 4.046931
ProportionHomeTreated: 0.380000
AverageHealingTime: 10.048562
```

## Empty Initial Condition with 1000 Target Healed Patients

```

Event Trace for First 20 Events:
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|   Event# |   Time | Event Type                |   PatientID |   Triage Queue |   Busy Nurses |   Occupied Beds |   Total Patients |   Total Healed |
+==========+========+===========================+=============+================+===============+=================+==================+================+
|        1 | 0.4441 | Arrival                   |             |              0 |             1 |               0 |                1 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        2 | 0.4646 | DepartureTriage           |           1 |              0 |             0 |               1 |                1 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        3 | 1.0562 | Arrival                   |             |              0 |             1 |               1 |                2 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        4 | 1.2512 | DepartureTriage           |           2 |              0 |             0 |               2 |                2 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        5 | 1.8274 | HospitalHealingCompletion |           1 |              0 |             0 |               1 |                2 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        6 | 1.9796 | Arrival                   |             |              0 |             1 |               1 |                3 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        7 | 3.0265 | Arrival                   |             |              0 |             2 |               1 |                4 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        8 | 3.6324 | Arrival                   |             |              0 |             3 |               1 |                5 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        9 | 4.143  | Arrival                   |             |              0 |             4 |               1 |                6 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       10 | 4.635  | Arrival                   |             |              1 |             4 |               1 |                7 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       11 | 4.7315 | DepartureTriage           |           3 |              0 |             4 |               2 |                7 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       12 | 5.1128 | Arrival                   |             |              1 |             4 |               2 |                8 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       13 | 5.6381 | Arrival                   |             |              2 |             4 |               2 |                9 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       14 | 5.8921 | DepartureTriage           |           7 |              1 |             4 |               2 |                9 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       15 | 6.0934 | Arrival                   |             |              2 |             4 |               2 |               10 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       16 | 7.0978 | DepartureTriage           |           8 |              1 |             4 |               2 |               10 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       17 | 7.285  | HospitalHealingCompletion |           2 |              1 |             4 |               1 |               10 |              2 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       18 | 7.7413 | DepartureTriage           |           4 |              0 |             4 |               1 |               10 |              2 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       19 | 8.8477 | DepartureTriage           |           9 |              0 |             3 |               2 |               10 |              2 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       20 | 9.2288 | Arrival                   |             |              0 |             4 |               2 |               11 |              2 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+

Future Event Lists:
After Event 1: [(0.4646, 'DepartureTriage', 1), (1.0562, 'Arrival', None)]
After Event 2: [(1.0562, 'Arrival', None), (1.8274, 'HospitalHealingCompletion', 1)]
After Event 3: [(1.2512, 'DepartureTriage', 2), (1.9796, 'Arrival', None), (1.8274, 'HospitalHealingCompletion', 1)]
After Event 4: [(1.8274, 'HospitalHealingCompletion', 1), (1.9796, 'Arrival', None), (7.285, 'HospitalHealingCompletion', 2)]
After Event 5: [(1.9796, 'Arrival', None), (7.285, 'HospitalHealingCompletion', 2)]
After Event 6: [(3.0265, 'Arrival', None), (7.285, 'HospitalHealingCompletion', 2), (4.7315, 'DepartureTriage', 3)]
After Event 7: [(3.6324, 'Arrival', None), (7.285, 'HospitalHealingCompletion', 2), (4.7315, 'DepartureTriage', 3), (7.7413, 'DepartureTriage', 4)]
After Event 8: [(4.143, 'Arrival', None), (4.7315, 'DepartureTriage', 3), (7.7413, 'DepartureTriage', 4), (7.285, 'HospitalHealingCompletion', 2), (14.8618, 'DepartureTriage', 5)]
After Event 9: [(4.635, 'Arrival', None), (4.7315, 'DepartureTriage', 3), (7.7413, 'DepartureTriage', 4), (14.8618, 'DepartureTriage', 5), (7.285, 'HospitalHealingCompletion', 2), (15.0677, 'DepartureTriage', 6)]
After Event 10: [(4.7315, 'DepartureTriage', 3), (7.285, 'HospitalHealingCompletion', 2), (5.1128, 'Arrival', None), (14.8618, 'DepartureTriage', 5), (15.0677, 'DepartureTriage', 6), (7.7413, 'DepartureTriage', 4)]
After Event 11: [(5.1128, 'Arrival', None), (7.285, 'HospitalHealingCompletion', 2), (5.8921, 'DepartureTriage', 7), (14.8618, 'DepartureTriage', 5), (15.0677, 'DepartureTriage', 6), (12.2969, 'HospitalHealingCompletion', 3), (7.7413, 'DepartureTriage', 4)]
After Event 12: [(5.6381, 'Arrival', None), (7.285, 'HospitalHealingCompletion', 2), (5.8921, 'DepartureTriage', 7), (14.8618, 'DepartureTriage', 5), (15.0677, 'DepartureTriage', 6), (12.2969, 'HospitalHealingCompletion', 3), (7.7413, 'DepartureTriage', 4)]
After Event 13: [(5.8921, 'DepartureTriage', 7), (7.285, 'HospitalHealingCompletion', 2), (6.0934, 'Arrival', None), (14.8618, 'DepartureTriage', 5), (15.0677, 'DepartureTriage', 6), (12.2969, 'HospitalHealingCompletion', 3), (7.7413, 'DepartureTriage', 4)]
After Event 14: [(6.0934, 'Arrival', None), (7.0978, 'DepartureTriage', 8), (7.7413, 'DepartureTriage', 4), (7.285, 'HospitalHealingCompletion', 2), (15.0677, 'DepartureTriage', 6), (12.2969, 'HospitalHealingCompletion', 3), (13.1566, 'HomeHealingCompletion', 7), (14.8618, 'DepartureTriage', 5)]
After Event 15: [(7.0978, 'DepartureTriage', 8), (7.285, 'HospitalHealingCompletion', 2), (7.7413, 'DepartureTriage', 4), (9.2288, 'Arrival', None), (15.0677, 'DepartureTriage', 6), (12.2969, 'HospitalHealingCompletion', 3), (13.1566, 'HomeHealingCompletion', 7), (14.8618, 'DepartureTriage', 5)]
After Event 16: [(7.285, 'HospitalHealingCompletion', 2), (8.8477, 'DepartureTriage', 9), (7.7413, 'DepartureTriage', 4), (9.2288, 'Arrival', None), (15.0677, 'DepartureTriage', 6), (12.2969, 'HospitalHealingCompletion', 3), (13.1566, 'HomeHealingCompletion', 7), (14.8618, 'DepartureTriage', 5), (9.8034, 'HomeHealingCompletion', 8)]
After Event 17: [(7.7413, 'DepartureTriage', 4), (8.8477, 'DepartureTriage', 9), (9.8034, 'HomeHealingCompletion', 8), (9.2288, 'Arrival', None), (15.0677, 'DepartureTriage', 6), (12.2969, 'HospitalHealingCompletion', 3), (13.1566, 'HomeHealingCompletion', 7), (14.8618, 'DepartureTriage', 5)]
After Event 18: [(8.8477, 'DepartureTriage', 9), (9.2288, 'Arrival', None), (9.8034, 'HomeHealingCompletion', 8), (10.1643, 'DepartureTriage', 10), (15.0677, 'DepartureTriage', 6), (12.2969, 'HospitalHealingCompletion', 3), (13.1566, 'HomeHealingCompletion', 7), (14.8618, 'DepartureTriage', 5), (11.8257, 'HomeHealingCompletion', 4)]
After Event 19: [(9.2288, 'Arrival', None), (10.1643, 'DepartureTriage', 10), (9.8034, 'HomeHealingCompletion', 8), (10.7959, 'HospitalHealingCompletion', 9), (15.0677, 'DepartureTriage', 6), (12.2969, 'HospitalHealingCompletion', 3), (13.1566, 'HomeHealingCompletion', 7), (14.8618, 'DepartureTriage', 5), (11.8257, 'HomeHealingCompletion', 4)]
After Event 20: [(9.2953, 'Arrival', None), (9.8034, 'HomeHealingCompletion', 8), (11.8257, 'HomeHealingCompletion', 4), (10.1643, 'DepartureTriage', 10), (13.2638, 'DepartureTriage', 11), (12.2969, 'HospitalHealingCompletion', 3), (13.1566, 'HomeHealingCompletion', 7), (14.8618, 'DepartureTriage', 5), (10.7959, 'HospitalHealingCompletion', 9), (15.0677, 'DepartureTriage', 6)]

Results for empty initial condition, 1000 healed patients:
SimulationLength: 1009.986168
TotalPatientsArrived: 1020.000000
TotalPatientsHealed: 1000.000000
ProbabilityTriageEmpty: 0.033074
ProbabilityBedsEmpty: 0.011644
ProbabilityBothEmpty: 0.000000
RejectionProbability: 0.138114
AverageNurseUtilization: 0.775408
AverageOccupiedBeds: 4.290690
ProportionHomeTreated: 0.363000
AverageHealingTime: 11.218985
```

## Half_full Initial Condition with 20 Target Healed Patients

```

Event Trace for First 20 Events:
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|   Event# |    Time | Event Type                |   PatientID |   Triage Queue |   Busy Nurses |   Occupied Beds |   Total Patients |   Total Healed |
+==========+=========+===========================+=============+================+===============+=================+==================+================+
|        1 |  0.0447 | HospitalHealingCompletion |           3 |              0 |             2 |               2 |                0 |              1 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        2 |  0.9234 | Arrival                   |             |              0 |             3 |               2 |                1 |              1 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        3 |  0.9884 | Arrival                   |             |              0 |             4 |               2 |                2 |              1 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        4 |  1.1139 | HospitalHealingCompletion |           4 |              0 |             4 |               1 |                2 |              2 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        5 |  1.3323 | DepartureTriage           |           1 |              0 |             3 |               2 |                2 |              2 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        6 |  1.3627 | HospitalHealingCompletion |           5 |              0 |             3 |               1 |                2 |              3 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        7 |  1.8364 | DepartureTriage           |           2 |              0 |             2 |               1 |                2 |              3 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        8 |  1.9119 | Arrival                   |             |              0 |             3 |               1 |                3 |              3 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        9 |  2.0405 | DepartureTriage           |           6 |              0 |             2 |               1 |                3 |              3 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       10 |  3.3879 | DepartureTriage           |           8 |              0 |             1 |               2 |                3 |              3 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       11 |  4.129  | DepartureTriage           |           7 |              0 |             0 |               3 |                3 |              3 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       12 |  5.0266 | HomeHealingCompletion     |           6 |              0 |             0 |               3 |                3 |              4 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       13 |  5.0274 | HomeHealingCompletion     |           2 |              0 |             0 |               3 |                3 |              5 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       14 |  5.2909 | HospitalHealingCompletion |           1 |              0 |             0 |               2 |                3 |              6 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       15 |  5.655  | Arrival                   |             |              0 |             1 |               2 |                4 |              6 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       16 |  6.1103 | Arrival                   |             |              0 |             2 |               2 |                5 |              6 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       17 |  7.2726 | Arrival                   |             |              0 |             3 |               2 |                6 |              6 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       18 |  7.316  | DepartureTriage           |          10 |              0 |             2 |               3 |                6 |              6 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       19 |  7.5612 | HospitalHealingCompletion |           7 |              0 |             2 |               2 |                6 |              7 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       20 | 10.408  | Arrival                   |             |              0 |             3 |               2 |                7 |              7 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+

Future Event Lists:
After Event 1: [(0.9234, 'Arrival', None), (1.1139, 'HospitalHealingCompletion', 4), (1.3323, 'DepartureTriage', 1), (1.8364, 'DepartureTriage', 2), (1.3627, 'HospitalHealingCompletion', 5)]
After Event 2: [(0.9884, 'Arrival', None), (1.1139, 'HospitalHealingCompletion', 4), (1.3323, 'DepartureTriage', 1), (1.8364, 'DepartureTriage', 2), (1.3627, 'HospitalHealingCompletion', 5), (2.0405, 'DepartureTriage', 6)]
After Event 3: [(1.1139, 'HospitalHealingCompletion', 4), (1.3627, 'HospitalHealingCompletion', 5), (1.3323, 'DepartureTriage', 1), (1.8364, 'DepartureTriage', 2), (2.0405, 'DepartureTriage', 6), (1.9119, 'Arrival', None), (4.129, 'DepartureTriage', 7)]
After Event 4: [(1.3323, 'DepartureTriage', 1), (1.3627, 'HospitalHealingCompletion', 5), (1.9119, 'Arrival', None), (1.8364, 'DepartureTriage', 2), (2.0405, 'DepartureTriage', 6), (4.129, 'DepartureTriage', 7)]
After Event 5: [(1.3627, 'HospitalHealingCompletion', 5), (1.8364, 'DepartureTriage', 2), (1.9119, 'Arrival', None), (4.129, 'DepartureTriage', 7), (2.0405, 'DepartureTriage', 6), (5.2909, 'HospitalHealingCompletion', 1)]
After Event 6: [(1.8364, 'DepartureTriage', 2), (2.0405, 'DepartureTriage', 6), (1.9119, 'Arrival', None), (4.129, 'DepartureTriage', 7), (5.2909, 'HospitalHealingCompletion', 1)]
After Event 7: [(1.9119, 'Arrival', None), (2.0405, 'DepartureTriage', 6), (5.2909, 'HospitalHealingCompletion', 1), (4.129, 'DepartureTriage', 7), (5.0274, 'HomeHealingCompletion', 2)]
After Event 8: [(2.0405, 'DepartureTriage', 6), (4.129, 'DepartureTriage', 7), (3.3879, 'DepartureTriage', 8), (5.0274, 'HomeHealingCompletion', 2), (5.655, 'Arrival', None), (5.2909, 'HospitalHealingCompletion', 1)]
After Event 9: [(3.3879, 'DepartureTriage', 8), (4.129, 'DepartureTriage', 7), (5.0266, 'HomeHealingCompletion', 6), (5.0274, 'HomeHealingCompletion', 2), (5.655, 'Arrival', None), (5.2909, 'HospitalHealingCompletion', 1)]
After Event 10: [(4.129, 'DepartureTriage', 7), (5.0274, 'HomeHealingCompletion', 2), (5.0266, 'HomeHealingCompletion', 6), (5.2909, 'HospitalHealingCompletion', 1), (5.655, 'Arrival', None), (10.9533, 'HospitalHealingCompletion', 8)]
After Event 11: [(5.0266, 'HomeHealingCompletion', 6), (5.0274, 'HomeHealingCompletion', 2), (7.5612, 'HospitalHealingCompletion', 7), (5.2909, 'HospitalHealingCompletion', 1), (5.655, 'Arrival', None), (10.9533, 'HospitalHealingCompletion', 8)]
After Event 12: [(5.0274, 'HomeHealingCompletion', 2), (5.2909, 'HospitalHealingCompletion', 1), (7.5612, 'HospitalHealingCompletion', 7), (10.9533, 'HospitalHealingCompletion', 8), (5.655, 'Arrival', None)]
After Event 13: [(5.2909, 'HospitalHealingCompletion', 1), (5.655, 'Arrival', None), (7.5612, 'HospitalHealingCompletion', 7), (10.9533, 'HospitalHealingCompletion', 8)]
After Event 14: [(5.655, 'Arrival', None), (10.9533, 'HospitalHealingCompletion', 8), (7.5612, 'HospitalHealingCompletion', 7)]
After Event 15: [(6.1103, 'Arrival', None), (10.9533, 'HospitalHealingCompletion', 8), (7.5612, 'HospitalHealingCompletion', 7), (12.8999, 'DepartureTriage', 9)]
After Event 16: [(7.2726, 'Arrival', None), (7.316, 'DepartureTriage', 10), (12.8999, 'DepartureTriage', 9), (10.9533, 'HospitalHealingCompletion', 8), (7.5612, 'HospitalHealingCompletion', 7)]
After Event 17: [(7.316, 'DepartureTriage', 10), (7.5612, 'HospitalHealingCompletion', 7), (12.8999, 'DepartureTriage', 9), (10.9533, 'HospitalHealingCompletion', 8), (10.408, 'Arrival', None), (19.8016, 'DepartureTriage', 11)]
After Event 18: [(7.5612, 'HospitalHealingCompletion', 7), (10.408, 'Arrival', None), (11.1269, 'HospitalHealingCompletion', 10), (10.9533, 'HospitalHealingCompletion', 8), (19.8016, 'DepartureTriage', 11), (12.8999, 'DepartureTriage', 9)]
After Event 19: [(10.408, 'Arrival', None), (10.9533, 'HospitalHealingCompletion', 8), (11.1269, 'HospitalHealingCompletion', 10), (12.8999, 'DepartureTriage', 9), (19.8016, 'DepartureTriage', 11)]
After Event 20: [(10.9533, 'HospitalHealingCompletion', 8), (12.8999, 'DepartureTriage', 9), (11.1269, 'HospitalHealingCompletion', 10), (19.8016, 'DepartureTriage', 11), (14.218, 'Arrival', None), (12.3686, 'DepartureTriage', 12)]

Results for half_full initial condition, 20 healed patients:
SimulationLength: 26.251625
TotalPatientsArrived: 20.000000
TotalPatientsHealed: 20.000000
ProbabilityTriageEmpty: 0.078060
ProbabilityBedsEmpty: 0.015996
ProbabilityBothEmpty: 0.000000
RejectionProbability: 0.000000
AverageNurseUtilization: 0.609177
AverageOccupiedBeds: 1.793282
ProportionHomeTreated: 0.200000
AverageHealingTime: 5.087082
```

## Half_full Initial Condition with 200 Target Healed Patients

```

Event Trace for First 20 Events:
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|   Event# |    Time | Event Type                |   PatientID |   Triage Queue |   Busy Nurses |   Occupied Beds |   Total Patients |   Total Healed |
+==========+=========+===========================+=============+================+===============+=================+==================+================+
|        1 |  0.0447 | HospitalHealingCompletion |           3 |              0 |             2 |               2 |                0 |              1 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        2 |  0.9234 | Arrival                   |             |              0 |             3 |               2 |                1 |              1 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        3 |  0.9884 | Arrival                   |             |              0 |             4 |               2 |                2 |              1 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        4 |  1.1139 | HospitalHealingCompletion |           4 |              0 |             4 |               1 |                2 |              2 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        5 |  1.3323 | DepartureTriage           |           1 |              0 |             3 |               2 |                2 |              2 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        6 |  1.3627 | HospitalHealingCompletion |           5 |              0 |             3 |               1 |                2 |              3 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        7 |  1.8364 | DepartureTriage           |           2 |              0 |             2 |               1 |                2 |              3 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        8 |  1.9119 | Arrival                   |             |              0 |             3 |               1 |                3 |              3 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        9 |  2.0405 | DepartureTriage           |           6 |              0 |             2 |               1 |                3 |              3 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       10 |  3.3879 | DepartureTriage           |           8 |              0 |             1 |               2 |                3 |              3 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       11 |  4.129  | DepartureTriage           |           7 |              0 |             0 |               3 |                3 |              3 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       12 |  5.0266 | HomeHealingCompletion     |           6 |              0 |             0 |               3 |                3 |              4 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       13 |  5.0274 | HomeHealingCompletion     |           2 |              0 |             0 |               3 |                3 |              5 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       14 |  5.2909 | HospitalHealingCompletion |           1 |              0 |             0 |               2 |                3 |              6 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       15 |  5.655  | Arrival                   |             |              0 |             1 |               2 |                4 |              6 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       16 |  6.1103 | Arrival                   |             |              0 |             2 |               2 |                5 |              6 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       17 |  7.2726 | Arrival                   |             |              0 |             3 |               2 |                6 |              6 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       18 |  7.316  | DepartureTriage           |          10 |              0 |             2 |               3 |                6 |              6 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       19 |  7.5612 | HospitalHealingCompletion |           7 |              0 |             2 |               2 |                6 |              7 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       20 | 10.408  | Arrival                   |             |              0 |             3 |               2 |                7 |              7 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+

Future Event Lists:
After Event 1: [(0.9234, 'Arrival', None), (1.1139, 'HospitalHealingCompletion', 4), (1.3323, 'DepartureTriage', 1), (1.8364, 'DepartureTriage', 2), (1.3627, 'HospitalHealingCompletion', 5)]
After Event 2: [(0.9884, 'Arrival', None), (1.1139, 'HospitalHealingCompletion', 4), (1.3323, 'DepartureTriage', 1), (1.8364, 'DepartureTriage', 2), (1.3627, 'HospitalHealingCompletion', 5), (2.0405, 'DepartureTriage', 6)]
After Event 3: [(1.1139, 'HospitalHealingCompletion', 4), (1.3627, 'HospitalHealingCompletion', 5), (1.3323, 'DepartureTriage', 1), (1.8364, 'DepartureTriage', 2), (2.0405, 'DepartureTriage', 6), (1.9119, 'Arrival', None), (4.129, 'DepartureTriage', 7)]
After Event 4: [(1.3323, 'DepartureTriage', 1), (1.3627, 'HospitalHealingCompletion', 5), (1.9119, 'Arrival', None), (1.8364, 'DepartureTriage', 2), (2.0405, 'DepartureTriage', 6), (4.129, 'DepartureTriage', 7)]
After Event 5: [(1.3627, 'HospitalHealingCompletion', 5), (1.8364, 'DepartureTriage', 2), (1.9119, 'Arrival', None), (4.129, 'DepartureTriage', 7), (2.0405, 'DepartureTriage', 6), (5.2909, 'HospitalHealingCompletion', 1)]
After Event 6: [(1.8364, 'DepartureTriage', 2), (2.0405, 'DepartureTriage', 6), (1.9119, 'Arrival', None), (4.129, 'DepartureTriage', 7), (5.2909, 'HospitalHealingCompletion', 1)]
After Event 7: [(1.9119, 'Arrival', None), (2.0405, 'DepartureTriage', 6), (5.2909, 'HospitalHealingCompletion', 1), (4.129, 'DepartureTriage', 7), (5.0274, 'HomeHealingCompletion', 2)]
After Event 8: [(2.0405, 'DepartureTriage', 6), (4.129, 'DepartureTriage', 7), (3.3879, 'DepartureTriage', 8), (5.0274, 'HomeHealingCompletion', 2), (5.655, 'Arrival', None), (5.2909, 'HospitalHealingCompletion', 1)]
After Event 9: [(3.3879, 'DepartureTriage', 8), (4.129, 'DepartureTriage', 7), (5.0266, 'HomeHealingCompletion', 6), (5.0274, 'HomeHealingCompletion', 2), (5.655, 'Arrival', None), (5.2909, 'HospitalHealingCompletion', 1)]
After Event 10: [(4.129, 'DepartureTriage', 7), (5.0274, 'HomeHealingCompletion', 2), (5.0266, 'HomeHealingCompletion', 6), (5.2909, 'HospitalHealingCompletion', 1), (5.655, 'Arrival', None), (10.9533, 'HospitalHealingCompletion', 8)]
After Event 11: [(5.0266, 'HomeHealingCompletion', 6), (5.0274, 'HomeHealingCompletion', 2), (7.5612, 'HospitalHealingCompletion', 7), (5.2909, 'HospitalHealingCompletion', 1), (5.655, 'Arrival', None), (10.9533, 'HospitalHealingCompletion', 8)]
After Event 12: [(5.0274, 'HomeHealingCompletion', 2), (5.2909, 'HospitalHealingCompletion', 1), (7.5612, 'HospitalHealingCompletion', 7), (10.9533, 'HospitalHealingCompletion', 8), (5.655, 'Arrival', None)]
After Event 13: [(5.2909, 'HospitalHealingCompletion', 1), (5.655, 'Arrival', None), (7.5612, 'HospitalHealingCompletion', 7), (10.9533, 'HospitalHealingCompletion', 8)]
After Event 14: [(5.655, 'Arrival', None), (10.9533, 'HospitalHealingCompletion', 8), (7.5612, 'HospitalHealingCompletion', 7)]
After Event 15: [(6.1103, 'Arrival', None), (10.9533, 'HospitalHealingCompletion', 8), (7.5612, 'HospitalHealingCompletion', 7), (12.8999, 'DepartureTriage', 9)]
After Event 16: [(7.2726, 'Arrival', None), (7.316, 'DepartureTriage', 10), (12.8999, 'DepartureTriage', 9), (10.9533, 'HospitalHealingCompletion', 8), (7.5612, 'HospitalHealingCompletion', 7)]
After Event 17: [(7.316, 'DepartureTriage', 10), (7.5612, 'HospitalHealingCompletion', 7), (12.8999, 'DepartureTriage', 9), (10.9533, 'HospitalHealingCompletion', 8), (10.408, 'Arrival', None), (19.8016, 'DepartureTriage', 11)]
After Event 18: [(7.5612, 'HospitalHealingCompletion', 7), (10.408, 'Arrival', None), (11.1269, 'HospitalHealingCompletion', 10), (10.9533, 'HospitalHealingCompletion', 8), (19.8016, 'DepartureTriage', 11), (12.8999, 'DepartureTriage', 9)]
After Event 19: [(10.408, 'Arrival', None), (10.9533, 'HospitalHealingCompletion', 8), (11.1269, 'HospitalHealingCompletion', 10), (12.8999, 'DepartureTriage', 9), (19.8016, 'DepartureTriage', 11)]
After Event 20: [(10.9533, 'HospitalHealingCompletion', 8), (12.8999, 'DepartureTriage', 9), (11.1269, 'HospitalHealingCompletion', 10), (19.8016, 'DepartureTriage', 11), (14.218, 'Arrival', None), (12.3686, 'DepartureTriage', 12)]

Results for half_full initial condition, 200 healed patients:
SimulationLength: 218.819863
TotalPatientsArrived: 199.000000
TotalPatientsHealed: 200.000000
ProbabilityTriageEmpty: 0.049787
ProbabilityBedsEmpty: 0.008353
ProbabilityBothEmpty: 0.000000
RejectionProbability: 0.163399
AverageNurseUtilization: 0.679209
AverageOccupiedBeds: 4.116812
ProportionHomeTreated: 0.355000
AverageHealingTime: 10.014572
```

## Half_full Initial Condition with 1000 Target Healed Patients

```

Event Trace for First 20 Events:
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|   Event# |    Time | Event Type                |   PatientID |   Triage Queue |   Busy Nurses |   Occupied Beds |   Total Patients |   Total Healed |
+==========+=========+===========================+=============+================+===============+=================+==================+================+
|        1 |  0.0447 | HospitalHealingCompletion |           3 |              0 |             2 |               2 |                0 |              1 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        2 |  0.9234 | Arrival                   |             |              0 |             3 |               2 |                1 |              1 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        3 |  0.9884 | Arrival                   |             |              0 |             4 |               2 |                2 |              1 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        4 |  1.1139 | HospitalHealingCompletion |           4 |              0 |             4 |               1 |                2 |              2 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        5 |  1.3323 | DepartureTriage           |           1 |              0 |             3 |               2 |                2 |              2 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        6 |  1.3627 | HospitalHealingCompletion |           5 |              0 |             3 |               1 |                2 |              3 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        7 |  1.8364 | DepartureTriage           |           2 |              0 |             2 |               1 |                2 |              3 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        8 |  1.9119 | Arrival                   |             |              0 |             3 |               1 |                3 |              3 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        9 |  2.0405 | DepartureTriage           |           6 |              0 |             2 |               1 |                3 |              3 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       10 |  3.3879 | DepartureTriage           |           8 |              0 |             1 |               2 |                3 |              3 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       11 |  4.129  | DepartureTriage           |           7 |              0 |             0 |               3 |                3 |              3 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       12 |  5.0266 | HomeHealingCompletion     |           6 |              0 |             0 |               3 |                3 |              4 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       13 |  5.0274 | HomeHealingCompletion     |           2 |              0 |             0 |               3 |                3 |              5 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       14 |  5.2909 | HospitalHealingCompletion |           1 |              0 |             0 |               2 |                3 |              6 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       15 |  5.655  | Arrival                   |             |              0 |             1 |               2 |                4 |              6 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       16 |  6.1103 | Arrival                   |             |              0 |             2 |               2 |                5 |              6 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       17 |  7.2726 | Arrival                   |             |              0 |             3 |               2 |                6 |              6 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       18 |  7.316  | DepartureTriage           |          10 |              0 |             2 |               3 |                6 |              6 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       19 |  7.5612 | HospitalHealingCompletion |           7 |              0 |             2 |               2 |                6 |              7 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       20 | 10.408  | Arrival                   |             |              0 |             3 |               2 |                7 |              7 |
+----------+---------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+

Future Event Lists:
After Event 1: [(0.9234, 'Arrival', None), (1.1139, 'HospitalHealingCompletion', 4), (1.3323, 'DepartureTriage', 1), (1.8364, 'DepartureTriage', 2), (1.3627, 'HospitalHealingCompletion', 5)]
After Event 2: [(0.9884, 'Arrival', None), (1.1139, 'HospitalHealingCompletion', 4), (1.3323, 'DepartureTriage', 1), (1.8364, 'DepartureTriage', 2), (1.3627, 'HospitalHealingCompletion', 5), (2.0405, 'DepartureTriage', 6)]
After Event 3: [(1.1139, 'HospitalHealingCompletion', 4), (1.3627, 'HospitalHealingCompletion', 5), (1.3323, 'DepartureTriage', 1), (1.8364, 'DepartureTriage', 2), (2.0405, 'DepartureTriage', 6), (1.9119, 'Arrival', None), (4.129, 'DepartureTriage', 7)]
After Event 4: [(1.3323, 'DepartureTriage', 1), (1.3627, 'HospitalHealingCompletion', 5), (1.9119, 'Arrival', None), (1.8364, 'DepartureTriage', 2), (2.0405, 'DepartureTriage', 6), (4.129, 'DepartureTriage', 7)]
After Event 5: [(1.3627, 'HospitalHealingCompletion', 5), (1.8364, 'DepartureTriage', 2), (1.9119, 'Arrival', None), (4.129, 'DepartureTriage', 7), (2.0405, 'DepartureTriage', 6), (5.2909, 'HospitalHealingCompletion', 1)]
After Event 6: [(1.8364, 'DepartureTriage', 2), (2.0405, 'DepartureTriage', 6), (1.9119, 'Arrival', None), (4.129, 'DepartureTriage', 7), (5.2909, 'HospitalHealingCompletion', 1)]
After Event 7: [(1.9119, 'Arrival', None), (2.0405, 'DepartureTriage', 6), (5.2909, 'HospitalHealingCompletion', 1), (4.129, 'DepartureTriage', 7), (5.0274, 'HomeHealingCompletion', 2)]
After Event 8: [(2.0405, 'DepartureTriage', 6), (4.129, 'DepartureTriage', 7), (3.3879, 'DepartureTriage', 8), (5.0274, 'HomeHealingCompletion', 2), (5.655, 'Arrival', None), (5.2909, 'HospitalHealingCompletion', 1)]
After Event 9: [(3.3879, 'DepartureTriage', 8), (4.129, 'DepartureTriage', 7), (5.0266, 'HomeHealingCompletion', 6), (5.0274, 'HomeHealingCompletion', 2), (5.655, 'Arrival', None), (5.2909, 'HospitalHealingCompletion', 1)]
After Event 10: [(4.129, 'DepartureTriage', 7), (5.0274, 'HomeHealingCompletion', 2), (5.0266, 'HomeHealingCompletion', 6), (5.2909, 'HospitalHealingCompletion', 1), (5.655, 'Arrival', None), (10.9533, 'HospitalHealingCompletion', 8)]
After Event 11: [(5.0266, 'HomeHealingCompletion', 6), (5.0274, 'HomeHealingCompletion', 2), (7.5612, 'HospitalHealingCompletion', 7), (5.2909, 'HospitalHealingCompletion', 1), (5.655, 'Arrival', None), (10.9533, 'HospitalHealingCompletion', 8)]
After Event 12: [(5.0274, 'HomeHealingCompletion', 2), (5.2909, 'HospitalHealingCompletion', 1), (7.5612, 'HospitalHealingCompletion', 7), (10.9533, 'HospitalHealingCompletion', 8), (5.655, 'Arrival', None)]
After Event 13: [(5.2909, 'HospitalHealingCompletion', 1), (5.655, 'Arrival', None), (7.5612, 'HospitalHealingCompletion', 7), (10.9533, 'HospitalHealingCompletion', 8)]
After Event 14: [(5.655, 'Arrival', None), (10.9533, 'HospitalHealingCompletion', 8), (7.5612, 'HospitalHealingCompletion', 7)]
After Event 15: [(6.1103, 'Arrival', None), (10.9533, 'HospitalHealingCompletion', 8), (7.5612, 'HospitalHealingCompletion', 7), (12.8999, 'DepartureTriage', 9)]
After Event 16: [(7.2726, 'Arrival', None), (7.316, 'DepartureTriage', 10), (12.8999, 'DepartureTriage', 9), (10.9533, 'HospitalHealingCompletion', 8), (7.5612, 'HospitalHealingCompletion', 7)]
After Event 17: [(7.316, 'DepartureTriage', 10), (7.5612, 'HospitalHealingCompletion', 7), (12.8999, 'DepartureTriage', 9), (10.9533, 'HospitalHealingCompletion', 8), (10.408, 'Arrival', None), (19.8016, 'DepartureTriage', 11)]
After Event 18: [(7.5612, 'HospitalHealingCompletion', 7), (10.408, 'Arrival', None), (11.1269, 'HospitalHealingCompletion', 10), (10.9533, 'HospitalHealingCompletion', 8), (19.8016, 'DepartureTriage', 11), (12.8999, 'DepartureTriage', 9)]
After Event 19: [(10.408, 'Arrival', None), (10.9533, 'HospitalHealingCompletion', 8), (11.1269, 'HospitalHealingCompletion', 10), (12.8999, 'DepartureTriage', 9), (19.8016, 'DepartureTriage', 11)]
After Event 20: [(10.9533, 'HospitalHealingCompletion', 8), (12.8999, 'DepartureTriage', 9), (11.1269, 'HospitalHealingCompletion', 10), (19.8016, 'DepartureTriage', 11), (14.218, 'Arrival', None), (12.3686, 'DepartureTriage', 12)]

Results for half_full initial condition, 1000 healed patients:
SimulationLength: 1005.065326
TotalPatientsArrived: 1017.000000
TotalPatientsHealed: 1000.000000
ProbabilityTriageEmpty: 0.036858
ProbabilityBedsEmpty: 0.014190
ProbabilityBothEmpty: 0.000000
RejectionProbability: 0.127005
AverageNurseUtilization: 0.757579
AverageOccupiedBeds: 4.283160
ProportionHomeTreated: 0.357000
AverageHealingTime: 10.893890
```

## Full Initial Condition with 20 Target Healed Patients

```

Event Trace for First 20 Events:
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|   Event# |   Time | Event Type                |   PatientID |   Triage Queue |   Busy Nurses |   Occupied Beds |   Total Patients |   Total Healed |
+==========+========+===========================+=============+================+===============+=================+==================+================+
|        1 | 0.0205 | DepartureTriage           |           3 |              0 |             3 |               7 |                0 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        2 | 0.4245 | HospitalHealingCompletion |           7 |              0 |             3 |               6 |                0 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        3 | 0.5115 | DepartureTriage           |           4 |              0 |             2 |               6 |                0 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        4 | 0.6059 | Arrival                   |             |              0 |             3 |               6 |                1 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        5 | 1.3323 | DepartureTriage           |           1 |              0 |             2 |               7 |                1 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        6 | 1.3627 | HospitalHealingCompletion |           5 |              0 |             2 |               6 |                1 |              2 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        7 | 1.8364 | DepartureTriage           |           2 |              0 |             1 |               7 |                1 |              2 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        8 | 2.0393 | DepartureTriage           |          12 |              0 |             0 |               7 |                1 |              2 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        9 | 2.4328 | HospitalHealingCompletion |           8 |              0 |             0 |               6 |                1 |              3 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       10 | 3.2116 | HomeHealingCompletion     |           3 |              0 |             0 |               6 |                1 |              4 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       11 | 3.5865 | HomeHealingCompletion     |           4 |              0 |             0 |               6 |                1 |              5 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       12 | 4.2475 | Arrival                   |             |              0 |             1 |               6 |                2 |              5 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       13 | 4.6494 | Arrival                   |             |              0 |             2 |               6 |                3 |              5 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       14 | 5.2686 | HospitalHealingCompletion |           2 |              0 |             2 |               5 |                3 |              6 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       15 | 5.9481 | DepartureTriage           |          14 |              0 |             1 |               6 |                3 |              6 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       16 | 5.9929 | HospitalHealingCompletion |          11 |              0 |             1 |               5 |                3 |              7 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       17 | 6.0328 | HospitalHealingCompletion |           6 |              0 |             1 |               4 |                3 |              8 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       18 | 6.0338 | HospitalHealingCompletion |           9 |              0 |             1 |               3 |                3 |              9 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       19 | 6.8397 | HospitalHealingCompletion |          10 |              0 |             1 |               2 |                3 |             10 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       20 | 8.8257 | Arrival                   |             |              0 |             2 |               2 |                4 |             10 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+

Future Event Lists:
After Event 1: [(0.4245, 'HospitalHealingCompletion', 7), (0.5115, 'DepartureTriage', 4), (0.6059, 'Arrival', None), (1.8364, 'DepartureTriage', 2), (1.3627, 'HospitalHealingCompletion', 5), (3.2116, 'HomeHealingCompletion', 3), (1.3323, 'DepartureTriage', 1), (2.4328, 'HospitalHealingCompletion', 8), (6.0338, 'HospitalHealingCompletion', 9), (6.8397, 'HospitalHealingCompletion', 10), (5.9929, 'HospitalHealingCompletion', 11), (6.0328, 'HospitalHealingCompletion', 6)]
After Event 2: [(0.5115, 'DepartureTriage', 4), (1.3627, 'HospitalHealingCompletion', 5), (0.6059, 'Arrival', None), (1.8364, 'DepartureTriage', 2), (5.9929, 'HospitalHealingCompletion', 11), (3.2116, 'HomeHealingCompletion', 3), (1.3323, 'DepartureTriage', 1), (2.4328, 'HospitalHealingCompletion', 8), (6.0338, 'HospitalHealingCompletion', 9), (6.8397, 'HospitalHealingCompletion', 10), (6.0328, 'HospitalHealingCompletion', 6)]
After Event 3: [(0.6059, 'Arrival', None), (1.3627, 'HospitalHealingCompletion', 5), (1.3323, 'DepartureTriage', 1), (1.8364, 'DepartureTriage', 2), (3.5865, 'HomeHealingCompletion', 4), (3.2116, 'HomeHealingCompletion', 3), (6.0328, 'HospitalHealingCompletion', 6), (2.4328, 'HospitalHealingCompletion', 8), (6.0338, 'HospitalHealingCompletion', 9), (6.8397, 'HospitalHealingCompletion', 10), (5.9929, 'HospitalHealingCompletion', 11)]
After Event 4: [(1.3323, 'DepartureTriage', 1), (1.3627, 'HospitalHealingCompletion', 5), (2.0393, 'DepartureTriage', 12), (1.8364, 'DepartureTriage', 2), (3.5865, 'HomeHealingCompletion', 4), (3.2116, 'HomeHealingCompletion', 3), (6.0328, 'HospitalHealingCompletion', 6), (2.4328, 'HospitalHealingCompletion', 8), (6.0338, 'HospitalHealingCompletion', 9), (6.8397, 'HospitalHealingCompletion', 10), (4.2475, 'Arrival', None), (5.9929, 'HospitalHealingCompletion', 11)]
After Event 5: [(1.3627, 'HospitalHealingCompletion', 5), (1.8364, 'DepartureTriage', 2), (2.0393, 'DepartureTriage', 12), (2.4328, 'HospitalHealingCompletion', 8), (3.5865, 'HomeHealingCompletion', 4), (3.2116, 'HomeHealingCompletion', 3), (6.0328, 'HospitalHealingCompletion', 6), (5.9929, 'HospitalHealingCompletion', 11), (6.0338, 'HospitalHealingCompletion', 9), (6.8397, 'HospitalHealingCompletion', 10), (4.2475, 'Arrival', None), (8.8977, 'HospitalHealingCompletion', 1)]
After Event 6: [(1.8364, 'DepartureTriage', 2), (2.4328, 'HospitalHealingCompletion', 8), (2.0393, 'DepartureTriage', 12), (5.9929, 'HospitalHealingCompletion', 11), (3.5865, 'HomeHealingCompletion', 4), (3.2116, 'HomeHealingCompletion', 3), (6.0328, 'HospitalHealingCompletion', 6), (8.8977, 'HospitalHealingCompletion', 1), (6.0338, 'HospitalHealingCompletion', 9), (6.8397, 'HospitalHealingCompletion', 10), (4.2475, 'Arrival', None)]
After Event 7: [(2.0393, 'DepartureTriage', 12), (2.4328, 'HospitalHealingCompletion', 8), (3.2116, 'HomeHealingCompletion', 3), (5.9929, 'HospitalHealingCompletion', 11), (3.5865, 'HomeHealingCompletion', 4), (4.2475, 'Arrival', None), (6.0328, 'HospitalHealingCompletion', 6), (8.8977, 'HospitalHealingCompletion', 1), (6.0338, 'HospitalHealingCompletion', 9), (6.8397, 'HospitalHealingCompletion', 10), (5.2686, 'HospitalHealingCompletion', 2)]
After Event 8: [(2.4328, 'HospitalHealingCompletion', 8), (3.5865, 'HomeHealingCompletion', 4), (3.2116, 'HomeHealingCompletion', 3), (5.9929, 'HospitalHealingCompletion', 11), (5.2686, 'HospitalHealingCompletion', 2), (4.2475, 'Arrival', None), (6.0328, 'HospitalHealingCompletion', 6), (8.8977, 'HospitalHealingCompletion', 1), (6.0338, 'HospitalHealingCompletion', 9), (6.8397, 'HospitalHealingCompletion', 10), (24.2288, 'HomeHealingCompletion', 12)]
After Event 9: [(3.2116, 'HomeHealingCompletion', 3), (3.5865, 'HomeHealingCompletion', 4), (4.2475, 'Arrival', None), (5.9929, 'HospitalHealingCompletion', 11), (5.2686, 'HospitalHealingCompletion', 2), (24.2288, 'HomeHealingCompletion', 12), (6.0328, 'HospitalHealingCompletion', 6), (8.8977, 'HospitalHealingCompletion', 1), (6.0338, 'HospitalHealingCompletion', 9), (6.8397, 'HospitalHealingCompletion', 10)]
After Event 10: [(3.5865, 'HomeHealingCompletion', 4), (5.2686, 'HospitalHealingCompletion', 2), (4.2475, 'Arrival', None), (5.9929, 'HospitalHealingCompletion', 11), (6.8397, 'HospitalHealingCompletion', 10), (24.2288, 'HomeHealingCompletion', 12), (6.0328, 'HospitalHealingCompletion', 6), (8.8977, 'HospitalHealingCompletion', 1), (6.0338, 'HospitalHealingCompletion', 9)]
After Event 11: [(4.2475, 'Arrival', None), (5.2686, 'HospitalHealingCompletion', 2), (6.0328, 'HospitalHealingCompletion', 6), (5.9929, 'HospitalHealingCompletion', 11), (6.8397, 'HospitalHealingCompletion', 10), (24.2288, 'HomeHealingCompletion', 12), (6.0338, 'HospitalHealingCompletion', 9), (8.8977, 'HospitalHealingCompletion', 1)]
After Event 12: [(4.6494, 'Arrival', None), (5.2686, 'HospitalHealingCompletion', 2), (6.0328, 'HospitalHealingCompletion', 6), (5.9929, 'HospitalHealingCompletion', 11), (6.8397, 'HospitalHealingCompletion', 10), (24.2288, 'HomeHealingCompletion', 12), (6.0338, 'HospitalHealingCompletion', 9), (8.8977, 'HospitalHealingCompletion', 1), (13.6539, 'DepartureTriage', 13)]
After Event 13: [(5.2686, 'HospitalHealingCompletion', 2), (5.9481, 'DepartureTriage', 14), (6.0328, 'HospitalHealingCompletion', 6), (8.8257, 'Arrival', None), (5.9929, 'HospitalHealingCompletion', 11), (24.2288, 'HomeHealingCompletion', 12), (6.0338, 'HospitalHealingCompletion', 9), (13.6539, 'DepartureTriage', 13), (8.8977, 'HospitalHealingCompletion', 1), (6.8397, 'HospitalHealingCompletion', 10)]
After Event 14: [(5.9481, 'DepartureTriage', 14), (5.9929, 'HospitalHealingCompletion', 11), (6.0328, 'HospitalHealingCompletion', 6), (8.8257, 'Arrival', None), (6.8397, 'HospitalHealingCompletion', 10), (24.2288, 'HomeHealingCompletion', 12), (6.0338, 'HospitalHealingCompletion', 9), (13.6539, 'DepartureTriage', 13), (8.8977, 'HospitalHealingCompletion', 1)]
After Event 15: [(5.9929, 'HospitalHealingCompletion', 11), (6.8397, 'HospitalHealingCompletion', 10), (6.0328, 'HospitalHealingCompletion', 6), (8.8257, 'Arrival', None), (8.8977, 'HospitalHealingCompletion', 1), (24.2288, 'HomeHealingCompletion', 12), (6.0338, 'HospitalHealingCompletion', 9), (13.6539, 'DepartureTriage', 13), (30.84, 'HospitalHealingCompletion', 14)]
After Event 16: [(6.0328, 'HospitalHealingCompletion', 6), (6.8397, 'HospitalHealingCompletion', 10), (6.0338, 'HospitalHealingCompletion', 9), (8.8257, 'Arrival', None), (8.8977, 'HospitalHealingCompletion', 1), (24.2288, 'HomeHealingCompletion', 12), (30.84, 'HospitalHealingCompletion', 14), (13.6539, 'DepartureTriage', 13)]
After Event 17: [(6.0338, 'HospitalHealingCompletion', 9), (6.8397, 'HospitalHealingCompletion', 10), (13.6539, 'DepartureTriage', 13), (8.8257, 'Arrival', None), (8.8977, 'HospitalHealingCompletion', 1), (24.2288, 'HomeHealingCompletion', 12), (30.84, 'HospitalHealingCompletion', 14)]
After Event 18: [(6.8397, 'HospitalHealingCompletion', 10), (8.8257, 'Arrival', None), (13.6539, 'DepartureTriage', 13), (30.84, 'HospitalHealingCompletion', 14), (8.8977, 'HospitalHealingCompletion', 1), (24.2288, 'HomeHealingCompletion', 12)]
After Event 19: [(8.8257, 'Arrival', None), (8.8977, 'HospitalHealingCompletion', 1), (13.6539, 'DepartureTriage', 13), (30.84, 'HospitalHealingCompletion', 14), (24.2288, 'HomeHealingCompletion', 12)]
After Event 20: [(8.8977, 'HospitalHealingCompletion', 1), (9.4792, 'Arrival', None), (11.2487, 'DepartureTriage', 15), (30.84, 'HospitalHealingCompletion', 14), (24.2288, 'HomeHealingCompletion', 12), (13.6539, 'DepartureTriage', 13)]

Results for full initial condition, 20 healed patients:
SimulationLength: 21.382099
TotalPatientsArrived: 21.000000
TotalPatientsHealed: 20.000000
ProbabilityTriageEmpty: 0.081847
ProbabilityBedsEmpty: 0.000000
ProbabilityBothEmpty: 0.000000
RejectionProbability: 0.266667
AverageNurseUtilization: 0.507520
AverageOccupiedBeds: 4.528530
ProportionHomeTreated: 0.500000
AverageHealingTime: 5.803015
```

## Full Initial Condition with 200 Target Healed Patients

```

Event Trace for First 20 Events:
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|   Event# |   Time | Event Type                |   PatientID |   Triage Queue |   Busy Nurses |   Occupied Beds |   Total Patients |   Total Healed |
+==========+========+===========================+=============+================+===============+=================+==================+================+
|        1 | 0.0205 | DepartureTriage           |           3 |              0 |             3 |               7 |                0 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        2 | 0.4245 | HospitalHealingCompletion |           7 |              0 |             3 |               6 |                0 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        3 | 0.5115 | DepartureTriage           |           4 |              0 |             2 |               6 |                0 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        4 | 0.6059 | Arrival                   |             |              0 |             3 |               6 |                1 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        5 | 1.3323 | DepartureTriage           |           1 |              0 |             2 |               7 |                1 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        6 | 1.3627 | HospitalHealingCompletion |           5 |              0 |             2 |               6 |                1 |              2 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        7 | 1.8364 | DepartureTriage           |           2 |              0 |             1 |               7 |                1 |              2 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        8 | 2.0393 | DepartureTriage           |          12 |              0 |             0 |               7 |                1 |              2 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        9 | 2.4328 | HospitalHealingCompletion |           8 |              0 |             0 |               6 |                1 |              3 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       10 | 3.2116 | HomeHealingCompletion     |           3 |              0 |             0 |               6 |                1 |              4 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       11 | 3.5865 | HomeHealingCompletion     |           4 |              0 |             0 |               6 |                1 |              5 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       12 | 4.2475 | Arrival                   |             |              0 |             1 |               6 |                2 |              5 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       13 | 4.6494 | Arrival                   |             |              0 |             2 |               6 |                3 |              5 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       14 | 5.2686 | HospitalHealingCompletion |           2 |              0 |             2 |               5 |                3 |              6 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       15 | 5.9481 | DepartureTriage           |          14 |              0 |             1 |               6 |                3 |              6 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       16 | 5.9929 | HospitalHealingCompletion |          11 |              0 |             1 |               5 |                3 |              7 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       17 | 6.0328 | HospitalHealingCompletion |           6 |              0 |             1 |               4 |                3 |              8 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       18 | 6.0338 | HospitalHealingCompletion |           9 |              0 |             1 |               3 |                3 |              9 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       19 | 6.8397 | HospitalHealingCompletion |          10 |              0 |             1 |               2 |                3 |             10 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       20 | 8.8257 | Arrival                   |             |              0 |             2 |               2 |                4 |             10 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+

Future Event Lists:
After Event 1: [(0.4245, 'HospitalHealingCompletion', 7), (0.5115, 'DepartureTriage', 4), (0.6059, 'Arrival', None), (1.8364, 'DepartureTriage', 2), (1.3627, 'HospitalHealingCompletion', 5), (3.2116, 'HomeHealingCompletion', 3), (1.3323, 'DepartureTriage', 1), (2.4328, 'HospitalHealingCompletion', 8), (6.0338, 'HospitalHealingCompletion', 9), (6.8397, 'HospitalHealingCompletion', 10), (5.9929, 'HospitalHealingCompletion', 11), (6.0328, 'HospitalHealingCompletion', 6)]
After Event 2: [(0.5115, 'DepartureTriage', 4), (1.3627, 'HospitalHealingCompletion', 5), (0.6059, 'Arrival', None), (1.8364, 'DepartureTriage', 2), (5.9929, 'HospitalHealingCompletion', 11), (3.2116, 'HomeHealingCompletion', 3), (1.3323, 'DepartureTriage', 1), (2.4328, 'HospitalHealingCompletion', 8), (6.0338, 'HospitalHealingCompletion', 9), (6.8397, 'HospitalHealingCompletion', 10), (6.0328, 'HospitalHealingCompletion', 6)]
After Event 3: [(0.6059, 'Arrival', None), (1.3627, 'HospitalHealingCompletion', 5), (1.3323, 'DepartureTriage', 1), (1.8364, 'DepartureTriage', 2), (3.5865, 'HomeHealingCompletion', 4), (3.2116, 'HomeHealingCompletion', 3), (6.0328, 'HospitalHealingCompletion', 6), (2.4328, 'HospitalHealingCompletion', 8), (6.0338, 'HospitalHealingCompletion', 9), (6.8397, 'HospitalHealingCompletion', 10), (5.9929, 'HospitalHealingCompletion', 11)]
After Event 4: [(1.3323, 'DepartureTriage', 1), (1.3627, 'HospitalHealingCompletion', 5), (2.0393, 'DepartureTriage', 12), (1.8364, 'DepartureTriage', 2), (3.5865, 'HomeHealingCompletion', 4), (3.2116, 'HomeHealingCompletion', 3), (6.0328, 'HospitalHealingCompletion', 6), (2.4328, 'HospitalHealingCompletion', 8), (6.0338, 'HospitalHealingCompletion', 9), (6.8397, 'HospitalHealingCompletion', 10), (4.2475, 'Arrival', None), (5.9929, 'HospitalHealingCompletion', 11)]
After Event 5: [(1.3627, 'HospitalHealingCompletion', 5), (1.8364, 'DepartureTriage', 2), (2.0393, 'DepartureTriage', 12), (2.4328, 'HospitalHealingCompletion', 8), (3.5865, 'HomeHealingCompletion', 4), (3.2116, 'HomeHealingCompletion', 3), (6.0328, 'HospitalHealingCompletion', 6), (5.9929, 'HospitalHealingCompletion', 11), (6.0338, 'HospitalHealingCompletion', 9), (6.8397, 'HospitalHealingCompletion', 10), (4.2475, 'Arrival', None), (8.8977, 'HospitalHealingCompletion', 1)]
After Event 6: [(1.8364, 'DepartureTriage', 2), (2.4328, 'HospitalHealingCompletion', 8), (2.0393, 'DepartureTriage', 12), (5.9929, 'HospitalHealingCompletion', 11), (3.5865, 'HomeHealingCompletion', 4), (3.2116, 'HomeHealingCompletion', 3), (6.0328, 'HospitalHealingCompletion', 6), (8.8977, 'HospitalHealingCompletion', 1), (6.0338, 'HospitalHealingCompletion', 9), (6.8397, 'HospitalHealingCompletion', 10), (4.2475, 'Arrival', None)]
After Event 7: [(2.0393, 'DepartureTriage', 12), (2.4328, 'HospitalHealingCompletion', 8), (3.2116, 'HomeHealingCompletion', 3), (5.9929, 'HospitalHealingCompletion', 11), (3.5865, 'HomeHealingCompletion', 4), (4.2475, 'Arrival', None), (6.0328, 'HospitalHealingCompletion', 6), (8.8977, 'HospitalHealingCompletion', 1), (6.0338, 'HospitalHealingCompletion', 9), (6.8397, 'HospitalHealingCompletion', 10), (5.2686, 'HospitalHealingCompletion', 2)]
After Event 8: [(2.4328, 'HospitalHealingCompletion', 8), (3.5865, 'HomeHealingCompletion', 4), (3.2116, 'HomeHealingCompletion', 3), (5.9929, 'HospitalHealingCompletion', 11), (5.2686, 'HospitalHealingCompletion', 2), (4.2475, 'Arrival', None), (6.0328, 'HospitalHealingCompletion', 6), (8.8977, 'HospitalHealingCompletion', 1), (6.0338, 'HospitalHealingCompletion', 9), (6.8397, 'HospitalHealingCompletion', 10), (24.2288, 'HomeHealingCompletion', 12)]
After Event 9: [(3.2116, 'HomeHealingCompletion', 3), (3.5865, 'HomeHealingCompletion', 4), (4.2475, 'Arrival', None), (5.9929, 'HospitalHealingCompletion', 11), (5.2686, 'HospitalHealingCompletion', 2), (24.2288, 'HomeHealingCompletion', 12), (6.0328, 'HospitalHealingCompletion', 6), (8.8977, 'HospitalHealingCompletion', 1), (6.0338, 'HospitalHealingCompletion', 9), (6.8397, 'HospitalHealingCompletion', 10)]
After Event 10: [(3.5865, 'HomeHealingCompletion', 4), (5.2686, 'HospitalHealingCompletion', 2), (4.2475, 'Arrival', None), (5.9929, 'HospitalHealingCompletion', 11), (6.8397, 'HospitalHealingCompletion', 10), (24.2288, 'HomeHealingCompletion', 12), (6.0328, 'HospitalHealingCompletion', 6), (8.8977, 'HospitalHealingCompletion', 1), (6.0338, 'HospitalHealingCompletion', 9)]
After Event 11: [(4.2475, 'Arrival', None), (5.2686, 'HospitalHealingCompletion', 2), (6.0328, 'HospitalHealingCompletion', 6), (5.9929, 'HospitalHealingCompletion', 11), (6.8397, 'HospitalHealingCompletion', 10), (24.2288, 'HomeHealingCompletion', 12), (6.0338, 'HospitalHealingCompletion', 9), (8.8977, 'HospitalHealingCompletion', 1)]
After Event 12: [(4.6494, 'Arrival', None), (5.2686, 'HospitalHealingCompletion', 2), (6.0328, 'HospitalHealingCompletion', 6), (5.9929, 'HospitalHealingCompletion', 11), (6.8397, 'HospitalHealingCompletion', 10), (24.2288, 'HomeHealingCompletion', 12), (6.0338, 'HospitalHealingCompletion', 9), (8.8977, 'HospitalHealingCompletion', 1), (13.6539, 'DepartureTriage', 13)]
After Event 13: [(5.2686, 'HospitalHealingCompletion', 2), (5.9481, 'DepartureTriage', 14), (6.0328, 'HospitalHealingCompletion', 6), (8.8257, 'Arrival', None), (5.9929, 'HospitalHealingCompletion', 11), (24.2288, 'HomeHealingCompletion', 12), (6.0338, 'HospitalHealingCompletion', 9), (13.6539, 'DepartureTriage', 13), (8.8977, 'HospitalHealingCompletion', 1), (6.8397, 'HospitalHealingCompletion', 10)]
After Event 14: [(5.9481, 'DepartureTriage', 14), (5.9929, 'HospitalHealingCompletion', 11), (6.0328, 'HospitalHealingCompletion', 6), (8.8257, 'Arrival', None), (6.8397, 'HospitalHealingCompletion', 10), (24.2288, 'HomeHealingCompletion', 12), (6.0338, 'HospitalHealingCompletion', 9), (13.6539, 'DepartureTriage', 13), (8.8977, 'HospitalHealingCompletion', 1)]
After Event 15: [(5.9929, 'HospitalHealingCompletion', 11), (6.8397, 'HospitalHealingCompletion', 10), (6.0328, 'HospitalHealingCompletion', 6), (8.8257, 'Arrival', None), (8.8977, 'HospitalHealingCompletion', 1), (24.2288, 'HomeHealingCompletion', 12), (6.0338, 'HospitalHealingCompletion', 9), (13.6539, 'DepartureTriage', 13), (30.84, 'HospitalHealingCompletion', 14)]
After Event 16: [(6.0328, 'HospitalHealingCompletion', 6), (6.8397, 'HospitalHealingCompletion', 10), (6.0338, 'HospitalHealingCompletion', 9), (8.8257, 'Arrival', None), (8.8977, 'HospitalHealingCompletion', 1), (24.2288, 'HomeHealingCompletion', 12), (30.84, 'HospitalHealingCompletion', 14), (13.6539, 'DepartureTriage', 13)]
After Event 17: [(6.0338, 'HospitalHealingCompletion', 9), (6.8397, 'HospitalHealingCompletion', 10), (13.6539, 'DepartureTriage', 13), (8.8257, 'Arrival', None), (8.8977, 'HospitalHealingCompletion', 1), (24.2288, 'HomeHealingCompletion', 12), (30.84, 'HospitalHealingCompletion', 14)]
After Event 18: [(6.8397, 'HospitalHealingCompletion', 10), (8.8257, 'Arrival', None), (13.6539, 'DepartureTriage', 13), (30.84, 'HospitalHealingCompletion', 14), (8.8977, 'HospitalHealingCompletion', 1), (24.2288, 'HomeHealingCompletion', 12)]
After Event 19: [(8.8257, 'Arrival', None), (8.8977, 'HospitalHealingCompletion', 1), (13.6539, 'DepartureTriage', 13), (30.84, 'HospitalHealingCompletion', 14), (24.2288, 'HomeHealingCompletion', 12)]
After Event 20: [(8.8977, 'HospitalHealingCompletion', 1), (9.4792, 'Arrival', None), (11.2487, 'DepartureTriage', 15), (30.84, 'HospitalHealingCompletion', 14), (24.2288, 'HomeHealingCompletion', 12), (13.6539, 'DepartureTriage', 13)]

Results for full initial condition, 200 healed patients:
SimulationLength: 219.572188
TotalPatientsArrived: 198.000000
TotalPatientsHealed: 200.000000
ProbabilityTriageEmpty: 0.039760
ProbabilityBedsEmpty: 0.000000
ProbabilityBothEmpty: 0.000000
RejectionProbability: 0.183007
AverageNurseUtilization: 0.641378
AverageOccupiedBeds: 4.472977
ProportionHomeTreated: 0.360000
AverageHealingTime: 10.111273
```

## Full Initial Condition with 1000 Target Healed Patients

```

Event Trace for First 20 Events:
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|   Event# |   Time | Event Type                |   PatientID |   Triage Queue |   Busy Nurses |   Occupied Beds |   Total Patients |   Total Healed |
+==========+========+===========================+=============+================+===============+=================+==================+================+
|        1 | 0.0205 | DepartureTriage           |           3 |              0 |             3 |               7 |                0 |              0 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        2 | 0.4245 | HospitalHealingCompletion |           7 |              0 |             3 |               6 |                0 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        3 | 0.5115 | DepartureTriage           |           4 |              0 |             2 |               6 |                0 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        4 | 0.6059 | Arrival                   |             |              0 |             3 |               6 |                1 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        5 | 1.3323 | DepartureTriage           |           1 |              0 |             2 |               7 |                1 |              1 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        6 | 1.3627 | HospitalHealingCompletion |           5 |              0 |             2 |               6 |                1 |              2 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        7 | 1.8364 | DepartureTriage           |           2 |              0 |             1 |               7 |                1 |              2 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        8 | 2.0393 | DepartureTriage           |          12 |              0 |             0 |               7 |                1 |              2 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|        9 | 2.4328 | HospitalHealingCompletion |           8 |              0 |             0 |               6 |                1 |              3 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       10 | 3.2116 | HomeHealingCompletion     |           3 |              0 |             0 |               6 |                1 |              4 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       11 | 3.5865 | HomeHealingCompletion     |           4 |              0 |             0 |               6 |                1 |              5 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       12 | 4.2475 | Arrival                   |             |              0 |             1 |               6 |                2 |              5 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       13 | 4.6494 | Arrival                   |             |              0 |             2 |               6 |                3 |              5 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       14 | 5.2686 | HospitalHealingCompletion |           2 |              0 |             2 |               5 |                3 |              6 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       15 | 5.9481 | DepartureTriage           |          14 |              0 |             1 |               6 |                3 |              6 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       16 | 5.9929 | HospitalHealingCompletion |          11 |              0 |             1 |               5 |                3 |              7 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       17 | 6.0328 | HospitalHealingCompletion |           6 |              0 |             1 |               4 |                3 |              8 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       18 | 6.0338 | HospitalHealingCompletion |           9 |              0 |             1 |               3 |                3 |              9 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       19 | 6.8397 | HospitalHealingCompletion |          10 |              0 |             1 |               2 |                3 |             10 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+
|       20 | 8.8257 | Arrival                   |             |              0 |             2 |               2 |                4 |             10 |
+----------+--------+---------------------------+-------------+----------------+---------------+-----------------+------------------+----------------+

Future Event Lists:
After Event 1: [(0.4245, 'HospitalHealingCompletion', 7), (0.5115, 'DepartureTriage', 4), (0.6059, 'Arrival', None), (1.8364, 'DepartureTriage', 2), (1.3627, 'HospitalHealingCompletion', 5), (3.2116, 'HomeHealingCompletion', 3), (1.3323, 'DepartureTriage', 1), (2.4328, 'HospitalHealingCompletion', 8), (6.0338, 'HospitalHealingCompletion', 9), (6.8397, 'HospitalHealingCompletion', 10), (5.9929, 'HospitalHealingCompletion', 11), (6.0328, 'HospitalHealingCompletion', 6)]
After Event 2: [(0.5115, 'DepartureTriage', 4), (1.3627, 'HospitalHealingCompletion', 5), (0.6059, 'Arrival', None), (1.8364, 'DepartureTriage', 2), (5.9929, 'HospitalHealingCompletion', 11), (3.2116, 'HomeHealingCompletion', 3), (1.3323, 'DepartureTriage', 1), (2.4328, 'HospitalHealingCompletion', 8), (6.0338, 'HospitalHealingCompletion', 9), (6.8397, 'HospitalHealingCompletion', 10), (6.0328, 'HospitalHealingCompletion', 6)]
After Event 3: [(0.6059, 'Arrival', None), (1.3627, 'HospitalHealingCompletion', 5), (1.3323, 'DepartureTriage', 1), (1.8364, 'DepartureTriage', 2), (3.5865, 'HomeHealingCompletion', 4), (3.2116, 'HomeHealingCompletion', 3), (6.0328, 'HospitalHealingCompletion', 6), (2.4328, 'HospitalHealingCompletion', 8), (6.0338, 'HospitalHealingCompletion', 9), (6.8397, 'HospitalHealingCompletion', 10), (5.9929, 'HospitalHealingCompletion', 11)]
After Event 4: [(1.3323, 'DepartureTriage', 1), (1.3627, 'HospitalHealingCompletion', 5), (2.0393, 'DepartureTriage', 12), (1.8364, 'DepartureTriage', 2), (3.5865, 'HomeHealingCompletion', 4), (3.2116, 'HomeHealingCompletion', 3), (6.0328, 'HospitalHealingCompletion', 6), (2.4328, 'HospitalHealingCompletion', 8), (6.0338, 'HospitalHealingCompletion', 9), (6.8397, 'HospitalHealingCompletion', 10), (4.2475, 'Arrival', None), (5.9929, 'HospitalHealingCompletion', 11)]
After Event 5: [(1.3627, 'HospitalHealingCompletion', 5), (1.8364, 'DepartureTriage', 2), (2.0393, 'DepartureTriage', 12), (2.4328, 'HospitalHealingCompletion', 8), (3.5865, 'HomeHealingCompletion', 4), (3.2116, 'HomeHealingCompletion', 3), (6.0328, 'HospitalHealingCompletion', 6), (5.9929, 'HospitalHealingCompletion', 11), (6.0338, 'HospitalHealingCompletion', 9), (6.8397, 'HospitalHealingCompletion', 10), (4.2475, 'Arrival', None), (8.8977, 'HospitalHealingCompletion', 1)]
After Event 6: [(1.8364, 'DepartureTriage', 2), (2.4328, 'HospitalHealingCompletion', 8), (2.0393, 'DepartureTriage', 12), (5.9929, 'HospitalHealingCompletion', 11), (3.5865, 'HomeHealingCompletion', 4), (3.2116, 'HomeHealingCompletion', 3), (6.0328, 'HospitalHealingCompletion', 6), (8.8977, 'HospitalHealingCompletion', 1), (6.0338, 'HospitalHealingCompletion', 9), (6.8397, 'HospitalHealingCompletion', 10), (4.2475, 'Arrival', None)]
After Event 7: [(2.0393, 'DepartureTriage', 12), (2.4328, 'HospitalHealingCompletion', 8), (3.2116, 'HomeHealingCompletion', 3), (5.9929, 'HospitalHealingCompletion', 11), (3.5865, 'HomeHealingCompletion', 4), (4.2475, 'Arrival', None), (6.0328, 'HospitalHealingCompletion', 6), (8.8977, 'HospitalHealingCompletion', 1), (6.0338, 'HospitalHealingCompletion', 9), (6.8397, 'HospitalHealingCompletion', 10), (5.2686, 'HospitalHealingCompletion', 2)]
After Event 8: [(2.4328, 'HospitalHealingCompletion', 8), (3.5865, 'HomeHealingCompletion', 4), (3.2116, 'HomeHealingCompletion', 3), (5.9929, 'HospitalHealingCompletion', 11), (5.2686, 'HospitalHealingCompletion', 2), (4.2475, 'Arrival', None), (6.0328, 'HospitalHealingCompletion', 6), (8.8977, 'HospitalHealingCompletion', 1), (6.0338, 'HospitalHealingCompletion', 9), (6.8397, 'HospitalHealingCompletion', 10), (24.2288, 'HomeHealingCompletion', 12)]
After Event 9: [(3.2116, 'HomeHealingCompletion', 3), (3.5865, 'HomeHealingCompletion', 4), (4.2475, 'Arrival', None), (5.9929, 'HospitalHealingCompletion', 11), (5.2686, 'HospitalHealingCompletion', 2), (24.2288, 'HomeHealingCompletion', 12), (6.0328, 'HospitalHealingCompletion', 6), (8.8977, 'HospitalHealingCompletion', 1), (6.0338, 'HospitalHealingCompletion', 9), (6.8397, 'HospitalHealingCompletion', 10)]
After Event 10: [(3.5865, 'HomeHealingCompletion', 4), (5.2686, 'HospitalHealingCompletion', 2), (4.2475, 'Arrival', None), (5.9929, 'HospitalHealingCompletion', 11), (6.8397, 'HospitalHealingCompletion', 10), (24.2288, 'HomeHealingCompletion', 12), (6.0328, 'HospitalHealingCompletion', 6), (8.8977, 'HospitalHealingCompletion', 1), (6.0338, 'HospitalHealingCompletion', 9)]
After Event 11: [(4.2475, 'Arrival', None), (5.2686, 'HospitalHealingCompletion', 2), (6.0328, 'HospitalHealingCompletion', 6), (5.9929, 'HospitalHealingCompletion', 11), (6.8397, 'HospitalHealingCompletion', 10), (24.2288, 'HomeHealingCompletion', 12), (6.0338, 'HospitalHealingCompletion', 9), (8.8977, 'HospitalHealingCompletion', 1)]
After Event 12: [(4.6494, 'Arrival', None), (5.2686, 'HospitalHealingCompletion', 2), (6.0328, 'HospitalHealingCompletion', 6), (5.9929, 'HospitalHealingCompletion', 11), (6.8397, 'HospitalHealingCompletion', 10), (24.2288, 'HomeHealingCompletion', 12), (6.0338, 'HospitalHealingCompletion', 9), (8.8977, 'HospitalHealingCompletion', 1), (13.6539, 'DepartureTriage', 13)]
After Event 13: [(5.2686, 'HospitalHealingCompletion', 2), (5.9481, 'DepartureTriage', 14), (6.0328, 'HospitalHealingCompletion', 6), (8.8257, 'Arrival', None), (5.9929, 'HospitalHealingCompletion', 11), (24.2288, 'HomeHealingCompletion', 12), (6.0338, 'HospitalHealingCompletion', 9), (13.6539, 'DepartureTriage', 13), (8.8977, 'HospitalHealingCompletion', 1), (6.8397, 'HospitalHealingCompletion', 10)]
After Event 14: [(5.9481, 'DepartureTriage', 14), (5.9929, 'HospitalHealingCompletion', 11), (6.0328, 'HospitalHealingCompletion', 6), (8.8257, 'Arrival', None), (6.8397, 'HospitalHealingCompletion', 10), (24.2288, 'HomeHealingCompletion', 12), (6.0338, 'HospitalHealingCompletion', 9), (13.6539, 'DepartureTriage', 13), (8.8977, 'HospitalHealingCompletion', 1)]
After Event 15: [(5.9929, 'HospitalHealingCompletion', 11), (6.8397, 'HospitalHealingCompletion', 10), (6.0328, 'HospitalHealingCompletion', 6), (8.8257, 'Arrival', None), (8.8977, 'HospitalHealingCompletion', 1), (24.2288, 'HomeHealingCompletion', 12), (6.0338, 'HospitalHealingCompletion', 9), (13.6539, 'DepartureTriage', 13), (30.84, 'HospitalHealingCompletion', 14)]
After Event 16: [(6.0328, 'HospitalHealingCompletion', 6), (6.8397, 'HospitalHealingCompletion', 10), (6.0338, 'HospitalHealingCompletion', 9), (8.8257, 'Arrival', None), (8.8977, 'HospitalHealingCompletion', 1), (24.2288, 'HomeHealingCompletion', 12), (30.84, 'HospitalHealingCompletion', 14), (13.6539, 'DepartureTriage', 13)]
After Event 17: [(6.0338, 'HospitalHealingCompletion', 9), (6.8397, 'HospitalHealingCompletion', 10), (13.6539, 'DepartureTriage', 13), (8.8257, 'Arrival', None), (8.8977, 'HospitalHealingCompletion', 1), (24.2288, 'HomeHealingCompletion', 12), (30.84, 'HospitalHealingCompletion', 14)]
After Event 18: [(6.8397, 'HospitalHealingCompletion', 10), (8.8257, 'Arrival', None), (13.6539, 'DepartureTriage', 13), (30.84, 'HospitalHealingCompletion', 14), (8.8977, 'HospitalHealingCompletion', 1), (24.2288, 'HomeHealingCompletion', 12)]
After Event 19: [(8.8257, 'Arrival', None), (8.8977, 'HospitalHealingCompletion', 1), (13.6539, 'DepartureTriage', 13), (30.84, 'HospitalHealingCompletion', 14), (24.2288, 'HomeHealingCompletion', 12)]
After Event 20: [(8.8977, 'HospitalHealingCompletion', 1), (9.4792, 'Arrival', None), (11.2487, 'DepartureTriage', 15), (30.84, 'HospitalHealingCompletion', 14), (24.2288, 'HomeHealingCompletion', 12), (13.6539, 'DepartureTriage', 13)]

Results for full initial condition, 1000 healed patients:
SimulationLength: 1006.012492
TotalPatientsArrived: 1012.000000
TotalPatientsHealed: 1000.000000
ProbabilityTriageEmpty: 0.033218
ProbabilityBedsEmpty: 0.011235
ProbabilityBothEmpty: 0.000000
RejectionProbability: 0.139628
AverageNurseUtilization: 0.771880
AverageOccupiedBeds: 4.373805
ProportionHomeTreated: 0.360000
AverageHealingTime: 11.217499
```

## Empty Initial Condition - 20 Replications

```

Results for empty with 20 replications:
SimulationLength: 208.548858 [95% CI: 201.411279, 215.686437]
TotalPatientsArrived: 212.150000 [95% CI: 210.442051, 213.857949]
TotalPatientsHealed: 200.000000 [95% CI: 200.000000, 200.000000]
ProbabilityTriageEmpty: 0.033271 [95% CI: 0.025273, 0.041269]
ProbabilityBedsEmpty: 0.029241 [95% CI: 0.018755, 0.039727]
ProbabilityBothEmpty: 0.002417 [95% CI: -0.001095, 0.005928]
RejectionProbability: 0.112365 [95% CI: 0.091446, 0.133285]
AverageNurseUtilization: 0.754527 [95% CI: 0.726000, 0.783054]
AverageOccupiedBeds: 4.212844 [95% CI: 4.056131, 4.369556]
ProportionHomeTreated: 0.347250 [95% CI: 0.328978, 0.365522]
AverageHealingTime: 10.718207 [95% CI: 10.097251, 11.339163]
```

## Half_full Initial Condition - 20 Replications

```

Results for half_full with 20 replications:
SimulationLength: 203.499382 [95% CI: 199.516699, 207.482066]
TotalPatientsArrived: 205.750000 [95% CI: 203.952083, 207.547917]
TotalPatientsHealed: 200.000000 [95% CI: 200.000000, 200.000000]
ProbabilityTriageEmpty: 0.041411 [95% CI: 0.032628, 0.050194]
ProbabilityBedsEmpty: 0.008527 [95% CI: 0.003863, 0.013191]
ProbabilityBothEmpty: 0.000198 [95% CI: -0.000102, 0.000498]
RejectionProbability: 0.127583 [95% CI: 0.108812, 0.146354]
AverageNurseUtilization: 0.743269 [95% CI: 0.720585, 0.765953]
AverageOccupiedBeds: 4.424502 [95% CI: 4.282469, 4.566535]
ProportionHomeTreated: 0.341750 [95% CI: 0.325627, 0.357873]
AverageHealingTime: 10.506737 [95% CI: 10.070308, 10.943166]
```

## Full Initial Condition - 20 Replications

```

Results for full with 20 replications:
SimulationLength: 198.475045 [95% CI: 192.236728, 204.713362]
TotalPatientsArrived: 200.550000 [95% CI: 198.932023, 202.167977]
TotalPatientsHealed: 200.000000 [95% CI: 200.000000, 200.000000]
ProbabilityTriageEmpty: 0.035921 [95% CI: 0.026553, 0.045289]
ProbabilityBedsEmpty: 0.009215 [95% CI: 0.004433, 0.013996]
ProbabilityBothEmpty: 0.000000 [95% CI: 0.000000, 0.000000]
RejectionProbability: 0.129331 [95% CI: 0.112587, 0.146074]
AverageNurseUtilization: 0.743236 [95% CI: 0.709173, 0.777300]
AverageOccupiedBeds: 4.331623 [95% CI: 4.207477, 4.455769]
ProportionHomeTreated: 0.347000 [95% CI: 0.330688, 0.363312]
AverageHealingTime: 10.254724 [95% CI: 9.869527, 10.639921]
```

## Comparison of Results

```

================================================================================
Comparison of Results Across Initial Conditions and Run Lengths
================================================================================

Comparison for 20 healed patients:

ProbabilityTriageEmpty:
  empty: 0.083793
  half_full: 0.078060
  full: 0.081847

ProbabilityBedsEmpty:
  empty: 0.018475
  half_full: 0.015996
  full: 0.000000

RejectionProbability:
  empty: 0.222222
  half_full: 0.000000
  full: 0.266667

AverageNurseUtilization:
  empty: 0.714442
  half_full: 0.609177
  full: 0.507520

AverageOccupiedBeds:
  empty: 2.650335
  half_full: 1.793282
  full: 4.528530

ProportionHomeTreated:
  empty: 0.600000
  half_full: 0.200000
  full: 0.500000

Comparison for 200 healed patients:

ProbabilityTriageEmpty:
  empty: 0.038114
  half_full: 0.049787
  full: 0.039760

ProbabilityBedsEmpty:
  empty: 0.002001
  half_full: 0.008353
  full: 0.000000

RejectionProbability:
  empty: 0.173077
  half_full: 0.163399
  full: 0.183007

AverageNurseUtilization:
  empty: 0.665023
  half_full: 0.679209
  full: 0.641378

AverageOccupiedBeds:
  empty: 4.046931
  half_full: 4.116812
  full: 4.472977

ProportionHomeTreated:
  empty: 0.380000
  half_full: 0.355000
  full: 0.360000

Comparison for 1000 healed patients:

ProbabilityTriageEmpty:
  empty: 0.033074
  half_full: 0.036858
  full: 0.033218

ProbabilityBedsEmpty:
  empty: 0.011644
  half_full: 0.014190
  full: 0.011235

RejectionProbability:
  empty: 0.138114
  half_full: 0.127005
  full: 0.139628

AverageNurseUtilization:
  empty: 0.775408
  half_full: 0.757579
  full: 0.771880

AverageOccupiedBeds:
  empty: 4.290690
  half_full: 4.283160
  full: 4.373805

ProportionHomeTreated:
  empty: 0.363000
  half_full: 0.357000
  full: 0.360000

================================================================================
Convergence Analysis as Simulation Length Increases
================================================================================

Convergence for empty initial condition:

ProbabilityTriageEmpty:
  20 patients: 0.083793
  200 patients: 0.038114
  1000 patients: 0.033074

ProbabilityBedsEmpty:
  20 patients: 0.018475
  200 patients: 0.002001
  1000 patients: 0.011644

RejectionProbability:
  20 patients: 0.222222
  200 patients: 0.173077
  1000 patients: 0.138114

AverageNurseUtilization:
  20 patients: 0.714442
  200 patients: 0.665023
  1000 patients: 0.775408

AverageOccupiedBeds:
  20 patients: 2.650335
  200 patients: 4.046931
  1000 patients: 4.290690

ProportionHomeTreated:
  20 patients: 0.600000
  200 patients: 0.380000
  1000 patients: 0.363000

Convergence for half_full initial condition:

ProbabilityTriageEmpty:
  20 patients: 0.078060
  200 patients: 0.049787
  1000 patients: 0.036858

ProbabilityBedsEmpty:
  20 patients: 0.015996
  200 patients: 0.008353
  1000 patients: 0.014190

RejectionProbability:
  20 patients: 0.000000
  200 patients: 0.163399
  1000 patients: 0.127005

AverageNurseUtilization:
  20 patients: 0.609177
  200 patients: 0.679209
  1000 patients: 0.757579

AverageOccupiedBeds:
  20 patients: 1.793282
  200 patients: 4.116812
  1000 patients: 4.283160

ProportionHomeTreated:
  20 patients: 0.200000
  200 patients: 0.355000
  1000 patients: 0.357000

Convergence for full initial condition:

ProbabilityTriageEmpty:
  20 patients: 0.081847
  200 patients: 0.039760
  1000 patients: 0.033218

ProbabilityBedsEmpty:
  20 patients: 0.000000
  200 patients: 0.000000
  1000 patients: 0.011235

RejectionProbability:
  20 patients: 0.266667
  200 patients: 0.183007
  1000 patients: 0.139628

AverageNurseUtilization:
  20 patients: 0.507520
  200 patients: 0.641378
  1000 patients: 0.771880

AverageOccupiedBeds:
  20 patients: 4.528530
  200 patients: 4.472977
  1000 patients: 4.373805

ProportionHomeTreated:
  20 patients: 0.500000
  200 patients: 0.360000
  1000 patients: 0.360000
```
