def find_anagrams(word, anagram):
    
    container = []
    anagram_container = []

    for i in word:
        container.append(i)
    for i in anagram:
        anagram_container.append(i)
    container.sort()
    anagram_container.sort()
    if anagram_container == container:
        print(True)
    else:
        print(False)
    return True

find_anagrams("below😎", "elb😂ow") # returns true
find_anagrams("hello", "fake") # returns false
