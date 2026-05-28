# 🌙 UniBalance  
### Student Burnout & Budget Survival Assistant

> **Track. Analyse. Balance. Thrive.**

<p align="center">
  <img src="a_wide_clean_promotional_poster_ui_mockup_scene.png" width="780">
</p>

---

## 📌 Overview

**UniBalance** is a Python-based command-line wellbeing assistant designed to help university students manage academic stress, burnout risk, sleep habits, deadlines, and personal spending.

The application combines wellbeing analytics, behavioural tracking, budget awareness, personalised recommendations, and visual reports into one integrated system.

Unlike a basic diary or budgeting tool, UniBalance transforms simple daily student inputs into meaningful insights that support healthier study and lifestyle decisions.

---

## ✨ Key Features

### 🧠 Burnout Risk Analysis

UniBalance calculates a burnout score using:

- sleep duration
- stress level
- study intensity
- deadline pressure

Example output:

```text
Burnout score: 90/100
Risk level: High Risk
```

---

### 💸 Budget Tracking

Users can enter a weekly budget and the application calculates:

- total spending
- remaining budget
- average daily spending
- overspending warnings

Example output:

```text
Warning: You exceeded your weekly budget.
```

---

### 📊 Weekly Wellbeing Reports

The system analyses recent records and generates:

- average sleep
- average stress
- study hour trends
- spending summaries
- highest burnout day

---

### 📈 Data Visualisation

UniBalance automatically generates PNG charts:

```text
wellbeing_trends.png
weekly_spending.png
```

These charts help users understand behavioural patterns over time.

---

## 🖥️ Program Preview

```text
====================================
      UniBalance Student Assistant
====================================
1. Daily check-in
2. View latest burnout risk
3. View weekly budget summary
4. Generate weekly wellbeing report
5. View saved records
6. Exit
====================================
Choose an option:
```

---

## 🚀 Advanced Python Concepts Used

| Concept | Implementation |
|---|---|
| Object-Oriented Programming | `DailyRecord` and `UniBalanceApp` classes |
| File I/O | CSV data storage and loading |
| Exception Handling | Input validation for numeric entries |
| Data Visualisation | Matplotlib chart generation |
| Lists & Dictionaries | Record analysis and summaries |
| Date & Time Module | Automatic timestamp generation |

---

## 🏗️ Program Structure

### `DailyRecord`

Responsible for:

- storing daily user information
- calculating burnout scores
- determining risk levels
- generating recommendations

### `UniBalanceApp`

Responsible for:

- managing menu navigation
- handling user input
- saving and loading records
- generating reports and charts

---

## 📂 Project Structure

```text
UniBalance/
│
├── unibalance.py
├── unibalance_records.csv
├── wellbeing_trends.png
├── weekly_spending.png
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Install the required library:

```bash
pip install matplotlib
```

Or install from `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

Open terminal inside the project folder and run:

```bash
python unibalance.py
```

---

## 🎯 Target Audience

UniBalance is designed for university students who experience academic stress, deadline pressure, poor sleep habits, burnout risk, and financial pressure during busy study periods.

---

## 💡 Creativity & Originality

UniBalance was designed as a realistic student wellbeing analytics system rather than a basic calculator or diary application.

The project combines mental wellbeing tracking, burnout analysis, budget awareness, behavioural recommendations, and visual trend reporting into one complete support tool.

---

## 🔥 Challenges Faced

During development, several challenges were encountered:

- managing CSV data correctly
- preventing invalid user input
- designing meaningful burnout calculations
- handling chart generation without interrupting terminal input
- structuring the program using classes and functions

These challenges were solved through modular design, input validation, exception handling, and testing.

---

## 🔮 Future Improvements

Potential future features include:

- GUI interface
- AI-generated recommendations
- cloud database storage
- multi-user accounts
- mobile app version
- productivity scoring system
- reminder system

---

## 🏁 Conclusion

UniBalance demonstrates how Python can be used to create a practical and meaningful application that supports student wellbeing.

The project combines data tracking, analysis, visualisation, and personalised recommendations into a complete command-line software system.
