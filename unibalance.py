import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt


DATA_FILE = "unibalance_records.csv"


class DailyRecord:
    def __init__(self, date, study_hours, sleep_hours,
                 stress_level, spending, deadlines, mood):

        self.date = date
        self.study_hours = study_hours
        self.sleep_hours = sleep_hours
        self.stress_level = stress_level
        self.spending = spending
        self.deadlines = deadlines
        self.mood = mood

        self.burnout_score = self.calculate_burnout_score()

    def calculate_burnout_score(self):

        score = 0

        # Sleep
        if self.sleep_hours < 5:
            score += 30
        elif self.sleep_hours < 7:
            score += 20
        else:
            score += 5

        # Stress
        if self.stress_level >= 8:
            score += 30
        elif self.stress_level >= 5:
            score += 20
        else:
            score += 5

        # Study hours
        if self.study_hours >= 8:
            score += 20
        elif self.study_hours >= 5:
            score += 10
        else:
            score += 5

        # Deadlines
        if self.deadlines >= 4:
            score += 20
        elif self.deadlines >= 2:
            score += 10
        else:
            score += 5

        return min(score, 100)

    def risk_level(self):

        if self.burnout_score >= 75:
            return "High Risk"

        elif self.burnout_score >= 45:
            return "Medium Risk"

        return "Low Risk"

    def recommendation(self):

        suggestions = []

        if self.sleep_hours < 6:
            suggestions.append(
                "Try to sleep earlier and avoid late-night study."
            )

        if self.stress_level >= 7:
            suggestions.append(
                "Take short breaks and divide tasks into smaller goals."
            )

        if self.study_hours >= 8:
            suggestions.append(
                "Avoid over-studying and use focused study sessions."
            )

        if self.deadlines >= 3:
            suggestions.append(
                "Prioritise your most urgent assignment first."
            )

        if self.spending > 40:
            suggestions.append(
                "Consider reducing unnecessary spending tomorrow."
            )

        if not suggestions:
            suggestions.append(
                "Your current balance looks healthy. Keep it up!"
            )

        return suggestions


