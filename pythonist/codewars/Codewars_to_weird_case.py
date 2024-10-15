def to_weird_case(words):
    res=[]  
    for w in words.split():
        new_w=''
        for i in range(len(w)):
            if i%2==0:
                new_w+=w[i].upper()
            else:
                new_w+=w[i].lower()
        res.append(new_w)
    return ' '.join(res)
def main():

    print(to_weird_case('Weird string case'))




if __name__ == "__main__":
    main()




#
