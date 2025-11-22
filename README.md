# Project Summary: Diabetes Risk Predictor

This document outlines the key facts and functionalities of the Diabetes Risk Predictor Python CLI application.

# General Information

The project is a Command-Line Interface (CLI) application.

The application is developed entirely in Python.

The purpose is to provide a preliminary assessment of diabetes risk.

Risk assessment is based on user-provided blood glucose readings (mg/dL).

The application uses standard medical thresholds (e.g., ADA/WHO guidelines).

The tool is strictly for educational and informational purposes.

The application is not a substitute for professional medical advice or diagnosis.

# Features

Test Type Support: The application supports three specific glucose tests:

Fasting Plasma Glucose (FPG)

Random Plasma Glucose (RPG)

Oral Glucose Tolerance Test (OGTT - 2-hour post-load)

Result Categories: It categorizes results into three primary risk levels:

Normal / Low Risk

Prediabetes / Elevated / Moderate Risk

Diabetes / High Risk

Input Handling: Input validation checks for valid numeric values.

Safety Warning: A special warning is displayed for extremely high glucose readings.

Output: The script displays a clear status, risk level, and tailored medical recommendations.

Execution Flow: The user can check multiple readings sequentially without restarting the script.

# Technical Details

Language: Python 3.x is required to run the script.

Dependencies: No external libraries or dependencies are needed.

File Name: The source code should be saved as diabetes_predictor.py.

# Running and Testing

Execution Command: The application is run using python diabetes_predictor.py in the terminal.

Test Cases: Specific glucose levels are recommended for testing all logic paths, including:

FPG tests at 95, 115, and 130 mg/dL.

RPG tests at 120, 185, and 210 mg/dL.

OGTT tests at 135, 190, and 205 mg/dL.

Error Testing: Inputting non-numeric values (abc) or extremely high values (700) validates error handling.
