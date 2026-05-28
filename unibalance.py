import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt


DATA_FILE = "unibalance_records.csv"


class DailyRecord:

    def __init__(
        self,
        date,
        study_hours,
        sleep_hours,
        stress_level,
        spending,
        deadlines,
        mood
    ):
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

        if self.sleep_hours < 5:
            score += 30
        elif self.sleep_hours < 7:
            score += 20
        else:
            score += 5

        if self.stress_level >= 8:
            score += 30
        elif self.stress_level >= 5:
            score += 20
        else:
            score += 5

        if self.study_hours >= 8:
            score += 20
        elif self.study_hours >= 5:
            score += 10
        else:
            score += 5

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
        else:
            return "Low Risk"

    def recommendation(self):
        suggestions = []

        if self.sleep_hours < 6:
            suggestions.append(
                "Try to sleep earlier and avoid late-night study."
            )

        if self.stress_level >= 7:
            suggestions.append(
                "Reduce over-studying and take breaks."
            )

        if self.deadlines >= 3:
            suggestions.append(
                "Prioritise your most urgent tasks."
            )

        if self.spending > 40:
            suggestions.append(
                "Consider reducing unnecessary spending."
            )

        if not suggestions:
            suggestions.append(
                "Your current balance looks healthy."
            )

        return suggestions


