from enum import IntEnum
from typing import Tuple, List

Nucleotide=IntEnum('Nucleotide', ('A','C','G','T'))
Codon=Tuple[Nucleotide, Nucleotide, Nucleotide]
Gene=List[Codon]

gene_str='ACGTGGCTCTCTAACGTACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT'

def string_to_gene(s):
    gene=[]
    for i in range(0,len(s),3):
        if (i+2)>=len(s):
            return gene
        codon=(Nucleotide[s[i]], Nucleotide[s[i+1]], Nucleotide[s[i+2]])
        gene.append(codon)
    return gene
my_gene=string_to_gene(gene_str)
print(my_gene)


def linear_contains(gene, key_codon):
    for codon in gene:
        if codon==key_codon:
            return True
        return False

acg=(Nucleotide.A,Nucleotide.C,Nucleotide.G)
gat=(Nucleotide.G,Nucleotide.A,Nucleotide.T)
print(linear_contains(my_gene, acg))
print(linear_contains(my_gene, gat))


def binary_contains(gene,key_codon):
    low: int = 0
    high: int = len(gene) - 1
    while low <= high: # пока еще есть место для поиска
        mid: int = (low + high) // 2
        if gene[mid] < key_codon:
            low = mid + 1
        elif gene[mid] > key_codon:
            high = mid - 1
        else:
            return True
    return False
my_sorted_gene= sorted(my_gene)
print(binary_contains(my_sorted_gene, acg)) # True
print(binary_contains(my_sorted_gene, gat))
