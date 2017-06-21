import string
def regularExpressionMatching(s, p):
    print s
    letters = frozenset(string.ascii_letters)
    print letters
    idx = 0
    isMatch = True
    prevCh = ''

    # process patter . and *
    #  1. single '.'
    #  something and *

    # d*c*x*a*b
    for curr in p:
        if isMatch:

            if curr == '.':
                # get letter in s[idx]
                if s[idx] in letters:
                pass
            elif curr == '*':
                if not prevChar:
                    isMatch = False
                else:
                    if prevChar == '.':
                        # repeating any letters
                    else:
                        # d* -- a letter and *
                        # see if prevch is a match in s ..
                        for c in s:
                            if c == prevChar:

            else:
                # handle "*
                # this should be just letters
                prevChar = curr
                if curr != s[idx]:
                    isMatch = False

            # follow the letter location
            idx += 1

    for c in s:
        if c in letters:
            print "yes"

regularExpressionMatching("caab", "d*c*x*a*b")