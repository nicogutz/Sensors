# Engineering Lecture Summary: Sensors and Actuators - Force Sensors

## Introduction to Force Sensors
- **Topics Covered**:
  - Elastic force transducers: Load cells and bending.
  - Various methods for measuring force.

## How to Measure Force
1. **Balance Against Gravitational Force**: 
   - Force can be balanced against gravitational force using known mass and gravity acceleration.
2. **Using Acceleration**: 
   - Measure force with known mass based on Newton's first law (F=ma).
3. **Hydraulic Pressure Method**:
   - Some transducers convert force into pressure for measurement.
4. **Displacement on Elastic Material**:
   - Commonly involves a spring and utilizes linear variable differential transformers to measure displacement.
  
### Elastic Force Transducer
- **Basic Concept**: 
  - Relates force applied to the displacement of a mass connected to a spring.

### Load Cells as Force Transducers
- **Construction**:
  - Steel bar with applied force causing compression, sensed by four strain gauges positioned in different orientations.
  - Arrangement in a Wheatstone bridge allows for differential measurement.

### Mechanism of Strain Gauges
- **Poisson Effect**: 
  - Vertical strain gauges compress while horizontal ones expand. A correct arrangement allows for both increase and decrease in signals.
  
### Sensitivity Calculation for Load Cells
1. **Parameters**:
   - Load-sensing member dimensions and material properties (e.g., Poisson's ratio, Young's modulus).
   - Gauge factor (GF) of strain gauges.
   - Excitation voltage.

2. **Output Voltage Formula**:
   - Sensitivity = Output voltage / Force
   - Influenced by the configuration of strain gauges in the Wheatstone bridge and gauge factor.

3. **Increasing Sensitivity**:
   - Options include changing the strain gauge material, excitation voltage, reducing load cell area, and choosing materials with different Young’s modulus.

### Temperature Effects on Load Cells
- **Considerations**: 
  - Temperature can impact resistance and gauge factor, though these effects can often be compensated through measurements.
- **Creep**: 
  - Adhesive creep impacts the transfer of strain, limiting how well strain gauges can control output under varying temperatures.

## bending Elastic Force Transducer
- **Under Bending Mechanics**:
  - Using bending rather than compression, as the force causes a moment and strain varies across strain gauges positioned on different sides of the beam.

## Applications of Force Sensors
1. **Bending Load Cells**: 
   - Used in weighing systems with mechanical safety features.
2. **Piezo-resistive Materials**:
   - High gauge factors for enhanced sensitivity with temperature stability issues.
3. **LVDT**: 
   - Utilizes springs for displacement measurement, allowing sensitivity changes by adjusting spring tension.
4. **Piezoelectric Sensors**: 
   - Specifically for AC forces, used in applications such as aerodynamic measurements. 

## Force Sensitive Resistor (FSR)
- **Characteristics**: 
  - Resistance decreases under applied force; non-linear relationship; generally low-cost with low accuracy (about 10%).

## Conclusion
- Overview of force sensor types, their construction, measurement principles, sensitivity calculations, and applications in different fields. Techniques to cope with various challenges, including temperature effects and dynamic force measurements, have been discussed.