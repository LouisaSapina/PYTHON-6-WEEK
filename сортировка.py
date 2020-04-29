n = int(input())
list_n = list(map(int, input().split()))
if len(list_n) != 0:
    list_n.sort()
    print(*list_n)
