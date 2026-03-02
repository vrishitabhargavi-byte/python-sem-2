def reverse_vowels(s):
    vowels = "aeiouAEIOU"
    a = list(s)
    i = 0
    j = len(a) - 1

    while i < j:
        if a[i] not in vowels:
            i += 1
        elif a[j] not in vowels:
            j -= 1
        else:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1

    result = ""
    for k in a:
        result=result+k
    return result
print("Reverse vowel is", reverse_vowels("leetcode"))