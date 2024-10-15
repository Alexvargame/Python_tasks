def longest_palindrome(s):
    j=0
    res=''
    for i in range(int(len(s)/2)+1):
        tmp=s[j:i+1]
        print(tmp,'l',len(tmp),i+1-j,'r',s[i+1:2*i+3-j][:-1])
        if tmp==s[i+1:i+3][:-1]:
            if len(tmp)>len(res):
                res=tmp
    return res


def main():
    print(longest_palindrome('bbbad'))
    #print(longest_palindrome('babad'))




if __name__ == "__main__":
    main()




#
