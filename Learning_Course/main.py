from class_direction import *
from class_employee import *
import json
from search import *

def main():
   prof=Professor("Иванов")
   prof1=Professor("Петров")
   a=Dir_iOS('Вводный', 'moblie','theory',30)
   b=Dir_iOS('Вводный_практика', 'mobile','practic',24)
   c=Dir_iOS('Часть1', 'moblie','theory',12)

   
 
   

   intern=Intern('Смирнов')
   intern1=Intern('Сидоров')
   #a.professor=prof.name
 
   a.add_prof(prof)

   
   c.add_intern(intern1)
   a.add_intern(intern)


   a.add_task("Контрольная №1")
   a.add_task("Контрольная №2")
 

   prof.add_course(c)

   c.add_prof(prof1)
   
   prof1.add_course(b)
   print('III',intern.add_point(a,'Контрольная №1',5))
   print('III',intern.add_point(a,'Контрольная №2',4))
   print('V',intern.result(a))
   prof.change_hours(a,12)
   



   
##   a_json=json.dumps(a.to_dict())
##   print('DUMP',a_json)
##   dec_a=json.loads(a_json)
##   print('LOAD',dec_a)

   data = {"professors": []}
   with open('data_employee.json','w',encoding="utf-8") as f:
      json.dump(data,f,indent=4,ensure_ascii = False)
   with open('data_employee.json',encoding="utf-8") as f:
      data=json.load(f)
      data['professors'].append(prof.to_dict())
   with open('data_employee.json','w') as f:
      json.dump(data,f,indent=4,ensure_ascii = False)
   data['professors'].append(prof1.to_dict())
   with open('data_employee.json','w') as f:
      json.dump(data,f,ensure_ascii = False,indent=4)

   
   with open('data_employee.json') as read_file:
      data=read_file.read()
      templ=json.loads(data)
   print('DATA',templ)

   data = {"interns": []}
   
   with open('data_interns.json','w',encoding="utf-8") as f:
      json.dump(data,f,ensure_ascii = False,indent=4)
   with open('data_interns.json') as f:
      data=json.load(f)
      data['interns'].append(intern.to_dict())
   with open('data_interns.json','w') as f:
      json.dump(data,f,ensure_ascii = False,indent=4)
   data['interns'].append(intern1.to_dict())
   with open('data_interns.json','w') as f:
      json.dump(data,f,ensure_ascii = False,indent=4)

   
   with open('data_interns.json') as read_file:
      data=read_file.read()
      templ=json.loads(data)
   print('DATA',templ)



   
   data = {"courses": []}
  
   with open('data_courses.json','w+') as f:
      json.dump(data,f,indent=4)

   with open('data_courses.json') as f:
      data=json.load(f)
   data['courses'].append(a.to_dict())
   print('d',data)

   with open('data_courses.json','w+') as f:
      #f.write(json.dumps(data,indent=4,ensure_ascii = False))
      json.dump(data,f,ensure_ascii = False,indent=2)
   data['courses'].append(b.to_dict())
   print('d',data)
   with open('data_courses.json','w+') as f:
      json.dump(data,f,ensure_ascii = False,indent=4)
   data['courses'].append(c.to_dict())
   print('d',data)

   with open('data_courses.json','w+') as f:
      data=json.dump(data,f,ensure_ascii = False,indent=4)
      


   print(search_intern('Смирнов'))
   print(search_intern('Петров'))
   print(search_course('Вводный'))
   print(search_course('Часть1'))
   print(search_course_info())

     
    
if __name__ == "__main__":
    main()


