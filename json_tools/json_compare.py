import json
import sys
from deepdiff import DeepDiff

def compare_json():
    print("📌 Paste your FIRST JSON data below and press Enter, then Ctrl+D (Linux/macOS) or Ctrl+Z (Windows) to finish:")

    # Read first JSON
    json1 = ""
    while True:
        try:
            line = input()
            json1 += line + "\n"
        except EOFError:
            break
            
    print("\n📌 Now paste your SECOND JSON data and press Ctrl+D (Linux/macOS) or Ctrl+Z (Windows) when done:")
    
    # Read second JSON
    json2 = ""
    while True:
        try:
            line = input()
            json2 += line + "\n"
        except EOFError:
            break

    try:
        # Parse both JSONs
        data1 = json.loads(json1)
        data2 = json.loads(json2)
        
        # Compare using deepdiff
        diff = DeepDiff(data1, data2, verbose_level=2)
        
        if diff:
            print("\n🔍 Differences found:")
            print(json.dumps(diff, indent=2))
        else:
            print("\n✅ The JSON objects are identical!")
            
        # Save comparison to file
        with open('json_comparison.txt', 'w') as f:
            if diff:
                f.write("JSON Comparison Results:\n\n")
                f.write(json.dumps(diff, indent=2))
            else:
                f.write("The JSON objects are identical!")
                
        print("\n✅ Comparison results saved to 'json_comparison.txt'")
        
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON format. Details: {str(e)}")

if __name__ == '__main__':
    compare_json()
