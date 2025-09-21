# 1. ใช้ for loop สร้างลิสต์เลขคู่ 2 ถึง 20
even_numbers = []
for i in range(2, 21, 2):
    even_numbers.append(i)

# 2. ใช้ while loop หาผลรวมของเลขคู่เหล่านั้น
total = 0
index = 0
while index < len(even_numbers):
    total += even_numbers[index]
    index += 1

# 3. แสดงผลทั้งลิสต์และผลรวม
print("Even numbers:", even_numbers)
print("Sum:", total)
