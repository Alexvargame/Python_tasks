from collections import namedtuple

State=namedtuple('State','x y')

class Pixel():
    def __init__(self,state,color,deep=0,parent=None):
        self.state=state
        self.color=color
        self.parent=parent
        self.deep=deep

class Image:
  def __init__(self, data, w, h):
    self.pixels = data
    self.width = w
    self.height = h

class Central_Pixels_Finder(Image):

    def __init__(self, data, w, h):#, colors,grid):
        super().__init__(data, w, h)
        # color_dict={}
        # for d in list(self(data)):
        #     key,value=d,
        self.colors=list(set(data))
        self.grid=self.make_grid(self.pixels, self.width, self.height)

    def central_pixels(self, colour):
        # gr = self.make_grid(self.pixels, self.width, self.height)
        central_pixels_lst=[]
        deep_max=1
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j].color==colour:
                    if self.grid[i][j].deep>deep_max:
                        deep_max=self.grid[i][j].deep
                        central_pixels_lst=[]
                        central_pixels_lst.append(self.grid[i][j])
                        #print('MMM', self.grid[i][j].deep, central_pixels_lst, deep_max)
                    elif self.grid[i][j].deep==deep_max:
                        central_pixels_lst.append(self.grid[i][j])
                        #print('OOO', self.grid[i][j].deep, central_pixels_lst, deep_max)
        return [p.state.x*self.width+p.state.y for p in central_pixels_lst]


    def pixel_deep(self):

        # print(pixel.state,pixel.color)
        # print(pixel.state.x,pixel.state.y,self.height-pixel.state.x,self.width-pixel.state.y)
        # print('MAX',max(pixel.state.x,pixel.state.y,self.height-pixel.state.x,self.width-pixel.state.y))
        # if pixel.state==(3,6):
        for k in range(len(self.grid)):
            for v in range(len(self.grid[0])):
                d1 = d2 = d3 = d4 = 0
                pixel=self.grid[k][v]

                for i in range(pixel.state.x,-1,-1):
                    if self.grid[i][pixel.state.y].color==pixel.color:
                        d1+=1
                    else:
                        break
                for i in range(pixel.state.x,self.height):
                    if self.grid[i][pixel.state.y].color==pixel.color:
                        d3+=1
                    else:
                        break
                for j in range(pixel.state.y,self.width):
                    if self.grid[pixel.state.x][j].color==pixel.color:
                        d2+=1
                    else:
                        break
                for j in range(pixel.state.y,-1,-1):
                    if self.grid[pixel.state.x][j].color==pixel.color:
                        d4+=1
                    else:
                        break
                pixel.deep=min(d1,d2,d3,d4)

    def make_grid(self,data,w,h):
            grid = []
            for x in range(0, h):
                grid.append([])
                for y in range(0, w):
                    char = data[x * w + y]
                    pixel = Pixel(state=State(x, y),color=char)
                    grid[x].append(pixel)
            return grid

