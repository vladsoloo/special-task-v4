import datetime

g = 2023
m = 3
n = 7

d = datetime.date(g, m, n)

one_day = datetime.timedelta(days=1)

prev_day = d - one_day
next_day = d + one_day

print(f"Дата: {d}")
print(f"Дата предыдущего дня: {prev_day}")
print(f"Дата следующего дня: {next_day}")
