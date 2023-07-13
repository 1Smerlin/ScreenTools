import os


def list_directory_contents(directory_path):
    try:
        file_list = os.listdir(directory_path)
        return file_list
    except FileNotFoundError:
        print(f"Das Verzeichnis {directory_path} wurde nicht gefunden.")
        return []


# Aktuelles Verzeichnis, ändern Sie dies, um ein anderes Verzeichnis auszulesen
directory_path = '.we'
contents = list_directory_contents(directory_path)

print(f"Inhalt des Verzeichnisses {directory_path}:")
for item in contents:
    print(item)
print(contents)
