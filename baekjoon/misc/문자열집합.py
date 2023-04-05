# 14425





import sys





N,M = map(int, input().split())

# 26 * 10000 * 4B = 260KB = 0.25 MB
# 500 word -> max = 0.25*500 = 125MB

MAX = 10000*500 + 10

idx = 1 # fresh index
next = [[-1]*26 for _ in range(MAX)]
chk = [-1]*MAX

def w2l(word):
    return [ord(x)-97 for x in word]

# insert
for _ in range(N):
    curr = 0 # root
    word = w2l(sys.stdin.readline().strip())
    for x in word:
        if next[curr][x]:
            curr = next[curr]


# find



