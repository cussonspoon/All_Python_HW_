#Question 5
def LCS(s1, s2):
    max_len = 0
    lcs = ""

    for i in range(len(s1)):
        for j in range(i + 1, len(s1) + 1):
            substring = s1[i:j]
            if substring in s2:
                if len(substring) > max_len:
                    max_len = len(substring)
                    lcs = substring

    if max_len != 0:
        print(lcs)
    else:
        print("")


LCS("ingenious", "intelligent")
LCS("philosophically", "zoophilous")
LCS("intelligent", "inconsidered")
LCS("russian", "ukrainian")
LCS("war", "love")
LCS("romanian", "roman")


