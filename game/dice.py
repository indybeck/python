import random

count_odd = 0
count_even = 0
number_count = {}
counter = 0

for x in range(1,7):
    number_count[x] = 0

#print number_count
for game in range(1, 11):
    print "starting game {0}".format(game)
    for x in range(100000):
        n = random.randint(1,6)
        #print n

        number_count[n] += 1
        num_type = n % 2
        #print num_type
        if num_type == 0:
            count_even += 1
            #print "{0} is even!".format(n)

        else:
            count_odd += 1
            #print "{0} is odd!".format(n)


    print "the tally count even: {0}".format(count_even)
    print "the tally count odd: {0}".format(count_odd)

    #print number_count
    print "==========================="
    print "count for each number"
    print "==========================="
    for k, v in number_count.iteritems():
        print "count for {0} is {1}".format(k, v)

    print "==========================="
    print ""
    print "End of the game !!"
    if count_even > count_odd:
        print "The even is winner"
    else:
        print "The odd is winner"
