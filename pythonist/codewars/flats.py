def flats_cost(N,M,X):
    return sum([(X+i*1000)*M for i in range(N//M)])+(X+(N//M)*1000)*(N%M)


    
def main():

    print(flats_cost(21,5,500))

if __name__ == "__main__":
    main()

#
