def temperature(tlst):
    res=[]
    for i  in range(len(tlst)-1):
        count=0
        print(tlst[i],tlst[i+1:])
        for j in range(i+1,len(tlst)):
            print(i,j,tlst[i],tlst[j])
            if tlst[j]>tlst[i]:
                count=j-i
                res.append(count)
                print(res)
                break
        if count==0:
            res.append(0)
    res.append(0)
    return res
                
                
        


def main():
    
    print(temperature([73,74,80,71,69,72,76,73]))

if __name__ == "__main__":
    main()

#
