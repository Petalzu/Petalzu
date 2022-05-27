from string import whitespace

#to check if a string has a balanced number of parenthesis
def is_balanced(text, brackets="()[]{}<>"):
    counts = {}
    left_for_right = {}
    for left, right in zip(brackets[::2], brackets[1::2]):
        assert left != right, "the bracket characters must differ"
        counts[left] = 0
        left_for_right[right] = left
    for c in text:
        if c in counts:
            counts[c] += 1
        elif c in left_for_right:
            left = left_for_right[c]
            if counts[left] == 0:
                return False
            counts[left] -= 1
    return not any(counts.values())

#presented in the previous chapter
def shorten(text, length=25, indicator="..."):
    if len(text) > length:
        text = text[:length - len(indicator)] + indicator
    return text

#to strip spurious characters, e.g. whitespace, from a string
def simplify(text,delete=""):
    result = []
    word = ""
    for char in text:
        if char in delete:
            continue
        elif char in whitespace:
            if word:
                result.append(word)
                word = ""
        else:
            word += char
    if word:
        result.append(word)
    return " ".join(result)

#checks if str1 is a substring of str2
def is_included(str1,str2):
    if str1 in str2:
        print(f'"{str1}" contains "{str2}"')
    else:
        print(f'"{str1}" does not contain "{str2}"')