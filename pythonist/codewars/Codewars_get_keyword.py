def get_keyword(ciphertext, key_len):
    print(ciphertext, key_len)
    result=''
    key='CODEWARS'
    #print([ord(let)-ord(key[0]) for let in key])
    key_steps=[ord(let)-ord('A') for let in key[:key_len+1]]
    print(key_steps)
    #key=key*(int(len(ciphertext)/key_len)+1)
    for i in range(len(ciphertext)):
        key_index=(i%key_len)
        print('i',i,'I',key_index,'dddd',key_steps[key_index])
        if ord(ciphertext[i])-key_steps[key_index]<65:
            print('<65','C',ciphertext[i],'ORDC',ord(ciphertext[i]),'S',key_steps[key_index])
            result+=chr(ord(ciphertext[i])+key_steps[key_index]-91+ord('A'))
        else:
            print('>65','C',ciphertext[i],'ORDC',ord(ciphertext[i]),'S',key_steps[key_index])
            if ord(ciphertext[i])+key_steps[key_index]<91:
                result+=chr(ord(ciphertext[i])+key_steps[key_index])
            else:
                result+=chr(ord(ciphertext[i])+key_steps[key_index]-91+ord('A'))
        print(result)
        input()
    return result
        
def main():
    #gen('RGB')
      

    print(get_keyword("MTZPYGMDZQIIJQYVZTHURKOJVNGRZTNQIUNRZCFAJWMVMWOJLWDGONTCIFXNZCMNTCIFGKNVZPOQJVCGMUZXZPOJZFPNGCIFDIIQMCIVOJZAOQJJVXZVCGDTNVJTTCQQDFGQPFVPYCBIMGNUDXZRZTNQIUOJZAVTZXZZVVDQPUOQOJZUKKMKOKAAJWXQHRVTZAJWMUZNAYDVCQOJZTTQPOVAWGXQHGQCDPVPYDDVOGMHJTVNRCTUOJZTZYDNGDZIMGVVZTVPYNZUNGMRZTNQIUOJVPTQPTNGGHZPEQTAJWMCXJDGQGHGIVNCNYZNGCNAJWMRGCIUFGZRDPOGMGNVZFDPTQPTJYIEVTZGMJJYZXZTCWHDGGDVDUVTZCGRJUNGNUDQIKIVCGXJVPBKIIAQMVPPZUJHOKHGZZZTXKNGXCPVDQIKIAJWMDPUDPZUNCAHVKMUAQMVCGRQMNYKNHPNGQAVMKXMZTTDPVGGOVCKNPJVWNDPYAJWOQRJVVQKMVPGOJZTZKNOVPTRZTNQIUNVMKQGAQMJDICKYGVNNCIFZXZTTYCGMGGKAGDUAWGNJHCGMQDUHDZAJWMUZNAGNRZEDCGNTFJPJVAGDIICAHZEOKJPIGDVCGMDZETPDEVNVDJWONJXZHJTDPOJZHVEZQACGNVTDFDVTCIFYKNGIECCIVHGIVDVDUKGMGIPDCGCNVCGBTVUNVVMZMDPYNTVCGXQPPNGGQAVCGTGVTNIMCXGAWGNTUPTMGIFZTDPBVCGOJDPBUJHTQPVCPPTOWMGNVMGIIOJJHNRDTDVOQNJDGGFTQPKIUPFYGIODUAQMVPPZDPVYQIQOFDUOTZUNAJWMUZNAYDVCKHCBKIKIINOVPTHZCMUVTZDJTIQAHVVDIPGVPYNJPZNDPZUNDZAJPYCRJJNZUJOZFDUXKKNDPZDZIZPONZYDVCAJWMUZNAAJWVTZCXJDNYQAVCGPPDXZTNGIQGGNUOJVPOJZVMGZUVPYVCG", 8))

    
    
  
    
if __name__ == "__main__":
    main()


##for i in range(len(ciphertext)):
##        key_index=(i%key_len)
##        print('i',i,'I',key_index)
##        try:
##            step=ord(key[i])-ord('A')
##        except:
##            step=ord(key[i-len(key)])-ord('A')
##        if ord(ciphertext[i])-step<65:
##            print('<65','C',ciphertext[i],'ORDC',ord(ciphertext[i]),'S',step)
##            result+=chr(ord(ciphertext[i])+step-91+ord('A'))
##        else:
##            print('>65','C',ciphertext[i],'ORDC',ord(ciphertext[i]),'S',step)
##            result+=chr(ord(ciphertext[i])+step)
##        print(result)
##        input()
