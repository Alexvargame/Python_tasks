

class CompressedGene:
    def __init__(self, gene):
        self._compress(gene)

    def _compress(self, gene):
        self.bit_string: int = 1 # начальная метка
        for nucleotide in gene.upper():
            self.bit_string <<= 2 # сдвиг влево на 2 бита
            if nucleotide == "A": #поменять 2 последних бита на 00
                self.bit_string|=0b00
            elif nucleotide =="C": #поменять 2 последних бита на 01
                self.bit_string|=0b01
            elif nucleotide =="G": #поменять 2 последних бита на 10
                self.bit_string|=0b10
            elif nucleotide == "T": #поменять 2 последних бита на 11
                self.bit_string|= 0b11
            else:
                raise ValueError ("Invalid Nucleotide:{}".format(nucleotide))

    def decompress(self):
        gene: str = ''
        for i in range(0, self.bit_string.bit_length() - 1, 2):
        # -1 чтобы исключить метку
            bits= self.bit_string >> i & 0b11
            
        # получить только 2 значимых бита
            if bits == 0b00: # А
    
       
                gene += "A"
            elif bits == 0b01: # с
                gene += "C"
            elif bits == 0b10: # G
                gene += "G"
            elif bits == 0b11: # т
                gene += "T"
            else:
                raise ValueError("Invalid bts:{}".format(bits))
        return gene[::-1] # [::-1] обращение строки посредством обратных срезов
    def __str__(self): #представление строки в биде красивого вывода
        return self.decompress()
if __name__== "__main__":

    from sys import getsizeof
    original="TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" 
    print("original is {} bytes".format(getsizeof(original)))
    compressed=CompressedGene(original)
    print("compressed is {} bytes".format(getsizeof(compressed.bit_string)))
    print(compressed.bit_string)
    print(compressed) # распаковка
    print("original and decompressed are the same: {}".format(original ==compressed.decompress())) 

