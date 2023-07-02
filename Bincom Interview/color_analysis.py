import re
from collections import Counter
import psycopg2

html_data = '''
<html>
<head>
<title>Our Python Class exam</title>

<style type="text/css">

	body{
		width:1000px;
		margin: auto;
	}
	table,tr,td{
		border:solid;
		padding: 5px;
	}
	table{
		border-collapse: collapse;
		width:100%;
	}
	h3{
		font-size: 25px;
		color:green;
		text-align: center;
		margin-top: 100px;
	}
	p{
		font-size: 18px;
		font-weight: bold;
	}
</style>

</head>
<body>
<h3>TABLE SHOWING COLOURS OF DRESS BY WORKERS AT BINCOM ICT FOR THE WEEK</h3>
<table>

	<thead>
		<th>DAY</th><th>COLOURS</th>
	</thead>
	<tbody>
	<tr>
		<td>MONDAY</td>
		<td>GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN</td>
	</tr>
	<tr>
		<td>TUESDAY</td>
		<td>ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE</td>
	</tr>
	<tr>
		<td>WEDNESDAY</td>
		<td>GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE</td>
	</tr>
	<tr>
		<td>THURSDAY</td>
		<td>BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN</td>
	</tr>
	<tr>
		<td>FRIDAY</td>
		<td>GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE</td>
	</tr>

	</tbody>
</table>

<p>Examine the sequence below very well, you will discover that for every 1s that appear 3 times, the output will be one, otherwise the output will be 0.</p>
<p>0101101011101011011101101000111 <span style="color:orange;">Input</span></p>
<p>0000000000100000000100000000001 <span style="color:orange;">Output</span></p>
<p>
</body>
</html>
'''
# todo questions   Which color of shirt is the mean color?
# 2.      Which color is mostly worn throughout the week?
# 3.      Which color is the median?
# 4.      BONUS Get the variance of the colors
# 5.      BONUS if a colour is chosen at random, what is the probability that the color is red?
# 6.      Save the colours and their frequencies in postgresql database
start_index = html_data.find('<tbody>')
end_index = html_data.find('</tbody>')
table_data = html_data[start_index:end_index]
colors = []

for line in table_data.split('\n'):
    if '<td>' in line:
        color = line.split('<td>')[-1].strip()
        colors.extend(color.split(', '))

mean_color = max(Counter(colors), key=Counter(colors).get)
most_worn_color = Counter(colors).most_common(1)[0][0]


# todo # 4.      BONUS Get the variance of the colors
# Function
def calculate_color_variance(colors):
    color_counts = Counter(colors)
    color_frequencies = list(color_counts.values())
    total_colors = len(colors)
    variance = sum((count - (total_colors / len(color_frequencies))) ** 2 for count in color_frequencies) / total_colors
    return variance


# todo # 5.      BONUS if a colour is chosen at random, what is the probability that the color is red?
def calculate_red_probability(colors):
    color_counts = Counter(colors)
    total_colors = len(colors)
    red_count = color_counts.get('RED', 0)
    red_probability = red_count / total_colors
    return red_probability


# todo # 6.      Save the colours and their frequencies in postgresql database
def save_to_database(colors):
    conn = psycopg2.connect(
        database="tomisin",
        user="tomisin",
        password="Abosede@1",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    create_table_query = '''CREATE TABLE colors (
                            color TEXT PRIMARY KEY,
                            frequency INTEGER);'''
    cursor.execute(create_table_query)
    color_counts = Counter(colors)
    for color, frequency in color_counts.items():
        insert_query = f"INSERT INTO colors (color, frequency) VALUES ('{color}', {frequency});"
        cursor.execute(insert_query)
    conn.commit()
    conn.close()
    print("Colors and frequencies saved to the database.")


# todo BONUS write a recursive searching algorithm to search for a number entered by user in a list of numbers.
def recursive_search(numbers, target, index=0):
    if index >= len(numbers):
        return False

    if numbers[index] == target:
        return True

    return recursive_search(numbers, target, index + 1)


number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

while True:
    try:
        target_number = int(input("Enter a number to search: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

result = recursive_search(number_list, target_number)
if result:
    print("Number found in the list!")
else:
    print("Number not found in the list.")

# todo Write a program that generates random 4 digits number of 0s and 1s and convert the generated number to base 10.

import random


def generate_random_binary():
    binary_number = ""
    for _ in range(4):
        binary_number += str(random.randint(0, 1))
    return binary_number


def convert_to_base_10(binary_number):
    decimal_number = int(binary_number, 2)
    return decimal_number


# Generate a random binary number
random_binary = generate_random_binary()
print("Random Binary Number:", random_binary)

# Convert the binary number to base 10
decimal_number = convert_to_base_10(random_binary)
print("Decimal Equivalent:", decimal_number)


# todo Write a program to sum the first 50 fibonacci sequence.

def fibonacci_sum(n):
    fib_sequence = [0, 1]

    while len(fib_sequence) < n:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)

    return sum(fib_sequence[:n])


fibonacci_sum_50 = fibonacci_sum(50)

print(f"The sum of the first 50 Fibonacci numbers is: {fibonacci_sum_50}")
