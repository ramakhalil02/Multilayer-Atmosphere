# Radiative Transfer Model for Earth's Multilayer Atmosphere

This project is from independent research and development conducted during my **Master of Science program in Computational Physics**. The entire methodology, analysis, and implementation of all numerical solvers were executed solely by me, and the full work is documented in the accompanying report and code.

---

## Table of Contents

* [About The Project](#about-the-project)
* [Core Objectives](#core-objectives)
* [Languages and Libraries](#languages-and-libraries)
* [Methods Implemented](#methods-implemented)
* [Key Findings](#key-findings)
* [Getting Started](#getting-started)
* [Full Project Report](#full-project-report)
* [Contact](#contact)

---

## About The Project

This work utilizes a **Radiative Transfer Model** to compute the average temperature of the Earth's surface. The atmosphere is modeled using a **multilayer approximation** to accurately calculate the absorption, transmission, and emission of both visible (VIS) and infrared (IR) radiation by each atmospheric layer.

The project simulates the **Greenhouse Effect** by analyzing the energy balance at the surface and between each atmospheric layer, providing a numerical demonstration of how atmospheric absorption parameters influence global temperature and outgoing flux.

## Core Objectives

1.  **Implement Multilayer Radiative Transfer:** Develop the energy balance equations for an atmosphere approximated by multiple distinct layers.

2.  **Compute Surface Temperature Iteratively:** Use an iterative process to solve the coupled energy balance equations until the temperature profile (including surface temperature, $T_{surf}$) reaches a steady-state/converged solution.

3.  **Analyze $\alpha_{IR}$ Sensitivity:** Investigate the relationship between the surface temperature, the outgoing IR flux, and the atmospheric absorption coefficient ($\alpha_{IR}$).

4.  **Compare to Simplified Models:** Validate the results by comparing them against well-known, simple models like the "No Atmosphere" and "Perfect Greenhouse Layer" models.

---

## Languages and Libraries

| Category | Tools & Libraries | Competency Demonstrated |
| :--- | :--- | :--- |
| **Language** | Python | Efficient development and handling of iterative numerical schemes and energy flux calculations. |
| **Numerical** | NumPy | Advanced array manipulation for representing multilayer parameters and solving linear/coupled systems. |
| **Visualization** | Matplotlib | Generating high-quality plots to show the convergence (temperature evolution) behavior for different parameters. |

---

## Methods Implemented

The computational core of the project implements the following techniques:

| Method | Role in Project | Key Implementation Detail |
| :--- | :--- | :--- |
| **Multilayer Approximation** | Atmospheric modeling. | The continuous atmosphere is divided into discrete layers, each characterized by its temperature and specific absorption/transmission properties for VIS and IR radiation. |
| **Radiative Transfer Equations** | Governing physics. | Energy balance is maintained by calculating incoming solar flux (VIS) and outgoing thermal flux (IR) using the **Stefan-Boltzmann Law** and absorption/emission rates ($\alpha_{IR}$). |
| **Iterative Convergence** | Numerical stability. | Temperatures are updated in a loop until the energy flux at the top of the atmosphere is constant, indicating thermal equilibrium. |
| **Simplified Model Benchmarking** | Validation. | Numerical results are compared against analytical solutions for the basic one-layer and no-atmosphere models. |

## Key Findings

* **Greenhouse Effect Quantified:** The surface temperature rose significantly as the infrared absorption coefficient ($\alpha_{IR}$) was increased, quantitatively demonstrating the enhanced Greenhouse Effect.
* **Convergence Behavior:** The time taken for the system to reach thermal equilibrium (convergence) was highly sensitive to the initial temperature guess and the value of $\alpha_{IR}$.
* **Flux Dependency:** The final outgoing longwave radiation (OLR) flux was found to be directly dependent on the $\alpha_{IR}$ value, illustrating the trapping and re-emission of heat.
* **Model Accuracy:** The final steady-state surface temperatures provided a realistic representation of Earth's average temperature, successfully reproducing values higher than the "No Atmosphere" model.

---

## Getting Started

### Execution

To run the simulation and generate the results and visualizations, execute the core solver script:

```bash
python Multilayer_Atmosphere.py
```
---

## Full Project Report

For a complete breakdown of the theoretical derivations and full numerical results (including the plots), please see the final project report:

[**Full Project Report (PDF)**](Multilayer_Atmosphere.pdf)

---

## Contact

I'm happy to hear your feedback or answer any questions about this project!

**Author** Rama Khalil

**Email**  rama.khalil.990@gmail.com
