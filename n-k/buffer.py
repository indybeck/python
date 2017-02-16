# prototype of buffered version;
# simulate with n with range size
import random

# simplified version
n = range(1000000)
k = 20
_buf_size = 100

def buf_read(n, k, buffer_size=100):

    candidates = []
    i = 0
    for _buf in [n[i:i+buffer_size] for i in xrange(0, len(n), buffer_size)]:
        #print _buf
        for v in sample(_buf, k):
            candidates.append(v)

    #print candidates
    return sample(candidates, k)


# using random sample function
def sample(n, k):
    return random.sample(n, k)


#getSample(n, k)
#print sample(n, k)

print buf_read(n, k, _buf_size)