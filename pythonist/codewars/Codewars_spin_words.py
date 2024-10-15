def return_length(a):
    return len(a)

def sort_by_length(arr):

    return sorted(arr,key=return_length)
    

def main():

    print(sort_by_length(["Telescopes", "Glasses", "Eyes", "Monocles"]))




if __name__ == "__main__":
    main()




#
