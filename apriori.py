
with open('basket.txt', 'r') as f:
    l = []
    for line in f:
        l.append(line.rstrip().split(','))
print(l)