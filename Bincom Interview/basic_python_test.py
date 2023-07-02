import re
import request
from collections import Counter
import psycopg2

url_request = "https://drive.google.com/file/d/1nf9WMDjZWIUnlnKyz7qomEYDdtWfW1Uf/view?pli=1"


def extract_colors(url_request):
    color_pattern = re.compile(r'(?i)\b[a-z]+\b')
    color_data = []

    for row in url_request.find_all('tr'):
        data = row.find_all('td')
        if len(data) == 2:
            colors = color_pattern.findall(data[1].text)
            color_data.extend(colors)

    return color_data


def calculate_mean_colors(colors):
    total_colors = len(colors)
    color_counts = Counter(colors)
    mean_color = color_counts.most_common(1)[0][0]

    return mean_color


def calculate_mode_color(colors):
    color_counts = Counter(colors)
    mode_color = color_counts.most_common(1)[0][0]

    return mode_color


def calculate_median_color(colors):
    sorted_colors = sorted(colors)
    n = len(sorted_colors)
    middle_index = n // 2

    if n % == 0:
        median_color = sorted_colors[middle_index]

    else:
        median_color = sorted_colors[middle_index]

    return median_color

def calculate_color_variance(colors):
    color_counts = Counter(colors)
    color_frequencies = list(color_counts.values())
    total_colors = len(colors)
    variance = sum(freq - (total_colors / len(color_frequencies))) ** for freq in color_frequencies) / total_colors

def calculate_color_probability(colors, target_color):
    total_colors = len(colors)
    color_counts = Counter(colors)
    color_frequency = color_counts[target_color]
    probability = color_frequency / total_colors

    probability_red = calculate_color_probability(extract_colors, 'RED')
    print(f"The probability of choosing the color red is: {probability_red}")


    return probability

def connect_to_database():
    conn = psycopg2.connect(
        host = "your_host",
        database = "your_database",
        user = "your_user",
        password = "your_password"
    )

    return conn

def save_colors_to_database(colors):
    conn = connect_to_database()

    try:
        with conn.cursor() as cursor:
            cursor.execute("CREATE TABLE IF NOT EXISTS colors (color TEXT, frequency INT)")
            conn.commit()

            color_counts = Counter(colors)
            for color, frequency in color_counts.items():
                cursor.execute("INSERT INTO colors (color, frequency) VALUES (%S, %S)",(color, frequency))
            conn.commit()
            print("Colors saved to the database successfully !")

    except(Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to pPostgreSQL", error)

    finally:
        if conn is not None:
            conn.close()
    save_colors_to_database(extract_colors)

if __name__ == '__main__':
    extract_colors = ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'BLUE', 'YELLOW', 'ORANGE', 'CREAM']