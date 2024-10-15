from time import time

def sum_pairs(ints, s):

    res = {}
    for dig in ints:
        if dig in res:
            return [res[dig], dig]
        res[s-dig] = dig

    return None

        


def main():

    print(sum_pairs([2, 3, 1, 4], 5))

   
    
if __name__ == "__main__":
    main()
