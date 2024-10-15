


def dirReduc(arr):
    if len(arr)<1 :
        return []
    ad={}
    res=arr.copy()
    direct={'NORTH':'SOUTH', 'SOUTH':'NORTH','EAST':'WEST','WEST':'EAST'}
    print("B",arr)
    #for i in range(1,len(arr)):
    i=1
    while i<len(arr):
        print('I',i, len(arr))
        
        print(arr[i-1],arr[i],direct[arr[i-1]])
        if arr[i]==direct[arr[i-1]]:
            arr.pop(i-1)
            arr.pop(i-1)
            print(arr)
            if i<3:
                i=1
            else:
                i-=2
        else:
            
            i+=1
        if len(arr)<2:
            return arr
            
    return arr
##    for a in arr:
##        key, value=a,arr.count(a)
##        ad[key]=value
##    if 'NORTH' in ad.keys() and 'SOUTH' in ad.keys():
##        ad['NORTH'],ad['SOUTH']= ad['NORTH']-min( ad['NORTH'],ad['SOUTH']),ad['SOUTH']-min( ad['NORTH'],ad['SOUTH'])
##    if 'WEST' in ad.keys() and 'EAST' in ad.keys():
##        ad['WEST'],ad['EAST']= ad['WEST']-min( ad['EAST'],ad['WEST']),ad['EAST']-min( ad['WEST'],ad['EAST'])
##    return [item for sublist in [[key]*ad[key] for key in ad.keys() if ad[key]>0] for item in sublist]

def main():

    print(dirReduc(['SOUTH', 'WEST', 'EAST', 'WEST', 'EAST', 'NORTH', 'EAST', 'WEST', 'SOUTH', 'WEST', 'WEST']))


if __name__ == "__main__":
    main()   
    
##for a in arr:
##        key, value=a,arr.count(a)
##        ad[key]=value
##    if 'NORTH' in ad.keys() and 'SOUTH' in ad.keys():
##        ad['NORTH'],ad['SOUTH']= ad['NORTH']-min( ad['NORTH'],ad['SOUTH']),ad['SOUTH']-min( ad['NORTH'],ad['SOUTH'])
##    if 'WEST' in ad.keys() and 'EAST' in ad.keys():
##        ad['WEST'],ad['EAST']= ad['WEST']-min( ad['EAST'],ad['WEST']),ad['EAST']-min( ad['WEST'],ad['EAST'])
##    return [item for sublist in [[key]*ad[key] for key in ad.keys() if ad[key]>0] for item in sublist]
