from itertools import permutations,combinations_with_replacement,combinations
from time import time

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

def to_list(arr):
    tmp=[]
    for a in arr:
        tmp.extend(list(a))
    return tmp
def elemental_forms(word):
    ELEMENTS_WORD={}
    for key,value in ELEMENTS.items():
        if key.lower() in word.lower():
            ELEMENTS_WORD[key]=value
    print('EL',ELEMENTS_WORD,[key.lower() for key in ELEMENTS_WORD.keys()])
    tb=time()
    r1= [[item for item in combinations_with_replacement([key.lower() for key in ELEMENTS_WORD.keys()], j)
          if sum(len(t) for t in item)==len(word) ]
              for j in range(1, len(ELEMENTS_WORD) + 1) ]
    for r in r1:
        for rr in r:
            print(sum(len(t) for t in rr),len(word),sum(len(t) for t in rr)==len(word))
            print(rr,set(to_list(rr)),set(word),set(rr)==set(word))
    result =[[item for item in combinations_with_replacement([key.lower() for key in ELEMENTS_WORD.keys()],j)
              if sum(len(t) for t in item)==len(word) and set(word.lower())==set(to_list(list(item))) ]#and set(word)==set([*t for t in list(item)])
           for j in range(1,len(ELEMENTS_WORD)+1)]
    te=time()
    print('T!',te-tb)
    print('rESULT',result)
    result=[r for r in result if r!=[]]
    adict = []
    alst=[]
    tb=time()
    if result:
        for res in result:
            print('RES',res)
            adict.append([])
            for r in res:
                print('R',r)
                if ''.join(list(r))==word.lower():
                    adict[-1].append(r)
                    print('ADICT1',adict)
                else:
                    word_copy=list(word.lower())
                    print(word_copy)
                    for r1 in r:
                        if r1 in word.lower():
                            for i in r1:
                                try:
                                    word_copy.remove(i)
                                except:
                                    break
                        else:
                            break
                    print('wc',word_copy)
                    if len(word_copy)==0:
                        adict[-1].append(r)
                        print('ADICT2',adict)
    te=time()
    print('T',te-tb)
    adict=[a for a in adict if len(a)>0]

    if len(adict)<1:
        return []
    print('adt1',adict,len(adict))
    for ad in adict:
        print('AD',ad)
        for j in range(len(ad)):
            if len(ad[j])==1:
                print('ad',ad,ad[j][0])
                alst.append([ELEMENTS_WORD[ad[j][0].capitalize()] +' ('+ad[j][0].capitalize() +')'])
            else:
                temp=[]
                al = [item for item in permutations(list(ad[j]), len(ad[j])) if ''.join(list(item)) == word.lower()]
                print('al',al)
                if al:
                    for i in range(len(al[0])):
                        temp.append(ELEMENTS_WORD[al[0][i].capitalize()] + ' (' + al[0][i].capitalize()+ ')')
                    # for i in range(len(al[0])):#len(list(ad[0]))):
                    #     temp.append(ELEMENTS_WORD[ad[0][i].capitalize()] + ' (' + ad[0][i].capitalize()+ ')')
                    alst.append(temp)
    print('alst',[a for a in alst],end='\n')
    return alst

def main():

    print(elemental_forms('fictitious'))



if __name__ == "__main__":
    main()

#                    # a=[item for item in permutations(list(r), len(r)) if ''.join(list(item))==word.lower()]
                    # if a:
                    #     a=list(set(a))
                    #     adict[-1].extend(a)
