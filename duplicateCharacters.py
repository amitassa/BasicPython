def removeDuplicates(str):
    duplicate_chars = []
    newString = ""
    for i in range(0, len(str)):
        ch = str[i]
        if ch in duplicate_chars:
            continue
        if str.count(ch) > 1 and (ch not in duplicate_chars):
            duplicate_chars.append(ch)
        newString += ch
    return newString

print(removeDuplicates("sccrarraasfasd"))
