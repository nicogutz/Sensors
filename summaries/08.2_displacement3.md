# Session 8.2: Motion Sensors - Induction

## Overview
This session covers the following topics:
- Induction definition
- Differential Transformer (LVDT)
- Resolver Sensor
- Inductosyn Sensors

## 1. Definition of Induction
Induction is defined through the equation:
\[ 
L = n^2 G \mu 
\]
Where:
- \( n \): number of windings
- \( G \): form factor (length and width)
- \( \mu \): permeability of the medium

Inductive sensors operate without contact, utilizing a magnetic field, unlike resistive sensors which rely on physical contact which leads to friction and erosion.

## 2. Inductive Displacement Sensors
### Self-Induction Sensors
- Composed of two coils in series.
- Changing the distance between the coils alters self-inductance; closer coils yield higher self-inductance.
- Changing the core material alters the permeability and thus affects inductance.
  
#### Measuring Changes
- Place the coils in an LC oscillator to measure self-inductance changes via frequency shifts.
- Useful in applications like ingestibles for monitoring in-body conditions by measuring pressure with non-contact methods.

### Mutual Induction Sensors
- The primary coil receives an AC voltage excitation, and generates a magnetic field that induces a voltage in a secondary coil.
- Voltage changes based on the distance and alignment of the coils.
  
#### Application
- Used in breathing detectors to monitor infant respiration, detecting changes in magnetic fields caused by breathing.

### Non-Linear Behavior of Mutual Induction
- Induced voltage behaves non-linearly with separation distance, necessitating signal linearization for effective measurement.

## 3. Differential Transformer (LVDT)
### Structure
- Consists of three coils: one primary and two secondary coils.
- A moving core between these coils influences the induced voltage.

### Operation
- Output voltage remains zero when the core is centered between the coils (maximum opposite outputs).
- Moving the core alters the output voltage in relation to the movement direction.

### Detection Mechanism
- Requires synchronous detection to interpret the signal accurately using a phase-sensitive detector (PSD).
- Calibration can provide a linear relationship between output voltage and displacement.

### Properties of LVDT
#### Pros:
- Linear operation over a large range (0.25%)
- High sensitivity (up to 0.5 to 2 mV per 0.01 mm/V)
- Contactless and allows for high precision.
  
#### Cons:
- Requires AC supply and specific detection circuitry.

## 4. Resolver Sensor
- Used for measuring rotational displacement.
- Composed of a rotor (with alternating current excitation) and stator coils that output voltage based on rotor position.

### Functionality
- The resolved voltage outputs are dependent on rotor position; two stators (sine and cosine) allow for a comprehensive understanding of the rotor's angle.

### Signal Processing
- Signals require electronic processing to derive absolute position values from the two, typically utilizing digital circuits.

### Properties
#### Pros:
- Long life and high precision at low cost.
  
#### Cons:
- Signal processing is mandatory for accurate readings.

## 5. Inductosyn Sensors
### Longitudinal Inductosyns
- Function similarly to resolvers but measure longitudinal movements.
- Utilize a PCB creation method where a slider detects displacement across a series of coils.

### Measurement Method
- The displacement can be determined by evaluating the induced voltage based on the slider's position relative to coil patterns, yielding extremely high resolutions (e.g., 500 nm precision).

### Rotary Inductosyns
- Utilize discs for excitation and signal measurement similar to the long-range inductosyns.

---

This lecture provided a technical foundation for understanding motion sensors based on inductive principles, showcasing various types, their structures, functionalities, and properties.