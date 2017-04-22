
syns = set(["run", "sprint", "jog"])
text1 = "go for a run"
text2 = "go for a jog"
N = 3

def generate_tuples(text, N):
    tmpList = text.split()
    #print len(tmpList) - N
    sublist = [tmpList[x:x+N] for x in range(0, len(tmpList)-N+1)]
    #print sublist

    return sublist

def compare_with_synonyms(t1, t2):
    result = True
    for i in range(len(t1)):
        if t1[i] != t2[i]:
            if t1[i] not in syns or not t2[i] in syns:
                result = False
    return result


# variables for counters
match_count = 0
#not_match_count = 0
total = 0
DEBUG = True

# generate n-tuples
tuples1 = generate_tuples(text1, N)
tuples2 = generate_tuples(text2, N)

# run through compare  --> insert assert code for testing ..
for idx in range(len(tuples1)):
    if DEBUG:
        print "comparing {0} and {1}".format(tuples1[idx], tuples2[idx])
    #print compare_with_synonyms(tuples1[idx], tuples2[idx])
    if compare_with_synonyms(tuples1[idx], tuples2[idx]):
        #print "match"
        match_count += 1
    else:
        #print "not match"
        #not_match_count += 1
        pass
    total += 1

print "{0}%".format(match_count / total * 100)
