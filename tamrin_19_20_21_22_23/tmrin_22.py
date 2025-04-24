import matplotlib.pyplot as plt

# پارامترها
p = 0.25
factor = 1 + p
initial = 1
target = 1_000_000

# شبیه‌سازی روزانه
count = initial
day = 0
days = [day]
counts = [count]
while count < target:
    day += 1
    count *= factor
    days.append(day)
    counts.append(count)

# رسم نمودار
plt.plot(days, counts)
plt.yscale('log')
plt.grid(True)
plt.show()

# نمایش تعداد روز
print(day)
