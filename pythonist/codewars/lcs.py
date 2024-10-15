

def lcs(x,y):
    for i in x:
        print('i',i)
        print('index',y.index(i))
        if y.index(i):
            print(i)



def main():

    print(lcs( "132535365", "123456789"))

    
if __name__ == "__main__":
    main()





