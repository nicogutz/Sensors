# Sensors and Actuators Session 3.1: Traditional DC and ECM Motors

## Previously in Sensors & Actuators
- Discussed key concepts: flux, torque, and equations related to steady state and characteristics of motors.
- Important equations:
  - \( \frac{d v}{dt} = e + Ri + Li \)
  - \( e = k \omega \)
  - \( T = k i \)

## Today's Session Overview
- Topics Covered:
  - Regenerative braking
  - Four quadrant operation
  - ECM (Electronically Commutated Motor) Drive structure
  - ECM Drive back-emf
  - ECM Drive Torque

## Regenerative Braking
- **Definition**: Regenerative braking allows an electric motor to slow down while converting kinetic energy back into electrical energy.
- **Mechanics**:
  - To slow down a motor while maintaining direction, we reverse the current.
  - The motor operates with a negative current, necessitating that the applied voltage is lower than the back-emf.
  - Current flows back to the battery during braking.

## Exercise Example
- **Problem Statement**: Calculate torque (\(T\)) and deceleration (\(\alpha\)) for a motor with given inertia and current limit.
- **Solution**:
  - Torque: \(T = k \cdot I = -6 \, N \cdot m\)
  - Deceleration: Formula applies torque to find rate of change of speed.

## Four Quadrant Operation
- **Concept**: Operations can be classified based on the direction of torque and speed.
  - Possible modes:
    - Positive torque and speed (forward motion)
    - Negative torque with speed (backward motion)
    - Generator mode (mechanical energy to electrical)

## Flux Weakening
- **Definition**: Technique to exceed rated speed of a motor by weakening the magnetic field.
- **Limitations**: Only applicable in field-wound motors, not permanent magnet motors, as the latter cannot change the magnetic field.

## Electronically Commutated Motor (ECM) Drive
- ECMs lack brushes and operate with electronic commutation.
- **Configuration**:
  - Rotor consists of permanent magnets.
  - Stator contains three phases (a, b, c) of coils.
  - Active currents create magnetic fields that interact to generate motion.

## ECM Drive Operation
### Back-emf 
- The back-emf is induced by the movement of the rotor within a magnetic field, calculated as:
  - For one conductor: \(e = B \cdot l \cdot u\)
  - Total for multiple conductors: \(e = 4N \cdot B \cdot l \cdot r \cdot \omega\)

### Torque Production
- Electromagnetic torque is calculated using:
  - \(T = 2N \cdot B \cdot l \cdot r \cdot I \) (proportional to current).

## Transition Sequences and Torque Control
- Torque varies during operation; it must remain constant through proper sequencing of activating phases.
- **Phases Activation**:
  - Activate two phases at a time for torque control while ensuring smooth transitions to avoid dips in torque.

## Torque Ripple
-  Torque ripple can occur due to the switching of phases and use of pulse width modulation (PWM) to regulate speed.

## Conclusion
- Understanding the mechanics of DC motors and ECMs is crucial in control systems for effective speed and performance management.