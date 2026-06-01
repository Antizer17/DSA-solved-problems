import sys

input_data = sys.stdin.read().split()
if not input_data:
    sys.exit()

N, M = int(input_data[0]), int(input_data[1])
viruses = input_data[2:]

base = 31
mod = (1 << 61) - 1
hashCount = {}
fullHash = []
powArr = [1] * M
total_pairs = 0

for i in range(1, M):
    powArr[i] = (powArr[i-1] * base) % mod

for v in viruses:
    h = 0
    for char in v:
        val = ord(char) - ord('a') + 1
        h = (h * base + val) % mod 
    hashCount[h] = hashCount.get(h, 0) + 1
    fullHash.append(h)

for j in range(M):
    freq = {}
    p_idx = M - 1 - j
    p = powArr[p_idx]
    for strings in range(N):
        hashed_val = ord(viruses[strings][j]) - ord('a') + 1
        masked_hash = (fullHash[strings] - hashed_val * p) % mod
        count = freq.get(masked_hash, 0)
        total_pairs += count
        freq[masked_hash] = freq.get(masked_hash, 0) + 1

duplicate_pairs = 0       
for count_val in hashCount.values():
    if count_val > 1:
        duplicate_pairs += (count_val * (count_val - 1)) // 2     

duplicate_pairs *= M

print(input_data)
