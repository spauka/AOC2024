from collections import Counter

l1, l2 = [], []
with open("../inputs/input1") as f:
    for line in f:
        i1, i2 = [int(i) for i in line.strip().split()]
        l1.append(i1)
        l2.append(i2)

l1.sort()
l2.sort()
c1 = Counter(l2)

print(sum(abs(i1-i2) for i1, i2 in zip(l1, l2)))
print(sum(n*c1[n] for n in l1))
