# physlib

[![PyPI version](https://img.shields.io/pypi/v/physlib.svg)](https://pypi.org/project/physlib/)
[![Python versions](https://img.shields.io/pypi/pyversions/physlib.svg)](https://pypi.org/project/physlib/)
[![License](https://img.shields.io/pypi/l/physlib.svg)](https://github.com/yourusername/physlib/blob/main/LICENSE)

**physlib** is a lightweight, modular Python library for solving common problems in physics. It covers key topics in mechanics, thermodynamics, waves, electricity, optics, and more.

## Features

- Kinematics and Dynamics  
- Work, Energy, and Momentum  
- Gravitational and Rotational Motion  
- Thermodynamics and Ideal Gas Law  
- Waves and Sound Calculations  
- Electricity and Magnetism (Ohm's Law, Coulomb's Law, etc.)  
- Optics (Snell's Law, Mirror and Lens Equations)

## Installation

Get from PyPi:
```bash
pip install physlib
```

Clone the repo and install locally:
```bash
    git clone https://github.com/mochathehuman/physlib.git
    cd pyslib
    pip install .
```
## Usage
    ```py
    from physlib import Kinematics, Dynamics, Thermodynamics

    # Kinematics example
    v = Kinematics.final_velocity(u=0, a=9.8, t=5)
    print(f"Final Velocity: {v} m/s")

    # Dynamics example
    force = Dynamics.force(m=10, a=2)
    print(f"Force: {force} N")

    # Thermodynamics example
    P = Thermodynamics.ideal_gas_pressure(n=1, T=300, V=0.01)
    print(f"Pressure: {P} Pa")
    ```

## Modules

| Module             | Topics Covered                          |
|--------------------|------------------------------------------|
| Kinematics         | Velocity, displacement, acceleration     |
| Dynamics           | Newton’s Laws, weight                   |
| WorkEnergy         | Work, kinetic & potential energy         |
| Momentum           | Momentum, impulse                       |
| Gravitation        | Newton’s Law of Gravitation              |
| Thermodynamics     | Ideal gas law, heat, efficiency          |
| Waves              | Wave speed, frequency, period            |
| Electromagnetism   | Ohm’s Law, Coulomb’s Law, power          |
| Optics             | Snell’s Law, mirror/lens formulas        |
| RotationalMotion   | Torque, angular velocity, inertia        |

## License

MIT License

---