lst=[0,5,34,63,635,6,44,5]
if len(set(lst))==len(lst):
   print("y")
else: print("n")
lst1=['a','i','o','u','e']

def remove_nums(int_list):
  #list starts with 0 index
  position = 3 - 1 
  idx = 0
  len_list = (len(int_list))
  while len_list>0:
    idx= (position+idx)%len_list
    print(idx, int_list.pop(idx))
    len_list -= 1
nums = [10,20,30,40,50,60,70,80,90]
remove_nums(nums)

lst1=[1,-2,-3,4,3,8,9,0,0,0,1,-4,-2,-5,4]
lst2=[]
for i in range(len(lst1)):
   for j in range(len(lst1)):
      for k in range(len(lst1)):
         if lst1[i]+lst1[j]+lst1[k]==0:
            t=(lst1[i],lst1[j], lst1[k])
            lst2.append(t)
print(len(lst2))
print(lst2)
print(len(set(lst2)))
print(set(lst2))
