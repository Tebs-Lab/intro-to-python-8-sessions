# Regular Expressions

# When working with text, especially when searching for patterns in text, regex is incredibly useful. Lets look at some of the basics.

# * Regex offers some very fancy features that can be very helpful...
#     * `.` is regex's version of `_` — it matches any one character.
#     * `*` and `+` are quantitative operations that modify the previous character:
#         * `.*` means "0 or more of any character"
#         * `.+` means "one or more of any character"
#         * `a+` means "one or more a's in a row"
#     * More specific quantitive operations use `{}`
#         * `a{1,3}` means between 1 and 3 a's in a row.
#         * The `?` can modify any other of these quantifiers to make it "greedy" which means it matches the shortest possible match. By default regex matches the longest possible match 
        
# * Character classes are grouped in `[]`
#     * A character class is a set of characters to match.
#     * The `-` is used to specify characters "between" each other, which has to do with the `ASCII` and `Unicode` formats and their lookup tables.
#     * But simply, `[a-z]` means all the lowercase letters from a to z. `[a-zA-Z] means all lower and uppercase letters.
#     * `[aeiou]` means any of the vowels. 
# * Character classes can be combined with the numerical operators!
    
# * `^` matches the start of a string and `$` matches the end of a string.

import pathlib
import re # this is the regular expression library built into python

containing_dir = pathlib.Path(__file__).parent.resolve()
path_to_frankenstein = containing_dir / 'book-texts/frankenstein-no-header-footer.txt'

book_text = ''
with open(path_to_frankenstein, 'r') as franken_reader:
    # This code reads the book line by line, and strips out newlines unless
    # they appear on a line by themselves. Essentially leaving in only line breaks
    # that are paragraph breaks!
    line = franken_reader.readline()
    while line != '':
        if line == '\n':
            book_text += line
        else:
            book_text += line.replace("\n", ' ')

        line = franken_reader.readline()
        
print(book_text)

# Find words with two vowels in a row in them
dual_vowel_words = ' [a-zA-Z]*[aeiouyAEIOUY]{2}[a-zA-Z]* '

double_vowel_instances = re.findall(dual_vowel_words, book_text)
for dv in double_vowel_instances:
    print(dv)


# Regex is useful in searching prose, but it's even more useful
# in text with "regular" patterns, such as log files.
# Because this log file is fairly small, we're going read the whole 
# file into memory and then run some regex on it. 
with open(containing_dir / 'mock-logs' / 'Hadoop_2k.log') as hadoop_log:
    full_log_text = hadoop_log.read()

# For this first one, we're going to extract the 'level' and 'service'
# and ignore the rest of the log. We'll use this info to try and see if
# a particular service is failing often.
extract_level_service_re = "\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3} ([a-zA-Z]+) \[.*?\] (.*?):"
all_level_service_match = re.findall(extract_level_service_re, full_log_text)

# This code creates a nested dictionary structure
# mapping each service to how many log entries of each level 
# were produced by that service.
report_dir = {}
for match in all_level_service_match:
    level = match[0]
    service = match[1]

    if service not in report_dir:
        report_dir[service] = {}
        report_dir[service][level] = 0
    elif level not in report_dir[service]:
        report_dir[service][level] = 0

    report_dir[service][level] += 1


for service, levels in report_dir.items():
    print(service)
    for level, number in levels.items():
        print("  ", level, number)

# org.apache.hadoop.mapreduce.v2.app.rm.RMContainerAllocator has a lot of errors
# lets look at just those log entries
find_rmca_errors = '.*org.apache.hadoop.mapreduce.v2.app.rm.RMContainerAllocator.*ERROR.*'
rmca_error_lines = re.findall(find_rmca_errors, full_log_text)

# Turns out they're all exactly the same error. 
# It's worth looking into the connection to the RM! (whatever that is)
for m in rmca_error_lines:
    print(m)