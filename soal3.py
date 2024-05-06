with open('mbox-short.txt', 'r') as file:
    lines = file.readlines()

email_histogram = {}
email_count = {}

for line in lines:
    if line.startswith('From:'):
        email = line.split()[1]
        email_histogram[email] = email_histogram.get(email, 0) + 1
        email_count[email] = email_count.get(email, 0) + 1

print("Histogram Email:")
for email, count in email_histogram.items():
    print(f"{email}: {'*' * count}")

print("\nJumlah Pesan Email:")
for email, count in email_count.items():
    print(f"{email}: {count}")
