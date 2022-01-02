word = input("Type any word without a space: ")
word = word.casefold()
rev_word = reversed(word)
if list(word) == list(rev_word):
	print("The word is palindrome.")
else:
	print("The word is not a palindrome.")