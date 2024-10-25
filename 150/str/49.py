def first_repeated_char(str1):
  for index,c in enumerate(str1):
    if str1[:index+1].count(c) > 1:
      return c
  return "None"
print(first_repeated_char("abcdabcd"))
print(first_repeated_char("abcd"))

print("---------------")
def first_repeated_char(str1):
  l=[]
  j=0
  for index,c in enumerate(str1):
    if str1[:index+1].count(c) > 1:
      l.append(index)
  return str1[l[0]]
  print(l)
#print(first_repeated_char("abcdabcd"))
print(first_repeated_char("abcdbad"))
print("---------------")

def first_repeated_word(str1):
  l_str=str1.split(" ")
  for index,c in enumerate(l_str):
    if l_str[:index+1].count(c) > 1:
      return c
  return "None"
print(first_repeated_word("ab ecd ab rrcd"))
print(first_repeated_word("e a b c d e"))

print("---------------")

def first_repeated_word1(str1):
  l=[]
  l_str=str1.split(" ")
  for index,c in enumerate(l_str):
    if l_str[:index+1].count(c) > 1:
      l.append(index)
  if len(l)>1:
      return  l_str[l[1]]
print(first_repeated_word1("ab ecd ab r ecd"))
print(first_repeated_word1("e a b c d e"))

print("----------")

def del_pass(str1):
  l_str=str1.split(" ")
  return ('*')*len(l_str)+('').join(l_str)
print(del_pass("ab ecd ab r ecd"))
print(del_pass("e a b c d e"))

print("---------------")
def first_repeated_char(str1):
  l=()
  cnt=0
  for index,c in enumerate(str1):
    if str1[:index+1].count(c) > cnt:
        cnt=str1[:index+1].count(c)
        t=((c, cnt))
  return t
#print(first_repeated_char("abcdabcd"))
print(first_repeated_char("abcdbaddd"))

print(" ------------")
def first_repeated_char(str1):
  l=[]
  cnt=0
  for index,c in enumerate(str1):
    if str1[:index+1].count(c) > 1:
        pass
    else: l.append(c)
  return ('').join(l)
#print(first_repeated_char("abcdabcd"))
print(first_repeated_char("abcdbaddd"))

print(" ------------")
def first_repeated_char(str1):
  l=[]
  l1=[]
  cnt=0
  for index,c in enumerate(str1):
    if str1.count(c) == 1: 
        l1.append(c)
    elif str1[:index+1].count(c) > 1:
        pass
    else: l.append(c)
  return ('').join(l), ('').join(l1)
#print(first_repeated_char("abcdabcd"))
print(first_repeated_char("abedcdbaddd"))

print("----------------")

def part_str(str1, str2):
    l=[]
    for i in range(len(str2)):
        l.append(str1.find(str2[i]))
    return str1[min(l):max(l)+1]
print(part_str("gdahklghhsk", "shl"))
print("-------------")
def part_str(str1):
    ll=list(str1)
    l=[]
    for i in ll:
        l.append(str1.find(i))
    print(l)
    return str1[min(l):max(l)+1]
print(part_str("gdkahsklghhskhhhhhh"))
    
