def upsidedown(a, b):
    a, b = str(a), str(int(b) + 1)
    ans = _solve_len_ge(len(a), a)
    for i in range(len(a) + 1, len(b) + 1):
        ans += _solve_len(i)
    return ans - _solve_len_ge(len(b), b)
    
def _solve_len(n):
    if n == 1: return 3
    if n % 2 == 0: return 4 * 5 ** (n // 2 - 1)
    return 4 * 5 ** (n // 2 - 1) * 3
def _solve_len_w0(n):
    if n % 2 == 0: return 5 ** (n // 2)
    return 5 ** (n // 2) * 3
def _solve_len_ge(n, v):
    tmp = ''
    print('n',n,'v',v)
    ans = _solve_len_w0(n)
    print(ans)
    for i in range(n // 2):
        for d in '01689':
            print('d',d,'v[]',v[:i+1])
            if tmp + d < v[:i+1]:
                ans -= _solve_len_w0(n - 2 - i * 2)
                print(ans)
            elif tmp + d > v[:i+1]:
                print(ans)
                return ans
            else:
                tmp += d
                print(tmp)
                break
        else: return ans
    if n % 2:
        i = n // 2
        for d in '018':
            if tmp + d < v[:i+1]:
                ans -= 1
            elif tmp + d > v[:i+1]:
                return ans
            else:
                tmp += d
                break
        else: return ans
    trans = str.maketrans('69', '96')
    tmp += (tmp[::-1] if n % 2 == 0 else tmp[:-1][::-1]).translate(trans)
    return ans - (tmp < v)

def main():
    
    print(upsidedown('100000','12345678900000000'))
    
    
  
    
if __name__ == "__main__":
    main()

