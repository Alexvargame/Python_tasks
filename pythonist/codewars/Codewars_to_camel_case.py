import re

def to_camel_case(text):
    return re.split(r'-|_',text)[0]+''.join([word.capitalize() for word in re.split(r'-|_',text)[1:]])

def main():

    
   
    print(to_camel_case("the-stealth-warrior"))
   
   


if __name__ == "__main__":
    main()

