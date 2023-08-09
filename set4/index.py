# 1. **Anagram Check**: Write a Python function that checks whether two given words are anagrams.

# Anagram - same word present in next word duplication allow 

    # - *Input*: "cinema", "iceman"
    # - *Output*: "True"
Sets = {1,2,2,3}
print(Sets)

word1 = "cinemaaa"
word2 = "icemannn"

x = set(list(word1))
y = set(list(word2))
x = sorted(x)
y = sorted(y)

x = "".join(x)
y = "".join(y)

if(x==y):
    print(True)
else:
    print(False)


# 2. **Bubble Sort**: Implement the bubble sort algorithm in Python.

# - *Input*: [64, 34, 25, 12, 22, 11, 90]

# - *Output*: "[11, 12, 22, 25, 34, 64, 90]"

list = [64, 34, 25, 12, 22, 11, 90]
list.sort()
print(list)