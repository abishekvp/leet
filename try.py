from collections import defaultdict

def groupAnagrams(strs):
    anagrams = defaultdict(list)  # key: sorted word, value: list of anagrams
    print(anagrams)
    for word in strs:
        key = ''.join(sorted(word))  # sort letters to form the key
        anagrams[key].append(word)

    return list(anagrams.values())

# Example usage
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
