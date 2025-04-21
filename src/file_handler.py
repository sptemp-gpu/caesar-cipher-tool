# file_handler.py

def save_to_file(file_name, text):
    with open(file_name, 'w') as file:
        file.write(text)

def load_from_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()
