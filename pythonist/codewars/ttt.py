
#from preloaded import MORSE_CODE
import re
#from collections import Count

def decode_bits(bits):
    n=2
    print(bits)
    astr=''
    for b in re.split(r'0{7,14}',bits):
        print(b,b.split('0'*(n+1)))
        if len(b)>0:
            for bb in re.split(r'0{3,6}',b):
                if len(bb)>0:
                    print('bb',bb,bb.split('0'*n))
                    for bbb in re.split(r'0{1,2}',bb):
                        print('bbb',bbb)
                        if len(bbb)==2 or len(bbb)==1:
                            astr+='.'
                        else:
                            astr+='-'
                    print('Str',astr)
                    astr+=' '
            astr+='  '
    print(astr)


    
##    morse_code='   '.join([' '.join([''.join(['-' if len(let.strip('0'))==3*n else '.' for let in l.strip('0').split('0'*1*n) if len(let.strip('0'))>0])
##                for l in b.strip('0').split('0'*n*3)]) for b in bits.strip('0').split('0'*n*7)])
    morse_code='   '.join([' '.join([''.join(['-' if len(let.strip('0'))==3*n else '.' for let in l.strip('0').split('0'*(n-1))
                                              if len(let.strip('0'))>0])
                for l in b.strip('0').split('0'*(n+1)) if len(l)>0]) for b in bits.strip('0').split('0'*(n*3+1))
                           if len(b)>0])
##    print('A',bits.strip('0').split('0'*(n*3+1)))
##    print('1',[ b.strip('0').split('0'*(n+1)) for b in bits.strip('0').split('0'*(n*3+1)) if len(b)>0])
##    print('2',[[l.strip('0').split('0'*(n-1))  for l in b.strip('0').split('0'*(n+1)) if len(l)>0 ] for b in bits.strip('0').split('0'*(n*3+1))])
##    
##    print('4',[[['-' if len(let.strip('0'))==3*n else '.' for let in l.strip('0').split('0'*(n-1)) if len(let.strip('0'))>0]
##                for l in b.strip('0').split('0'*(n+1))] for b in bits.strip('0').split('0'*(n*3+1))])
##
    
    print('morse_code',morse_code)
    return morse_code

def decode_morse(morse_code):
    MORSE_CODE={'....':'H','.':'E','.-':'A','...':'S','---':'O','-.--':'Y',
                '.---':'J','..-':'U','-..':'D','..':'I','--':'M'}

    text=[m.split(' ') for m in morse_code.strip(' ').split('   ')]
    for t in text:
        for i in range(len(t)):
            if t[i] in MORSE_CODE.keys():
                t[i]=MORSE_CODE[t[i]]
            
    return ' '.join([''.join(t) for t in text])


def main():
    #print((decode_bits('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011')))#'.... . -.--   .--- ..- -.. .')
    #print((decode_bits('101')))
    #print(decode_morse(decode_bits('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011')))#'.... . -.--   .--- ..- -.. .'))
    print(decode_morse(decode_bits('111000111')))
    # print((decode_bits('110011')))
    # print(decode_morse(decode_bits('110011')))
    # print((decode_bits('1100111111')))
    # print(decode_morse(decode_bits('1100111111')))
##    print(decode_morse(decode_bits('110000000000000011')))
##    print(decode_morse(decode_bits('110000011')))
##    print(decode_morse(decode_bits('110011')))
##    print(decode_morse(decode_bits('11011')))

    #print(decode_morse('. .'))
##    print(decode_morse('...   ---   ...'))
    #print(decode_bits('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011'))
    #print(decode_bits('11001100000011111100111111'))
  
    
if __name__ == "__main__":
    main()    
