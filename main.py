#Create a function that takes in a string, reverses it, and then checks if the reversed string is the same as the original, therefore making it a palindrome. Uses lists to compare the two words.


def palindrome_checker(word):
    reversedWord = []
    for letter in word:
        reversedWord.insert(0, letter)
    listWord = list(word)

    if reversedWord == listWord:
        return True
    else:
        return False


#test

print(palindrome_checker('potato'))
print(palindrome_checker('racecar'))
