import os


def write_to_file(path: str) -> bool:
    if os.path.isfile(path):
        with open(path, 'w') as file:
            file.write("Kilroy was here!")
        return True
    else:
        return False




