from typing import List,Callable
from util import dot_product

class Neuron:
    def __init__(self,weights,learning_rate,activation_fuction,
                 derivative_activation_function):
        self.weights=weights
        self.learning_rate=learning_rate
        self.activation_fuction=activation_fuction
        self.derivative_activation_function=derivative_activation_function
        self.output_cache=0.0
        self.delta=0.0
    def output(self,inputs):
        self.output_cache=dot_product(inputs,self.weights)
        return self.activation_fuction(self.output_cache)


def main():
    pass

if __name__=="__main__":
    main()