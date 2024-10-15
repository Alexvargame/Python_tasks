from class_direction import *
from class_employee import *
import json



def search_intern(name):
    
    with open('data_interns.json') as rf:
        for t in json.loads(rf.read())['interns']:
            if t['name']==name:
                return t
            
        return f"Такого интерна нет"
             
def search_course(name):
    
    with open('data_courses.json') as rf:
        
        for t in json.loads(rf.read())['courses']:
           
            if t['name']==name:
                return t
            
        return f"Такого курса нет"
             
def search_course_info():

    info=[]
    report_dict={}

    name=input('Название')
    with open('data_courses.json') as rf:
        
        for t in json.loads(rf.read())['courses']:
           
            if t['name']==name:
                print (f"Такой курс есть")
                print (f"Выберите информацию, которую ищете")
                ds=input("Описание, y/n")
                if ds=='y':
                    info.append('description')
                tp=input("Тип занятий, y/n")
                if tp=='y':
                    info.append('theory_prctic')
                h=input("Кол-во часов, y/n")
                if h=='y':
                    info.append('hours')
                pf=input("Список преподавателей, y/n")
                if pf=='y':
                    info.append('professor')
                i=input("Кол-во интернов, y/n")
                if i=='y':
                    info.append('interns')
                ts=input("Кол-во заданий, y/n")
                if ts=='y':
                    info.append('tasks')
                print(info)
                for k in t.keys():
                    if k in info:
                        key,value=k,t[k]
                        report_dict[k]=value
                return report_dict
                
                
                
                
                
            
        return f"Такого курса нет"
    
