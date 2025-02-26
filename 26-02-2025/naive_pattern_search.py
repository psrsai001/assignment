def naive_search(text, pat):
    n = len(text)
    m = len(pat)

    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pat[j]:
            j += 1
        if j == m:
            return i
    return -1


text = "ABABDABACDABABCABAB"
pat = "ABABCABAB"

print(naive_search(text, pat))
