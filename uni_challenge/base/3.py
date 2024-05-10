# Open the file for reading
with open('3.txt', 'r') as file:
    # Read the entire line from the file
    txt = file.readline().split(" ")
    a, b = int(txt[0]), int(txt[1])

# every second num is odd, avg is median, num of nums is diff/2 (+1 if odd)
odds = (b-a)/2
avg = (a+b)/2

result = int(odds)*int(avg)
if (b-a)%2 == 1 and b%2 == 1:
    result += b
elif (b-a)%2 == 1 and a%2 == 1:
    result += a
print(int(result))
