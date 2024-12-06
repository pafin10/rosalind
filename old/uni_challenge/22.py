with open('22.txt', 'r') as f:
    alphabet = f.readline().split()
    n = int(f.readline())

alphabet.sort()
strings = []


def generatePermutations(n, alph):
    out = []

    def recursive_permutations(current_str, depth):
        if depth == n:
            out.append(current_str)
            return

        for char in alph:
            recursive_permutations(current_str + char, depth + 1)

    recursive_permutations("", 0)
    return out


ans = generatePermutations(n, alphabet)
print(*ans, sep="\n")
