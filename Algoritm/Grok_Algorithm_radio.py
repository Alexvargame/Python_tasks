
states_needed=set(['mt','wa','or','id','nv','ut','ca','az'])
arr=[1,2,2,3,3,3]
stations={}
stations['kone']=set(['id','nv','ut'])
stations['ktwo']=set(['wa','id','mt'])
stations['kthree']=set(['or','nv','ca'])
stations['kfour']=set(['nv','ut'])
stations['kfive']=set(['ca','az'])
    
final_stations=set()
while states_needed:   
    best_station=None
    states_covered=set()
    
    for station , states_for_station in stations.items():
        print('bs',best_station,'sc',states_covered)
        covered=states_needed&states_for_station
        print('s',station ,'sfs', states_for_station,'cov',covered)
        if len(covered)>len(states_covered):
            best_station=station
            states_covered=covered
            print('1','bs',best_station,'sc',states_covered)
            input()
        input()
    states_needed-=states_covered
    print('sn',states_needed)
        
    final_stations.add(best_station)

print(final_stations)


def main():
    pass



if __name__ == "__main__":
    main()




#
