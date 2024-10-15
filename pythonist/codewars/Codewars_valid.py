

def valid(s):

    if len(s)<6:
        return False
    if not any([True for r in s if r.islower()]):
        return False
    if not any([True for r in s if r.isupper()]):
        return False
    if not any([True for r in s if r.isdigit()]):
        return False
    if not any([True for r in s if r.isalpha()]):
        return False
    return True


def main():
    

    print(valid("fjd3IR9"))


 
if __name__ == "__main__":
    main()


###
