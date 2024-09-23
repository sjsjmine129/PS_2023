n = int(input())

print(2**n - 1)


def function(N, start, end, middle):
    if N == 1:
        print(start, end)
        return

    function(N-1, start, middle, end)
    print(start, end)
    function(N-1, middle, end, start)


function(n, 1, 3, 2)
