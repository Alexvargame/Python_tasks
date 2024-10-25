class Arab_Rome():
    def __init__(self, number):
        self.number=number
    def list_(self):
        li=[]
        num=self.number
        while num>0:
            li.append(num%10)
            num=num//10    
        return li
    def convert(self, li):
        l=[]
        ch_=['I','V','X','X','X']
        
        for i in range(len(li)):
            print(li[i])
            if li[i]<4:
                l.append(ch_[i]*li[i])
            elif li[i]==4:
                l.append(ch_[i]+ch_[i+1])
            elif li[i]==5:
                l.append(ch_[i+1])
            elif 5<li[i]<9:
                l.append(ch_[i+1]+ch_[i]*(li[i]-5))
            else:
                l.append(ch_[i]+ch_[i+2])
        print(l)      
        print((('').join(l[::-1])))
a=Arab_Rome(11)
print(a.list_())
a.convert(a.list_())
class py_solution:
    def int_to_Roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                print(i, roman_num, num, val[i])
                roman_num += syb[i]
                num -= val[i]
                print(roman_num, num, val[i])
                print()
            i += 1
        return roman_num
#print(py_solution().int_to_Roman(1))
print(py_solution().int_to_Roman(151))
class py_solution:
    def roman_to_int(self, s):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            print(i, s[i],rom_val[s[i]])
            input()
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]
        return int_val
#print(py_solution().roman_to_int('MMMCMLXXXVI'))
#print(py_solution().roman_to_int('MMMM'))
print(py_solution().roman_to_int('XIV'))
