def clean_string(s):
    ind=len(s)-s[::-1].find('#')
    print(s[ind:])
    res=''
    res=s[:s.find('#')]
    print(res)
    for l in s[s.find('#'):]:
        if l!='#':
            res+=l
        else:
            res=res[:-1]
    return res
        


def main():
    print(clean_string('abc#d###c'))
    

if __name__ == "__main__":
    main()

#
