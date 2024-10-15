def plusOne(digits):
     """
        :type digits: List[int]
        :rtype: List[int]
     """
     print(''.join([str(d) for d in digits]))
     import itertools
     print(list(itertools.zip_longest('122','1', fillvalue=0)))
     number = int(''.join([str(d) for d in digits]))+1
     lst_number = list(str(number))
     lst_number = [int(l) for l in lst_number]
     return lst_number

def main():
    print('res', plusOne([1, 2, 3]))



if __name__ == "__main__":
    main()
