def dailyTemperatures(temperatures):

    res = [0]*len(temperatures)
    stack = []

    for i, tmp in enumerate(temperatures):
        while stack and stack[-1][1] < tmp:
            prev_idx, prev_tmp = stack.pop()
            res[prev_idx] = i - prev_idx
        stack.append([i, tmp])
    #
    # for i in range(1, len(temperatures)):
    #     print("TEMP - I - I-1", temperatures[i], temperatures[i-1], i)
    #     if temperatures[i] > temperatures[i-1]:
    #         print('BIGGER')
    #
    #         res[i-1] = 1
    #         stack.pop()
    #         if stack:
    #             print('!!!!!Qeq')
    #             j = len(stack) - 1
    #             while temperatures[i] > stack[-1][1]:
    #                 print(stack)
    #                 stack.pop()
    #                 res[stack[-1][0]+1] = i - stack[-1][0]+1
    #         stack.append((i, temperatures[i]))
    #         print('BIGGER res stack', res, stack)
    #     else:
    #         print('SMALLER')
    #         if temperatures[i] < stack[-1][1]:
    #             stack.append((i, temperatures[i]))
    #         else:
    #             print('!!!!!Qeq')
    #             j = len(stack)-1
    #             while temperatures[i] > stack[j][1]:
    #                 stack.pop()
    #             res[i-1] = i-stack[-1][0]
    #         print('SMALKLE res stack', res, stack)
    return res

def main():
    print('res', dailyTemperatures([73,74,75,71,69,72,76,73]))



if __name__ == "__main__":
    main()
