from functools import reduce


def dirReduc(arr):
    alst=[['WEST','EAST'],['NORTH','SOUTH']]
    j=len(arr)-2
    while j>0:
        print('J',j)
        for i in range(len(arr)):
            change=0
            print("i",i)
            print(arr[i:i+2],list(reversed(arr[i:i+2])) )
            print(arr)
            if arr[i:i+2] in alst or list(reversed(arr[i:i+2])) in alst:
                print(arr[i])
                arr.remove(arr[i])
                print(arr[i])
                arr.remove(arr[i])
                print(arr,i)
                input()
        j=j-1
        
    return arr
        

def re(arr):
    ad={}
    for a in arr:
        key, value=a,arr.count(a)
        ad[key]=value
    if 'NORTH' in ad.keys() and 'SOUTH' in ad.keys():
        ad['NORTH'],ad['SOUTH']= ad['NORTH']-min( ad['NORTH'],ad['SOUTH']),ad['SOUTH']-min( ad['NORTH'],ad['SOUTH'])
    if 'WEST' in ad.keys() and 'EAST' in ad.keys():
        ad['WEST'],ad['EAST']= ad['WEST']-min( ad['EAST'],ad['WEST']),ad['EAST']-min( ad['WEST'],ad['EAST'])
    return [item for sublist in [[key]*ad[key] for key in ad.keys() if ad[key]>0] for item in sublist]
def main():

##    print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
##    print(dirReduc([ "SOUTH","NORTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
##    print(dirReduc([ "EAST", "SOUTH","NORTH", "WEST", "NORTH", "WEST"]))
##    print(dirReduc([ 'NORTH', 'NORTH', 'WEST', 'EAST']))

    print(re(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
    print(re(['NORTH', 'WEST', 'SOUTH', 'EAST']))
    print(re([ "EAST", "SOUTH","NORTH", "WEST", "NORTH", "WEST"]))
    print(re([ 'NORTH', 'NORTH', 'WEST', 'EAST']))
      
    
if __name__ == "__main__":
    main()


##    print(cakes({'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}))
##    print(cakes({'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}, {'sugar': 500, 'flour': 2000, 'milk': 2000}))
##
##def cakes(recipe, avaliable):
##    l=[]
##    for key,value in recipe.items():
##        if key in avaliable.keys():
##            l.append(avaliable[key]//value)
##        else:
##            return 0
##    return min(l)
##
##    
##
##
##    print(permutations('aabb'))
##    print(same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] ))
##    print(same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] ))
##    print(same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] ))
##    print(same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] ))
##    print(same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] ))
##    
##   
 ##def permutations(s):
##    
##    
##    return reduce(lambda x,y,z,r:x+y+z+r,s.split())
##
##def same_structure_as(l1,l2):
##
##    def eq(x,y):
##        print(x,y,type(x),type(y))
##        return type(x)==type(y)
##    l=list(map(lambda x,y: eq(x,y),l1,l2))
##    return l

    
##def remov_nb(n):
##    res=[]
##    
##    for i in range(n+1):
##        for j in range(i+1,n+1):
##         
##            if (0+i)/2*(i+1-0)-i+(i+j+1)/2*(j-i)-j+(j+1+n)/2*(n+1-j-1)==i*j:
##                res.append([i,j])
##                res.append([j,i])
##    return res
##                
##    
