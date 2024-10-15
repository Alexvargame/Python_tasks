import io
import os
import os.path
import glob


with open('base.txt','rt') as f:
    for line in f:
        pass

s=io.StringIO()
print(s.write('Hello\n'))
s=io.StringIO('HEllo')
print(s.read(2))
print(s.read(1))

pyfiles=glob.glob('*.py')

name_sz_date=[(name,os.path.getsize(name),os.path.getmtime(name)) for name in pyfiles]
print(name_sz_date)

if __name__ == '__main__':

    pass
