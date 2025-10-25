names = ["Anu", "Meena", "Rani", "Anand"]
count = 0

for i in names:
    for j in i:
        if j == 'a' or j == 'A':
            count += 1

print("Total occurrences of 'a':", count)
    

