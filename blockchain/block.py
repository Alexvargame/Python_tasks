import json
import os
import hashlib

blockchain_dir=os.curdir+'/blockchain/'

def get_hash(filename):
  
    file=open(blockchain_dir+filename, 'rb').read()
    
    return hashlib.md5(file).hexdigest()

def get_files():
    files=os.listdir(blockchain_dir)
    return sorted([int(i) for i in files])
    
def check_integrity():
  
    files=get_files()
    for file in files[1:]:
        h=json.load(open(blockchain_dir+str(file)))['hash']
        prev_file=str(file-1)
        actual_hash=get_hash(prev_file)
        
        if actual_hash==h:
            res='Ok'
        else:
            res="Not"
        print('block {} is {}'.format(prev_file, res))
            
    
def write_block(name,amount, to_whom, prev_hash=''):
    files=get_files()
    prev_file=files[-1]
    filename=str(last_file+1)

    prev_hash=get_hash(str(prev_file))

    data={'name':name,
          'amount':amount,
          'to_whom':to_whom,
          'hash':prev_hash
          }
    with open(blockchain_dir+filename,'w') as file:
        json.dump(data,file, indent=4,ensure_ascii=False)

def main():
    #write_block('oleg','4','ksu')
    check_integrity()


if __name__=='__main__':
    main()
