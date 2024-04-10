import subprocess

def backup_directory(source_dir, destination):
    try:
        subprocess.run(['rsync', '-avz', source_dir, destination])
        return "Backup successful!"
    except subprocess.CalledProcessError as e:
        return f"Backup failed with error: {e}"

if __name__ == "__main__":
    source_directory = input("Enter the directory to backup: ")

    destination_directory = input("Enter the destination directory: ")

    result = backup_directory(source_directory, destination_directory)
    print(result)
