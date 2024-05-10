def longest_common_substring(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)

    # matrix to store the lengths of common substrings
    dp = [[0] * (len_str2 + 1) for _ in range(len_str1 + 1)]

    max_len = 0
    end_index = 0

    for i in range(1, len_str1 + 1):
        for j in range(1, len_str2 + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_index = i - 1
            else:
                dp[i][j] = 0

    longest_substring = str1[end_index - max_len + 1: end_index + 1]
    return longest_substring

seqs = []
with open('13.txt', 'r') as f:
    sequence = ''
    for line in f:
        if not line.startswith('>'):
            sequence += line.strip()
        elif sequence:
            seqs.append(sequence)
            sequence = ''
    seqs.append(sequence)

seqs.sort(key=len)
ln = len(seqs[0])

longestSS = seqs[0]

wind = ln
for i in range(1, len(seqs)):
    ss = longest_common_substring(seqs[0], seqs[i])
    if len(ss) < len(longestSS):
        longestSS = ss
print(longestSS)