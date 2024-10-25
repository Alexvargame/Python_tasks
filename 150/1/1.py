import re
def text_match(text):
        patterns ='abbb?'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(text_match("ac"))
print(text_match("abbbbbbc"))
print(text_match("abbbc"))
