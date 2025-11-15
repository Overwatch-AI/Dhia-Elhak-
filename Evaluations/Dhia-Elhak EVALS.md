
## Step 3 – Retrieval & Answer Evaluation

- **Model used for /query**: gemini-2.5-pro
- **Number of evaluated questions**: 20
- **Answer accuracy**: 90.0%
- **Page-reference accuracy**: 82.5%

### Q1

- **Question**: I'm calculating our takeoff weight for a dry runway. We're at 2,000 feet pressure altitude, and the OAT is 50°C. What's the climb limit weight ?
- **Labelled answer**: Based on the data for a dry runway at 2,000 feet pressure altitude with an OAT of 50°C, the Climb Limit Weight is 52,200 kg.
- **Model answer**: Based on the provided data for a dry runway at 2,000 feet pressure altitude and an OAT of 50°C, the climb limit weight is 52.2 (1000 KG).
- **Labelled pages**: 83
- **Returned pages**: 83
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q2

- **Question**: We're doing a Flaps 15 takeoff. Remind me, what is the first flap selection we make during retraction, and at what speed?
- **Labelled answer**: For a Flaps 15 takeoff, the first flap selection during retraction is Flaps 5, which you select at V2 + 15 knots.
- **Model answer**: Based on the Takeoff Flap Retraction Speed Schedule for a Flaps 15 takeoff, the first flap selection during retraction is to Flaps 5 at a speed of V2 + 15.
- **Labelled pages**: 41
- **Returned pages**: 41
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q3

- **Question**: We're planning a Flaps 40 landing on a wet runway at a 1,000-foot pressure altitude airport. If the wind-corrected field length is 1,600 meters, what is our field limit weight?
- **Labelled answer**: For a Flaps 40 landing on a wet runway at 1,000 feet pressure altitude with a 1,600-meter wind-corrected field length, the field limit weight is 55,800 kg
- **Model answer**: Based on the provided information for a Flaps 40 landing on a wet runway at a 1,000-foot pressure altitude with a wind-corrected field length of 1,600 meters, the field limit weight is 55,800 kg.
- **Labelled pages**: 99
- **Returned pages**: 99, 107
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 5.00

### Q4

- **Question**: Reviewing the standard takeoff profile: After we're airborne and get a positive rate of climb, what is the first action we take?
- **Labelled answer**: After getting a positive rate of climb, the first action is to call for "GEAR UP". This is shown in both the "Takeoff Procedure" table and the "Takeoff" flight pattern diagram.
- **Model answer**: Based on the takeoff flight pattern diagram, the first action taken after establishing a positive rate of climb is "Gear up."
- **Labelled pages**: 39, 51
- **Returned pages**: 51
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q5

- **Question**: Looking at the panel scan responsibilities for when the aircraft is stationary, who is responsible for the forward aisle stand?
- **Labelled answer**: Based on the "Panel Scan Diagram" for when the airplane is not moving under its own power, the Captain is responsible for the forward aisle stand (the area labeled with the number 6).
- **Model answer**: Based on the Panel Scan Diagram for when the airplane is not moving under its own power, the Captain is responsible for the forward aisle stand. The diagram shows this area (labeled as section 6) is shaded, and the legend indicates shaded areas are the Captain's responsibility.
- **Labelled pages**: 6
- **Returned pages**: 6
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q6

- **Question**: For a standard visual pattern, what three actions must be completed prior to turning base?
- **Labelled answer**: According to the "Visual Traffic Pattern" diagram, the three actions to complete prior to turning base are:
Gear down
Flaps 15 (landing flaps for 1 engine)
Arm speedbrake
- **Model answer**: Based on the provided visual traffic pattern diagram, the actions to be completed prior to turning base are:

*   Gear down
*   Flaps 15 (landing flaps for 1 engine)
*   Arm speedbrake

The context also lists "Start descent as required" as an action for this phase of flight.
- **Labelled pages**: 56
- **Returned pages**: 56
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q7

- **Question**: When the Pilot Not Flying (PNF) makes CDU entries during flight, what must the Pilot Flying (PF) do prior to execution
- **Labelled answer**: The Pilot Flying must verify the entries prior to execution.
- **Model answer**: When the Pilot Not Flying (PNF) makes CDU entries during flight, the entries must be verified by the Pilot Flying (PF) prior to execution.
- **Labelled pages**: 5
- **Returned pages**: 5
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q8

- **Question**: I see an amber "STAIRS OPER" light illuminated on the forward attendant panel; what does that light indicate?
- **Labelled answer**: That amber STAIRS OPER (Operating) light indicates that the airstair is in transit (i.e., currently extending or retracting).
- **Model answer**: An illuminated amber "STAIRS OPER" light on the forward attendant panel indicates that the airstair is in transit.
- **Labelled pages**: 126
- **Returned pages**: 126
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q9

- **Question**: We've just completed the engine start. What is the correct configuration for the ISOLATION VALVE switch during the After Start Procedure?
- **Labelled answer**: During the After Start Procedure, the ISOLATION VALVE switch should be set to AUTO.
- **Model answer**: During the After Start Procedure, the ISOLATION VALVE switch should be set to AUTO.
- **Labelled pages**: 35
- **Returned pages**: 35
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q10

- **Question**: During the Descent and Approach procedure, what action is taken with the AUTO BRAKE select switch , and what is the Pilot Flying's final action regarding the autobrake system during the Landing Roll procedure?
- **Labelled answer**: Here are the autobrake actions for those two phases of flight:
Descent and Approach Procedure
During the Descent and Approach Procedure, you set the AUTO BRAKE select switch to the desired brake setting.

Landing Roll Procedure
The Pilot Flying's final action regarding the autobrake system is to disarm the autobrake prior to reaching taxi speed.
- **Model answer**: During the Descent and Approach procedure, the AUTO BRAKE select switch is set to the desired brake setting.

During the Landing Roll procedure, the Pilot Flying's final action regarding the autobrake system is to disarm the autobrake prior to taxi speed and continue manual braking as required.
- **Labelled pages**: 43, 47
- **Returned pages**: 43, 47
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q11

- **Question**: We need to hold at 10,000 feet, and our weight is 60,000 kg. What is the expected total fuel flow in kilograms per hour?
- **Labelled answer**: The expected total fuel flow for holding at 10,000 feet with a weight of 60,000 kg is 2100 kilograms per hour (KG/HR). It is important to note that the fuel flow value provided in this table already includes a 5% additional fuel allowance for holding in a racetrack pattern
- **Model answer**: Based on the Holding Planning table, the total fuel flow for holding at 10,000 feet with a weight of 60,000 kg is 2100 kg/hr.
- **Labelled pages**: 93
- **Returned pages**: 93, 105
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 5.00

