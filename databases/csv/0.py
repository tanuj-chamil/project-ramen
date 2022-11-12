from os import listdir
from os.path import isfile, join
mypath= 'E:\Academic\Semester 05\Charaterization\codebase\project-ramen\databases\csv'
files = [f for f in listdir(mypath) if isfile(join(mypath, f))][1:]

for f in files:
    _ = open(f,'r')
    content = 'L,I\n'+_.read()
    _.close()
    
    _ = open(f,'w')
    _.write(content)
    _.close()
