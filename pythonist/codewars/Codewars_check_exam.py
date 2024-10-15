def check_exam(arr1,arr2):

    return sum([4 if a[0]==a[1] else -1 for a in list(zip(arr1,arr2)) if a[1]!='' and a[0]!=''])



def main():
    print(check_exam(["a", "a", "b", ""], ["a", "c", "b", "d"]))




if __name__ == "__main__":
    main()




#
