import string
class Tomato:
    states={0:"None",1:"Flower", 2:"Green", 3:"Red"}
    def __init__(self, _index):
        self._index=_index
        self._state=0
    def grow(self):
        if self._state<3:
            self._state+=1
        return self._state
        
    def is_ripe(self):
        if self._state==3:
            return True
        return False
class TomatoBush:
    def __int__(self, num):
       # self.num_tomatoes=tomatoes
        self.tomatoes = [Tomato(index) for index in range(0, num)]
        #self.tomatoes=[]
        #for i in range(self.num_tomatoes):
        #    self.tomatoes.append(Tomato(index))
    def grow_all(self):
        for tomato in self.tomatoes:  
            tomato.grow()
    def all_are_ripe(self):
        for tomato in self.tomatoes:
            if not tomato.is_ripe():
                break
                return False
        return True
    def give_away_all(self):
        self.tomatoes=[]
        return self.tomatoes
class Gardener:
    def __init__(self, name, plant):
        self.name=name
        self._plant=plant
    def work(self):
        print('Gardener is working...')
        self._plant.grow_all()
        print('Gardener finished')
    def harvest(self):
        if self._plant.all_are_ripe():
            print("Finished")
        else:
            print("Not  jet")
    def knowladge_base(self):
        print("report")
if __name__ == '__main__':
    
    tombush1=TomatoBush(4)
    gardenman=Gardener("Rob", tombush1)
    gardenman.knowladge_base()