def main():

    # img=Image([1,1,4,4,4,4,2,2,2,2,
    #             1,1,1,1,2,2,2,2,2,2,
    #             1,1,1,1,2,2,2,2,2,2,
    #             1,1,1,1,1,3,2,2,2,2,
    #             1,1,1,1,1,3,3,3,2,2,
    #             1,1,1,1,1,1,3,3,3,3], 10, 6)
    # res [(188, 4), (381, 4), (410, 4), (439, 4)]
    #
    # equal[481]                                                #17
    img=Image([6, 7, 7, 7, 7, 7, 6, 6, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 5, 5, 5, 7, 7, 7, 7, 7, 7,
               6, 7, 7, 7, 7, 7, 6, 6, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 5, 5, 5, 7, 7, 7, 7, 7, 7,
               6, 7, 7, 7, 7, 7, 6, 6, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 5, 5, 5, 7, 7, 7, 7, 7, 7,
               6, 5, 5, 5, 7, 7, 6, 6, 5, 5, 7, 5, 5, 5, 5, 5, 5, 5, 7, 7, 7, 7, 7, 5, 5, 5, 5, 5, 5,
               6, 5, 5, 5, 7, 7, 6, 6, 5, 5, 7, 5, 5, 5, 5, 5, 5, 5, 7, 7, 7, 7, 7, 5, 5, 5, 5, 5, 5,
               6, 5, 5, 5, 7, 7, 6, 6, 5, 5, 7, 5, 5, 5, 5, 5, 5, 5, 7, 7, 7, 7, 7, 5, 5, 5, 5, 5, 5,
               6, 5, 5, 5, 7, 7, 6, 6, 5, 5, 7, 5, 5, 5, 5, 5, 5, 5, 7, 7, 7, 7, 7, 5, 5, 5, 5, 5, 5,
               6, 6, 6, 6, 5, 5, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 7, 7, 5, 5, 7, 7, 7, 6, 6, 6, 6, 6, 6,
               6, 6, 6, 6, 5, 5, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 7, 7, 5, 5, 7, 7, 7, 6, 6, 6, 6, 6, 6,
               6, 6, 6, 6, 5, 5, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 7, 7, 5, 5, 7, 7, 7, 6, 6, 6, 6, 6, 6,
               6, 6, 6, 6, 5, 5, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 7, 7, 5, 5, 7, 7, 7, 6, 6, 6, 6, 6, 6,
               6, 6, 6, 6, 5, 5, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 7, 7, 5, 5, 7, 7, 7, 6, 6, 6, 6, 6, 6,
               6, 6, 6, 6, 5, 5, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 7, 7, 5, 5, 7, 7, 7, 6, 6, 6, 6, 6, 6,
               6, 5, 5, 5, 5, 5, 5, 5, 6, 6, 5, 6, 6, 6, 6, 6, 5, 5, 5, 5, 7, 7, 7, 7, 7, 7, 7, 7, 7,
               6, 5, 5, 5, 5, 5, 5, 5, 6, 6, 5, 6, 6, 6, 6, 6, 5, 5, 5, 5, 7, 7, 7, 7, 7, 7, 7, 7, 7,
               6, 5, 5, 5, 5, 5, 5, 5, 6, 6, 5, 6, 6, 6, 6, 6, 5, 5, 5, 5, 7, 7, 7, 7, 7, 7, 7, 7, 7,
               6, 5, 5, 5, 5, 5, 5, 5, 6, 6, 5, 6, 6, 6, 6, 6, 5, 5, 5, 5, 7, 7, 7, 7, 7, 7, 7, 7, 7,
               6, 5, 5, 5, 5, 5, 5, 5, 6, 6, 5, 6, 6, 6, 6, 6, 5, 5, 5, 5, 7, 7, 7, 7, 7, 7, 7, 7, 7,
               6, 5, 5, 5, 5, 5, 5, 5, 6, 6, 5, 6, 6, 6, 6, 6, 5, 5, 5, 5, 7, 7, 7, 7, 7, 7, 7, 7, 7,#5
               7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7,
               5, 5, 5, 5, 7, 7, 5, 5, 7, 7, 5, 7, 7, 7, 7, 7, 6, 6, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6,
               5, 5, 5, 5, 7, 7, 5, 5, 7, 7, 5, 7, 7, 7, 7, 7, 6, 6, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6,
               5, 5, 5, 5, 7, 7, 5, 5, 7, 7, 5, 7, 7, 7, 7, 7, 6, 6, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6,
               5, 7, 7, 7, 6, 6, 7, 7, 6, 6, 7, 5, 5, 5, 5, 5, 5, 5, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6,
               5, 7, 7, 7, 6, 6, 7, 7, 6, 6, 7, 5, 5, 5, 5, 5, 5, 5, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6,
               5, 7, 7, 7, 6, 6, 7, 7, 6, 6, 7, 5, 5, 5, 5, 5, 5, 5, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6,
               5, 5, 5, 5, 7, 7, 7, 7, 5, 5, 7, 6, 6, 6, 6, 6, 5, 5, 7, 7, 5, 5, 5, 7, 7, 7, 7, 7, 7,
               5, 5, 5, 5, 7, 7, 7, 7, 5, 5, 7, 6, 6, 6, 6, 6, 5, 5, 7, 7, 5, 5, 5, 7, 7, 7, 7, 7, 7,
               7, 7, 7, 7, 6, 6, 5, 5, 5, 5, 6, 5, 5, 5, 5, 5, 7, 7, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7],29,29)

    # img=Image([24, 24, 24,
    #            24, 24, 25,
    #            24, 25, 25],3,3)
    CPF=Central_Pixels_Finder(img.pixels,img.width,img.height)#,grid=[],colors=[])
    CPF.pixel_deep()
    print(CPF.central_pixels(CPF.colors[0]),
    CPF.central_pixels(CPF.colors[1]),
    CPF.central_pixels(CPF.colors[2]))

if __name__ == "__main__":
    main()

