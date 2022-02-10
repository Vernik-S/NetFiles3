import os
class File_Sort:
    def __init__(self, file_name, file_content):
        self.file_name = file_name
        self.content = file_content

    def __len__(self):
        return len(self.content.split("\n"))

    def __lt__(self, other):
        return len(self) < len(other)


jedi_path = os.getcwd()
jedi_path += "/files_for_sort/"
files = os.listdir(jedi_path)
keyword = 'your_keyword'
files_for_sort = []
for file in files:
    if os.path.isfile(os.path.join(jedi_path, file)):
        with open(os.path.join(jedi_path, file),'r', encoding="utf-8") as f:
            #new_file = File_Sort(file, f.readlines())
            new_file = File_Sort(file, f.read())
            files_for_sort.append(new_file)

#print(files_for_sort)

with open(os.path.join(os.getcwd(), "res.txt"), "w", encoding="utf-8") as f:
    for file in sorted(files_for_sort):
        f.write(file.file_name + "\n")
        f.write(str(len(file)) + "\n")
        f.write(file.content + "\n")