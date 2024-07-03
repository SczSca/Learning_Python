from pathlib import Path

#  Get the absolute path of the parent directory of the current script
base = Path(__file__).parent.parent.absolute()

#  Create a path object for the home directory
base2 = Path.home()

#  Create a path object for a specific file in the home directory
trybase = Path(base,"tr1","tr2","tr3","tr4","tr5")

# Print the relative path from the base directory to the specific file in the home directory
tr1 = trybase.relative_to(base,"tr1")
tr2 = trybase.relative_to(Path(base,"tr1","tr2"))

print(tr1)
print(tr2)



def print_py_file_paths():
    guide = Path(__file__).parent.parent.absolute()

    for py in guide.glob("*.py"):
        print(py)

    '''for py in guide.glob("**/*.py"):
        print(py)''' #prints all py files including subfolders

print_py_file_paths()