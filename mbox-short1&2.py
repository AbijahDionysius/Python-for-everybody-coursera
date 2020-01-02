#8.4
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0.0
for line in fh:
    line = line.strip()
    if not line.startswith('X-DSPAM-Confidence: '):
        continue
    count = count +1
    find_variable =line.find(':')
    extract_variable =line[find_variable+1:]
    converted_variable = float(extract_variable)
    total = total +converted_variable
    avg = total/count
print("Average spam confidence:", avg)


--------------------------------------------------------
#8.5
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    split_line =line.split()
    if split_line[0]!= 'From':
        continue
    email = split_line[1]
    count = count +1
    print(email)
print("There were", count, "lines in the file with From as the first word")


#8.5 Open the file mbox-short.txt and read it line by line.
#When you find a line that starts with 'From ' like the following line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message).
#Then print out a count at the end.
#Hint: make sure not to include the lines that start with 'From:'.
-------------------------------------------------------------------------------------------------------------------------------------------------------
