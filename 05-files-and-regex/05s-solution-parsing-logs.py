from collections import Counter
import pathlib
import re

containing_dir = pathlib.Path(__file__).parent.resolve()

# Because the file isn't particularly long, I'm going to load it into memory for ease of use
with open(containing_dir / 'mock-logs' / 'Hadoop_2k.log') as hadoop_log:
    FULL_LOG_TEXT = hadoop_log.read()

# Count how many log entries were made during each minute (note that all entries occur within the same hour in this logfile)
# Notes about this regex: 
#   The date is always at the start of the line
#   We'll use parenthesis to make a "match group" to extract just the hour
#   We'll ignore the rest of the message
hours_extract_expression = "\d{4}-\d{2}-\d{2} \d{2}:(\d{2})"
matches = re.findall(hours_extract_expression, FULL_LOG_TEXT)
unique_minutes = Counter() # Because it's almost the same amount of work, I'm counting how many logs per minute.
for m in matches:
    unique_minutes[m] += 1

print("====Q1======")
for minute, c in unique_minutes.items():
    print(minute, c)



# Find all the distinct IP addresses that occur in the logs.
# Note: this isn't perfect, since ip number values can only be 0-255.
# You CAN write a regex that will perfectly handle this, but it's complicated and 
# I think it's easier, and less error prone, to just filter such values later.
ip_regex = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}" 
matches = re.findall(ip_regex, FULL_LOG_TEXT)
unique_ips = Counter()

for ip_address in matches:
    # Here's the filtering code
    ip_segments = ip_address.split('.')
    for ip_segment in ip_segments:
        if 0 >= int(ip_segment) >= 255:
            print("invalid ip detected:", ip_address, ip_segment)
            continue
    
    unique_ips[ip_address] += 1

print("====Q2======")
for ip_address, c in unique_ips.items():
    print(ip_address, c)


# Extract each unique error message
# Error messages are the final section of each line. There are probably a lot of ways to match this.
message_regex = '[INFO|WARN|ERROR|FATAL].*?:(.*)'
unique_messages = set()
matches = re.findall(message_regex, FULL_LOG_TEXT)
for m in matches:
    unique_messages.add(m)

print("====Q3======")
print(len(unique_messages)) # 736, out of 2000 total entries. Interesting!
for m in unique_messages:
    print(m)


# Find the all ip addresses that occur in error entries, but do not occur in any non-error entries
# I reuse the ip address code and add something to make note of the type of error
ip_error_regex = '[ERROR|FATAL].*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
matches = re.findall(ip_error_regex, FULL_LOG_TEXT)
erroring_ips = Counter()

for ip_address in matches:
    # Here's the filtering code
    ip_segments = ip_address.split('.')
    for ip_segment in ip_segments:
        if 0 >= int(ip_segment) >= 255:
            print("invalid ip detected:", ip_address, ip_segment)
            continue
    
    erroring_ips[ip_address] += 1

print('====Q4====')
for ip, c in erroring_ips.items():
    print(ip, c) # Note in the results that this shows MOST messages with an IP address are errors.