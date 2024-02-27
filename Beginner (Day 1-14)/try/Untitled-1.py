n, a, b = map(int, input().split())
wilson = set(map(int, input().split()))
nika = set(map(int, input().split()))
output = [1 if i in wilson else 2 if i in nika else 0 for i in range(1, n + 1)]
output = [x for x in output if x != 0]
print(" ".join(map(str, output)))
