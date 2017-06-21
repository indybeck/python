def unique_chars_in_string(input_string):
    bag = set()
    for c in input_string:
        if c not in bag:
            bag.add(c)
        else:
            return False
    
    return True

def unique_chars_in_string2(input_string):
	#print set(input_string)
	#print input_string
	return len(set(input_string)) == len(input_string)

#print(unique_chars_in_string(""))
print (unique_chars_in_string2("abcedd"))