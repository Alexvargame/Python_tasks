from typing import Tuple,List
from enum import IntEnum

Nucleotide=IntEnum('Nucleotide',('A','C','G','T'))
Codon=(Nucleotide,Nucleotide,Nucleotide)
Gene=[Codon]
gene_str='TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA'

def string_to_genes(s):
    gene=[]
    for i in range(0,len(s),3):
        if(i+2)>=len(s):
            return gene
        codon=(Nucleotide[s[i]],Nucleotide[s[i+1]],Nucleotide[s[i+2]])
        gene.append(codon)
    return gene
                            
def binary_contains(gene,key_codon):
    low=0
    high=len(gene)-1
    while low<=high:
        mid=(low+high)//2
        if gene[mid]<key_codon:
            low=mid+1
        elif gene[mid]>key_codon:
            high=mid-1
        else:
            return True
    return False

            

def main():
    my_gene=string_to_genes(gene_str)
    print(my_gene)
    acg = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
    gat= (Nucleotide.G, Nucleotide.A, Nucleotide.T)
    my_sorted_gene=sorted(my_gene)
    print(binary_contains(my_sorted_gene,acg))
    print(binary_contains(my_sorted_gene,gat))
    

if __name__=="__main__":

    main()





