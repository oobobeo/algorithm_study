# 12951
# input -> sys.stdin.readline().strip()

import sys

trees = {} # {name: num, ..}
count = 0
while True:
    tree_name = sys.stdin.readline().strip()
    if not tree_name: break
    count += 1
    if tree_name in trees:
        trees[tree_name] += 1
    else:
        trees[tree_name] = 1

# sort by name
tree_names_sorted = sorted(list(sorted(trees.keys())))


# num -> percentage
for k in tree_names_sorted:
    percentage = round(trees[k]/count*100,4)
    percentage = "{:.4f}".format(percentage)
    print(f"{k} {percentage}")

