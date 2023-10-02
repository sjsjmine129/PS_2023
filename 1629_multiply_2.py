import sys
input = sys.stdin.readline
A, B, C = map(int, input().split())


def mul_modeC(b):
    if b == 1:
        return A % C

    int_b = b//2

    if (b % 2 == 0):
        temp = mul_modeC(int_b)
        return (temp*temp) % C
    else:
        return (mul_modeC(int_b+1) * mul_modeC(int_b)) % C


print(mul_modeC(B))
