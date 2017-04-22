# Plagiarism Detection with synonyms

input1: synonyms
input2, input3: source files for n-tuple comparison
input4: tuple_size

comments: 
simple way to resolve this would be:
use set of ("run, sprint, jog") and quickly check if a word is a member.
This approach has a problem to scale in my opinion.
I like to use more generic dictionay of synonyms.
If list of synonyms becomes larger, we can should consider:
 1. use something like Redis
 2. use something like mongodb 
 mongodb would be considered 
 if this is really large
 if we need to do version control of dictionaries
 we can use redis and mongodb in combination of course
 redis can cache whichever version of dictionary that is used.
 

## Synonyms dictionary
1. source will have a list of synonyms
run, sprint, jog

build a dictionary with key for each words:
->
{
    "run": "run, sprint, jog",
    "sprint": "run, sprint, jog",
    "jog": "run, sprint, jog"
}

2. each line can have more than 3
run, sprint, jog, gallop

build a dictionary with key for each words:
->
{
    "run": "run, sprint, jog, gallop",
    "sprint": "run, sprint, jog, gallop",
    "jog": "run, sprint, jog, gallop",
    "gallop": "run, sprint, jog, gallop"
}

3. each line is different synonyms list
run, sprint, jog
stop, cease, finish
->
{
    "run": "run, sprint, jog",
    "sprint": "run, sprint, jog",
    "jog": "run, sprint, jog",
    "stop": stop, cease, finish",
    "cease": stop, cease, finish",
    "finish": stop, cease, finish" 
}



## input files
1. if multiple lines are in a file:
the code merges them into a single line and separate them by a space.
 
2. if the size of file is bigger than _bufsize (default = 1024 MB).
default value is tunable based on the system. 
Or improve to be calculated based on resources.
if file is large than the _bufsize, it throws FileSizeTooLarge exception
(* example of custom exception in python)
Too large file can cause a problem as you can imagine. It is safe guarding.

### possible improvements for large input files other sources
other sources are like twitter feed, google docs, dropbox, or webpages crawlers, etc.
1. we can chunk files by size then process them.. 
2. we can introduce preprocessing, 
   Personal preference would be using something like mongodb, or couchdb
   generate a chunk as a json doc with a meta data, here is an simple example

   {
     "_source": "file1.txt",
     "_source_type": "file",
     "_datetime": "",
     "_chunkID": 1,
     "_totalNoChunks"; 20,
     ... 
     "_body": "go for a run with .... "
     
   }
    
    With this approach, we can simply get all docs with _sourcefile of "file1.txt"
    Also, we can index these docs to improve retrieval of docs.
    So it is better than chunks of files in my opinion
    
3. it depends on other usage or sources, 
we can use something like ElasticSearch or Solr if text search is more important



## tuple size
1. if N is given (sys.argv[4]),
check the value has to be:  0 < N <= number of words in smaller input files
 - large than '0'
 - smaller or eqaul to the number of words in smaller files
 input file1: go for a walk (4)
 input file2: went for a walk with a dog(7)
 input file1 is smaller file. Therefore N is checked - 0 < N < 4
 
2. tunable_tuple_size 
tune the tuple size for better performance.
In general i don't think having the tuple size as large as the whole file.

example
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

N = 4 I consider as poor performance. Tunable is to allow to use tune easily.
we can introduce as a parameters in config file later.

Couple of comments:
1. tried to write a pure functions with no side effects.
2. kept main logic in main() function
3. tried to use various options
   - use try, except  instead of if statements alone
   - use of customer exception
   - idea of error_codes and usage 
4. tried to add a friendlier comments as much as I can.