### Q12

- **Question**: I'm looking at the exterior light switches on the overhead panel. What is the function of the TAXI Light switch?
- **Labelled answer**: The TAXI Light switch controls the taxi light, which is mounted on the nose wheel strut.

OFF: The nose wheel well taxi light is extinguished.

ON: The nose wheel well taxi light is illuminated.
- **Model answer**: The TAXI Light switch has two positions:

*   **ON**: The nose wheel well taxi light is illuminated.
*   **OFF**: The nose wheel well taxi light is extinguished.

The taxi light is mounted on the nose wheel strut and points in the same direction as the nose wheel.
- **Labelled pages**: 112, 131
- **Returned pages**: 112, 131
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q13

- **Question**: where exactly are the Logo Lights located on the airframe?
- **Labelled answer**: Based on the manual, the Logo Lights are located on the top of each horizontal stabilizer surface.

They are positioned to point light onto both sides of the vertical stabilizer.
- **Model answer**: Error: Could not generate a response. Invalid operation: The `response.text` quick accessor requires the response to contain a valid `Part`, but none were returned. The candidate's [finish_reason](https://ai.google.dev/api/generate-content#finishreason) is 2.
- **Labelled pages**: 131
- **Returned pages**: None
- **Answer correctness (YES/NO)**: NO
- **Page reference correctness (0–10)**: 0.00

### Q14

- **Question**: I'm preparing for a Flaps 15 go-around. If our weight-adjusted gradient is 4% and our speed is VREF+20, what is the gradient adjustment for speed?
- **Labelled answer**: Based on the "ENGINE INOP Go-Around Climb Gradient Flaps 15" table, the gradient adjustment for speed when flying at VREF+20 with a weight-adjusted go-around gradient of 4% is 0.28%
- **Model answer**: Based on the "Gradient Adjustment for Speed (%)" table for a Flaps 15 go-around, with a weight-adjusted go-around gradient of 4% and a speed of VREF+20, the gradient adjustment is 0.28%.
- **Labelled pages**: 101
- **Returned pages**: 101, 107
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 5.00

### Q15

- **Question**: I'm holding the BCF (Halon) fire extinguisher. After I pull the ring pin, what is the action required to discharge the agent?
- **Labelled answer**: After pulling the ring pin, you must press the top lever to discharge the agent.

The manual also recommends aiming at the base of the fire from a distance of six feet.
- **Model answer**: After pulling the ring pin, you must aim at the base of the fire from a distance of six feet and press the top lever.
- **Labelled pages**: 146
- **Returned pages**: 146
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q16

- **Question**: I'm calculating my takeoff performance. The available runway is 2,000 meters with a 1.0% uphill slope. Factoring in a 10-knot tailwind, what is the final slope and wind-corrected field length I should use?
- **Labelled answer**: Here is the two-step calculation based on the "Takeoff Field Corrections - Dry Runway" tables:

Step 1: Slope Correction

Using the "Slope Corrections" table, find the row for FIELD LENGTH AVAILABLE (M) of 2000.

Find the column for RUNWAY SLOPE (%) of 1.0 (uphill).

The intersection gives a Slope Corrected Field Length of 1,760 meters.

Step 2: Wind Correction

Using the "Wind Corrections" table, you must use the 1,760-meter value from Step 1 as your input. This requires interpolation between the 1600m and 1800m rows.

Find the column for a 10-knot tailwind (the "10" column).

The value for a 1600m corrected length is 1680.

The value for a 1800m corrected length is 1880.

Interpolating for your 1,760m length gives a final value of 1,840 meters.

The final slope and wind-corrected field length you should use is 1,840 meters.
- **Model answer**: Error: Could not generate a response. Invalid operation: The `response.text` quick accessor requires the response to contain a valid `Part`, but none were returned. The candidate's [finish_reason](https://ai.google.dev/api/generate-content#finishreason) is 2.
- **Labelled pages**: 81
- **Returned pages**: None
- **Answer correctness (YES/NO)**: NO
- **Page reference correctness (0–10)**: 0.00

### Q17

- **Question**: I need to check the crew oxygen. There are 3 of us, and the bottle temperature gauge reads 30°C. What is the minimum required pressure in PSI for our 114 Cu. Ft. cylinder?
- **Labelled answer**: For 3 crew members at a bottle temperature of 30°C, the minimum required pressure for the 114/115 Cu. Ft. cylinder is 690 PSI.
- **Model answer**: Based on the "Required Pressure (PSI) for 114/115 Cu. Ft. Cylinder" table, for 3 crew members with a bottle temperature of 30°C, the minimum required pressure is 690 PSI.
- **Labelled pages**: 94
- **Returned pages**: 94
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q18

- **Question**: We're on an ILS approach. What three actions should I initiate as soon as the glideslope comes alive?
- **Labelled answer**: Based on the ILS Approach diagram and the Landing Procedure, as soon as the glideslope is "alive," you should initiate these three actions:

Call for "GEAR DOWN"

Call for "FLAPS 15"

Arm speed brake
- **Model answer**: Based on the provided documents, when the glideslope comes alive during an ILS approach, the following three actions should be initiated:

1.  Lower the gear.
2.  Set flaps to 15.
3.  Arm the speedbrake.
- **Labelled pages**: 45, 52
- **Returned pages**: 45, 52
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q19

- **Question**: What are the three available settings on the POSITION light switch located on the forward overhead panel?
- **Labelled answer**: Here are the three available settings on the POSITION Light switch:


STROBE & STEADY 


OFF 


STEADY
- **Model answer**: Based on the provided diagram and text, the three available settings on the POSITION light switch are:

*   STROBE & STEADY
*   OFF
*   STEADY
- **Labelled pages**: 113
- **Returned pages**: 113
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q20

- **Question**: Looking at the components of the passenger entry door, what is the name of the bar that secures the emergency escape slide to the aircraft floor?
- **Labelled answer**: Based on the "Passenger Entry/Galley Service Doors" diagram in the manual, the bar that secures the emergency escape slide to the floor brackets is called the GIRT BAR.
- **Model answer**: Based on the diagram of the Passenger Entry/Galley Service Doors, the bar that secures the emergency escape slide to the aircraft floor is the Girt Bar.
- **Labelled pages**: 123
- **Returned pages**: 123
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00


