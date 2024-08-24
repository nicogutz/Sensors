### Multiple Choice Questions

1. What is the basic function of the Power Processing Unit (PPU) in an electric motor drive system?
   - A) To convert AC voltage into DC voltage.
   - B) To regulate the motor's torque.
   - C) To drive the motor at a fixed speed.
   - D) To control the temperature of the motor.
   <details><summary>Answer</summary>A) To convert AC voltage into DC voltage.</details>

2. In an Electronic Commutated Motor (ECM), how many phases are always active?
   - A) One phase
   - B) Two phases
   - C) Three phases
   - D) Four phases
   <details><summary>Answer</summary>B) Two phases</details>

3. The equation for back-emf in a DC motor is given by what formula?
   - A) $e = 4.N.B.l.r.I$
   - B) $e = k \cdot \omega$
   - C) $e = 4.N.B.l.r.\omega$
   - D) $e = T_{em} \cdot \omega$
   <details><summary>Answer</summary>C) $e = 4.N.B.l.r.\omega$</details>

4. What is the purpose of the capacitor in the PPU system?
   - A) To increase the current.
   - B) To stabilize the voltage.
   - C) To convert AC to DC.
   - D) To store energy for later use.
   <details><summary>Answer</summary>B) To stabilize the voltage.</details>

5. The voltage applied to the motor using PWM depends on which of the following?
   - A) The frequency of the AC supply
   - B) The duty cycle of the PWM
   - C) The type of motor
   - D) The temperature of the motor
   <details><summary>Answer</summary>B) The duty cycle of the PWM</details>

6. In the PWM calculation, what does $d$ represent?
   - A) The difference in voltage
   - B) The duty cycle ratio
   - C) The input voltage
   - D) The speed of the motor
   <details><summary>Answer</summary>B) The duty cycle ratio</details>

7. How does the PWM achieve average voltage at the entrance of the motor $V_a$?
   - A) By varying the resistance
   - B) By switching between full voltage and zero voltage
   - C) By increasing the duty cycle
   - D) By changing the input current
   <details><summary>Answer</summary>B) By switching between full voltage and zero voltage</details>

8. In which condition is a short-circuit avoided in the full bridge setup for driving a DC motor?
   - A) Both upper transistors are off
   - B) Both lower transistors are off
   - C) Only one transistor from pole A and one from pole B are on
   - D) Both upper transistors are on
   <details><summary>Answer</summary>C) Only one transistor from pole A and one from pole B are on</details>

9. When the current is flowing through the top transistors and back through the diodes, which configuration does this represent?
   - A) T + on, T + on (S1)
   - B) T + on, T - on (S2)
   - C) T - on, T - on (S3)
   - D) All transistors off
   <details><summary>Answer</summary>A) T + on, T + on (S1)</details>

10. How do you describe the relationship between effective voltage and duty cycle in a PWM?
    - A) $v = (1 - d)V_d$
    - B) $v = d \cdot V_d$
    - C) $v = d + V_d$
    - D) $v = d/V_d$
    <details><summary>Answer</summary>B) $v = d \cdot V_d$</details>

11. What happens to the average voltage as the duty cycle $d$ approaches 1?
    - A) The average voltage increases to maximum.
    - B) The average voltage stays constant.
    - C) The average voltage decreases to zero.
    - D) The average voltage fluctuates wildly.
    <details><summary>Answer</summary>A) The average voltage increases to maximum.</details>

12. When regenerative mode is active, what happens to the current?
    - A) Current flows to the motor.
    - B) Current flows to the power supply.
    - C) No current flows.
    - D) The current fluctuates rapidly.
    <details><summary>Answer</summary>B) Current flows to the power supply.</details>

13. In the context of a switching cycle, what does the equation $i = d \cdot i_{motor}$ represent?
    - A) The average power delivered to the motor
    - B) The relationship between input current and motor current
    - C) The resistance of the motor
    - D) The back-emf at the motor
    <details><summary>Answer</summary>B) The relationship between input current and motor current</details>

14. How is the average current at the motor calculated in PWM?
    - A) $i_{o} = i_{a} + i_{b}$
    - B) $i_{o} = d - d_{b} \cdot i_{motor}$
    - C) $i_{o} = d \cdot i_{a}$
    - D) $i_{o} = d_{b} \cdot i_{motor}$
    <details><summary>Answer</summary>B) $i_{o} = d - d_{b} \cdot i_{motor}$</details>

15. If a desired voltage of $75V$ is needed from a power supply of $300V$, what is the duty cycle $d_a$ for pole A?
    - A) 0.375
    - B) 0.625
    - C) 0.5
    - D) 0.25
    <details><summary>Answer</summary>B) 0.625</details>

16. If the power delivered to the motor is equal to the power drawn from the power supply, which of the following is true?
    - A) $P_{motor} = P_{0} + P_{d}$
    - B) $P_{motor} = P_{d} - P_{0}$
    - C) $P_{motor} = P_{0}$
    - D) $P_{motor} = P_{d}$
    <details><summary>Answer</summary>D) $P_{motor} = P_{d}$</details>

17. In the PWM implementation, when the control voltage is greater than the triangular wave voltage, what happens to the switch?
    - A) The switch is on.
    - B) The switch is off.
    - C) The switch alternates between on and off.
    - D) The switch remains in its last state.
    <details><summary>Answer</summary>B) The switch is off.</details>

18. What do the equations $v = v_a - v_b$ and $v_b = (v_d / 2) - (v_0 / 2)$ represent in a PWM-controlled motor drive?
    - A) The relationships between motor speed and voltage.
    - B) The voltages across the power poles in the drive system.
    - C) The control voltages used for regulation.
    - D) The energy losses in the system.
    <details><summary>Answer</summary>B) The voltages across the power poles in the drive system.</details>

19. What is the significance of the PWM frequency in motor drives?
    - A) It determines the maximum voltage supplied to the motor.
    - B) It affects the average speed of the motor.
    - C) It controls the efficiency of energy conversion.
    - D) It impacts the responsiveness of the motor to changes in commands.
    <details><summary>Answer</summary>D) It impacts the responsiveness of the motor to changes in commands.</details>

20. When obtaining a desired voltage of 75V from a 300V supply, which of the values is the calculated voltage at node b?
    - A) 75V
    - B) 112.5V
    - C) 25V
    - D) 187.5V
    <details><summary>Answer</summary>B) 112.5V</details>