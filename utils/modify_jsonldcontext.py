import json
import sys

def modify_jsonld_category(input_file: str):
    """Modify the JSON-LD context to update 'category' to '@type' and save in-place."""
    try:
        # Load the JSON-LD context from file
        with open(input_file, "r", encoding="utf-8") as f:
            jsonld_data = json.load(f)
        
        # Modify the 'category' field
        if "@context" in jsonld_data and "category" in jsonld_data["@context"]:
            jsonld_data["@context"]["category"] = "@type"
        else:
            print("Error: 'category' field not found in JSON-LD context.")
        
        # Write the modified JSON-LD back to the same file
        with open(input_file, "w", encoding="utf-8") as f:
            json.dump(jsonld_data, f, indent=3)
        
        print(f"Updated JSON-LD context saved to {input_file}")
    except Exception as e:
        print(f"Error processing JSON-LD: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python modify_jsonld.py <json_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    modify_jsonld_category(input_file)
