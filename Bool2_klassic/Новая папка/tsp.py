from typing import Dict, List, Iterable, Tuple
from itertools import permutations,product

def possible_mnemonics(phone_number,phone_mapping):
    letter_tuples=[]
    print(phone_number,phone_mapping)
    for digit in phone_number:
        letter_tuples.append(phone_mapping.get(digit,(digit,)))
    return product(*letter_tuples)



def main():
    vt_distances = {
        "Rutland":
            {"Burlington": 67,
             "White River Junction": 46,
             "Bennington": 55,
             "Brattleboro": 75},
        "Burlington":
            {"Rutland": 67,
             "White River Junction": 91,
             "Bennington": 122,
             "Brattleboro": 153},
        "White River Junction":
            {"Rutland": 46,
             "Burlington": 91,
             "Bennington": 98,
             "Brattleboro": 65},
        "Bennington":
            {"Rutland": 55,
             "Burlington": 122,
             "White River Junction": 98,
             "Brattleboro": 40},
        "Brattleboro":
            {"Rutland": 75,
             "Burlington": 153,
             "White River Junction": 65,
             "Bennington": 40
             }
    }
    vt_cities=vt_distances.keys()
    city_permutations=permutations(vt_cities)
    tsp_path=[c+(c[0],) for c in city_permutations]
    best_path=tuple()
    min_distance=999999999999
    for path in tsp_path:
        distance=0
        last=path[0]
        for next in path[1:]:
            distance+=vt_distances[last][next]
            last=next
        if distance<min_distance:
            min_distance=distance
            best_path=path
    print(f"The shortest path is {best_path} in {min_distance} miles")
    phone_mapping = {'1': ('1',),
                    '2': ('a','b','c'),
                    '3': ('d', 'e', 'f'),
                    '4': ('g', 'h', 'i'),
                    '5': ('j', 'k', 'l'),
                    '6': ('m', 'n', 'o'),
                    '7': ('p','q','r','s'),
                    '8': ('t', 'u', 'v'),
                    '9': ('w', 'x', 'y','z'),
                    '0': ('0',)
                    }
    phone_number=input("Enter number:")
    for mnemonic in possible_mnemonics(phone_number,phone_mapping):
        print(''.join(mnemonic))


if __name__=="__main__":
    main()
