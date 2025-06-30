import json
import yaml


def main():
    # Example prompt blocks structure
    prompt_blocks = {
        "intro": "You are a helpful assistant.",
        "task": "Summarize the following article in three bullet points."
    }
    
    # --- Save to JSON ---
    with open("blocks.json", "w") as fp:
        json.dump(prompt_blocks, fp, indent=2)
    
    # --- Load from JSON ---
    with open("blocks.json") as fp:
        json_lib = json.load(fp)
    
    # --- Save to YAML ---
    with open("blocks.yaml", "w") as fp:
        yaml.safe_dump(prompt_blocks, fp)
    
    # --- Load from YAML ---
    with open("blocks.yaml") as fp:
        yaml_lib = yaml.safe_load(fp)
    
    print("JSON blocks:", json_lib)
    print("YAML blocks:", yaml_lib)

if __name__=="main":
    main()
