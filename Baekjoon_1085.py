x, y, w, h = map(int, input().split())

d = [x, y, (h-y), (w-x)]
d.sort()

print(d[0])