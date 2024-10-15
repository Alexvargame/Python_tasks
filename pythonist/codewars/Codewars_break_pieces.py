

def break_pieces(shape):
    for s in shape:
        print(s)
    res=[]
    shp=[list(sh) for sh in shape[0].split('\n')[1:]]
    indxs=[i[0] for i in enumerate(shp) if ' ' not in i[1]]
    for i in range(1,len(indxs)):
        #print(shp[indxs[i-1]:indxs[i]+1])
        trf=list(list(i) for i in zip(*shp[indxs[i-1]:indxs[i]+1]))
        indxs_tr=[i[0] for i in enumerate(trf) if ' ' not in i[1]]
        if len([i[0] for i in enumerate(trf) if ' ' not in i[1]])==2:
            res.append(''.join(['\n'+''.join(sh) for sh in shp[indxs[i-1]:indxs[i]+1]]))
        else:
            for j in range(1,len(indxs_tr)):   
                res.append(''.join(['\n'+''.join(sh[indxs_tr[j-1]:indxs_tr[j]+1])for sh in shp[indxs[i-1]:indxs[i]+1]]))
    for r in res:
        print(r)
    return res

def main():

   print(break_pieces([('\n+------------+\n|            |\n|            |\n|            |\n+------+-----+\n|      |     |\n|      |     |\n+------+-----+')]))

if __name__ == "__main__":
    main()




#
