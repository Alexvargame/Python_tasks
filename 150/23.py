s=input("s:",)
n=int(input("n:", ))
if len(s)>2:
    for i in range(n):
        print(s[0:2])
else:
    for i in range(n):
        print(s)
    

gl=['a','e','y','u','i','o']
if s[0] in gl:
    print("yes")
else: print("No")
def histogram( items ):
    for n in items:
        output = ''
        times = n
        while( times > 0 ):
          output +='*'
          times = times - 1
        print(output)
histogram([2, 3, 6, 5])

print(('').join(gl))

nums = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]
for x in nums:
    if x==237:
        print(x)
        break
    else:
        if x%2==0:
            print(x)
color_list_1 = set (["White", "Black", "Red"])
color_list_2 = set (["Red", "Green"])
col=[]
i=0
for i in color_list_1:
    print(i) 
    if color_list_1[i] in color_list_2:
        break
    else : col.append(i)
print(col)
        
