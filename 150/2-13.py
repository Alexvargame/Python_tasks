string_maps = {
"1": "abc",
"2": "def",
"3": "Гхи",
"4": "JKL",
"5": "мно",
"6": "pqrs",
"7": "tuv",
"8": "wxy",
"9": "z"
}
lst1=[]
lst2=[]
for v in string_maps.values():
   lst1.append(v)
print(lst1)
for i in range(len(lst1)):
   for j in range(len(lst1)):
            t=(lst1[i],lst1[j])
            lst2.append(t)
print(len(lst2))
print(lst2)
print(len(set(lst2)))
print(set(lst2))

n=int(input("n:", ))
nums=[]
for n in range(10, 10**n):
   if(list(str(n))==list(str(n))[::-1]):
      nums.append(n)
print(set(nums))

def gen_strobogrammatic(n):
    """
    :type n: int
    :rtype: List[str]
    """
    result = helper(n, n)
    return result
def helper(n, length):
    if n == 0:
        return [""]
    if n == 1:
        return ["1", "0", "8"]
    middles = helper(n-2, length)
    result = []
    for middle in middles:
        if n != length:
            result.append("0" + middle + "0")
        result.append("8" + middle + "8")
        result.append("1" + middle + "1")
        result.append("9" + middle + "6")
        result.append("6" + middle + "9")
    return result
print("n = 2: \n",gen_strobogrammatic(2))
print("n = 3: \n",gen_strobogrammatic(3))
print("n = 4: \n",gen_strobogrammatic(4))


n1=int(input("n1:", ))

def lists(n1):
   lsts=[1,1,1,1]
   for i in range(4, n1+1):
      new=lsts[i-4]+lsts[i-3]+lsts[i-2]+lsts[i-1]
      lsts.append(new)
   return(lsts[n1])
print(lists(n1))
