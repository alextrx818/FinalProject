import json
import pandas as pd
import os
from datetime import datetime

# Define input file path
input_file = "paste_json_here.txt"

def json_to_spreadsheet():
    print(f"📌 Reading JSON from `{input_file}`...")

    # Read JSON from the text file
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            # Skip the first line (comment)
            file.readline()
            raw_json = file.read()
    except FileNotFoundError:
        print(f"❌ Error: `{input_file}` not found! Create the file and paste your JSON inside it.")
        return

    # Convert JSON string to Python dictionary
    try:
        data = json.loads(raw_json)
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON format. Details: {str(e)}")
        return

    # If JSON is a single dictionary, convert it to a list
    if isinstance(data, dict):
        data = [data]

    # Extract all unique field names (including unknown ones)
    all_fields = set()
    for item in data:
        all_fields.update(item.keys())

    # Convert set to sorted list for consistent column order
    all_fields = sorted(all_fields)

    # Process data dynamically
    rows = []
    for item in data:
        row_data = {field: item.get(field, "") for field in all_fields}
        rows.append(row_data)

    # Convert to DataFrame
    df = pd.DataFrame(rows)

    # Define output directory
    save_path = os.path.expanduser("~/output")
    os.makedirs(save_path, exist_ok=True)

    # Generate timestamped filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Ask user for file format
    print("\n📌 Choose file format: 1 = Excel (.xlsx), 2 = CSV (.csv)")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        filename = os.path.join(save_path, f"json_table_{timestamp}.xlsx")
        df.to_excel(filename, index=False)
    elif choice == "2":
        filename = os.path.join(save_path, f"json_table_{timestamp}.csv")
        df.to_csv(filename, index=False)
    else:
        print("❌ Invalid choice. Defaulting to CSV format.")
        filename = os.path.join(save_path, f"json_table_{timestamp}.csv")
        df.to_csv(filename, index=False)

    print(f"\n✅ Success! Your JSON data has been saved as **{filename}**")
    print("📂 To download the file:")
    print("   1. Open VS Code Explorer (Remote SSH)")
    print("   2. Navigate to: ~/output/")
    print("   3. Right-click on the file")
    print("   4. Select 'Download'")

if __name__ == '__main__':
    json_to_spreadsheet()
