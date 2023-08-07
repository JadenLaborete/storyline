import os

#This function takes a parameter of root_dir to search for python files within the direcotry
def find_files_googleoauth2(root_dir):
    '''
     to search for Python files within a specified directory (root_dir)
     and its subdirectories that use the google.oauth2 library.

    :param root_dir:
    :return:
    '''
    #Creates an empty list to hold the google files
    google_oauth2_files = []

    for dirpath, _, filenames in os.walk(root_dir): # uses os.walk to iterate through the directory path and the file names
        for filename in filenames: # nested for loop with the placeholder variable 'filename' to check through the filenames in the directory
            if filename.endswith(',py'):
                file_path = os.path.join(dirpath, filename)
                with open(file_path, mode= 'r', encoding= 'utf-8') as file:
                    content = file.read()
                    if "google.oauth2" in content:
                        google_oauth2_files.append(file_path)

    return google_oauth2_files

if __name__ == "__main__":
    root_directory = ""  # Replace this with the actual root directory
    files_with_oauth2 = find_files_googleoauth2(root_directory)

    if files_with_oauth2:
        print("Files using google.oauth2 library:")
        for file_path in files_with_oauth2:
            print(file_path)
    else:
        print("No files using google.oauth2 library were found.")
