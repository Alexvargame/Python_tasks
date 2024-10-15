
    
##def spiralize(size):
##    matrix=[['0' for _ in range(size)] for _ in range(size)]
##    print(matrix)
##    matrix[0]=['1' for _ in range(size)]
##    print(matrix)
##    matrix=list(zip(*matrix[::-1]))
##    print(matrix)
##    matrix=list(zip(*matrix[::-1]))
##    print(matrix)
##def spiral(n):
##    dx,dy = 1,0            # Starting increments
##    x,y = 0,0              # Starting location
##    myarray = [[None]* n for j in range(n)]
##    for i in xrange(n**2):
##        myarray[x][y] = i
##        nx,ny = x+dx, y+dy
##        if 0<=nx<n and 0<=ny<n and myarray[nx][ny] == None:
##            x,y = nx,ny
##        else:
##            dx,dy = -dy,dx
##            x,y = x+dx, y+dy
##    return myarray
def spiral_matrix(n):
    m = [[0] * n for i in range(n)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    x, y, c = 0, -1, 1
    for i in range(n + n - 1):
        for j in range((n + n - i) // 2):

            x += dx[i % 4]
            y += dy[i % 4]
            #print(m[x][y],m[x-1][y],m[x][y+1],m[x][y]
            if x==n-1 or y==n-1 or ((m[x-1][y]!=c) and m[x][y+1]!=c):# and m[x+1][y]!=c):# or m[x][y+1]!='0' or m[x-1][y]!='0':
                m[x][y] = c
               # input()
##            print(x,y,c)
##            input()
            #c += 1
    return m
for i in spiral_matrix(10): print(*i)
def main():

    #print(spiralize(5))
    spiral_matrix(10)

    
    
  
    
if __name__ == "__main__":
    main()
