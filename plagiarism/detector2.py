import sys
import os

# error_codes = {
#     1: "InvalidNumberOfInputs",
#     2: "TooLargeTupleSize"
# }

usages = {
    1: "ERROR: 3 required args: \n\tsynonyms_file \n\tinput_file_1 \n\tinput_file_2\nOne optional arg: \n\ttuple size(N=3 by default)\n",
    2: "ERROR: Tuple size is too large or too small for input files\n",
    3: "usage help for error code 3"
}


class FileSizeTooLarge(Exception):
    '''
    example of custom exception
    '''
    pass


def check_input_args(no_args):
    # valid values: 3, 4
    assert (2 < no_args < 5), usages[1]
    return True


def build_dict(line):
    syns = {}
    for w in line.split():
        syns[w] = line.split()

    return syns


def generate_tuples(text, N):
    tmpList = text.split()
    #print len(tmpList) - N
    sublist = [tmpList[x:x+N] for x in range(0, len(tmpList)-N+1)]
    #print sublist

    return sublist


def compare_with_synonyms(t1, t2, syns_dict):
    result = True
    for i in range(len(t1)):
        if t1[i] != t2[i]:
            if t1[i] in syns_dict.keys():
                if t2[i] not in syns_dict[t1[i]]:
                    result = False
            else:
                result = False

    return result


''' -------------------------------------------------------
main - start from here
------------------------------------------------------- '''
def main():

    # variables for counters
    match_count = 0
    total = 0
    DEBUG = True  # personal debug
    N = 3  # default value for tuple size
    max_tuple_size = 4  # set it larger than default tuple size of 3
    tunable_tuple_size = 100

    syns_dict = {}
    input_filenames = []
    input_texts = {}
    _bufsize = 1024  # 1024MB buffer size for input file handling

    # check command line args
    try:
        check_input_args(len(sys.argv[1:]))

        # building dictionary
        ''' -------------------------------------------------------
        Building dictonary from synonyms input file
        arg1: syns.txt
        ------------------------------------------------------- '''
        filename = sys.argv[1]
        with open(filename, 'r') as f:
            for line in f:
                syns_dict.update(build_dict(line))

        if DEBUG:
            print "INFO: dictionary has created successfully"
            print syns_dict

        # building corpus from input files
        ''' -----------------------------------------------------------
         processing 2 corpus from arg2, arg3 respectively for comparision
         each file read into input_texts dict {}
         get a value by  " input_texts[filename] "
        -----------------------------------------------------------  '''
        for filename in sys.argv[2:4]:
            input_filenames.append(filename)
            if os.path.getsize(filename) < _bufsize:
                with open(filename, 'r') as f:
                    ''' -----------------------------------------------------------
                     following for loop is to handle multi lines in input files
                     merge multi lines into a single line seperate them by space
                    -----------------------------------------------------------  '''
                    data = []
                    for line in f.readlines():
                        data.append(line.rstrip())
                    input_texts[filename] = " ".join(data)
            else:
                raise FileSizeTooLarge("{0} is too large".format(filename))

        # processing optional arg of tuple_size, if given
        if len(sys.argv) == 5:
            if sys.argv[4] is not None:
                N = int(sys.argv[4])

        # purely debugging (personal preference) remove if desired
        if DEBUG:
            print input_filenames
            print input_texts[input_filenames[0]]
            print input_texts[input_filenames[1]]

        # Processing tuple_size
        ''' -----------------------------------------------------------
         max_tuple_size: calculated based on the number of words(tuples) in input files.
         It assigns whichever is smaller as you can't generate tuples list
         if tuple size is larger than actual number of tuples in a input file

         example,
         file1: go for a run
         file2: go for a jog in the morning

         optionally, I added "tunable_tuple_size" this is an experimetal or empirically tuned.
         for plagirism detector, what would be an appropriate size of max_tuple_size?
         I don't think having max_tuple_size as the number of words in a file is appropriate.
         I put 100 as a starter, we should experiment with real life examples.

         simple example is:
         input1: go for a run
         input2: went for a jog

         N = 3
         comparing ['go', 'for', 'a'] and ['went', 'for', 'a']
         comparing ['for', 'a', 'run'] and ['for', 'a', 'jog']
         output: 50%

         where N = 4
         comparing ['go', 'for', 'a', 'run'] and ['went', 'for', 'a', 'jog']
         output: 0%
        ----------------------------------------------------------- '''

        len_input1 = len(str(input_texts[input_filenames[0]]).split())
        len_input2 = len(str(input_texts[input_filenames[1]]).split())
        if len_input1 <= len_input2:
            max_tuple_size = len_input1
        else:
            max_tuple_size = len_input2

        # comparing with tunable
        if max_tuple_size > tunable_tuple_size:
            max_tuple_size = tunable_tuple_size

        # debug output
        if DEBUG:
            print "calculated max_tuple size {0}".format(max_tuple_size)

        ''' -----------------------------------------------------------
         generating n-tuples from each input_texts -
        ----------------------------------------------------------- '''
        if 0 < N <= max_tuple_size:
            tuples1 = generate_tuples(input_texts[input_filenames[0]], N)
            tuples2 = generate_tuples(input_texts[input_filenames[1]], N)
        else:
            '''
            catching where tuple_size is way too big or a bigger than a smaller file.
            '''
            raise ValueError(usages[2])

        # n-tuple comparison with synonyms support
        for idx in range(len(tuples1)):
            if DEBUG:
                print "comparing {0} and {1}".format(tuples1[idx], tuples2[idx])

            if compare_with_synonyms(tuples1[idx], tuples2[idx], syns_dict):
                # if match, increment the counter
                match_count += 1
            else:
                ''' -----------------------------------------------------------
                for now it is a place holder. else section can be removed otherwise
                -----------------------------------------------------------  '''
                pass

            # counting total number of matching
            total += 1

        if total > 0:
            print '{0}%'.format(int((float(match_count) / float(total)) * 100.0))
        else:
            print "No comparison performed."

    except AssertionError as err:
        '''
         handling assertion error - in this case, error_code[1[ - invalid number of inputs.  It has to be 2 < n < 5
         writing out to stderr.
        '''
        sys.stderr.write(usages[1])
    except ValueError as err:
        sys.stderr.write(err.message)

    '''
    You can choose to handle exception or pass-thru the exception and exit the execution.

     File "detector2.py", line 114, in main
     raise FileSizeTooLarge("{} is too large".format(filename))
      __main__.FileSizeTooLarge: file3.txt is too large
    '''
    # also passing thru all other exceptions as I don't want this code to swallow exceptions.
    # finally:
    # place holder for now, if needed
    #     pass


if __name__ == "__main__":
    main()


