N, K = map(int, input().split())

w = [0]
v = [0]
record = []

for i in range(1, N+1):
    W, V = map(int, input().split())
    w.append(W)
    v.append(V)

for i in range(N+1):
    record.append([0 for item in range(K+1)])

# print(record)
# print(w)
# print(v)

for k in range(1, K+1):
    for i in range(1, N+1):
        temp = record[i-1][k]
        if w[i] <= k:
            if temp < v[i]+record[i-1][k-w[i]]:
                temp = v[i]+record[i-1][k-w[i]]

        record[i][k] = temp

# for i in record:
#     print(i)
print(record[N][K])
