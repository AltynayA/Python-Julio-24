def runnerUp(n, arr):
    newlist = list(map(int, arr))
    newlist.sort()
    nodupl = []
    for i in range(len(newlist)):
        if newlist[i] not in nodupl:
            nodupl.append(newlist[i])
    print(nodupl[-2])
    




if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    runnerUp(n, arr)