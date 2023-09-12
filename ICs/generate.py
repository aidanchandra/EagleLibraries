import os

# List all files in the current directory
for filename in os.listdir('.'):
    print("|  ICs | [%s](ICs/%s) | ABCDEFG |"%(filename,filename))