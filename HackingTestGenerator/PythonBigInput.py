def create_hack(a, b, n):
    pow2 = 2 ** ((b - a - 1).bit_length() - 1)
    start = 858993459 % pow2

    def sequence(x, CPython=False):
        i = perturb = hash(x)
        i %= pow2
        yield i
        while True:
            if CPython:
                perturb >>= 5
            i = (5 * i + perturb + 1) % pow2
            yield i
            if not CPython:
                perturb >>= 5

    def prime_dict(a, b, n):
        A = set()

        for i in sequence(start, True):
            i = i + (a + 1 - i + pow2 - 1) // pow2 * pow2
            if i == start:
                i = i - pow2 if i - pow2 >= a else i + pow2
            A.add(i)
            if len(A) == 10:
                break

        for i in sequence(start, False):
            i = i + (a + 1 - i + pow2 - 1) // pow2 * pow2
            if i == start:
                i = i - pow2 if i - pow2 >= a else i + pow2
            A.add(i)
            if len(A) == n or len(A) == pow2 // 2 - 10:
                break

        assert all(a <= x < b for x in A)

        return sorted(A)

    A = prime_dict(a, b, n // 2)
    while len(A) < n:
        A.append(start)
    return A

# import sys
# input_file = open(r'samples.txt', 'w');sys.stdout = input_file

n=2*10**5
MX= 10**9
A = create_hack(1,MX,n)
print(1)
print(n,n)
print(*A,sep=' ')

# print(max(A),min(A))