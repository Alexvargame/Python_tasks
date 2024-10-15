import re


class Topology:
    def __init__(self,topology_example):
        self.topology=self._normalize(topology_example)


    def _normalize(self,topology_example):
        topology={}
        for key, value in topology_example.items():
            if value not in topology.keys():
                topology[key] = value
        return topology

    def delete_link(self,link1,link2):
        del_lst=[]
        for l in self.topology:
            if (l==link1 and self.topology[l]==link2) or (l==link2 and self.topology[l]==link1):
                del_lst.append(l)
        for l in del_lst:
            del self.topology[l]
        if len(del_lst)==0:
            print("Такого устройства нет")

    def delete_not(self,node):
        del_lst=[]
        for l in self.topology:
            if l[0]==node or self.topology[l][0]==node:
                del_lst.append(l)
        for l in del_lst:
            del self.topology[l]
        if len(del_lst)==0:
            print("Такого устройства нет")
    def add_link(self,link1,link2):
        if link1 in self.topology.keys():
            if link2 in self.topology.values():
                print('Такое соединение существует')
            else:
                print('Соединение с таким портом сущестсвует')
        else:
            self.topology[link1]=link2

    def __add__(self, other):

        temp_topology=self.topology.copy()
        temp_topology.update(other.topology)
        return Topology(temp_topology)

    def __iter__(self):
        return iter(self.topology.items())





def main():
    topology_example = {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
                        ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
                        ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
                        ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
                        ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
                        ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
                        ('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
                        ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
                        ('SW1', 'Eth0/3'): ('R3', 'Eth0/0')}
    topology_example2 = {('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
                         ('R1', 'Eth0/6'): ('R9', 'Eth0/0')}
    t1=Topology(topology_example)
    t2=Topology(topology_example2)
    t3=t1+t2
    print(t3.topology)
    for link in t1:
        print(link)

if __name__ == "__main__":
    main()

#
