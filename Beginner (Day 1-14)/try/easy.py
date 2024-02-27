word = input()
bug_count = 0
while "TP" in word or "PT" in word:
    if "TP" in word:
        word = word.replace("TP", "PG", 1)
        bug_count += 1
    elif "PT" in word:
        word = word.replace("PT", "GP", 1)
        bug_count += 1
print(bug_count)
