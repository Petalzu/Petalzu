
import string


sentence = input("please enter a sentence:")
for w in string.punctuation:
    sentence = sentence.replace(w ,"")
words = sentence.split()
word = max(words, key=len, default='')
num = len(words)
print("the sentence has ",num,"words and the longest word is ",word)