import csv
from collections import defaultdict
import matplotlib.pyplot as plt

FILENAME = "weather_log.csv"  # Same folder as this script

def visualize_weather():
    data = []
    dates = []
    temps = []
    conditions = defaultdict(int)

    print("✅ Script started...")

    try:
        with open(FILENAME, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            print("📄 Reading CSV rows...")
            for row in reader:
                print("➡️ Row found:", row)
                try:
                    dates.append(row["Date"])
                    temps.append(float(row["Temperature"]))  # convert to float
                    conditions[row["Condition"]] += 1
                except ValueError:
                    print("⚠️ Skipping row due to value error:", row)
                    continue

        if not dates:
            print("❌ No valid data found. Exiting.")
            return

        print("📊 Data collected. Plotting graphs...")

        # Plot 1: Temperature over time
        plt.figure(figsize=(10, 7))
        plt.plot(dates, temps, marker='o')
        plt.title("Temperature Over Time")
        plt.xlabel("Date")
        plt.ylabel("Temperature (°C)")
        plt.xticks(rotation=45)
        plt.grid()
        plt.tight_layout()
        plt.show()

        # Plot 2: Weather Conditions bar chart
        plt.figure(figsize=(7, 5))
        plt.bar(conditions.keys(), conditions.values(), color='skyblue')
        plt.title("Weather Conditions")
        plt.xlabel("Condition")
        plt.ylabel("Frequency")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        print("✅ Visualization complete!")

    except FileNotFoundError:
        print(f"❌ File not found: {FILENAME}")

visualize_weather()