## Step 3 – Retrieval & Answer Evaluation

- **Model used for /query**: gemini-2.5-pro
- **Number of evaluated questions**: 20
- **Answer accuracy**: 90.0%
- **Page-reference accuracy**: 81.7%

### Q1

- **Question**: I'm calculating our takeoff weight for a dry runway. We're at 2,000 feet pressure altitude, and the OAT is 50°C. What's the climb limit weight ?
- **Labelled answer**: Based on the data for a dry runway at 2,000 feet pressure altitude with an OAT of 50°C, the Climb Limit Weight is 52,200 kg.
- **Model answer**: For a dry runway at 2,000 feet pressure altitude and an OAT of 50°C, the climb limit weight is 52,200 kg.
- **Labelled pages**: 83
- **Returned pages**: 83
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q2

- **Question**: We're doing a Flaps 15 takeoff. Remind me, what is the first flap selection we make during retraction, and at what speed?
- **Labelled answer**: For a Flaps 15 takeoff, the first flap selection during retraction is Flaps 5, which you select at V2 + 15 knots.
- **Model answer**: Based on the Takeoff Flap Retraction Speed Schedule for a Flaps 15 takeoff, the first flap selection is Flaps 5, made at a speed of V2 + 15.
- **Labelled pages**: 41
- **Returned pages**: 41
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q3

- **Question**: We're planning a Flaps 40 landing on a wet runway at a 1,000-foot pressure altitude airport. If the wind-corrected field length is 1,600 meters, what is our field limit weight?
- **Labelled answer**: For a Flaps 40 landing on a wet runway at 1,000 feet pressure altitude with a 1,600-meter wind-corrected field length, the field limit weight is 55,800 kg
- **Model answer**: Based on the Field Limit Weight table for a Flaps 40 landing, for
- **Labelled pages**: 99
- **Returned pages**: None
- **Answer correctness (YES/NO)**: NO
- **Page reference correctness (0–10)**: 0.00

### Q4

- **Question**: Reviewing the standard takeoff profile: After we're airborne and get a positive rate of climb, what is the first action we take?
- **Labelled answer**: After getting a positive rate of climb, the first action is to call for "GEAR UP". This is shown in both the "Takeoff Procedure" table and the "Takeoff" flight pattern diagram.
- **Model answer**: Based on the provided takeoff flight pattern diagram, after achieving a positive rate of climb, the first action taken is "Gear up."
- **Labelled pages**: 39, 51
- **Returned pages**: 51
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q5

- **Question**: Looking at the panel scan responsibilities for when the aircraft is stationary, who is responsible for the forward aisle stand?
- **Labelled answer**: Based on the "Panel Scan Diagram" for when the airplane is not moving under its own power, the Captain is responsible for the forward aisle stand (the area labeled with the number 6).
- **Model answer**: Based on the Panel Scan Diagram for when the airplane is not moving under its own power, the Captain is responsible for the forward aisle stand. This area is designated by the number 6 in the diagram and is shaded to indicate the Captain's area of responsibility.
- **Labelled pages**: 6
- **Returned pages**: 6
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q6

- **Question**: For a standard visual pattern, what three actions must be completed prior to turning base?
- **Labelled answer**: According to the "Visual Traffic Pattern" diagram, the three actions to complete prior to turning base are:
Gear down
Flaps 15 (landing flaps for 1 engine)
Arm speedbrake
- **Model answer**: Based on the provided Visual Traffic Pattern diagram, the three actions to be completed prior to turning base are:

*   Gear down
*   Flaps 15 (landing flaps for 1 engine)
*   Arm speedbrake
- **Labelled pages**: 56
- **Returned pages**: 56
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q7

- **Question**: When the Pilot Not Flying (PNF) makes CDU entries during flight, what must the Pilot Flying (PF) do prior to execution
- **Labelled answer**: The Pilot Flying must verify the entries prior to execution.
- **Model answer**: When the Pilot Not Flying (PNF) makes CDU entries during flight, the entries must be verified by the Pilot Flying (PF) prior to execution.
- **Labelled pages**: 5
- **Returned pages**: 5
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q8

- **Question**: I see an amber "STAIRS OPER" light illuminated on the forward attendant panel; what does that light indicate?
- **Labelled answer**: That amber STAIRS OPER (Operating) light indicates that the airstair is in transit (i.e., currently extending or retracting).
- **Model answer**: An illuminated amber "STAIRS OPER" light on the forward attendant panel indicates that the airstair is in transit.
- **Labelled pages**: 126
- **Returned pages**: 126
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q9

- **Question**: We've just completed the engine start. What is the correct configuration for the ISOLATION VALVE switch during the After Start Procedure?
- **Labelled answer**: During the After Start Procedure, the ISOLATION VALVE switch should be set to AUTO.
- **Model answer**: During the After Start Procedure, the ISOLATION VALVE switch should be set to AUTO.
- **Labelled pages**: 35
- **Returned pages**: 35
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q10

- **Question**: During the Descent and Approach procedure, what action is taken with the AUTO BRAKE select switch , and what is the Pilot Flying's final action regarding the autobrake system during the Landing Roll procedure?
- **Labelled answer**: Here are the autobrake actions for those two phases of flight:
Descent and Approach Procedure
During the Descent and Approach Procedure, you set the AUTO BRAKE select switch to the desired brake setting.

Landing Roll Procedure
The Pilot Flying's final action regarding the autobrake system is to disarm the autobrake prior to reaching taxi speed.
- **Model answer**: During the Descent and Approach procedure, the AUTO BRAKE select switch is set to the desired brake setting.

During the Landing Roll procedure, the Pilot Flying's final action regarding the autobrake system is to disarm the autobrake prior to taxi speed and continue manual braking as required.
- **Labelled pages**: 43, 47
- **Returned pages**: 43, 47
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q11

- **Question**: We need to hold at 10,000 feet, and our weight is 60,000 kg. What is the expected total fuel flow in kilograms per hour?
- **Labelled answer**: The expected total fuel flow for holding at 10,000 feet with a weight of 60,000 kg is 2100 kilograms per hour (KG/HR). It is important to note that the fuel flow value provided in this table already includes a 5% additional fuel allowance for holding in a racetrack pattern
- **Model answer**: For a weight of 60,000 kg holding at a pressure altitude of 10,000 feet, the total fuel flow is 2100 kg/hr. This data is for holding in a racetrack pattern.
- **Labelled pages**: 93
- **Returned pages**: 93, 105
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 5.00

### Q12

