import json
import csv
import os

INPUT_FILE = "api_data.json"
OUTPUT_FILE = "converted_api_data.csv"


def load_json_data(filename):
      if not os.path.exists(filename):
            print("JSON file not found.")
            return []
      with open(filename, "r", encoding="utf-8") as f:
          try:
               return json.load(f)
          except :
               print("Error decoding JSON.")
               


def convert_to_csv(data, output_filename):
    if not data:
        print("No data to convert.")
        return

    fieldnames = list(data[0].keys())

    with open(output_filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)



        print(f"Converted {len(data)} records to {output_filename}.")




def main():
     print("Converting JSON to CSV...")
     data = load_json_data(INPUT_FILE)
     convert_to_csv(data, OUTPUT_FILE)

if __name__ == "__main__":
    main()
