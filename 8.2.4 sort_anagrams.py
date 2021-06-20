def count_letters(word1, word2):
    """The function takes two words and counts its letters to find an anagram.
    :param word1: a given word
    :param word2: a given word
    :type word1: str
    :type word2: str
    :return True/False: True if the two words have the same letters in the same amount.
    :rtype: bool"""
    for letter in word1:
        if letter in word2:
            if word1.count(letter) != word1.count(letter):
                return False
    return True


def sort_anagrams(list_of_strings):
    """The function take a list of strings and returns a list of lists with the words of the same letters (anagrams).
    :param list_of_strings: list of strings.
    :type list_of_strings: list
    :return anagrams_list: list of lists with words of the same letters (anagrams).
    :rtype anagrams_list: list"""
    anagrams_list = []
    for string in list_of_strings:
        inside_list = []
        for word in list_of_strings:
            if len(string) == len(word) and count_letters(string, word) is True:
                inside_list.append(word)
        if inside_list not in anagrams_list:
            anagrams_list.append(inside_list)
    return anagrams_list


print(sort_anagrams(['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters', 'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']))
