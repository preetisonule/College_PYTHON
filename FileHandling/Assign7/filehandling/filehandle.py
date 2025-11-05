def file_exists(filename):
    try:
        with open(filename, "r"):
            return True
    except FileNotFoundError:
        return False
