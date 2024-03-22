n = int(input("Enter height: "))
m = int(input("Enter width: "))

rows = []
for i in range(n):
    row = []
    for j in range(m):
        row.append((i + j) % 2)
    rows.append(row)

for row in rows:
    print(row)
