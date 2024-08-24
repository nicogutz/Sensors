# Sensors and Actuators - Motion Sensors: Strain Gages

## Overview
In this session, we focus on measuring small resistances using strain gages, discussing types, applications, and methodologies.

### Previous Topics in Sensors & Actuators
- Resistive Potentiometers
- Resistive Strain Gages
  - Non-linear behavior when loaded
  - Use of resistors in parallel to linearize signals
  - Importance of computer calculations for accurate measurements

## Today's Agenda
- Measuring small resistance changes
- Unbounded and bonded strain gages
- Special types of strain gages
- Practical exercises

## Strain Gage Applications
Strain gages are generally applied in two primary tasks:
1. Experimental stress analysis of machines and structures.
2. Construction of sensors for force, torque, pressure, flow, and acceleration.

## Measuring Small Resistances
To measure small displacements:
- Utilize a setup with a known resistance and an excitation voltage. 
- For example, a 100Ω strain gage may show small changes, becoming 100.4Ω when strained. This results in accurate voltage readings that require highly precise measurement systems for detection.

## Types of Strain Gages
### Basic Principle of Measurement
Strain gages use resistance changes to measure strain. They can be categorized into:
- **Unbonded Metal-Wire Gages:** Free from fixed attachment, allowing for movement in response to stress.
- **Bonded Gages:** Attached to a structure, enhancing stability and direct measurement of strain.

### Unbonded Metal-Wire Gage
- Operates on a Wheatstone bridge configuration with four resistors.
- When subjected to tension/compression, two resistors increase in resistance and two decrease, allowing for precise measurements of small displacements.

### Sensitivity
The sensitivity of the unbonded metal-wire gage can be derived from the change in voltage relationships:
1. Under strain, voltage output (Vo) relates to the difference in resistance.
2. Sensitivity is calculated as the ratio of output to input during deformation.
3. The gage factor (GF) indicates the sensitivity level, which can be enhanced by adjusting excitation voltage or material choice.

### Temperature Effects
Temperature changes impact all resistances equally in a Wheatstone bridge, making their effect negligible due to the relative measurements. 

### Unbonded Gage Properties
- **Advantages:**
  - Linear behavior; small temperature coefficient; high accuracy.
- **Disadvantages:**
  - Small gage factor (GF = 2-4); sensitivity to mechanical shocks.

### Bonded Metal-Wire Gages
- These are glued to structures, improving measurement accuracy.
- They exhibit high transverse sensitivity which can affect readings if not accounted for.

### Bonded Metal-Foil Gages
- Properties:
  - Resistance ranges from 120Ω to 1000Ω; maximum strain capacity is 0.5% to 4%.
- **Pros:**
  - Low transverse sensitivity; better stability; AC and DC excitation compatible.
- **Cons:**
  - GF remains low around 2; limited operational temperature range.

### Deposited Thin-Metal-Film Gages
- These gages are produced through techniques like evaporation and sputtering directly onto a carrier, providing high accuracy with minimized thermal effects but are expensive for small volumes.

### Semiconductor Strain Gages
- Comprised of materials like silicon, these offer:
  - High sensitivity (GF > 100); small dimensions allowing for compact sensor designs.
- Drawbacks include limited temperature ranges and high thermal coefficients.

## Example Calculation Exercise
### Given Parameters:
- Steel rod: cross-sectional area = 1 cm², Young's modulus (E) = 210 GPa.
- Stress = 700 N/cm² (70 Kg/cm²).
- Gage Factor (GF) = 2.
- Resistance (R) = 120Ω.
- Execution current: \(I_{exec} = 30 mA\).
- Temperature = 20°C.

### Output Voltage Calculation:
1. Calculate Strain (ε): 
   - \(\epsilon = \frac{\sigma}{E}\)
2. Calculate Change in Resistance (ΔR): 
   - Using GF.
3. Compute output voltage based on the bridge configuration and apply results for evaluation against noise levels.

### Signal-to-Noise Ratio:
- Key to understanding the reliability of measurements is analyzing thermal or Johnson noise which impacts system resolution.

## Special Strain Gages
### Elastic Mercury Tube
- Composed of conductive fluid encased within a silicon tube, allowing for significant displacement measurements.
- Applications include physiological monitoring like lung volume detection.

This encapsulated view of strain gages and their functionalities highlights their applications in engineering technology and the critical nature of precision measurement and sensitivity in sensor designs.