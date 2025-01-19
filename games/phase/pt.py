import os
import json

def get_folder_paths():
    # Get the current directory
    current_path = os.getcwd()
    
    # Get only immediate directories (no recursion)
    dirs = [d for d in os.listdir(current_path) if os.path.isdir(os.path.join(current_path, d))]
    
    # Create formatted paths
    folder_paths = [{"path": f"games/phase/{dir_name}/index.html"} for dir_name in dirs]
    
    # Write to JSON file
    with open('folder_paths.json', 'w', encoding='utf-8') as f:
        json.dump(folder_paths, f, indent=4)
    
    return folder_paths

# Run the function and print results
if __name__ == "__main__":
    paths = get_folder_paths()
    print("Generated paths:")
    print(json.dumps(paths, indent=4))