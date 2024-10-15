def generateParentheses(n):
    stack = []
    res = []

    def backtrack(opened, closed):

        if opened == closed == n:
            res.append(''.join(stack))
            return

        if opened < n:
            stack.append('(')
            backtrack(opened + 1, closed)
            stack.pop()
        if closed < opened:
            stack.append(')')
            backtrack(opened, closed + 1)
            stack.pop()

    backtrack(0, 0)
    return res





def main():
    print('res', generateParentheses(3))



if __name__ == "__main__":
    main()
