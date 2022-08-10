import math
import psycopg2 as pg2
import re
import pandas as pd
from collections import Counter
import random

# We open the html file and read it as file_obj
handle = input("Enter a file handle: ")
with open(handle, "r") as file_obj:
    file = file_obj.read()

# We use Regex to extra the content of the file table.
data = re.findall(r"<td>(.*)</td>", file)
# print(data)

#  Eliminate the week-days from the list.
for color in data:
    if color == 'MONDAY' or color == 'TUESDAY' or color =='WEDNESDAY' or color == 'THURSDAY' or color == 'FRIDAY' :
        data.remove(color)

# Add all the lists together to create one list.

new_data = str(",".join(data))
clear_data = new_data.split(",")
# print(clear_data)

# Remove whitespaces from the clear_data list.
list = [color.strip() for color in clear_data]
# print(list)

# Create an empty dictionary
# Iterate through list to get each color. Count and map number of occurence to the color.

dict1 = Counter(list)
print(dict1)


# Solving question 1.
total = 0
mean_color = ""
new_dict = len(dict1)
for num in dict1.values():
    total += int(num)
mean = total / new_dict
print(f"The Mean Value is: {mean}. " 'Approximately', math.ceil(mean))
print('The Mean color is Orange and Red')


# Solving for Question 2.

max_frequency = 0
frequency_col = ""
for k, v in dict1.items():
    if v > max_frequency:
        frequency_col = k
        max_frequency = v
print(f"The value worn mostly is: {max_frequency}")
print(f"The color worn mostly is: {frequency_col}")


# Solving for Question 3

mid = int((total + 1) /2)
mid_color = ""
for k, v in dict1.items():
    if v == mid:
        mid_color = a

print(f"The Median Value is: {mid}")
print('The Median Color is: Green')


# Solving for Question 4.

# Getting the Variance of color.

mean = math.ceil(mean)
denominator = new_dict -1

numerator = 0
for v in dict1.values():
    numerator += math.pow((v - mean), 2)
    variance = numerator / denominator

print(f"The Variance Value is:', {variance}")


# Solving for Question 5

# BONUS if a colour is chosen at random, what is the probability that the color is red?

red = int(dict1["RED"])
probability_of_red = total / red
print(f'The Probability of chosing red at random is: {probability_of_red}')

# POSTGRES TASK

# Get database details from User.
database = input('Enter db name: ')
username = input('Enter db username: ')
password = input('Enter dbn password: ')

# Establish database connection with detail provided
conn = pg2.connect(
    database = database,
    user = username,
    password = password,
    host='127.0.0.1',
    port = "5432"
)

cur = conn.cursor()

cur.execute('''DROP TABLE IF EXISTS color_data''')

cur.execute(
    '''CREATE TABLE color_data (colors VARCHAR NOT NULL, color_frequency VARCHAR NOT NULL)'''
)

# Iterate through each color in dictionary and insert the details in our table.
for colorInfo in color_count_keys:
    cur.execute('''INSERT INTO color_data (colors, color_frequency) VALUES (%s, %s)''',)
                (colorInfo, color_count[colorItem])

# read sql table and print table using pandas
table = pd.read_sql('''SELECT * from color_data''', conn)
print(table, "n")

conn.commit()
cur.close()
conn.close()


# Solving for Question 7

def recursive_search(user_list, element):
    if len(user_list) == 0:
        return False
    else:
        mid = len(user_list) // 2
        if user_list[mid] == element:
            return True

        else:
            if element < user_list[mid]:
                return recursive_search(user_list[:mid], element)
            else:
                return recursive_search(user_list[mid + 1:], element)

list2 = [12, 10, 223, 947, 1901, 43, 90]
x = 52
recursive_search(list2, x)


# Solution to Question 8

r_string = ""

for i in range(0, 4):
    number = random.choice(range(0, 2))
    r_string += str(number)

decimal = int(r_string, 2)
print(f"The binary output is: {r_string}")
print(f"It's corresponding decimal is: {decimal}")


# Solving for Question 9.

def fibonacci(number):
    # Returns a list containing 0 if the number is 0
    if number == 0:
        return [0]
    # Returns a list containing 0, 1 if the number is 0
    if number == 1:
        return [0, 1]

    series = [0, 1]


    for i in range(2, number):
        series.append(series[i-1] + series[i-2])
    return series

print('\nThe sum is', sum(fibonacci(50)))
