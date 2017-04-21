Let's define a group of anagrams as a list of words, where for each pair of words w1 and w2, w1 is an anagram of w2.

Given a list of words, split it into the smallest possible number of groups of anagrams and return this number as the answer.

Example

For words = ["tea", "eat", "apple", "ate", "vaja", "cut", "java", "utc"], the output should be
groupsOfAnagrams(words) = 4.

The 4 groups of anagrams in this example are ("tea", "eat", "ate"), ("apple"), ("vaja", "java"), and ("cut", "utc").

Input/Output

[time limit] 4000ms (py)
[input] array.string words

A list of words, each containing only lowercase English letters.

Guaranteed constraints:
1 ≤ words.length ≤ 105,
1 ≤ words[i].length ≤ 10.

[output] integer

The smallest possible number of groups of anagrams into which words can be split.