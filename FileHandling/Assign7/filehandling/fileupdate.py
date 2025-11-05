def update_file(filename, lines):
    with open(filename, "a") as f:
        f.writelines(lines)
