from pathlib import Path

def write_file(file_name, file_content):
    # Convert file_name to a Path object if it's not already one
    file_path = Path(file_name)
    
    # Ensure the file name has a .txt extension
    if file_path.suffix != '.txt':
        file_path = file_path.with_suffix('.txt')
    
    # Open the file in write mode and write the content
    with open(file_path, 'w') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    # Convert file_name to a Path object if it's not already one
    file_path = Path(file_name)
    
    # Ensure the file name has a .txt extension
    if file_path.suffix != '.txt':
        file_path = file_path.with_suffix('.txt')
    
    # Open the file in append mode and append the content
    with open(file_path, 'a') as file:
        file.write(append_content)

def read_file(file_name):
    # Convert file_name to a Path object if it's not already one
    file_path = Path(file_name)
    
    # Ensure the file name has a .txt extension
    if file_path.suffix != '.txt':
        file_path = file_path.with_suffix('.txt')
    
    # Open the file in read mode and return the content
    with open(file_path, 'r') as file:
        return file.read()