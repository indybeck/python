def groupsOfAnagrams(words):
    anagrams = set()
    for w in words:
        #print sorted(w)
        #print ''.join(sorted(w))
        #print str(sorted(w))

        #anagrams.add(str(sorted(w)))
        anagrams.add(''.join(sorted(w)))
        print anagrams

    return len(anagrams)


words = ["tea", "eat", "apple", "ate", "vaja", "cut", "java", "utc"]
print groupsOfAnagrams(words)