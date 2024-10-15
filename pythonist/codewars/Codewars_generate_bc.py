import re

import re
def generate_bc(url, separator):
    print(url)
    url_lst =[]#[u[:min([(m.start()) for m in re.finditer(r'[#?-]',u)])] for u in url.split('/') if u not in ['https:', '', 'http:']]
    for u in url.split('/'):
        if u not in ['https:', '', 'http:']:
            print(re.findall(r'[#?=]',u))
            if re.findall(r'[#?=]',u):
                url_lst.append(u[:min([(m.start()) for m in re.finditer(r'[#?=]',u)])])
            else:
                url_lst.append(u)
    print(url_lst)
    if len(url_lst) == 1:
        return '<span class="active">HOME</span>'
    if 'index' in url_lst[-1]:
        url_lst=url_lst[:-1]
    print(url_lst)
    astr = ''
    lnk = ''
    home = '<a href="/">HOME</a>' + separator
    for s in url_lst[1:-1]:
        if len(s)>30:

            slst = [w[0] for w in s.split('-') if
                        w not in ["the", "of", "in", "from", "by", "with", "and", "or", "for", "to", "at", "a"]]
            print('SL',slst)
            sl = ''.join(slst)
        else:
            sl = s#' '.join(s.split('-'))
        lnk += '/' + s + '/'
        astr += f'<a href="{lnk}">' + sl.upper() + '</a>' + separator
        lnk = lnk[:-1]
    print(' '.join(url_lst[-1].split('.')[0].split('-')))
    print([w[0] for w in url_lst[-1].split('.')[0].split('-') if
                      w not in ["the", "of", "in", "from", "by", "with", "and", "or", "for", "to", "at", "a"]])
    if len(' '.join(url_lst[-1].split('.')[0].split('-'))) > 30:
        sp = ''.join([w[0] for w in url_lst[-1].split('.')[0].split('-') if
                      w not in ["the", "of", "in", "from", "by", "with", "and", "or", "for", "to", "at", "a"]])

    else:
        sp = ' '.join(url_lst[-1].split('.')[0].split('-'))

    span = '<span class="active">' + sp.upper() + '</span>'
    print(home)
    print(astr)
    print(span)
    return home+astr+span

def main():
    print(generate_bc("http://www.linkedin.it/app/kamehameha-uber-insider-eurasian-and-uber-at-from", " > "))
    
    
  
    
if __name__ == "__main__":
    main()
