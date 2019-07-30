from collections import defaultdict


def anagram_dict(word1, word2):
    result = {}
    for word in word1:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1

    for word in word2:
        if word in result:
            result[word] -= 1
        else:
            result[word] = 1
    for value in result.values():
        if value != 0:
            return False
    return True


def anagram(word1, word2):
    return is_equal(sorted(word1), sorted(word2))


def is_equal(word1, word2):
    if len(word1) != len(word2):
        return False
    for idx in range(len(word1) - 1):
        chara = word1[idx]
        charb = word2[idx]
        if chara != charb:
            return False
    return True


def anagram_fast(word1, word2):
    result = defaultdict(int)

    for word in word1:
        result[word] += 1

    for word in word2:
        result[word] -= 1

    for values in result.values():
        if values != 0:
            return False
    return True


word1 = 'atds'
word2 = 'dasst'

print(anagram(word1, word2))
print(anagram_fast(word1, word2))
print(anagram_dict(word1, word2))
