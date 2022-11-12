from os import listdir
from os.path import isfile, join
mypath= 'E:\Academic\Semester 05\Charaterization\codebase\project-ramen\databases\csv'
files = [f for f in listdir(mypath) if isfile(join(mypath, f))][1:]

f =  open('filenames.txt','w')
f.write(",".join(files))
f.close()

