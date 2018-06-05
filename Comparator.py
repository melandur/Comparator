import os

# Set the paths to the folders
path1 = 'C:/Users/CorePy/Desktop/train1/'
path2 = 'C:/Users/CorePy/Desktop/test1/'

try:
     # Check folders
     folder1 = os.listdir(str(path1))
     folder2 = os.listdir(str(path2))
     redundent_files = set(folder1) & set(folder2)

     if len(redundent_files) > 0:
          print(str(len(redundent_files)) + " redundant files detected!")
          for elem in redundent_files:
               print(" - " + elem)

except:
     print("No redundancy detected")

