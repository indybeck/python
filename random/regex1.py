import string
from collections import deque

def regularExpressionMatching(s, p):

    alpha_letters = frozenset(string.ascii_letters)
    block = [".", "*", ".*"]
    seq = []

    result = False

    for ch in s:
        if ch in alpha_letters:
            seq.append(".*{0}*".format(ch))
        else:
            result = False

    reduced_seq = []
    for x in seq:
        if x not in reduced_seq:
            reduced_seq.append(x)
    #print reduced_seq

    p_seq = []
    dequeue = deque(p)
    print dequeue
    x1 = dequeue.popleft()
    print x1
    if x1 == '*':
        result = False
    else:
        while dequeue:
            if x1 in alpha_letters:
                print x1
                x2 = dequeue.popleft()
                    # print x1
                    # print x2
                    # print "---> {0}".format(x1.join(x2))
                    p_seq.append(".*{0}{1}".format(x1, x2))
                    pass

            elif x1 == '.':
                # '.' - don't popleft and move on ..
                pass

            else:
                # this should be a garbage in p; but we never know
                print "debug: {0}".format(x1)

            x1 = dequeue.popleft()
            print p_seq


    print p_seq





regularExpressionMatching("caab", "d*c*x*a*b")

# c a b
# .*d*, .*c*, .*x*, .*a*, .*b

# .* - c - -.* -  a* - b

# .*, ., ., ., .