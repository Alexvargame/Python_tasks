from time import time
from collections import deque


ELEMENTS={'H': 'Hydrogen', 'He': 'Helium', 'Li': 'Lithium', 'Be': 'Beryllium',
 'B': 'Boron', 'C': 'Carbon', 'N': 'Nitrogen', 'O': 'Oxygen', 'F': 'Fluorine',
 'Ne': 'Neon', 'Na': 'Sodium', 'Mg': 'Magnesium', 'Al': 'Aluminium',
 'Si': 'Silicon', 'P': 'Phosphorus', 'S': 'Sulfur', 'Cl': 'Chlorine',
 'Ar': 'Argon', 'K': 'Potassium', 'Ca': 'Calcium', 'Sc': 'Scandium',
 'Ti': 'Titanium', 'V': 'Vanadium', 'Cr': 'Chromium', 'Mn': 'Manganese',
 'Fe': 'Iron', 'Co': 'Cobalt', 'Ni': 'Nickel', 'Cu': 'Copper', 'Zn': 'Zinc',
 'Ga': 'Gallium', 'Ge': 'Germanium', 'As': 'Arsenic', 'Se': 'Selenium',
 'Br': 'Bromine', 'Kr': 'Krypton', 'Rb': 'Rubidium', 'Sr': 'Strontium',
 'Y': 'Yttrium', 'Zr': 'Zirconium', 'Nb': 'Niobium', 'Mo': 'Molybdenum',
 'Tc': 'Technetium', 'Ru': 'Ruthenium', 'Rh': 'Rhodium', 'Pd': 'Palladium',
 'Ag': 'Silver', 'Cd': 'Cadmium', 'In': 'Indium', 'Sn': 'Tin', 'Sb': 'Antimony',
 'Te': 'Tellurium', 'I': 'Iodine', 'Xe': 'Xenon', 'Cs': 'Caesium',
 'Ba': 'Barium', 'La': 'Lanthanum', 'Ce': 'Cerium', 'Pr': 'Praseodymium',
 'Nd': 'Neodymium', 'Pm': 'Promethium', 'Sm': 'Samarium', 'Eu': 'Europium',
 'Gd': 'Gadolinium', 'Tb': 'Terbium', 'Dy': 'Dysprosium', 'Ho': 'Holmium',
 'Er': 'Erbium', 'Tm': 'Thulium', 'Yb': 'Ytterbium', 'Lu': 'Lutetium',
 'Hf': 'Hafnium', 'Ta': 'Tantalum', 'W': 'Tungsten', 'Re': 'Rhenium',
 'Os': 'Osmium', 'Ir': 'Iridium', 'Pt': 'Platinum', 'Au': 'Gold', 'Hg': 'Mercury',
 'Tl': 'Thallium', 'Pb': 'Lead', 'Bi': 'Bismuth', 'Po': 'Polonium', 'At': 'Astatine',
 'Rn': 'Radon', 'Fr': 'Francium', 'Ra': 'Radium', 'Ac': 'Actinium', 'Th': 'Thorium',
 'Pa': 'Protactinium', 'U': 'Uranium', 'Np': 'Neptunium', 'Pu': 'Plutonium', 'Am': 'Americium',
 'Cm': 'Curium', 'Bk': 'Berkelium', 'Cf': 'Californium', 'Es': 'Einsteinium',
 'Fm': 'Fermium', 'Md': 'Mendelevium', 'No': 'Nobelium', 'Lr': 'Lawrencium',
 'Rf': 'Rutherfordium', 'Db': 'Dubnium', 'Sg': 'Seaborgium', 'Bh': 'Bohrium',
 'Hs': 'Hassium', 'Mt': 'Meitnerium', 'Ds': 'Darmstadtium', 'Rg': 'Roentgenium',
 'Cn': 'Copernicium', 'Uut': 'Ununtrium', 'Fl': 'Flerovium', 'Uup': 'Ununpentium',
 'Lv': 'Livermorium', 'Uus': 'Ununseptium', 'Uuo': 'Ununoctium'}


class Queue():
    def __init__(self):
        self._container=deque()
    @property
    def empty(self):
        return not self._container

    def push(self,item):
        self._container.append(item)
    def pop(self):
        return self._container.popleft()
    def __repr__(self):
        return repr(self._container)

class Element():
    def __init__(self,name,code,parent=None,comb=''):
        self.name=name
        self.code=code
        self.parent=parent
        self.comb=comb

class Word:
    def __init__(self,elems,word):
        self.elems=elems
        self.word=word


    def __str__(self):
        output=[]
        for el in self.elems:
            output.append(el.name+'('+el.code+')')
        return ', '.join(output)

    def successors(self,el):
        ables=[]
        varias=[self.word[i] for i in range(1,len(self.word)) if self.word[i-1]==el.code.lower()[-1]]
        for e in self.elems:
            if e.code.lower()[0] in varias:
                ables.append(e)
        return ables


def patch_word(W,start,word):
    word=word.lower()
    res=[]
    frontier = Queue()
    initial = start
    frontier.push(Element(initial.name, initial.code, None,initial.code.lower()))
    explored = {initial}
    while not frontier.empty:
        # print('EX',explored)
        current_el = frontier.pop()
        #print(word,current_el,current_el.comb,current_el.name.lower())
        if current_el.comb==word:
            if el_to_word(current_el) not in res:
                res.append(el_to_word(current_el))

        for child in W.successors(current_el):
            # if child in explored:
            #     continue
            # explored.add(child)
            new_comb=current_el.comb+child.code.lower()
            if new_comb not in word:
                continue
            print(new_comb)
            frontier.push(Element(child.name, child.code,current_el,new_comb))
    return res

def el_to_word(node):
    var_word=[(node.name+'('+node.code+')')]
    while node.parent is not None:
        node=node.parent
        var_word.append(node.name+'('+node.code+')')
    var_word.reverse()
    print('word',var_word)
    return var_word

def elemental_forms(word):
    if word == '':
        return []
    word = word.lower()
    ELEMENTS_WORD={}
    ELEMENTS_START={}
    elems=[]
    elems_starts=[]
    solutions=[]
    for key,value in ELEMENTS.items():
        if key.lower() in word.lower():
            ELEMENTS_WORD[key]=value
            el=Element(value,key)
            elems.append(el)
        if key.lower()[0]==word.lower()[0]:
            ELEMENTS_START[key]=value
            el=Element(value,key)
            elems_starts.append(el)
    print('EL',ELEMENTS_WORD,[key.lower() for key in ELEMENTS_WORD.keys()])
    W=Word(elems,word)
    for start in elems_starts:
        solution=patch_word(W,start,word)
        if solution:
            solutions.extend(solution)
    print(len(solutions))
    return solutions

def main():

    print(elemental_forms('He'))



if __name__ == "__main__":
    main()

#                    # a=[item for item in permutations(list(r), len(r)) if ''.join(list(item))==word.lower()]
                    # if a:
                    #     a=list(set(a))
                    #     adict[-1].extend(a)
