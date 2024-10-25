import numpy as np
import requests
from bs4 import BeautifulSoup


lst1=[]
#url1='C:/Python36-32/ex/avito/1.txt'
#url12='C:/Python36-32/ex/avito/1.html'
url='http://127.0.0.1:8000/'
matrix=[]
l_result=[]


def scrap(url):
    response=requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    items=soup.find_all('p')
    for i in range(len(items)):
            lst1.append(items[i].text.split(' '))
    matrix=np.array(lst1, dtype=np.int)
    return matrix
    
"""
def scrap(url):
    with open(url) as f:
        lst=f.readlines()
        for l in lst:
            lst1.append(l.replace('\n','').split(' '))
    matrix=np.array(lst1, dtype=np.int)
    return matrix
"""
def read_matrix(matrix, n):
    if 2*n-len(matrix)>0:
        f=len(matrix)-n
        for i in range(f,n):
            l_result.append(matrix[i][f])
        for i in range(f+1,n):
            l_result.append(matrix[n-1][i])
        for i in range(f+1,n):
            l_result.append(matrix[n-1-i+f][n-1])
        for i in range(f+1, n-1):
            l_result.append(matrix[f][n-1-i+f])
        return read_matrix(matrix,n-1)
    else: return l_result
matrix=scrap(url)
print(matrix, len(matrix))
print(read_matrix(matrix, len(matrix)))


