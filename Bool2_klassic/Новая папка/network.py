from __future__ import annotations
from typing import List,Callable,Tuple,TypeVar
from functools import reduce
from layer import Layer
from util import sigmoid,derivative_sigmoid

T=TypeVar('T')

class Network:
    def __init__(self,layer_structure,learning_rate,
                 activation_function=sigmoid,
                 derivative_activation_function=derivative_sigmoid):
        if len(layer_structure)<3:
            raise ValueError("Error: Should ba least 3 layers(1 input,1 hidden, 1 output")
        self.layers=[]
        input_layer=Layer(None,layer_structure[0],learning_rate,activation_function,
                          derivative_activation_function)
        self.layers.append(input_layer)
        for previous,num_neurons in enumerate(layer_structure[1::]):
            next_layer=Layer(self.layers[previous],num_neurons,
                             learning_rate,activation_function,
                             derivative_activation_function)
            self.layers.append(next_layer)



    # Помещает входные данные на первый слой, затем выводит их
    # с первого слоя и подает на второй слой в качестве входных данных,
    # со второго - на третий и т. д.

    def outputs(self,input):
        return reduce(lambda inputs,layer:layer.outputs(inputs),self.layers,
                      input)

    # Определяет изменения каждого нейрона на основании ошибок
    # выходных данных по сравнению с ожидаемым выходом
    def backpropagate(self, expected):
        last_layer=len(self.layers)-1
        self.layers[last_layer].calculate_deltas_for_output_layer(expected)
        for l in range(last_layer-1,0,-1):
            self.layers[l].calculate_deltas_for_hidden_layer(self.layers[l+1])

    # сама функция backpropagate() не изменяет веса
    # Функция иpdate_weights использует дельты, вычисленные в backpropagate(),
    # чтобы действительно изменить веса
    def update_weights(self):
        for layer in self.layers[1:]:
            for neuron in layer.neurons:
                for w in range(len(neuron.weights)):
                    neuron.weights[w]=neuron.weights[w]+(neuron.learning_rate*(layer.previous_layer.output_cache[w])*neuron.delta)

    #Функция traiп() использует результаты выполнения функции oиtpиts()
    # для нескольких входных данных, сравнивает их
    # с ожидаемыми результатами и передает полученное
    # в backpropagate() и иpdate_weights()
    def train(self, inputs, expecteds):
        for location,xs in enumerate(inputs):
            ys=expecteds[location]
            outs=self.outputs(xs)
            self.backpropagate(ys)
            self.update_weights()

    # Для параметризованных результатов, которые требуют классификации,
    # зта функция возвращает правильное количество попыток
    # и процентное отношение по сравнению с общим количеством
    def validate(self, inputs, expected,interpret_output):
        correct=0
        for input, expected in zip(inputs,expected):
            result=interpret_output(self.outputs(input))
            if result==expected:
                correct+=1
        percentage=correct/len(inputs)
        return correct,len(inputs),percentage











def main():
    pass

if __name__=="__main__":
    main()