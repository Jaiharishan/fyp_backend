import random
import csv

# Number of rows
num_rows = 50

# Open a CSV file in write mode
with open('coordinates.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    # Write the header
    writer.writerow(['X', 'Y'])

    # Generate and write the coordinates
    for _ in range(num_rows):
        x = random.randint(0, 500)
        y = random.randint(0, 500)
        writer.writerow([x, y])

print("CSV file created successfully.")