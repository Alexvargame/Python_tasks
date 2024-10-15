import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from numpy.lib.stride_tricks import as_strided
def main():
    # x=np.asarray(range(1,26), np.int8).reshape(5,5)
    # print(as_strided(x,shape=(3,),strides=(1,)))
    # print(as_strided(x, shape=(3,), strides=(2,)))
    # x = np.asarray(range(1, 26), np.int16).reshape(5, 5)
    # print(as_strided(x, shape=(25,), strides=(2,)))
    # x = np.asarray(range(1, 26), np.int64).reshape(5, 5)
    # print(as_strided(x, shape=(3,4), strides=(40,8)))
    x=np.array([1,4,9,16])
    print(np.mean(x))
    data=np.array([2,7,3,1])
    bins=[0,5,10]
    hist,_=np.histogram(data,bins)
    print(*hist)
    x=np.array([1.,2.,np.nan])
    print(np.nanstd(x))
    x=np.fmin([-1,-5,6],[0,np.nan,-1])
    print(x,*x)
    basket=np.array([[1,1,0],[0,0,1],[1,0,0],[1,1,1],[1,1,0]])
    copurchases=[(i,j,np.sum(basket[:,i]+basket[:,j]==2)) for i in range(3) for j in range(i+1,3)]
    result=max(copurchases,key=lambda x:x[2])
    print(result)
    X=np.array([[35,30000],[45,45000],[40,50000],
               [35,33000],[25,32500],[40,40000]])
    KNN=KNeighborsRegressor(n_neighbors=3).fit(X[:,0].reshape(-1,1),X[:,1])
    print('KNN',KNN)
    res=KNN.predict([[30]])
    print(int(res[0]),res)
    basket=np.array([[1,1,1,1],[1,1,1,0]])
    print(basket[:,2:],basket[:,2])
    co_perchases=np.sum(np.all(basket[:,2:],axis=1))/basket.shape[0]
    print(co_perchases)
    print(np.all(basket[:2:],axis=1))

if __name__ == "__main__":
    main()

#
