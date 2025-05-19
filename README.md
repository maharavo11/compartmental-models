# compartmental-models

# Epidemiological Modeling with CmdStanPy: SIR and SEIR Models

This project demonstrates how to fit Susceptible-Infected-Recovered (SIR) and Susceptible-Exposed-Infected-Recovered (SEIR) epidemiological models to outbreak data using `cmdstanpy`. The analysis is performed on flu data from a boarding school and simulated incidence data.

## Table of Contents
1. [Installation](#installation)
2. [Data](#data)
3. [Models Explored](#models-explored)
    - [SIR Model with Prevalence Data](#sir-model-with-prevalence-data)
    - [Prior Predictive Checks for SIR Model](#prior-predictive-checks-for-sir-model)
    - [SEIR Model with Prevalence Data](#seir-model-with-prevalence-data)
    - [SEIR Model with Incidence Data](#seir-model-with-incidence-data)
4. [Stan Model Files](#stan-model-files)
5. [Running the Analysis](#running-the-analysis)

## Installation

This project relies heavily on `cmdstanpy`. Ensure it's installed correctly.

```python
# Install utilities (if not already present)
# !curl -O "https://raw.githubusercontent.com/MLGlobalHealth/StatML4PopHealth/main/practicals/resources/scripts/utilities.py"

# from utilities import custom_install_cmdstan, test_cmdstan_installation
# custom_install_cmdstan()
