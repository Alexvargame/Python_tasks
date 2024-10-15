
def divisors(integer):
    if list(d for d in range(2,integer) if integer%d==0):
        return list(d for d in range(2,integer) if integer%d==0)
    return "{} is prime".format(integer)
    

def main():

    print(divisors(13))




if __name__ == "__main__":
    main()




#
