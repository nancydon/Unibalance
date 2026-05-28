# UniBalance — Student Burnout & Budget Survival Assistant

## Project Overview

UniBalance is a Python-based command-line wellbeing assistant designed for university students who struggle with balancing academic pressure, sleep, stress, deadlines, and personal spending.

The application allows users to complete daily wellbeing check-ins, analyse burnout risk levels, monitor weekly spending habits, and generate wellbeing reports with visual charts.

Unlike a basic diary or to-do list, UniBalance combines self-reflection, data tracking, analysis, and personalised recommendations to help students identify unhealthy patterns early and make better lifestyle decisions.

---

# Problem Statement

Many university students experience:

* High academic stress
* Poor sleep schedules
* Multiple overlapping deadlines
* Burnout
* Financial pressure

However, students often lack a simple system that combines wellbeing tracking and budget awareness in one place.

UniBalance aims to solve this problem by transforming simple daily inputs into meaningful wellbeing insights and behavioural recommendations.

---

# Key Features

## 1. Daily Wellbeing Check-in

Users can enter:

* Study hours
* Sleep hours
* Stress level
* Daily spending
* Number of upcoming deadlines
* Mood

The system stores all records in a CSV file for future analysis.

---

## 2. Burnout Risk Analysis

The application calculates a burnout score based on:

* Sleep duration
* Stress level
* Study intensity
* Deadline pressure

Risk levels include:

* Low Risk
* Medium Risk
* High Risk

The program also generates personalised recommendations based on the user’s condition.

Example:

```text id="j1y6co"
Burnout score: 90/100
Risk level: High Risk
```

---

## 3. Budget Tracking System

Users can input a weekly budget.

The application calculates:

* Remaining budget
* Average daily spending
* Overspending warnings

Example:

```text id="n88y1r"
Warning: You exceeded your weekly budget.
```

---

## 4. Weekly Wellbeing Report

The system analyses recent records and generates:

* Average sleep statistics
* Stress summaries
* Study hour trends
* Spending summaries
* Highest burnout day analysis

---

## 5. Data Visualisation

UniBalance automatically generates charts including:

* Weekly wellbeing trends
* Weekly spending trends

Charts are saved as PNG files:

```text id="ccwpk1"
wellbeing_trends.png
weekly_spending.png
```

These visualisations help users better understand behavioural patterns over time.

---

# Advanced Python Concepts Used

This project demonstrates multiple advanced Python programming concepts required by the assignment rubric.

| Advanced Concept            | Implementation                        |
| --------------------------- | ------------------------------------- |
| Object-Oriented Programming | DailyRecord and UniBalanceApp classes |
| File I/O                    | CSV data storage and loading          |
| Exception Handling          | Input validation for numeric entries  |
| Data Visualisation          | Matplotlib graph generation           |
| Lists & Dictionaries        | Record analysis and summaries         |
| Date & Time Module          | Automatic timestamp generation        |

The application thoughtfully integrates these concepts to enhance both functionality and user experience.

---

# Program Structure

The project is organised into multiple functions and classes for readability and maintainability.

## Main Classes

### DailyRecord

Responsible for:

* Storing daily user information
* Calculating burnout scores
* Determining risk levels
* Generating recommendations

### UniBalanceApp

Responsible for:

* Managing program flow
* Handling user input
* Saving and loading records
* Generating reports and charts

---

# File Structure

```text id="6vhjlwm"
UniBalance/
│
├── unibalance.py
├── unibalance_records.csv
├── wellbeing_trends.png
├── weekly_spending.png
└── README.md
```

---

# Installation
## Install Matplotlib

Run:

```bash id="hbn2kh"
pip install matplotlib
```

---

# How to Run

Open terminal inside the project folder:

```bash id="bjlwm7"
python unibalance.py
```

---

# Menu System

```text id="h0f0f4"
1. Daily check-in
2. View latest burnout risk
3. View weekly budget summary
4. Generate weekly wellbeing report
5. View saved records
6. Exit
```

---

# Functionality Demonstration

## Example Burnout Analysis

```text id="79tvgn"
Burnout score: 100/100
Risk level: High Risk
```

---

## Example Recommendations

```text id="2kssr6"
- Try to sleep earlier and avoid late-night study.
- Prioritise your most urgent assignment first.
- Avoid over-studying and use focused study sessions.
```

---

# Creativity & Originality

UniBalance was designed as a realistic student wellbeing analytics system rather than a basic calculator or diary application.

The project combines:

* Mental wellbeing tracking
* Burnout analysis
* Financial awareness
* Behavioural recommendations
* Data visualisation

into one integrated student support tool.

The idea focuses on solving a real-world university student problem using data-driven insights.

---

# Challenges Faced

During development, several challenges were encountered:

* Managing CSV data correctly
* Preventing invalid user input
* Designing meaningful burnout calculations
* Handling graph generation without interrupting terminal input
* Structuring the program using classes and functions

These challenges were resolved through exception handling, modular design, and testing.


