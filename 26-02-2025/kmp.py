def compute_lps(pat):
    n = len(pat)
    length, i = 0, 1
    lps = [0] * n
    while i < n:
        if pat[i] == pat[length]:
            lps[i] = length + 1
            length += 1
            i += 1
        elif length != 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1
    return lps


def kmp_search(text, pat):
    n = len(text)
    m = len(pat)
    lps = compute_lps(pat)
    i = j = 0

    while i < n:
        if text[i] == pat[j]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and text[i] != pat[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


text = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
print(compute_lps(pat))
print(kmp_search(text, pat))
