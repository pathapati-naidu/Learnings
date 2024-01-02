import os.path
import shutil
text_file='practise.txt'
file_creation = "samp2.txt"
if not os.path.isfile(file_creation):
    with open(file_creation, 'x') as file:
        file = file.write("")

copy_file=shutil.copyfile(src="C:\\Users\prmah\OneDrive\Desktop\\Python\\PYTHON-LEARNINGS\\ReactProject\\Python_Learnings\\Object_oriented\\text.csv",dst="samp.txt")
copy = shutil.copy(
    src="C:\\Users\prmah\OneDrive\Desktop\\Python\\PYTHON-LEARNINGS\\ReactProject\\Python_Learnings\\Object_oriented\\text.csv",
    dst="samp2.txt")
copy2 = shutil.copy2(
    src="practise.txt",
    dst="samp1.txt")
meta_data=os.stat(copy2)
print(meta_data)