import re


def count_smileys(arr):
##
##    for r in arr:
##        print(r)
##        if re.fullmatch('[:,;]~?[D,)]',r) :
##            print('R',r)

    return len([r for r in arr if re.fullmatch('[:,;][~,-]?[D,)]',r)])
def main():
    print(count_smileys([':-D',':~)',';~D',':)',';)']))




if __name__ == "__main__":
    main()




#
