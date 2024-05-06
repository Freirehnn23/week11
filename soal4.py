def count_email_domains(filename):
    counts_domain = {}
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith("From "):
                email = line.split()[1]
                domain = email.split('@')[1]
                counts_domain[domain] = counts_domain.get(domain, 0) + 1
    return counts_domain

filename = input("Masukkan nama file: ")
counts_domain = count_email_domains(filename)
print(counts_domain)

