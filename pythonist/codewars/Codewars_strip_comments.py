import re

def strip_comments(strng, markers):
    print(strng)
    if '$' in markers:
        markers.remove('$')
        markers.append('\$')
    if '*' in markers:
        markers.remove('*')
        markers.append('\*')
    print(markers)
    st=re.split(r'[=\n]\s*', strng)
    print(st)
    for s in st:
        print('6666',s,(re.findall('|'.join(markers),s)))
        if len((re.findall('|'.join(markers),s)))>0:
            print(s.find(re.findall('|'.join(markers),s)[0]))
            print(s[:s.find(re.findall('|'.join(markers),s)[0])] )
             
    print('aaa',[s[:s.find(re.findall('|'.join(markers),s)[0])-1] if len((re.findall('|'.join(markers),s)))>0 else s for s in re.split(r'[=\n]\s*', strng)])
    return '\n'.join([s[:s.find(re.findall('|'.join(markers),s)[0])-1] if len((re.findall('|'.join(markers),s)))>0 else s for s in re.split(r'[=\n]\s*', strng) ])
   
                   
                                                    
def main():

   
    #print(strip_comments("apples, pears #! and bananas\ngrapes\nbananas !apples", ["#", "!"]))
    print(strip_comments(" oranges\napples apples . # watermelons\ncherries strawberries - cherries\ncherries lemons strawberries ^ cherries\n= watermelons pears",['#', '=', ',', '!', '@']))

    
    



   


if __name__ == "__main__":
    main()

