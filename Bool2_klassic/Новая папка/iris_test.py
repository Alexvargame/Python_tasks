from typing import List
import csv
from util import normalize_by_feature_scalling
from random import shuffle
from network import Network

def iris_interpret_output(output):
    if max(output)==output[0]:
        return "Iris-setosa"
    elif max(output)==output[1]:
        return "Iris-versicolor"
    else:
        return "Iris-virginica"


def main():
    iris_parameters=[]
    iris_classifications=[]
    iris_species=[]
    with open('iris.csv',mode='r') as iris_file:
        irises=list(csv.reader(iris_file))
        shuffle(irises)
        for iris in irises:
            parameters=[float(n) for n in iris [0:4]]
            iris_parameters.append(parameters)
            species=iris[4]
            if species=='Iris-setosa':
                iris_classifications.append([1.0,0.0,0.0])
            elif species=='Iris-versicolor':
                iris_classifications.append([0.0,1.0,0.0])
            else:
                iris_classifications.append([0.0,0.0,1.0])
            iris_species.append(species)
    normalize_by_feature_scalling(iris_parameters)
    iris_network=Network([4,6,3],0.3)
    iris_trainers=iris_parameters[0:100]
    iris_trainers_corrects=iris_classifications[0:100]
    for _ in range(50):
        iris_network.train(iris_trainers,iris_trainers_corrects)
    iris_testers=iris_parameters[100:150]
    iris_testers_corrects=iris_species[100:150]
    iris_results=iris_network.validate(iris_testers,iris_testers_corrects,iris_interpret_output)
    print(f"{iris_results[0]} correct of {iris_results[1]}={iris_results[2]*100}%")



if __name__=="__main__":
    main()