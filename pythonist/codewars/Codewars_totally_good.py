
from itertools import permutations

def valid_str(item,bads):
    for st in bads:
        if st in ''.join(list(item)):

            return False
    return True

def totally_good(alphabet, bads):
    return len([item for item in permutations(alphabet,len(alphabet)) if valid_str(item,bads)])
        
def main():
    print(totally_good('ABCDEFGHI',['AB','CD','EFGH','BC','FG','BH','ABCDE','DAC','ADG','IFBC']))
    totally_good('ABCD',[])
    totally_good('ABCDE',[])
    totally_good('ABCD',['AB'])
    totally_good('ABCD',['BA'])
    totally_good('ABCD',['A'])
    totally_good('ABC',['AB','CA'])

    

    
if __name__ == "__main__":
    main()




#
