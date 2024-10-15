def parts_sums(ls):
    
    print([sum(ls)-ls[i] for i in range(len(ls))])
    result=[sum(ls)]
    for i in range(len(ls)):
        
        result.append(result[i]-ls[i])
        
    print(result)
    return [sum(ls[i:]) for i in range(len(ls))]+[0]

def main():
    print(parts_sums([0, 1, 3, 6, 10]))




if __name__ == "__main__":
    main()




#
