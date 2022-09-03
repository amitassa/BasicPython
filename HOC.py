def HOC(str):
    max_occured_char = ""
    max_occured_char_appearances = 0
    checked_chars = []
    for ch in str:
        if ch not in checked_chars:
            checked_chars.append(ch)
        else:
            continue
        appearances = str.count(ch)
        if (appearances > max_occured_char_appearances):
            max_occured_char_appearances = appearances
            max_occured_char = ch
    return max_occured_char


print(HOC("aaab1111"))