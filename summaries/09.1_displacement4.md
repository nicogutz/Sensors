# Sensors and Actuators Lecture Summary

## Session Overview
- Focus on Displacement Sensors
  - Capacitive Sensors
  - Piezoelectric Sensors
  - Optical Encoders
  - Hall Effect Magnetic Sensors
  
### Capacitive Sensors

#### Definition of Capacitance
- **Capacitance equation**: \( C = \frac{εA}{x} \)
  - \( A \): Surface area of plates
  - \( x \): Distance between plates
  - \( ε \): Dielectric constant

#### Basic Capacitive Sensors
- Variability in capacitance can be achieved by modifying plate distance.
- A basic circuit includes a capacitor (Cx), which measures displacement with an AC excitation voltage.

#### Variable Differential Capacitor Sensor
- Measures relative movements using two capacitors (C1, C2) and calculates \( \frac{C1 - C2}{C1 + C2} \).
- Offers advantages as it reduces sensitivity to environmental factors since both capacitors are affected similarly.

#### Measurement Method
- Configured using a Wheatstone bridge for capacitors, where impedances replace resistances.
- Allows for linear relationships between input displacement and output signal.

#### Properties
**Advantages:**
- Small mass
- Broad frequency spectrum
- High linearity 
- Applicable for both static and dynamic measurements

**Disadvantages:**
- Requires AC excitation
- Sensitive to noise (high output impedance)

### Piezoelectric Sensors

#### Basics
- **Piezoelectric effect**: Generates electric charge through mechanical stress in materials like quartz and barium titanate.
- Output is in form of charges rather than voltage.

#### Mechanics of Operation
- Force application causes deformation, leading to charge generation.
- Measurement of the generated charge must involve creating a current; otherwise, charges dissipate.

#### Equations
- **Charge generation**: \( q = Kx \)
  - \( i = \frac{dq}{dt} = K \frac{dx}{dt} \)
- Impedance of the system needs to be analyzed to see the current and voltage relationships, forming a high-pass filter effect.

#### Properties
**Advantages:**
- Effective for medium to high frequencies
- High output voltage
- No external excitation voltage is needed

**Disadvantages:**
- Not suitable for static measurements
- Sensitive to temperature changes
- High output impedance complicates amplification

### Optical Encoders

#### Fundamentals
- Measure rotational displacement using light sources and detectors around an optical disk.
- Incremental output produced based on the number of light pulses that pass through openings as it rotates.

#### Detection Mechanism
- Incremental encoders give pulse trains, which are counted to track position. A second light adds directional information.
- A quadrature system introduces two additional sensors to offer directional and absolute position information.

#### Modes of Operation
- Various modes allow counting in both forward and reverse; resolution can be increased by using digital signal processing techniques.
  
#### Absolute Optical Encoders
- Utilize a unique code for each position, enabling noise reduction and maintaining position awareness despite interruptions.

### Conclusion
- Covers various displacement sensors, highlighting their definitions, operation, measurements, properties, and advantages/disadvantages.
- Emphasizes the importance of understanding sensor behavior in engineering applications.