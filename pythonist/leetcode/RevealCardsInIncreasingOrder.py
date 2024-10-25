import collections
def deckRevealedIncreasing(self, deck: List[int]):
    deck.sort()
    q = collections.deque(range(len(deck)))
    res = [0]*len(deck)
    for num in deck:
        idx = q.popleft()
        res[idx] = num
        if q:
            q.append(q.popleft())

    return res



def main():
    print('res', deckRevealedIncreasing([17,13,11,2,3,5,7]))



if __name__ == "__main__":
    main()
