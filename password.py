with open("keylog.txt", "r") as f:
    lines = f.readlines()

counts = {}
for l in lines:
    l = l.strip()
    counts[l[0]] = counts.get(l[0], 0) - 1
    counts[l[2]] = counts.get(l[2], 0) + 1

for w in sorted(counts, key=counts.get):
    print(w, end='')