


def create_phone_number(n):
    str_n=[str(d) for d in n]
    print (str_n,n[:3])
    print(''.join(str_n[:3]))
    return f"({''.join(str_n[:3])}) {''.join(str_n[3:6])}-{''.join(str_n[6:])}"

    
def main():
    print(create_phone_number([1, 0, 3, 9, 9, 1, 0, 4, 0, 5]))




if __name__ == "__main__":
    main()




#
