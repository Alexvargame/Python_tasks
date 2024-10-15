def spin_words(sentence):
    print(sentence.split(' '))
    new_sentence=' '.join([word[::-1] if len(word)>4  else word for word in sentence.split(' ')])
    print(new_sentence)
   
    return None
 
def main():

    print(spin_words("Hey fellow warriors"))
    print(spin_words("This is a test"))
    print(spin_words("This is another test"))
       

   

if __name__ == "__main__":
    main()    
