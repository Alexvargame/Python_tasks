import re


def decode_bits(bits):
    print('bit', bits)
    n = 2
    morse_code = ''
    for b in re.split(r'0{7,14}', bits):

        if len(b) > 0:
            for bb in re.split(r'0{3,6}', b):
                if len(bb) > 0:
                    print('bb', bb, bb.split('0' * n))
                    for bbb in re.split(r'0{1,2}', bb):
                        print('bbb', bbb)
                        if len(bbb) == 2 or len(bbb) == 1:
                            morse_code += '.'
                        else:
                            morse_code += '-'
                    morse_code += ' '
            morse_code += '  '
    #     morse_code='   '.join([' '.join([''.join(['-' if len(let.strip('0'))==3*n else '.' for let in l.strip('0').split('0'*(n-1)) if len(let.strip('0'))>0])
    #                 for l in b.strip('0').split('0'*(n+1)) if len(l)>0]) for b in bits.strip('0').split('0'*(n*3+1)) if len(b)>0])

    return morse_code


def decode_morse(morse_code):
    print('code', morse_code)
    text = [m.split(' ') for m in morse_code.strip(' ').split('   ')]
    print('text', text)
    for t in text:
        for i in range(len(t)):
            if t[i] in MORSE_CODE.keys():
                t[i] = MORSE_CODE[t[i]]

    return ' '.join([''.join(t) for t in text])


def main():
    print(decode_morse('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011'))


if __name__ == "__main__":
    main()