class UniBalanceApp:

    def __init__(self):

        self.records = []
        self.weekly_budget = 200

        self.load_records()

    def load_records(self):

        if not os.path.exists(DATA_FILE):
            return

        try:

            with open(DATA_FILE, "r", newline="",
                      encoding="utf-8") as file:

                reader = csv.DictReader(file)

                for row in reader:

                    record = DailyRecord(
                        row["date"],
                        float(row["study_hours"]),
                        float(row["sleep_hours"]),
                        int(row["stress_level"]),
                        float(row["spending"]),
                        int(row["deadlines"]),
                        row["mood"]
                    )

                    # Load saved burnout score
                    record.burnout_score = int(
                        row["burnout_score"]
                    )

                    self.records.append(record)

        except Exception:
            print("Warning: Data file could not be loaded.")

    def save_record(self, record):

        file_exists = os.path.exists(DATA_FILE)

        with open(DATA_FILE, "a", newline="",
                  encoding="utf-8") as file:

            fieldnames = [
                "date",
                "study_hours",
                "sleep_hours",
                "stress_level",
                "spending",
                "deadlines",
                "mood",
                "burnout_score"
            ]

            writer = csv.DictWriter(file, fieldnames=fieldnames)

            if not file_exists:
                writer.writeheader()

            writer.writerow({
                "date": record.date,
                "study_hours": record.study_hours,
                "sleep_hours": record.sleep_hours,
                "stress_level": record.stress_level,
                "spending": record.spending,
                "deadlines": record.deadlines,
                "mood": record.mood,
                "burnout_score": record.burnout_score
            })

    def get_float_input(self, prompt,
                        min_value=None,
                        max_value=None):

        while True:

            try:

                value = float(input(prompt))

                if min_value is not None and value < min_value:
                    print(
                        f"Please enter a value >= {min_value}"
                    )
                    continue

                if max_value is not None and value > max_value:
                    print(
                        f"Please enter a value <= {max_value}"
                    )
                    continue

                return value

            except ValueError:
                print("Invalid input. Please enter a number.")

    def get_int_input(self, prompt,
                      min_value=None,
                      max_value=None):

        while True:

            try:

                value = int(input(prompt))

                if min_value is not None and value < min_value:
                    print(
                        f"Please enter a value >= {min_value}"
                    )
                    continue

                if max_value is not None and value > max_value:
                    print(
                        f"Please enter a value <= {max_value}"
                    )
                    continue

                return value

            except ValueError:
                print("Invalid input. Please enter a whole number.")

    def daily_check_in(self):

        print("\n--- Daily Check-in ---")

        date = datetime.now().strftime("%Y-%m-%d")

        study_hours = self.get_float_input(
            "Study hours today: ", 0, 24
        )

        sleep_hours = self.get_float_input(
            "Sleep hours last night: ", 0, 24
        )

        stress_level = self.get_int_input(
            "Stress level (1-10): ", 1, 10
        )

        spending = self.get_float_input(
            "Money spent today ($): ", 0
        )

        deadlines = self.get_int_input(
            "Number of upcoming deadlines: ", 0
        )

        mood = input("Mood today: ")

        record = DailyRecord(
            date,
            study_hours,
            sleep_hours,
            stress_level,
            spending,
            deadlines,
            mood
        )

        self.records.append(record)

        self.save_record(record)

        print("\nCheck-in saved successfully!")

        print(
            f"Burnout score: "
            f"{record.burnout_score}/100"
        )

        print(
            f"Risk level: "
            f"{record.risk_level()}"
        )

        print("\nPersonalised Suggestions:")

        for suggestion in record.recommendation():
            print(f"- {suggestion}")

    def view_latest_burnout_risk(self):

        if not self.records:
            print("\nNo records found.")
            return

        latest = self.records[-1]

        print("\n--- Latest Burnout Risk ---")

        print(f"Date: {latest.date}")

        print(
            f"Burnout score: "
            f"{latest.burnout_score}/100"
        )

        print(
            f"Risk level: "
            f"{latest.risk_level()}"
        )

        print("\nSuggestions:")

        for suggestion in latest.recommendation():
            print(f"- {suggestion}")

    def budget_summary(self):

        if not self.records:
            print("\nNo records found.")
            return

        print("\n--- Weekly Budget Summary ---")

        self.weekly_budget = self.get_float_input(
            "Enter your weekly budget ($): ",
            0
        )

        recent_records = self.records[-7:]

        total_spending = sum(
            record.spending for record in recent_records
        )

        remaining = self.weekly_budget - total_spending

        average_daily = (
            total_spending / len(recent_records)
        )

        print(
            f"\nTotal spending: "
            f"${total_spending:.2f}"
        )

        print(
            f"Remaining budget: "
            f"${remaining:.2f}"
        )

        print(
            f"Average daily spending: "
            f"${average_daily:.2f}"
        )

        if remaining < 0:
            print(
                "Warning: You exceeded your weekly budget."
            )

        elif remaining < self.weekly_budget * 0.2:
            print(
                "Warning: Your remaining budget is low."
            )

        else:
            print("Your spending is under control.")

    def generate_weekly_report(self):

        if not self.records:
            print("\nNo records found.")
            return

        recent_records = self.records[-7:]

        avg_sleep = sum(
            record.sleep_hours
            for record in recent_records
        ) / len(recent_records)

        avg_stress = sum(
            record.stress_level
            for record in recent_records
        ) / len(recent_records)

        avg_study = sum(
            record.study_hours
            for record in recent_records
        ) / len(recent_records)

        total_spending = sum(
            record.spending
            for record in recent_records
        )

        highest_burnout = max(
            recent_records,
            key=lambda r: r.burnout_score
        )

        print("\n--- Weekly Wellbeing Report ---")

        print(
            f"Average sleep: "
            f"{avg_sleep:.1f} hours"
        )

        print(
            f"Average stress: "
            f"{avg_stress:.1f}/10"
        )

        print(
            f"Average study time: "
            f"{avg_study:.1f} hours"
        )

        print(
            f"Total spending: "
            f"${total_spending:.2f}"
        )

        print(
            f"Highest burnout day: "
            f"{highest_burnout.date}"
        )

        if avg_sleep < 6:
            main_issue = "insufficient sleep"

        elif avg_stress >= 7:
            main_issue = "high stress"

        elif total_spending > self.weekly_budget:
            main_issue = "overspending"

        else:
            main_issue = "overall balance is healthy"

        print(f"Main issue detected: {main_issue}")

        self.create_charts(recent_records)

    def create_charts(self, records):

        dates = [r.date for r in records]

        sleep = [r.sleep_hours for r in records]

        stress = [r.stress_level for r in records]

        burnout = [r.burnout_score for r in records]

        spending = [r.spending for r in records]

        # Wellbeing trend chart
        plt.figure(figsize=(10, 5))

        plt.plot(dates, sleep,
                 marker="o",
                 label="Sleep")

        plt.plot(dates, stress,
                 marker="o",
                 label="Stress")

        plt.plot(dates, burnout,
                 marker="o",
                 label="Burnout")

        plt.title("Weekly Wellbeing Trends")

        plt.xlabel("Date")

        plt.ylabel("Values")

        plt.xticks(rotation=45)

        plt.legend()

        plt.tight_layout()

        plt.savefig("wellbeing_trends.png")

        plt.close()

        # Spending chart
        plt.figure(figsize=(10, 5))

        plt.bar(dates, spending)

        plt.title("Weekly Spending")

        plt.xlabel("Date")

        plt.ylabel("Spending ($)")

        plt.xticks(rotation=45)

        plt.tight_layout()

        plt.savefig("weekly_spending.png")

        plt.close()

        print("\nCharts generated successfully.")

        print(
            "Saved files:"
        )

        print("- wellbeing_trends.png")

        print("- weekly_spending.png")

    def view_saved_records(self):

        if not self.records:
            print("\nNo saved records.")
            return

        print("\n--- Saved Records ---")

        for record in self.records:

            print(
                f"{record.date} | "
                f"Study: {record.study_hours}h | "
                f"Sleep: {record.sleep_hours}h | "
                f"Stress: {record.stress_level}/10 | "
                f"Spending: ${record.spending:.2f} | "
                f"Deadlines: {record.deadlines} | "
                f"Mood: {record.mood} | "
                f"Burnout: {record.burnout_score}/100"
            )

    def show_menu(self):

        print("\n====================================")

        print("      UniBalance Student Assistant")

        print("====================================")

        print("1. Daily check-in")

        print("2. View latest burnout risk")

        print("3. View weekly budget summary")

        print("4. Generate weekly wellbeing report")

        print("5. View saved records")

        print("6. Exit")

        print("====================================")

    def run(self):

        while True:

            self.show_menu()

            choice = input("Choose an option: ")

            if choice == "1":
                self.daily_check_in()

            elif choice == "2":
                self.view_latest_burnout_risk()

            elif choice == "3":
                self.budget_summary()

            elif choice == "4":
                self.generate_weekly_report()

            elif choice == "5":
                self.view_saved_records()

            elif choice == "6":

                print(
                    "\nThank you for using UniBalance!"
                )

                break

            else:
                print(
                    "Invalid option. "
                    "Please choose 1-6."
                )


if __name__ == "__main__":

    app = UniBalanceApp()

    app.run()
