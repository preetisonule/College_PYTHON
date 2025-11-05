from filehandling.fileread import read_file
from filehandling.filewrite import write_file
from filehandling.fileupdate import update_file
from filehandling.filehandle import file_exists

# Input file names
file1 = "filehandling/file1.txt"
file2 = "filehandling/file2.txt"
file3 = "filehandling/file3.txt"   # final file
file4 = "filehandling/file4.txt"

# Step 1: Check if files exist
for f in [file1, file2, file4]:
    if not file_exists(f):
        print(f"Error: {f} not found!")
        exit()

# Step 2: Read from file1 and file2
content1 = read_file(file1)
content2 = read_file(file2)

write_file(file3, content1 + content2)

content4 = read_file(file4)

file3_content = read_file(file3)

first_10 = file3_content[:10]
rest = file3_content[10:]

new_content = first_10 + content4 + rest

write_file(file3, new_content)

print("File3 created successfully with merged content!")
