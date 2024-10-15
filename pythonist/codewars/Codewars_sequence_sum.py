
def sequence_sum(begin_number, end_number, step):
    return sum(i for i in range(begin_number,end_number+1,step))



def main():
    print(sequence_sum(2,6,2))


       
if __name__ == "__main__":
    main()
