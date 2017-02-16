# Description
# N items, where N cannot fit in memory
# select K items, where K can fit in memory, out of N such that each items in N has 1/N opportunities to be picked.

import random

# simplified version
n = ['a','b','c']
k = 2

def getSample(n, k):
    result = []
    for i, v in enumerate(n):
        if i < k:
            result.append(v)
        else:
            p = random.randrange(i+1)
            # print i
            # print p
            if p < k:
                result[p] = v
            print result

# using random sample function does all that, if we rely on python random, we should just use sample function
def sample(n, k):
    print random.sample(n, k)

#getSample(n, k)
sample(n, k)