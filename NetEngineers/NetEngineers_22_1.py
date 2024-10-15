import csv
import re
from pprint import pprint

import yaml


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
    top=Topology(topology_example)
    #print(top.topology)
    top.delete_link(('R3', 'Eth0/1'), ('R4', 'Eth0/0'))
    #print(top.topology)
    top.delete_link(('R5', 'Eth0/0'), ('R3', 'Eth0/2'))
    #print(top.topology)
    top.delete_not('SW1')
    print(top.topology)
    top.add_link(('R3', 'Eth0/1'), ('R4', 'Eth0/0'))
    print(top.topology)
    top.add_link(('R3', 'Eth0/1'), ('R4', 'Eth0/0'))
    print(top.topology)
    top.add_link(('R3', 'Eth0/1'), ('R7', 'Eth0/0'))
    print(top.topology)

if __name__ == "__main__":
    main()

#
