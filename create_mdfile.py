import os

def read_file_names(file_path):
    """
    Reads file names from a .txt file where each file name is on a new line.

    :param file_path: Path to the .txt file
    :return: List of unique file names
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        # Use a set to ensure uniqueness, then convert to a list
        file_names = list(set(line.strip() for line in file if line.strip()))
    
    return file_names

def create_md_files(file_names, output_folder):
    """
    Creates a .md file for each unique name in the list.

    :param file_names: List of file names
    :param output_folder: Folder where .md files will be created
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for name in file_names:
        # Ensure the file name is safe for the file system
        safe_name = "".join(c for c in name if c.isalnum() or c in (" ", "-", "_")).strip()
        file_path = os.path.join(output_folder, f"{safe_name}.md")
        if os.path.exists(file_path):
            print(f"Skipping duplicate: {file_path}")
            continue  # Skip creating the file if it already exists
        with open(file_path, 'w', encoding='utf-8') as md_file:
            md_file.write(f"# {safe_name}\n\n")  # Write a title header to the .md file
        print(f"Created: {file_path}")

if __name__ == "__main__":
    txt_file_path = input("Enter the path to the .txt file containing file names: ").strip()
    output_folder = input("Enter the path to the output folder for .md files: ").strip()
    
    try:
        file_names = read_file_names(txt_file_path)
        print("Creating .md files...")
        create_md_files(file_names, output_folder)
        print("All .md files created successfully! No duplicates.")
    except Exception as e:
        print(f"An error occurred: {e}")
