import random
import secrets

random_number = ''.join(secrets.choice('01') for _ in range(4))

decimal_number = int(random_number, 2)

print(f"Generated number: {random_number}")
print(f"Decimal representation: {decimal_number}")