- **Question**: I'm looking at the exterior light switches on the overhead panel. What is the function of the TAXI Light switch?
- **Labelled answer**: The TAXI Light switch controls the taxi light, which is mounted on the nose wheel strut.

OFF: The nose wheel well taxi light is extinguished.

ON: The nose wheel well taxi light is illuminated.
- **Model answer**: The TAXI Light switch has two positions:

*   **ON:** The nose wheel well taxi light is illuminated.
*   **OFF:** The nose wheel well taxi light is extinguished.

The taxi light is mounted on the nose wheel strut and points in the same direction as the nose wheel.
- **Labelled pages**: 112, 131
- **Returned pages**: 112, 131
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q13

- **Question**: where exactly are the Logo Lights located on the airframe?
- **Labelled answer**: Based on the manual, the Logo Lights are located on the top of each horizontal stabilizer surface.

They are positioned to point light onto both sides of the vertical stabilizer.
- **Model answer**: The Logo Lights are located on the top of each horizontal stabilizer surface. They are positioned to illuminate both sides of the vertical stabilizer. The "Exterior Lighting Locations" diagram also shows a logo light on each horizontal stabilizer.
- **Labelled pages**: 131
- **Returned pages**: 113, 131, 132
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 3.33

### Q14

- **Question**: I'm preparing for a Flaps 15 go-around. If our weight-adjusted gradient is 4% and our speed is VREF+20, what is the gradient adjustment for speed?
- **Labelled answer**: Based on the "ENGINE INOP Go-Around Climb Gradient Flaps 15" table, the gradient adjustment for speed when flying at VREF+20 with a weight-adjusted go-around gradient of 4% is 0.28%
- **Model answer**: Based on the "Gradient Adjustment for Speed (%)" table for a Flaps 15 go-around, with a weight-adjusted go-around gradient of 4% and a speed of VREF+20, the gradient adjustment for speed is 0.28%.
- **Labelled pages**: 101
- **Returned pages**: 101, 107
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 5.00

### Q15

- **Question**: I'm holding the BCF (Halon) fire extinguisher. After I pull the ring pin, what is the action required to discharge the agent?
- **Labelled answer**: After pulling the ring pin, you must press the top lever to discharge the agent.

The manual also recommends aiming at the base of the fire from a distance of six feet.
- **Model answer**: After pulling the ring pin, you must aim at the base of the fire from a distance of six feet and press the top lever. You should then use a side-to-side motion to suppress the fire.
- **Labelled pages**: 146
- **Returned pages**: 146
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q16

- **Question**: I'm calculating my takeoff performance. The available runway is 2,000 meters with a 1.0% uphill slope. Factoring in a 10-knot tailwind, what is the final slope and wind-corrected field length I should use?
- **Labelled answer**: Here is the two-step calculation based on the "Takeoff Field Corrections - Dry Runway" tables:

Step 1: Slope Correction

Using the "Slope Corrections" table, find the row for FIELD LENGTH AVAILABLE (M) of 2000.

Find the column for RUNWAY SLOPE (%) of 1.0 (uphill).

The intersection gives a Slope Corrected Field Length of 1,760 meters.

Step 2: Wind Correction

Using the "Wind Corrections" table, you must use the 1,760-meter value from Step 1 as your input. This requires interpolation between the 1600m and 1800m rows.

Find the column for a 10-knot tailwind (the "10" column).

The value for a 1600m corrected length is 1680.

The value for a 1800m corrected length is 1880.

Interpolating for your 1,760m length gives a final value of 1,840 meters.

The final slope and wind-corrected field length you should use is 1,840 meters.
- **Model answer**: Error: Could not generate a response. Invalid operation: The `response.text` quick accessor requires the response to contain a valid `Part`, but none were returned. The candidate's [finish_reason](https://ai.google.dev/api/generate-content#finishreason) is 2.
- **Labelled pages**: 81
- **Returned pages**: None
- **Answer correctness (YES/NO)**: NO
- **Page reference correctness (0–10)**: 0.00

### Q17

- **Question**: I need to check the crew oxygen. There are 3 of us, and the bottle temperature gauge reads 30°C. What is the minimum required pressure in PSI for our 114 Cu. Ft. cylinder?
- **Labelled answer**: For 3 crew members at a bottle temperature of 30°C, the minimum required pressure for the 114/115 Cu. Ft. cylinder is 690 PSI.
- **Model answer**: Based on the "Required Pressure (PSI) for 114/115 Cu. Ft. Cylinder" table, for 3 crew members at a bottle temperature of 30°C, the minimum required pressure is 690 PSI.
- **Labelled pages**: 94
- **Returned pages**: 94
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q18

- **Question**: We're on an ILS approach. What three actions should I initiate as soon as the glideslope comes alive?
- **Labelled answer**: Based on the ILS Approach diagram and the Landing Procedure, as soon as the glideslope is "alive," you should initiate these three actions:

Call for "GEAR DOWN"

Call for "FLAPS 15"

Arm speed brake
- **Model answer**: As soon as the glideslope comes alive, the following three actions should be initiated:

1.  Lower the gear.
2.  Set flaps to 15.
3.  Arm the speedbrake.
- **Labelled pages**: 45, 52
- **Returned pages**: 45, 52
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q19

- **Question**: What are the three available settings on the POSITION light switch located on the forward overhead panel?
- **Labelled answer**: Here are the three available settings on the POSITION Light switch:


STROBE & STEADY 


OFF 


STEADY
- **Model answer**: Based on the provided context, the three available settings on the POSITION light switch are:

*   STROBE & STEADY
*   OFF
*   STEADY
- **Labelled pages**: 113
- **Returned pages**: 113
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q20

- **Question**: Looking at the components of the passenger entry door, what is the name of the bar that secures the emergency escape slide to the aircraft floor?
- **Labelled answer**: Based on the "Passenger Entry/Galley Service Doors" diagram in the manual, the bar that secures the emergency escape slide to the floor brackets is called the GIRT BAR.
- **Model answer**: Based on the diagram of the Passenger Entry/Galley Service Doors, the bar that secures the emergency escape slide to the aircraft floor is called the Girt Bar.
- **Labelled pages**: 123
- **Returned pages**: 123
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00


## Step 3 – Retrieval & Answer Evaluation

- **Model used for /query**: gemini-2.5-pro
- **Number of evaluated questions**: 20
- **Answer accuracy**: 95.0%
- **Page-reference accuracy**: 83.3%

### Q1

