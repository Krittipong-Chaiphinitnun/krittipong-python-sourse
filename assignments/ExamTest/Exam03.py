even_numbers = []
for i in range(2, 21, 2):

total = 0
index = 0
while index < len(even_numbers):
    total += even_numbers[index]
    index += 1

print("ลิสต์เลขคู่:", even_numbers)
print("ผลรวมของเลขคู่:", total)