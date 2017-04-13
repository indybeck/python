import re
from itertools import groupby
from collections import deque

def integerValueOfRomanNumeral(s):
    romans = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000
    }

    invalids = ["XLX", "VC", "LC", "VV", "LL" ]

    s_test = "XLX"
    result = 0
    sum = 0


    """
     process 3 letters -
     III = 3
     if 3 letter contains
     IV = 4
     IX = 9
     IL = -1  : XLIX = 49

     XL = 40 (next letter is bigger .. in the same class 10 and 50 )
     XLX  --> this is L  so  -1 if this value matches to any of letter's value then return -1
    """

    print s
    # test if romans are incorrect thus, return -1
    print len([invalid for invalid in invalids if invalid in s])

    if len([invalid for invalid in invalids if invalid in s]) > 0:

        result = -1
        print result
    else:
        for k, g in groupby(s):
            if k != "M" and len(list(g)) > 3:
                result = -1

    # go after combined number 2 digit XI, IX, IV, VI, XC, CX
    # actually only thing care are: IV, IX, XL, XC, CD, CM
    debug = True
    if result != -1:
        print "here .... "
        queue = deque(list(s))
        while queue:
            curr = queue.pop()
            print "curr -- {0}".format(curr)
            if curr == "V" and len(queue) > 0:
                # followed by I -> IV
                n = queue.pop()
                print "n -- {0}".format(n)
                if n == "I":
                    sum += romans["IV"]
                else:
                    queue.append(n)
                    sum += romans[curr]
                    #sum += romans[n]

            elif curr == "X" and len(queue) > 0:
                # followed by I  IX 9
                n = queue.pop()
                print "n -- {0}".format(n)
                if n == "I":
                    sum += romans["IX"]
                else:
                    queue.append(n)
                    sum += romans[curr]
                    #sum += romans[n]

            elif curr == "L" and len(queue) > 0:
                n = queue.pop()
                if n == "X":
                    sum += romans["XL"]
                else:
                    queue.append(n)
                    sum += romans[curr]

            elif curr == "C" and len(queue) > 0:
                # followed by X  - XC 90
                n = queue.pop()
                print "n -- {0}".format(n)
                if n == "X":
                    sum += romans["XC"]
                else:
                    queue.append(n)
                    sum += romans[curr]
                    #sum += romans[n]

            elif curr == "D" and len(queue) > 0:
                # followed by C - CD 400
                n = queue.pop()
                if n == "C":
                    sum += romans["CD"]
                else:
                    queue.append(n)
                    sum += romans[curr]
                    #sum += romans[n]

            elif curr == "M" and len(queue) > 0:
                # followed by C - CM 900
                n = queue.pop()
                if n == "C":
                    sum += romans["CM"]
                else:
                    queue.append(n)
                    sum += romans[curr]
                    #sum += romans[n]

            else:
                sum += romans[curr]

            if debug:
                #print len(queue)
                print queue
                print "sum is {0}".format(sum)

        result = sum

    print "sum -->"
    return result


print "----"
print integerValueOfRomanNumeral("MMCDXV")

#MDCCXLI - 1741
#MMCXLIV - 2144

#MMCDXV