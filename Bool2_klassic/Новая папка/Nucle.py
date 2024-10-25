
class CompressedGene:
    def __init__(self,gene):
        self._compress(gene)

    def _compress(self, gene):
        self.bit_string=1
        for nucleotide in gene.upper():
            self.bit_string<<=2
           # print(self.bit_string)
            if nucleotide =='A':
                #print('A',int(0b00))
                self.bit_string |=0b00
            elif nucleotide =='C':
               # print('C',int(0b01))
                self.bit_string |=0b01
            elif nucleotide =='G':
              #  print('G',int(0b10))
                self.bit_string |=0b10
            elif nucleotide =='T':
              #  print('T',int(0b11))
                self.bit_string |=0b11
            else:
                raise ValueError("invalid Nucleotide:{}".format(nucleotide))
            #print(self.bit_string)
        print(self.bit_string)
        
    def decompress(self):
        gene=''
        for i in range(0,self.bit_string.bit_length()-1,2):
            bits=self.bit_string >> i & 0b11
            if bits==0b00:
                
                gene+='A'
            elif bits==0b01:
                gene+='C'
                
            elif bits==0b10:
                gene+='G'
            elif bits==0b11:
                gene+='T'
            else:
                raise ValueError("invalid bits:{}".format(bits))
        return gene[::-1]
    def __str__(self):
        return self.decompress()

                


if __name__=="__main__":

    n1=CompressedGene('TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA')
    print(n1)






