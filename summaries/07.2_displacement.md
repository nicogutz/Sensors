# Engineering Lecture Summary: Sensors and Actuators - Motion Sensors 1

### Introduction to Motion Sensors
- **Definition**: Motion sensors are electromechanical transducers that convert motion quantities into electrical quantities.
- **Focus**: This session will cover various types of displacement sensors, starting with the simplest forms—resistive potentiometers and strain gauges.

### Importance of Displacement Sensors
- Displacement sensors are fundamental as many other sensor types (e.g., pressure sensors, temperature sensors) incorporate motion sensors in their mechanisms.
- Example applications illustrate how displacement translates into resistance or voltage changes in more complex sensors.

### Types of Motion Sensors
1. **Resistive Potentiometers**
2. **Strain Gauges**
3. **Inductive Sensors**
4. **Capacitive Sensors**
5. **Piezoelectric Sensors**
6. **Optical Sensors**
7. **Hall Effect Sensors**
8. **Ultrasonic Sensors**

### Resistive Potentiometers
- **Function**: Convert a displacement (translational or rotational) into a resistance change.
- **Range**: Typically from 10Ω to 1MΩ with ranges from 2-500 mm in translation and 10° to +50 rotations in rotation.
- **Excitation**: Usually powered by DC voltage, but AC may be used for better signal amplification.
- **Materials**:
  - Carbon: Cheap, low friction, but wears out.
  - Wire-wound: Offers better resolution but produces discrete steps.
  - Conducting plastics: High durability and low friction but more expensive.

#### Characteristics
- **Linearity**: Typically linear; however, non-linear effects can occur due to ratings.
- **Friction**: Resulting from material choice, impacts performance.
- **Noise**: Present during operation due to mechanical movement.
- **Displacement**: Capable of measuring large displacements.
- **Electrical Interference**: Proper care to manage excitation voltage to avoid resistance changes from heating.

#### Data Acquisition Connection
- Non-linearities under loading must be addressed, often compensated with electronic adjustments or calculations.
- Resistors in parallel create a non-linear relationship that must be linearized through additional circuitry or software compensation.

### Strain Gauges
- **Function**: Measure resistance changes due to deformation of a thin wire when stretched, influenced by:
  - Increase in length (higher resistance),
  - Decrease in diameter (higher resistance),
  - Piezo-resistive effect (internal structure changes during applied stress).

#### Behavior
- Best operated within the elastic zone to maintain proportionality; exceeding leads to plastic deformation.
- Maximum strain for materials like steel is typically around 0.2%.

#### Equations Relevant to Strain Gauges
1. **Resistance Change**: Changes based on length, area, and resistivity.
2. **Volume Change**: Determined through calculations considering area and length, including Poisson's ratio.
3. **Gage Factor (GF)**: A key parameter representing sensitivity, derived from the change in resistance relative to the change in length.

#### Material Selection
- The Gage Factor is crucial for determining sensor performance and varies by material type.
- For example, materials like Constantan exhibit low thermal coefficients, maintaining accuracy despite temperature variations.

### Summary Points
- Gage Factor is temperature-dependent but generally has a minor effect, except in high-precision systems.
- Understanding the underlying physics and materials involved in resistive sensors is key to practical applications in engineering and technology.

### Questions
- Closing remarks invited questions regarding the content or specific aspects covered in the session.