class UniBalanceApp:

    def __init__(self):
        self.records = []
        self.weekly_budget = 200

        if not os.path.exists(DATA_FILE):
            self.create_sample_data()

        self.load_records()

    def create_sample_data(self):
        sample_rows = [
            ["2026-05-15", 9, 4.5, 9, 48, 5, "Exhausted"],
            ["2026-05-16", 8, 5, 8, 35, 4, "Overwhelmed"],
            ["2026-05-17", 7, 5.5, 8, 28, 3, "Tired"],
            ["2026-05-18", 6, 6.5, 6, 15, 2, "Okay"],
            ["2026-05-19", 5, 7.5, 4, 12, 1, "Calm"],
            ["2026-05-20", 4, 8, 3, 8, 0, "Relaxed"],
            ["2026-05-21", 10, 4, 10, 52, 6, "Burned Out"]
        ]

        with open(DATA_FILE, "w", newline="", encoding="utf-8") as file:
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
            writer.writeheader()

            for row in sample_rows:
                record = DailyRecord(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6]
                )

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

    def load_records(self):
        self.records = []

        try:
            with open(DATA_FILE, "r", newline="", encoding="utf-8") as file:
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

                    if "burnout_score" in row:
                        record.burnout_score = int(row["burnout_score"])

                    self.records.append(record)

        except Exception:
            print("Warning: Data could not be loaded.")

    def save_record(self, record):
        file_exists = os.path.exists(DATA_FILE)

        with open(DATA_FILE, "a", newline="", encoding="utf-8") as file:
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

    def line(self):
        print("=" * 60)

    def pause(self):
        input("\nPress Enter to return to the main menu...")

    def get_float_input(self, prompt, min_value=None, max_value=None):
        while True:
            try:
                value = float(input(prompt))

                if min_value is not None and value < min_value:
                    print(f"Please enter a value >= {min_value}")
                    continue

                if max_value is not None and value > max_value:
                    print(f"Please enter a value <= {max_value}")
                    continue

                return value

            except ValueError:
                print("Invalid input. Please enter a number.")

    def get_int_input(self, prompt, min_value=None, max_value=None):
        while True:
            try:
                value = int(input(prompt))

                if min_value is not None and value < min_value:
                    print(f"Please enter a value >= {min_value}")
                    continue

                if max_value is not None and value > max_value:
                    print(f"Please enter a value <= {max_value}")
                    continue

                return value

            except ValueError:
                print("Invalid input. Please enter a whole number.")

    def daily_check_in(self):
        self.line()
        print("           DAILY WELLBEING CHECK-IN")
        self.line()

        date = datetime.now().strftime("%Y-%m-%d")

        study_hours = self.get_float_input(
            "Study hours today: ",
            0,
            24
        )

        sleep_hours = self.get_float_input(
            "Sleep hours last night: ",
            0,
            24
        )

        stress_level = self.get_int_input(
            "Stress level (1-10): ",
            1,
            10
        )

        spending = self.get_float_input(
            "Money spent today ($): ",
            0
        )

        deadlines = self.get_int_input(
            "Upcoming deadlines: ",
            0
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

        print("\nCheck-in saved successfully.")
        print(f"\nBurnout Score: {record.burnout_score}/100")
        print(f"Risk Level: {record.risk_level()}")

        print("\nPersonalised Suggestions:")
        for suggestion in record.recommendation():
            print(f"- {suggestion}")

        self.create_burnout_chart(
            record,
            "daily_checkin_burnout.png"
        )

    def view_latest_burnout_risk(self):
        if not self.records:
            print("\nNo records found.")
            return

        latest = self.records[-1]

        self.line()
        print("             BURNOUT RISK ANALYSIS")
        self.line()

        print(f"Date: {latest.date}")
        print(f"Mood: {latest.mood}")
        print(f"Study Hours: {latest.study_hours}")
        print(f"Sleep Hours: {latest.sleep_hours}")
        print(f"Stress Level: {latest.stress_level}/10")
        print(f"Deadlines: {latest.deadlines}")

        print("-" * 60)
        print(f"Burnout Score: {latest.burnout_score}/100")
        print(f"Risk Level: {latest.risk_level()}")

        print("\nPersonalised Suggestions:")
        for suggestion in latest.recommendation():
            print(f"- {suggestion}")

        self.create_burnout_chart(
            latest,
            "latest_burnout_analysis.png"
        )

    def budget_summary(self):
        if not self.records:
            print("\nNo records found.")
            return

        self.line()
        print("             WEEKLY BUDGET SUMMARY")
        self.line()

        self.weekly_budget = self.get_float_input(
            "Enter your weekly budget ($): ",
            0
        )

        recent_records = self.records[-7:]

        total_spending = sum(r.spending for r in recent_records)
        remaining = self.weekly_budget - total_spending
        avg_daily = total_spending / len(recent_records)

        print(f"\nWeekly Budget: ${self.weekly_budget:.2f}")
        print(f"Total Spent: ${total_spending:.2f}")
        print(f"Remaining Budget: ${remaining:.2f}")
        print(f"Average Daily Spending: ${avg_daily:.2f}")

        if remaining < 0:
            print("\nWarning: You exceeded your weekly budget.")
        elif remaining < self.weekly_budget * 0.2:
            print("\nWarning: Your remaining budget is low.")
        else:
            print("\nYour spending is under control.")

        self.create_budget_summary_chart(recent_records)
        self.create_weekly_spending_chart(recent_records)

    def generate_weekly_report(self):
        if not self.records:
            print("\nNo records found.")
            return

        recent_records = self.records[-7:]

        avg_sleep = sum(r.sleep_hours for r in recent_records) / len(recent_records)
        avg_stress = sum(r.stress_level for r in recent_records) / len(recent_records)
        avg_study = sum(r.study_hours for r in recent_records) / len(recent_records)
        total_spending = sum(r.spending for r in recent_records)

        highest_burnout = max(
            recent_records,
            key=lambda r: r.burnout_score
        )

        self.line()
        print("            WEEKLY WELLBEING REPORT")
        self.line()

        print(f"Average Sleep: {avg_sleep:.1f} hours")
        print(f"Average Stress: {avg_stress:.1f}/10")
        print(f"Average Study Time: {avg_study:.1f} hours")
        print(f"Total Spending: ${total_spending:.2f}")
        print(f"Highest Burnout Day: {highest_burnout.date}")
        print(f"Highest Burnout Score: {highest_burnout.burnout_score}/100")

        self.create_wellbeing_trends_chart(recent_records)

    def create_burnout_chart(self, record, filename):
        score = record.burnout_score
        remaining = 100 - score
        suggestions = record.recommendation()

        bg_color = "#071126"
        panel_color = "#0b1633"
        border_color = "#6d5cae"
        accent_color = "#ff4f64"
        muted_color = "#25345f"
        text_color = "#f8fafc"
        sub_text_color = "#cbd5e1"
        purple_text = "#c4a7ff"

        fig = plt.figure(figsize=(7, 9), facecolor=bg_color)
        ax = fig.add_axes([0, 0, 1, 1])
        ax.set_facecolor(bg_color)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis("off")

        card = plt.Rectangle(
            (0.03, 0.03),
            0.94,
            0.94,
            linewidth=1.5,
            edgecolor=border_color,
            facecolor=panel_color,
            alpha=0.95
        )
        ax.add_patch(card)

        ax.text(
            0.11,
            0.93,
            "🔥 Burnout Risk Analysis",
            fontsize=18,
            fontweight="bold",
            color=text_color,
            va="center"
        )

        ax.plot(
            [0.07, 0.93],
            [0.89, 0.89],
            color=border_color,
            linewidth=1,
            alpha=0.8
        )

        gauge_ax = fig.add_axes([0.22, 0.50, 0.56, 0.36])
        gauge_ax.set_facecolor(panel_color)

        gauge_ax.pie(
            [score, remaining],
            startangle=90,
            counterclock=False,
            colors=[accent_color, muted_color],
            wedgeprops={
                "width": 0.22,
                "edgecolor": panel_color
            }
        )

        gauge_ax.text(
            0,
            0.12,
            str(score),
            ha="center",
            va="center",
            fontsize=46,
            fontweight="bold",
            color=text_color
        )

        gauge_ax.text(
            0,
            -0.20,
            "/100",
            ha="center",
            va="center",
            fontsize=20,
            color=sub_text_color
        )

        gauge_ax.axis("equal")
        gauge_ax.axis("off")

        risk_color = accent_color

        if record.risk_level() == "Medium Risk":
            risk_color = "#f59e0b"
        elif record.risk_level() == "Low Risk":
            risk_color = "#22c55e"

        ax.text(
            0.5,
            0.46,
            record.risk_level(),
            ha="center",
            va="center",
            fontsize=23,
            fontweight="bold",
            color=risk_color
        )

        ax.plot(
            [0.08, 0.92],
            [0.38, 0.38],
            color=border_color,
            linewidth=1,
            alpha=0.8
        )

        ax.text(
            0.11,
            0.33,
            "Personalised Suggestions",
            fontsize=12,
            fontweight="bold",
            color=purple_text,
            va="center"
        )

        icon_list = ["☾", "📖", "☑", "$"]
        icon_colours = [
            "#4fd1c5",
            "#8b5cf6",
            "#3b82f6",
            "#f59e0b"
        ]

        y_start = 0.27
        line_gap = 0.07

        for i, suggestion in enumerate(suggestions[:4]):
            y = y_start - i * line_gap

            icon_circle = plt.Circle(
                (0.14, y),
                0.028,
                color=icon_colours[i % len(icon_colours)]
            )
            ax.add_patch(icon_circle)

            ax.text(
                0.14,
                y,
                icon_list[i % len(icon_list)],
                ha="center",
                va="center",
                fontsize=12,
                color="white",
                fontweight="bold"
            )

            ax.text(
                0.20,
                y,
                suggestion,
                ha="left",
                va="center",
                fontsize=9.5,
                color=text_color
            )

            if i < min(len(suggestions[:4]), 4) - 1:
                ax.plot(
                    [0.20, 0.88],
                    [y - 0.035, y - 0.035],
                    color="#334155",
                    linewidth=0.6,
                    alpha=0.7
                )

        plt.savefig(
            filename,
            facecolor=bg_color,
            bbox_inches="tight",
            dpi=200
        )

        plt.close()

        print(f"\nChart generated: {filename}")

    def create_budget_summary_chart(self, records):
        spending = [r.spending for r in records]

        total_spending = sum(spending)
        remaining = self.weekly_budget - total_spending
        avg_daily = total_spending / len(records)
        used_percent = total_spending / self.weekly_budget * 100

        bg_color = "#071126"
        panel_color = "#0b1633"
        border_color = "#6d5cae"
        box_color = "#101a3a"
        text_color = "#f8fafc"
        sub_text_color = "#cbd5e1"
        red = "#ff4f64"
        orange = "#f97316"
        green = "#7ddc6f"
        blue = "#60a5fa"

        if remaining < 0:
            status_text = "Over Budget"
            status_color = red
            warning_text = "You exceeded your weekly budget."
        elif remaining < self.weekly_budget * 0.2:
            status_text = "Low Remaining"
            status_color = orange
            warning_text = "Your remaining budget is low."
        else:
            status_text = "On Track"
            status_color = green
            warning_text = "Your spending is under control."

        fig = plt.figure(figsize=(6, 7), facecolor=bg_color)
        ax = fig.add_axes([0, 0, 1, 1])
        ax.set_facecolor(bg_color)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis("off")

        card = plt.Rectangle(
            (0.03, 0.03),
            0.94,
            0.94,
            linewidth=1.5,
            edgecolor=border_color,
            facecolor=panel_color
        )
        ax.add_patch(card)

        ax.text(
            0.08,
            0.92,
            "💰 Weekly Budget Summary",
            fontsize=17,
            fontweight="bold",
            color=text_color,
            va="center"
        )

        ax.plot(
            [0.07, 0.93],
            [0.87, 0.87],
            color=border_color,
            linewidth=1,
            alpha=0.8
        )

        ax.text(
            0.5,
            0.76,
            "Remaining Budget",
            ha="center",
            va="center",
            fontsize=12,
            color=sub_text_color
        )

        ax.text(
            0.5,
            0.68,
            f"${remaining:.0f}",
            ha="center",
            va="center",
            fontsize=42,
            fontweight="bold",
            color=status_color
        )

        ax.text(
            0.5,
            0.60,
            status_text,
            ha="center",
            va="center",
            fontsize=16,
            fontweight="bold",
            color=status_color
        )

        ax.add_patch(
            plt.Rectangle(
                (0.12, 0.52),
                0.76,
                0.035,
                facecolor="#1e293b",
                edgecolor="#334155"
            )
        )

        progress_width = min(used_percent, 100) / 100 * 0.76

        ax.add_patch(
            plt.Rectangle(
                (0.12, 0.52),
                progress_width,
                0.035,
                facecolor=status_color,
                edgecolor=status_color
            )
        )

        ax.text(
            0.5,
            0.47,
            f"{used_percent:.1f}% of weekly budget used",
            ha="center",
            va="center",
            fontsize=10,
            color=sub_text_color
        )

        metrics = [
            ("Weekly Budget", f"${self.weekly_budget:.0f}", blue),
            ("Total Spent", f"${total_spending:.0f}", red),
            ("Avg Daily", f"${avg_daily:.2f}", text_color)
        ]

        x_positions = [0.09, 0.365, 0.64]
        y = 0.31
        box_w = 0.27
        box_h = 0.12

        for i, (label, value, value_color) in enumerate(metrics):
            x = x_positions[i]

            metric_box = plt.Rectangle(
                (x, y),
                box_w,
                box_h,
                linewidth=1,
                edgecolor="#263b70",
                facecolor=box_color,
                alpha=0.95
            )
            ax.add_patch(metric_box)

            ax.text(
                x + box_w / 2,
                y + 0.078,
                label,
                ha="center",
                va="center",
                fontsize=8.5,
                color=sub_text_color
            )

            ax.text(
                x + box_w / 2,
                y + 0.035,
                value,
                ha="center",
                va="center",
                fontsize=14,
                fontweight="bold",
                color=value_color
            )

        warning_box = plt.Rectangle(
            (0.08, 0.11),
            0.84,
            0.13,
            linewidth=1.2,
            edgecolor=status_color,
            facecolor="#1b1730",
            alpha=0.95
        )
        ax.add_patch(warning_box)

        icon = "⚠️" if status_text != "On Track" else "✅"

        ax.text(
            0.5,
            0.175,
            f"{icon} {warning_text}",
            ha="center",
            va="center",
            fontsize=11,
            color=text_color
        )

        plt.savefig(
            "weekly_budget_summary.png",
            facecolor=bg_color,
            bbox_inches="tight",
            dpi=200
        )

        plt.close()

        print("\nChart generated: weekly_budget_summary.png")

    def create_wellbeing_trends_chart(self, records):
        dates = [r.date for r in records]
        sleep = [r.sleep_hours for r in records]
        stress = [r.stress_level for r in records]
        burnout = [r.burnout_score for r in records]

        plt.figure(figsize=(10, 5))

        plt.plot(
            dates,
            sleep,
            marker="o",
            linewidth=3,
            label="Sleep(hrs)"
        )

        plt.plot(
            dates,
            stress,
            marker="o",
            linewidth=3,
            label="Stress(1~10)"
        )

        plt.plot(
            dates,
            burnout,
            marker="o",
            linewidth=3,
            label="Burnout(Score)"
        )

        plt.title("Weekly Wellbeing Trends", fontsize=16, fontweight="bold")
        plt.xlabel("Date")
        plt.ylabel("Value")
        plt.xticks(rotation=45)
        plt.grid(alpha=0.3)
        plt.legend()
        plt.tight_layout()
        plt.savefig("weekly_wellbeing_trends.png")
        plt.close()

        print("\nChart generated: weekly_wellbeing_trends.png")

    def create_weekly_spending_chart(self, records):
        dates = [r.date for r in records]
        spending = [r.spending for r in records]

        plt.figure(figsize=(10, 5))
        plt.bar(dates, spending)

        plt.title("Weekly Spending", fontsize=16, fontweight="bold")
        plt.xlabel("Date")
        plt.ylabel("Spending ($)")
        plt.xticks(rotation=45)

        plt.tight_layout()
        plt.savefig("weekly_spending.png")
        plt.close()

        print("\nChart generated: weekly_spending.png")

    def view_saved_records(self):
        if not self.records:
            print("\nNo saved records.")
            return

        self.line()
        print("                 SAVED RECORDS")
        self.line()

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
        print("\n")
        self.line()
        print("        UniBalance Student Assistant")
        print("     Track. Analyse. Balance. Thrive.")
        self.line()
        print("1. Daily check-in")
        print("2. View latest burnout risk")
        print("3. View weekly budget summary")
        print("4. Generate weekly wellbeing report")
        print("5. View saved records")
        print("6. Exit")
        self.line()

    def run(self):
        while True:
            self.show_menu()

            choice = input("Choose an option: ").strip()

            if choice == "1":
                self.daily_check_in()
                self.pause()

            elif choice == "2":
                self.view_latest_burnout_risk()
                self.pause()

            elif choice == "3":
                self.budget_summary()
                self.pause()

            elif choice == "4":
                self.generate_weekly_report()
                self.pause()

            elif choice == "5":
                self.view_saved_records()
                self.pause()

            elif choice == "6":
                print("\nThank you for using UniBalance!")
                break

            else:
                print("Invalid option. Please choose 1-6.")
                self.pause()


if __name__ == "__main__":
    app = UniBalanceApp()
    app.run()
