import os

def find_files_googleoauth2(root_dir):
    google_oauth2_files = []
    searched_directories = set()

    for dirpath, _, filenames in os.walk(root_dir):
        searched_directories.add(dirpath)  # Add the current directory to the set
        for filename in filenames:
            if filename.endswith('.py'):
                file_path = os.path.join(dirpath, filename)
                with open(file_path, mode='r', encoding='utf-8') as file:
                    content = file.read()
                    if "google.oauth2" in content:
                        google_oauth2_files.append(file_path)

    # Prints the searched directories
    print("Directories searched:")
    for directory in searched_directories:
        print(directory)

    # If no files are found
    if not google_oauth2_files:
        print("No files using google.oauth2 library were found.")

    return google_oauth2_files

if __name__ == "__main__":
    root_directory = "/Users/jadenlaborete/PycharmProjects/storyline"  # Replace this with the actual root directory
    files_with_oauth2 = find_files_googleoauth2(root_directory)

    if files_with_oauth2:
        print("Files using google.oauth2 library:")
        for file_path in files_with_oauth2:
            print(file_path)