- **Question**: I'm calculating our takeoff weight for a dry runway. We're at 2,000 feet pressure altitude, and the OAT is 50°C. What's the climb limit weight ?
- **Labelled answer**: Based on the data for a dry runway at 2,000 feet pressure altitude with an OAT of 50°C, the Climb Limit Weight is 52,200 kg.
- **Model answer**: Based on the provided data for a dry runway takeoff with Flaps 5 at 2,000 feet pressure altitude and an OAT of 50°C, the climb limit weight is 52,200 kg.
- **Labelled pages**: 83
- **Returned pages**: 83
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q2

- **Question**: We're doing a Flaps 15 takeoff. Remind me, what is the first flap selection we make during retraction, and at what speed?
- **Labelled answer**: For a Flaps 15 takeoff, the first flap selection during retraction is Flaps 5, which you select at V2 + 15 knots.
- **Model answer**: For a Flaps 15 takeoff, the first flap selection during retraction is to Flaps 5 at a speed of V2 + 15.
- **Labelled pages**: 41
- **Returned pages**: 41
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q3

- **Question**: We're planning a Flaps 40 landing on a wet runway at a 1,000-foot pressure altitude airport. If the wind-corrected field length is 1,600 meters, what is our field limit weight?
- **Labelled answer**: For a Flaps 40 landing on a wet runway at 1,000 feet pressure altitude with a 1,600-meter wind-corrected field length, the field limit weight is 55,800 kg
- **Model answer**: Based on the provided information for a Flaps 40 landing on a wet runway at a 1,000-foot pressure altitude with a wind-corrected field length of 1,600 meters, the field limit weight is 55,800 kg.

This is determined from the "Field Limit Weight (1000 KG)" table by finding the intersection of the "1600" meter wind corrected field length row and the "WET" column under the "1000" foot airport pressure altitude. The value in the table is 55.8.

Additionally, when determining a maximum weight for a wet runway, the dry runway limit weight must also be checked, and the lower of the two weights is used. The dry runway limit for the same conditions is 64,400 kg. The lower of the two values is 55,800 kg.
- **Labelled pages**: 99
- **Returned pages**: 99, 104, 107
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 3.33

### Q4

- **Question**: Reviewing the standard takeoff profile: After we're airborne and get a positive rate of climb, what is the first action we take?
- **Labelled answer**: After getting a positive rate of climb, the first action is to call for "GEAR UP". This is shown in both the "Takeoff Procedure" table and the "Takeoff" flight pattern diagram.
- **Model answer**: Based on the provided takeoff flight pattern diagram, after establishing a positive rate of climb, the first action is "Gear up."
- **Labelled pages**: 39, 51
- **Returned pages**: 51
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 5.00

### Q5

- **Question**: Looking at the panel scan responsibilities for when the aircraft is stationary, who is responsible for the forward aisle stand?
- **Labelled answer**: Based on the "Panel Scan Diagram" for when the airplane is not moving under its own power, the Captain is responsible for the forward aisle stand (the area labeled with the number 6).
- **Model answer**: Based on the Panel Scan Diagram for when the airplane is not moving under its own power, the Captain is responsible for the forward aisle stand.
- **Labelled pages**: 6
- **Returned pages**: 6
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q6

- **Question**: For a standard visual pattern, what three actions must be completed prior to turning base?
- **Labelled answer**: According to the "Visual Traffic Pattern" diagram, the three actions to complete prior to turning base are:
Gear down
Flaps 15 (landing flaps for 1 engine)
Arm speedbrake
- **Model answer**: Based on the visual traffic pattern diagram, the three actions to complete prior to turning base are:
*   Gear down
*   Flaps 15 (landing flaps for 1 engine)
*   Arm speedbrake
- **Labelled pages**: 56
- **Returned pages**: 56
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q7

- **Question**: When the Pilot Not Flying (PNF) makes CDU entries during flight, what must the Pilot Flying (PF) do prior to execution
- **Labelled answer**: The Pilot Flying must verify the entries prior to execution.
- **Model answer**: When the Pilot Not Flying (PNF) makes CDU entries during flight, the entries must be verified by the Pilot Flying (PF) prior to execution.
- **Labelled pages**: 5
- **Returned pages**: 5
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q8

- **Question**: I see an amber "STAIRS OPER" light illuminated on the forward attendant panel; what does that light indicate?
- **Labelled answer**: That amber STAIRS OPER (Operating) light indicates that the airstair is in transit (i.e., currently extending or retracting).
- **Model answer**: An illuminated amber "STAIRS OPER" light indicates that the airstair is in transit.
- **Labelled pages**: 126
- **Returned pages**: 126
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q9

- **Question**: We've just completed the engine start. What is the correct configuration for the ISOLATION VALVE switch during the After Start Procedure?
- **Labelled answer**: During the After Start Procedure, the ISOLATION VALVE switch should be set to AUTO.
- **Model answer**: During the After Start Procedure, the ISOLATION VALVE switch should be set to AUTO.
- **Labelled pages**: 35
- **Returned pages**: 35
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q10

- **Question**: During the Descent and Approach procedure, what action is taken with the AUTO BRAKE select switch , and what is the Pilot Flying's final action regarding the autobrake system during the Landing Roll procedure?
- **Labelled answer**: Here are the autobrake actions for those two phases of flight:
Descent and Approach Procedure
During the Descent and Approach Procedure, you set the AUTO BRAKE select switch to the desired brake setting.

Landing Roll Procedure
The Pilot Flying's final action regarding the autobrake system is to disarm the autobrake prior to reaching taxi speed.
- **Model answer**: During the Descent and Approach procedure, the AUTO BRAKE select switch is set to the desired brake setting.

During the Landing Roll procedure, the Pilot Flying's final action regarding the autobrake system is to disarm the autobrake prior to taxi speed and continue with manual braking as required.
- **Labelled pages**: 43, 47
- **Returned pages**: 43, 47
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q11

- **Question**: We need to hold at 10,000 feet, and our weight is 60,000 kg. What is the expected total fuel flow in kilograms per hour?
- **Labelled answer**: The expected total fuel flow for holding at 10,000 feet with a weight of 60,000 kg is 2100 kilograms per hour (KG/HR). It is important to note that the fuel flow value provided in this table already includes a 5% additional fuel allowance for holding in a racetrack pattern
- **Model answer**: Based on the Holding Planning table, for a weight of 60,000 kg and a pressure altitude of 10,000 feet, the expected total fuel flow is 2100 kg/hr. This value is for holding in a racetrack pattern.
- **Labelled pages**: 93
- **Returned pages**: 93, 105
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 5.00

