import json
import sys

def pretty_print_json():
    print("📌 Paste your raw JSON data below and press Enter, then Ctrl+D (Linux/macOS) or Ctrl+Z (Windows) to finish:")

    # Read JSON input from user
    raw_json = ""
    while True:
        try:
            line = input()
            raw_json += line + "\n"
        except EOFError:
            break

    try:
        # Parse JSON and print it with nice formatting
        data = json.loads(raw_json)
        formatted_json = json.dumps(data, indent=2, sort_keys=True)
        print("\n✨ Formatted JSON:")
        print(formatted_json)
        
        # Also save to file
        with open('formatted_json.txt', 'w') as f:
            f.write(formatted_json)
        print("\n✅ Formatted JSON also saved to 'formatted_json.txt'")
        
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON format. Details: {str(e)}")

if __name__ == '__main__':
    pretty_print_json()
