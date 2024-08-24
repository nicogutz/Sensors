```markdown
# Lecture Summary: Temperature Sensors

## Types of Temperature Sensors
1. Thermocouples
2. Resistance Temperature Detectors (RTDs)
3. Thermistors
4. Semiconductor Sensors

## 1. Thermocouples
- **Principle**: Based on the thermoelectric effect (Seebeck effect), which generates voltage at a junction of two different metals when temperature exceeds absolute zero (0 K).
  
### Key Features:
- **Junctions**: Typically requires two junctions for operation. One junction is kept at a reference temperature (0°C).
- **Sensitivity**: Voltage output is non-linear, requiring calibration tables.

### Common Types:
- **Type J (Iron-Constantan)**: -50°C to 760°C, high sensitivity.
- **Type K (Chromel-Alumel)**: -184°C to 1260°C, broader range but lower sensitivity.
- **Type S, R, T, etc.**: Vary in composition and range, generally used for specific applications.

### Measurement System:
- **Cold Junction Compensation**: Necessary to correct the readings by measuring the temperature of the reference junction.

## 2. Resistance Temperature Detectors (RTDs)
- **Operating Principle**: Resistance changes with temperature; primarily uses pure metal, platinum being the most common.

### Key Features:
- **Types**: 
  - **PT100**: 100 Ω at 0°C.
  - **PT1000**: 1000 Ω at 0°C.
- **Temperature Range**: Typically -200°C to +850°C.

### Construction Types:
1. Thin Film: Limited to 300°C due to strain effects.
2. Wire Wound: Better performance up to 660°C.
3. Coiled Elements: Best performance, operating up to 850°C.

### Measurement Formula:
- **Callendar-Van-Dusen Equation**: Provides the resistance-temperature relationship for linearized results.

## 3. Thermistors
- **Definition**: Cheap, resistive temperature sensors made of ceramic materials.

### Key Features:
- **Types**: Typically NTC (Negative Temperature Coefficient) where resistance decreases with increasing temperature.
- **Temperature Range**: Generally optimized for -50°C to +100°C.
  
### Characteristics:
- Highly non-linear but predictable, requiring calibration. The resistance at a reference temperature (usually 25°C) is known.

## 4. Semiconductor Sensors
- **Principle**: Based on the relationship between current and voltage in diodes or transistors, governed by Ebers-Moll equation.

### Key Features:
- **Output**: Voltage change is proportional to absolute temperature.
- **Typical Specifications**: Ranges from -55°C to +150°C.
- **Advantages**: Integrated circuits enable easier use in various applications.

### Use Case Examples:
- **AD592, TMP17**: Active sensors with good linearity, typically suitable for general temperature measurement.

## Summary of Comparison
| Sensor Type | Temperature Range | Accuracy | Output | Cost |
|-------------|-------------------|----------|--------|------|
| Thermocouple | -184°C to +2300°C | High | Low voltage output | Medium |
| RTD | -200°C to +850°C | High | Requires excitation | Medium |
| Thermistor | 0°C to +100°C | Poor | Varies | Low |
| Semiconductor | -55°C to +150°C | 1°C | 10 mV/K typical | Medium |

## Final Remarks
- The choice of temperature sensor depends on the application requirements, including temperature range, cost, response time, and accuracy.
- Students should prepare for upcoming exercises and exam instructions as outlined in the announcements.
```