### Q12

- **Question**: I'm looking at the exterior light switches on the overhead panel. What is the function of the TAXI Light switch?
- **Labelled answer**: The TAXI Light switch controls the taxi light, which is mounted on the nose wheel strut.

OFF: The nose wheel well taxi light is extinguished.

ON: The nose wheel well taxi light is illuminated.
- **Model answer**: The TAXI Light switch has two positions with the following functions:
*   **ON**: The nose wheel well taxi light is illuminated.
*   **OFF**: The nose wheel well taxi light is extinguished.

The taxi light is mounted on the nose wheel strut and points in the same direction as the nose wheel.
- **Labelled pages**: 112, 131
- **Returned pages**: 112, 131
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q13

- **Question**: where exactly are the Logo Lights located on the airframe?
- **Labelled answer**: Based on the manual, the Logo Lights are located on the top of each horizontal stabilizer surface.

They are positioned to point light onto both sides of the vertical stabilizer.
- **Model answer**: The Logo Lights are located on the top of each horizontal stabilizer surface. They are positioned to illuminate both sides of the vertical stabilizer. An exterior lighting diagram confirms this location, showing a white logo light on each horizontal stabilizer.
- **Labelled pages**: 131
- **Returned pages**: 113, 131, 132
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 3.33

### Q14

- **Question**: I'm preparing for a Flaps 15 go-around. If our weight-adjusted gradient is 4% and our speed is VREF+20, what is the gradient adjustment for speed?
- **Labelled answer**: Based on the "ENGINE INOP Go-Around Climb Gradient Flaps 15" table, the gradient adjustment for speed when flying at VREF+20 with a weight-adjusted go-around gradient of 4% is 0.28%
- **Model answer**: Based on the "Gradient Adjustment for Speed (%)" table for a Flaps 15 Go-Around, with a weight-adjusted go-around gradient of 4% and a speed of VREF+20, the gradient adjustment for speed is 0.28%.
- **Labelled pages**: 101
- **Returned pages**: 101
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q15

- **Question**: I'm holding the BCF (Halon) fire extinguisher. After I pull the ring pin, what is the action required to discharge the agent?
- **Labelled answer**: After pulling the ring pin, you must press the top lever to discharge the agent.

The manual also recommends aiming at the base of the fire from a distance of six feet.
- **Model answer**: After pulling the ring pin, the required action is to aim at the base of the fire from a distance of six feet and press the top lever.
- **Labelled pages**: 146
- **Returned pages**: 146
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q16

- **Question**: I'm calculating my takeoff performance. The available runway is 2,000 meters with a 1.0% uphill slope. Factoring in a 10-knot tailwind, what is the final slope and wind-corrected field length I should use?
- **Labelled answer**: Here is the two-step calculation based on the "Takeoff Field Corrections - Dry Runway" tables:

Step 1: Slope Correction

Using the "Slope Corrections" table, find the row for FIELD LENGTH AVAILABLE (M) of 2000.

Find the column for RUNWAY SLOPE (%) of 1.0 (uphill).

The intersection gives a Slope Corrected Field Length of 1,760 meters.

Step 2: Wind Correction

Using the "Wind Corrections" table, you must use the 1,760-meter value from Step 1 as your input. This requires interpolation between the 1600m and 1800m rows.

Find the column for a 10-knot tailwind (the "10" column).

The value for a 1600m corrected length is 1680.

The value for a 1800m corrected length is 1880.

Interpolating for your 1,760m length gives a final value of 1,840 meters.

The final slope and wind-corrected field length you should use is 1,840 meters.
- **Model answer**: Error: Could not generate a response. Invalid operation: The `response.text` quick accessor requires the response to contain a valid `Part`, but none were returned. The candidate's [finish_reason](https://ai.google.dev/api/generate-content#finishreason) is 2.
- **Labelled pages**: 81
- **Returned pages**: None
- **Answer correctness (YES/NO)**: NO
- **Page reference correctness (0–10)**: 0.00

### Q17

- **Question**: I need to check the crew oxygen. There are 3 of us, and the bottle temperature gauge reads 30°C. What is the minimum required pressure in PSI for our 114 Cu. Ft. cylinder?
- **Labelled answer**: For 3 crew members at a bottle temperature of 30°C, the minimum required pressure for the 114/115 Cu. Ft. cylinder is 690 PSI.
- **Model answer**: For a 114 Cu. Ft. cylinder at a bottle temperature of 30°C with 3 crew members, the minimum required pressure is 690 PSI.
- **Labelled pages**: 94
- **Returned pages**: 94
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q18

- **Question**: We're on an ILS approach. What three actions should I initiate as soon as the glideslope comes alive?
- **Labelled answer**: Based on the ILS Approach diagram and the Landing Procedure, as soon as the glideslope is "alive," you should initiate these three actions:

Call for "GEAR DOWN"

Call for "FLAPS 15"

Arm speed brake
- **Model answer**: Based on the provided context, when the glideslope comes alive during an ILS approach, you should initiate the following three actions:
*   Lower the gear ("Gear down")
*   Set flaps to 15
*   Arm the speedbrake
- **Labelled pages**: 45, 52
- **Returned pages**: 45, 52
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q19

- **Question**: What are the three available settings on the POSITION light switch located on the forward overhead panel?
- **Labelled answer**: Here are the three available settings on the POSITION Light switch:


STROBE & STEADY 


OFF 


STEADY
- **Model answer**: Based on the provided diagram and text, the three available settings on the POSITION light switch are:
*   STROBE & STEADY
*   OFF
*   STEADY
- **Labelled pages**: 113
- **Returned pages**: 113
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q20

- **Question**: Looking at the components of the passenger entry door, what is the name of the bar that secures the emergency escape slide to the aircraft floor?
- **Labelled answer**: Based on the "Passenger Entry/Galley Service Doors" diagram in the manual, the bar that secures the emergency escape slide to the floor brackets is called the GIRT BAR.
- **Model answer**: Based on the provided diagram of the Passenger Entry/Galley Service Doors, the bar that secures the emergency escape slide to the aircraft floor is the Girt Bar.
- **Labelled pages**: 123
- **Returned pages**: 123
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00


## Step 3 – Retrieval & Answer Evaluation

- **Model used for /query**: gemini-2.5-pro
- **Number of evaluated questions**: 20
- **Answer accuracy**: 90.0%
- **Page-reference accuracy**: 80.8%

### Q1

