import os

def fetch_file_names_recursive(folder_path):
    """
    Fetches file names from a folder and its subfolders, removes file extensions, and returns a list of clean file names.

    :param folder_path: Path to the folder containing files
    :return: List of file names without extensions
    """
    # List to store clean file names
    clean_file_names = []
    
    # Walk through the directory tree
    for root, _, files in os.walk(folder_path):
        for file in files:
            # Remove the file extension and append to the list
            clean_file_names.append(os.path.splitext(file)[0])
    
    return clean_file_names

# Example usage
if __name__ == "__main__":
    folder_path = input("Enter the path to the folder: ").strip()
    try:
        clean_names = fetch_file_names_recursive(folder_path)
        print("Clean file names (including subfolders):")
        for name in clean_names:
            print(name)
    except Exception as e:
        print(f"An error occurred: {e}")
