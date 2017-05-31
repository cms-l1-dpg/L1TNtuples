import os

fname='file_list.txt'

with open(fname) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 

for line in content:
 os.system('bsub -q 1nd ' + os.getcwd() + '/bjob_launch.sh l1Ntuple_nano.py ' + os.getcwd() + ' ' + os.path.dirname(line) + '/ ' + os.path.basename(line) + ' ' + ' L1Ntuple_' + os.path.splitext(os.path.basename(line))[0]+'.root ' )

