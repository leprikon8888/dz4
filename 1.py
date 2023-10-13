"""Task 1
Дано число (чотиризначне). Перевірити, чи воно є «щасливим квитком». Примітка: щасливим квитком називається число, у/
якому, при парній кількості цифр, сума цифр його лівої половини дорівнює сумі цифр його правої половини.
Наприклад, 1322 є щасливим квитком, тому що 1 + 3 = 2 + 2."""

bilet = input("input bilet number: ")
a = list(bilet)
half = int(len(a)/2)
first_half = a[:half]
second_half = a[half:]
if sum(map(int, first_half)) == sum(map(int, second_half)):
    print('lucky bilet')
else:
    print('not lucky bilet')


