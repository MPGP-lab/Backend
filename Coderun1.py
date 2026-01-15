from collections import Counter

n = int(input())
a = list(map(int, input().split()))

cnt = Counter(a)
ans = 0

for v in cnt.values():
    if v == 1:
        ans += 1
 
print(ans)
