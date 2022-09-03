def isAnagram(firstWord, secondWord):
    if len(firstWord) != len(secondWord):
        # if the two words are not in the same length - they are not anagrams
        return False

    for char in firstWord:
        # checking existance of every character from the first word, in the second word
        char_index = secondWord.find(char)
        if char_index == -1:
            return False
        else:
            # removing the char from the second word so we won`t "find" it again (and gain efficiency for bonus)
            secondWord = secondWord[:char_index] + secondWord[(char_index+1):]

    return True

print(isAnagram("final", "fnial"))
