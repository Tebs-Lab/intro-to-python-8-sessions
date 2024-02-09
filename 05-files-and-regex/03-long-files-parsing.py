# A counter is a dictionary where the default value for every key is 0.
from collections import Counter

# This should be familiar
import pathlib

# the string module has several functions we'll use to parse strings.
import string

# Open the book
containing_dir = pathlib.Path(__file__).parent.resolve()
path_to_frankenstein = containing_dir / 'book-texts/frankenstein-no-header-footer.txt'
with open(path_to_frankenstein, 'r') as franken_reader:
    # The type of franken_reader is a <class '_io.TextIOWrapper'>
    print(type(franken_reader))
    
    # This type has some interesting methods.
    ## .read() will process the whole file and we can put it in a string
    whole_text = franken_reader.read()
    print(whole_text)

    # NOTE: Once the file has been "read" it cannot be read a second time
    # in fact reading any part of the file "consumes" that section. So if you run the following
    # code without commenting out the above call to "read()" nothing will be output.

    # Read, with a parameter, will read the specified number of bytes
    first_50_bytes = franken_reader.read(50)
    print(first_50_bytes)
    
    # Readline can be used to read one line at a time. 
    first_line = franken_reader.readline()
    print(first_line)


# This time, we're going to read the book and count every word we encounter.
word_counts = Counter()
with open(path_to_frankenstein, 'r') as franken_reader:
    line = franken_reader.readline()
    
    # The final line will be an empty string
    # No other lines (even blank ones) will be the empty string
    # An empty line will instead be the newline character "\n"
    while line != '':
        # The split function turns a string into an array of words based on 
        # where the whitespace characters are. You can split on other characters too!
        words = line.split() 
        
        for word in words:
            word_counts[word] += 1
            
        line = franken_reader.readline()
        
        
# Now that we have the word counts... Lets check them out!
for count in word_counts.most_common():
    print(count)
    
# If you look carefully there are some odd ones that we'd need better processing
# # to handle. Here are some examples:
#     ('contumely?', 1)
#     ('at,', 1)
#     ('“Fear', 1)
#     ('“Farewell!', 1)

# It turns out, python has a lot of great stuff built in, including a solution to this problem...
# So lets try again.
word_counts = Counter()
with open(path_to_frankenstein, 'r') as franken_reader:
    line = franken_reader.readline()
    
    # The final line will be an empty string
    # No other lines (even blank ones) will be the empty string
    # An empty line will instead be the newline character "\n"
    while line != '':
        # Lets lowercase everything so we don't count A and a separately.
        line = line.lower()
        
        # explanation of maketrans: https://docs.python.org/3.3/library/stdtypes.html?highlight=maketrans#str.maketrans
        # replace hyphen (EM AND EN DASH) with a space. 
        # (Note, it's hard to tell, but these two dashes are different characters)
        line = line.translate(str.maketrans('-—', '  '))
        
        # remove anything in string.punctuation and the two weird quotes
        line = line.translate(str.maketrans('', '', string.punctuation + '“' + '”'))
        
        # The split function turns a string into an array of words based on 
        # where the whitespace characters are. You can split on other characters too!
        words = line.split() 
        for word in words:
            word_counts[word] += 1
            
        line = franken_reader.readline()
        
        
# Now that we have the word counts... Lets check them out!
for count in word_counts.most_common():
    print(count)

