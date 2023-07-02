from collections import Counter
import re
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

start_index = html_data.find('<tbody>')
end_index = html_data.find('</tbody>')
table_data = html_data[start_index:end_index]
colors = []

for line in table_data.split('\n'):
    if '<td>' in line:
        color = line.split('<td>')[-1].strip()
        colors.extend(color.split(', '))

mean_color = max(Counter)
mean_color = max(Counter(colors), key=Counter(colors).get)

most_worn_color = Counter(colors).most_common(1)[0][0]

sorted_colors = sorted(colors)
middle_index = len(sorted_colors) // 2

if len(sorted_colors) % 2 == 0:
    median_color = sorted_colors[middle_index]

else:
    median_color = int(sorted_colors[middle_index] + sorted_colors[middle_index + 1]) / 2

red_count = Counter(colors)['RED']
total_count = len(colors)
red_probability = red_count / total_count

conn = psycopg2.connect(database="tomisin", user="tomisin", password="Abosede@1", host="localhost", port="5432")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS colors (color VARCHAR(255), frequency INT)")

for color, frequency in Counter(colors).items():
    cur.execute("INSERT INTO colors (color, frequency) VALUES (%s, %s)", (color, frequency))

conn.commit()
conn.close()

print("1. Mean color: ", mean_color)
print("2. Most worn color throughout the week: ", most_worn_color)
print("3. Median color: ", median_color)
print("5. Probability of choosing red color randomly: ", red_probability)