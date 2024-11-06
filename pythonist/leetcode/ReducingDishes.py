def maxSatisfaction(satisfaction):
    total = 0
    satisfaction_total = 0
    for s in sorted(satisfaction, reverse=True):
        satisfaction_total += s
        if satisfaction_total <= 0:
            return total
        total += satisfaction_total

    return total


def main():
    print('res', maxSatisfaction(satisfaction=[-1, -8, 0, 5, -9]))



if __name__ == "__main__":
    main()
