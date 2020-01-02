import re


with open("regex_sum_319771_actual.txt", "r") as f:
    nums = re.findall(r'([0-9]+)', f.read())
    print(sum([int(i) for i in nums]))
#The code does the pull of numbers from text and sums the numbers of it using Regular expressions
