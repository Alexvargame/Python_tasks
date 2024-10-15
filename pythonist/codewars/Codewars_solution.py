def solution(number):
    print([d  for d in range(1,number) if (d%3==0 or d%5==0)])


    
def main():

    print(solution(10))

if __name__ == "__main__":
    main()

#
