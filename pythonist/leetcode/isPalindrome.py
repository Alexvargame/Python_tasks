def isPalindrome(s):


    """
           :type s: str
           :rtype: bool
    """
    s = ''.join([l.lower() for l in s if l.isalpha()])
    print(s, s[::-1])
    if s == s[::-1]:
        return True
    return False


def main():
    print('res', isPalindrome("OP"))



if __name__ == "__main__":
    main()