- **Question**: I'm calculating our takeoff weight for a dry runway. We're at 2,000 feet pressure altitude, and the OAT is 50°C. What's the climb limit weight ?
- **Labelled answer**: Based on the data for a dry runway at 2,000 feet pressure altitude with an OAT of 50°C, the Climb Limit Weight is 52,200 kg.
- **Model answer**: For a dry runway at 2,000 feet pressure altitude and an OAT of 50°C, the climb limit weight is 52,200 kg.
- **Labelled pages**: 83
- **Returned pages**: 83
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q2

- **Question**: We're doing a Flaps 15 takeoff. Remind me, what is the first flap selection we make during retraction, and at what speed?
- **Labelled answer**: For a Flaps 15 takeoff, the first flap selection during retraction is Flaps 5, which you select at V2 + 15 knots.
- **Model answer**: For a Flaps 15 takeoff, the first flap selection during retraction is Flaps 5, which is selected at a speed of V2 + 15.
- **Labelled pages**: 41
- **Returned pages**: 41
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q3

- **Question**: We're planning a Flaps 40 landing on a wet runway at a 1,000-foot pressure altitude airport. If the wind-corrected field length is 1,600 meters, what is our field limit weight?
- **Labelled answer**: For a Flaps 40 landing on a wet runway at 1,000 feet pressure altitude with a 1,600-meter wind-corrected field length, the field limit weight is 55,800 kg
- **Model answer**: Based on the "Field Limit Weight (1000 KG)" table for a Flaps 40 landing, the field limit weight for a wind-corrected field length of 1,600 meters on a wet runway at a 1,000-foot pressure altitude is 55,800 kg.

When finding a maximum weight for a wet runway, the dry runway limit weight must also be determined, and the lower of the two weights is used. In this case, the dry limit is 64,400 kg and the wet limit is 55,800 kg, making the latter the correct field limit weight.
- **Labelled pages**: 99
- **Returned pages**: 99, 104, 107
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 3.33

### Q4

- **Question**: Reviewing the standard takeoff profile: After we're airborne and get a positive rate of climb, what is the first action we take?
- **Labelled answer**: After getting a positive rate of climb, the first action is to call for "GEAR UP". This is shown in both the "Takeoff Procedure" table and the "Takeoff" flight pattern diagram.
- **Model answer**: Based on the provided takeoff flight pattern diagram, the first action taken after establishing a positive rate of climb is "Gear up."
- **Labelled pages**: 39, 51
- **Returned pages**: 51
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 5.00

### Q5

- **Question**: Looking at the panel scan responsibilities for when the aircraft is stationary, who is responsible for the forward aisle stand?
- **Labelled answer**: Based on the "Panel Scan Diagram" for when the airplane is not moving under its own power, the Captain is responsible for the forward aisle stand (the area labeled with the number 6).
- **Model answer**: Based on the "Panel Scan Diagram" for when the airplane is not moving under its own power, the Captain is responsible for the forward aisle stand. This area is designated by the number 6 in the diagram and is shaded to indicate the Captain's area of responsibility.
- **Labelled pages**: 6
- **Returned pages**: 6
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q6

- **Question**: For a standard visual pattern, what three actions must be completed prior to turning base?
- **Labelled answer**: According to the "Visual Traffic Pattern" diagram, the three actions to complete prior to turning base are:
Gear down
Flaps 15 (landing flaps for 1 engine)
Arm speedbrake
- **Model answer**: Based on the visual traffic pattern diagram, the three actions to be completed prior to turning base are:

*   Gear down
*   Flaps 15 (landing flaps for 1 engine)
*   Arm speedbrake
- **Labelled pages**: 56
- **Returned pages**: 56
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q7

- **Question**: When the Pilot Not Flying (PNF) makes CDU entries during flight, what must the Pilot Flying (PF) do prior to execution
- **Labelled answer**: The Pilot Flying must verify the entries prior to execution.
- **Model answer**: When the Pilot Not Flying (PNF) makes CDU entries during flight, the Pilot Flying (PF) must verify the entries prior to execution.
- **Labelled pages**: 5
- **Returned pages**: 5
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q8

- **Question**: I see an amber "STAIRS OPER" light illuminated on the forward attendant panel; what does that light indicate?
- **Labelled answer**: That amber STAIRS OPER (Operating) light indicates that the airstair is in transit (i.e., currently extending or retracting).
- **Model answer**: An illuminated amber "STAIRS OPER" light indicates that the airstair is in transit.
- **Labelled pages**: 126
- **Returned pages**: 126
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q9

- **Question**: We've just completed the engine start. What is the correct configuration for the ISOLATION VALVE switch during the After Start Procedure?
- **Labelled answer**: During the After Start Procedure, the ISOLATION VALVE switch should be set to AUTO.
- **Model answer**: According to the After Start Procedure, the ISOLATION VALVE switch should be set to AUTO.
- **Labelled pages**: 35
- **Returned pages**: 35
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q10

- **Question**: During the Descent and Approach procedure, what action is taken with the AUTO BRAKE select switch , and what is the Pilot Flying's final action regarding the autobrake system during the Landing Roll procedure?
- **Labelled answer**: Here are the autobrake actions for those two phases of flight:
Descent and Approach Procedure
During the Descent and Approach Procedure, you set the AUTO BRAKE select switch to the desired brake setting.

Landing Roll Procedure
The Pilot Flying's final action regarding the autobrake system is to disarm the autobrake prior to reaching taxi speed.
- **Model answer**: During the Descent and Approach procedure, the AUTO BRAKE select switch is set to the desired brake setting.

During the Landing Roll procedure, the Pilot Flying's final action regarding the autobrake system is, prior to taxi speed, to disarm the autobrake and continue manual braking as required.
- **Labelled pages**: 43, 47
- **Returned pages**: 43, 47
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q11

- **Question**: We need to hold at 10,000 feet, and our weight is 60,000 kg. What is the expected total fuel flow in kilograms per hour?
- **Labelled answer**: The expected total fuel flow for holding at 10,000 feet with a weight of 60,000 kg is 2100 kilograms per hour (KG/HR). It is important to note that the fuel flow value provided in this table already includes a 5% additional fuel allowance for holding in a racetrack pattern
- **Model answer**: Based on the "Holding Planning" table for flaps up, at a weight of 60,000 kg and a pressure altitude of 10,000 feet, the expected total fuel flow is 2100 kg/hr. This value is for holding in a racetrack pattern.
- **Labelled pages**: 93
- **Returned pages**: 93, 105
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 5.00

### Q12

