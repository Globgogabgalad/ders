import os

def list_files():
    files = os.listdir()
    for item in files:
        print(item)

def change_directory(path):
    try:
        os.chdir(path)
        print(f"Changed directory to: {os.getcwd()}")
    except FileNotFoundError:
        print(f"Directory '{path}' not found.")
    except PermissionError:
        print(f"Permission denied: '{path}'.")

def remove_file(filename):
    try:
        os.remove(filename)
        print(f"Removed file: {filename}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except PermissionError:
        print(f"Permission denied: Unable to remove '{filename}'.")

def make_directory(dirname):
    try:
        os.mkdir(dirname)
        print(f"Created directory: {dirname}")
    except FileExistsError:
        print(f"Directory '{dirname}' already exists.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{dirname}'.")

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Contents of {filename}:")
            print(content)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except IsADirectoryError:
        print(f"{filename} is a directory, not a file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def convert_to_txt(source_file, target_file):
    try:
        with open(source_file, 'r') as src, open(target_file, 'w') as tgt:
            content = src.read()
            tgt.write(content)
        print(f"Converted '{source_file}' to '{target_file}'.")
    except FileNotFoundError:
        print(f"File '{source_file}' not found.")
    except Exception as e:
        print(f"An error occurred during conversion: {e}")

def convert_format(source_file, target_format):
    target_file = f"{os.path.splitext(source_file)[0]}.{target_format}"
    try:
        with open(source_file, 'r') as src, open(target_file, 'w') as tgt:
            content = src.read()
            tgt.write(content)  # Here you can modify the content for the specific format if needed
        print(f"Converted '{source_file}' to '{target_file}'.")
    except FileNotFoundError:
        print(f"File '{source_file}' not found.")
    except Exception as e:
        print(f"An error occurred during conversion: {e}")

def format_converter(format, source_file):
    valid_formats = ['java', 'py', 'php', 'cpp', 'html']
    if format not in valid_formats:
        print("Unsupported format. Use 'java', 'py', 'php', 'cpp', or 'html'.")
        return
    
    convert_format(source_file, format)

def make_txt(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Created file '{filename}' with specified content.")
    except Exception as e:
        print(f"An error occurred while creating '{filename}': {e}")

def show_help():
    commands = [
        "ls        - List files in the current directory",
        "cd <dir>  - Change to directory <dir>",
        "rm <file> - Remove file <file>",
        "mkdir <dir> - Create directory <dir>",
        "txt <file> - Read contents of <file>",
        "format <format> <file> - Convert <file> to the specified format (java, py, php, cpp, html)",
        "maketxt <filename> <content> - Create a new .txt file with specified content",
        "help      - Show this help message",
        "exit      - Exit the file explorer"
    ]
    print("Available commands:")
    for command in commands:
        print(command)

def main():
    while True:
        command = input(f"{os.getcwd()} > ").strip().lower().split()
        if not command:
            continue
        cmd = command[0]

        if cmd == 'ls':
            list_files()
        elif cmd == 'cd':
            if len(command) > 1:
                change_directory(command[1])
            else:
                print("Usage: cd <directory>")
        elif cmd == 'rm':
            if len(command) > 1:
                remove_file(command[1])
            else:
                print("Usage: rm <filename>")
        elif cmd == 'mkdir':
            if len(command) > 1:
                make_directory(command[1])
            else:
                print("Usage: mkdir <directory_name>")
        elif cmd == 'txt':
            if len(command) > 1:
                read_file(command[1])
            else:
                print("Usage: txt <filename>")
        elif cmd == 'format':
            if len(command) > 2:
                format_converter(command[1], command[2])
            else:
                print("Usage: format <format> <filename>")
        elif cmd == 'maketxt':
            if len(command) > 2:
                filename = command[1]
                content = ' '.join(command[2:])  # Join the remaining parts as content
                make_txt(filename, content)
            else:
                print("Usage: maketxt <filename> <content>")
        elif cmd == 'help':
            show_help()
        elif cmd == 'exit':
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
