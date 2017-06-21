def insert_star_between_pairs(a_string):    
    prev = None
    result = ""
    tmp = []
    print a_string
    if a_string is not None:
        for curr in a_string:

            if prev == curr:
                tmp.append('*')
                tmp.append(curr)
            else:
                tmp.append(curr)
            prev = curr


        result = ''.join(tmp)
    else:
        result = None

    print result
                    
    return result


def insert_star_between_pairs_2(a_string):
    #print "before processing: " + a_string
    if a_string is None:
        print a_string
        return None
    elif len(a_string) <= 1:
        print a_string + " --- is this always the last one"
        return a_string
    elif a_string[0:1] == a_string[1:2]:
        print a_string
        #print len(a_string)
        #print "processing " + a_string[1:len(a_string)]
        return a_string[0:1] + "*" + insert_star_between_pairs_2(a_string[1:len(a_string)])
    
    print a_string
    return a_string[0:1] + insert_star_between_pairs_2(a_string[1:len(a_string)])


insert_star_between_pairs_2("aaa")