- **Question**: I'm looking at the exterior light switches on the overhead panel. What is the function of the TAXI Light switch?
- **Labelled answer**: The TAXI Light switch controls the taxi light, which is mounted on the nose wheel strut.

OFF: The nose wheel well taxi light is extinguished.

ON: The nose wheel well taxi light is illuminated.
- **Model answer**: The TAXI Light switch has two positions:
*   **ON** – The nose wheel well taxi light is illuminated.
*   **OFF** – The nose wheel well taxi light is extinguished.

The taxi light is mounted on the nose wheel strut and points in the same direction as the nose wheel.
- **Labelled pages**: 112, 131
- **Returned pages**: 112, 131
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q13

- **Question**: where exactly are the Logo Lights located on the airframe?
- **Labelled answer**: Based on the manual, the Logo Lights are located on the top of each horizontal stabilizer surface.

They are positioned to point light onto both sides of the vertical stabilizer.
- **Model answer**: Based on the provided documents, the Logo Lights are located on the top of each horizontal stabilizer surface. They are positioned to point light on both sides of the vertical stabilizer. This location is also depicted in the "Exterior Lighting Locations" diagram.
- **Labelled pages**: 131
- **Returned pages**: 113, 131, 132
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 3.33

### Q14

- **Question**: I'm preparing for a Flaps 15 go-around. If our weight-adjusted gradient is 4% and our speed is VREF+20, what is the gradient adjustment for speed?
- **Labelled answer**: Based on the "ENGINE INOP Go-Around Climb Gradient Flaps 15" table, the gradient adjustment for speed when flying at VREF+20 with a weight-adjusted go-around gradient of 4% is 0.28%
- **Model answer**: Based on the "Gradient Adjustment for Speed (%)" table for a Flaps 15 go-around, with a weight-adjusted go-around gradient of 4% and a speed of VREF+20, the gradient adjustment for speed is 0.28%.
- **Labelled pages**: 101
- **Returned pages**: 101, 107
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 5.00

### Q15

- **Question**: I'm holding the BCF (Halon) fire extinguisher. After I pull the ring pin, what is the action required to discharge the agent?
- **Labelled answer**: After pulling the ring pin, you must press the top lever to discharge the agent.

The manual also recommends aiming at the base of the fire from a distance of six feet.
- **Model answer**: After pulling the ringed safety pin, the required actions are to:
*   Aim at the base of the fire from a distance of six feet.
*   Press the top lever.
*   Use a side-to-side motion to suppress the fire.
- **Labelled pages**: 146
- **Returned pages**: 146
- **Answer correctness (YES/NO)**: NO
- **Page reference correctness (0–10)**: 10.00

### Q16

- **Question**: I'm calculating my takeoff performance. The available runway is 2,000 meters with a 1.0% uphill slope. Factoring in a 10-knot tailwind, what is the final slope and wind-corrected field length I should use?
- **Labelled answer**: Here is the two-step calculation based on the "Takeoff Field Corrections - Dry Runway" tables:

Step 1: Slope Correction

Using the "Slope Corrections" table, find the row for FIELD LENGTH AVAILABLE (M) of 2000.

Find the column for RUNWAY SLOPE (%) of 1.0 (uphill).

The intersection gives a Slope Corrected Field Length of 1,760 meters.

Step 2: Wind Correction

Using the "Wind Corrections" table, you must use the 1,760-meter value from Step 1 as your input. This requires interpolation between the 1600m and 1800m rows.

Find the column for a 10-knot tailwind (the "10" column).

The value for a 1600m corrected length is 1680.

The value for a 1800m corrected length is 1880.

Interpolating for your 1,760m length gives a final value of 1,840 meters.

The final slope and wind-corrected field length you should use is 1,840 meters.
- **Model answer**: Error: Could not generate a response. Invalid operation: The `response.text` quick accessor requires the response to contain a valid `Part`, but none were returned. The candidate's [finish_reason](https://ai.google.dev/api/generate-content#finishreason) is 2.
- **Labelled pages**: 81
- **Returned pages**: None
- **Answer correctness (YES/NO)**: NO
- **Page reference correctness (0–10)**: 0.00

### Q17

- **Question**: I need to check the crew oxygen. There are 3 of us, and the bottle temperature gauge reads 30°C. What is the minimum required pressure in PSI for our 114 Cu. Ft. cylinder?
- **Labelled answer**: For 3 crew members at a bottle temperature of 30°C, the minimum required pressure for the 114/115 Cu. Ft. cylinder is 690 PSI.
- **Model answer**: Based on the "Required Pressure (PSI) for 114/115 Cu. Ft. Cylinder" table, for a bottle temperature of 30°C and 3 crew members using oxygen, the minimum required pressure is 690 PSI.
- **Labelled pages**: 94
- **Returned pages**: 94
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q18

- **Question**: We're on an ILS approach. What three actions should I initiate as soon as the glideslope comes alive?
- **Labelled answer**: Based on the ILS Approach diagram and the Landing Procedure, as soon as the glideslope is "alive," you should initiate these three actions:

Call for "GEAR DOWN"

Call for "FLAPS 15"

Arm speed brake
- **Model answer**: Based on the provided documents, when the glideslope comes alive during an ILS approach, you should initiate the following three actions:

*   Lower the gear.
*   Set flaps to 15.
*   Arm the speedbrake.

The Pilot Flying would make the calls "GEAR DOWN" and "FLAPS 15."
- **Labelled pages**: 45, 52
- **Returned pages**: 45, 52
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q19

- **Question**: What are the three available settings on the POSITION light switch located on the forward overhead panel?
- **Labelled answer**: Here are the three available settings on the POSITION Light switch:


STROBE & STEADY 


OFF 


STEADY
- **Model answer**: Based on the provided context, the three available settings on the POSITION light switch are:

*   STROBE & STEADY
*   OFF
*   STEADY
- **Labelled pages**: 113
- **Returned pages**: 113
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

### Q20

- **Question**: Looking at the components of the passenger entry door, what is the name of the bar that secures the emergency escape slide to the aircraft floor?
- **Labelled answer**: Based on the "Passenger Entry/Galley Service Doors" diagram in the manual, the bar that secures the emergency escape slide to the floor brackets is called the GIRT BAR.
- **Model answer**: Based on the provided diagram of the Passenger Entry/Galley Service Doors, the name of the bar that secures the emergency escape slide to the aircraft floor is the Girt Bar.
- **Labelled pages**: 123
- **Returned pages**: 123
- **Answer correctness (YES/NO)**: YES
- **Page reference correctness (0–10)**: 10.00

