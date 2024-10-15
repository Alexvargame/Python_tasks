def countVowelsPermutation(n):
    modulo = 10 ** 9 + 7
    cache = [1, 1, 1, 1, 1]
    a = 0
    e = 1
    i = 2
    o = 3
    u = 4

    for _ in range(n-1):
        prev = list(cache)
        cache[a] = (prev[e] + prev[i] + prev[u]) % modulo
        cache[e] = (prev[a] + prev[i]) % modulo
        cache[i] = (prev[e] + prev[o]) % modulo
        cache[o] = prev[i] % modulo
        cache[u] = (prev[i] + prev[o]) % modulo


    return sum(cache) % modulo

def main():
    print('res', countVowelsPermutation(4))



if __name__ == "__main__":
    main()
