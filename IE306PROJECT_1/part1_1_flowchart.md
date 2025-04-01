graph TD
    A["Start"] --> B["Initialize Simulation (Time=0, Resources Idle, Queues Empty)"];
    B --> C["Schedule First Patient Arrival"];
    C --> D["Get Next Event from FEL"];
    D --> E["Event Type?"];

    E -- Patient Arrival --> F["Update Time, Increment Patient Count"];
    F --> G["Schedule Next Patient Arrival"];
    G --> H["Triage Nurse Available? (Busy less than S)"];
    H -- Yes --> I["Assign Patient to Nurse, Increment Busy Nurses"];
    I --> J["Schedule Triage Completion Event"];
    J --> K["Check Termination Condition"];
    H -- No --> L["Add Patient to Triage Queue"];
    L --> K;

    E -- Triage Completion --> M["Update Time, Decrement Busy Nurses"];
    M --> N["Determine Condition (Stable p1 / Critical p2)"];
    N -- Stable --> O["Schedule Home Healing Completion Event"];
    O --> P["Check Triage Queue"];
    N -- Critical --> Q["Hospital Bed Available? (Occupied less than K)"];
    Q -- Yes --> R["Assign Patient to Bed, Increment Occupied Beds"];
    R --> S["Schedule Hospital Healing Completion Event"];
    S --> P;
    Q -- No --> T["Increment Rejected Count"];
    T --> U["Schedule Home Healing Completion Event (Adjusted Time alpha)"];
    U --> P;

    P -- Queue Not Empty --> V["Remove Patient from Queue"];
    V --> W["Assign Patient to Nurse, Increment Busy Nurses"];
    W --> X["Schedule Triage Completion Event"];
    X --> K;
    P -- Queue Empty --> K;

    E -- Hospital Healing Completion --> Y["Update Time, Decrement Occupied Beds"];
    Y --> Z["Increment Healed Count"];
    Z --> K;

    E -- Home Healing Completion --> AA["Update Time"];
    AA --> BB["Increment Healed Count"];
    BB --> K;

    K -- No --> D;
    K -- Yes --> CC["End Simulation, Calculate & Report Stats"];
