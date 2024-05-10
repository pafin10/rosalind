# Open the file for reading
with open('2.txt', 'r') as file:
    # Read the entire line from the file
    txt = file.readline().strip()
    ind = file.readline().strip()


a, b, c, d = map(int, ind.split(" "))

print(txt[a:b + 1] + " " + txt[c:d + 1])
