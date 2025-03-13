num = int(input("Enter the number you want to convert to base two. "))
binary = ""

if num == 0:
    binary = "0"
else:
    while num > 0:
        binary = str(num % 2) + binary  # باقی‌مانده تقسیم بر 2 را به ابتدای رشته باینری اضافه می‌کنیم
        num = num // 2  # تقسیم عدد به دو

print(f"The number in base 2 is equal to {binary}")
