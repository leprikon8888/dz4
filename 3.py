"""Task 3
Дано коло з центром на початку координат та радіусом 4. Користувач вводить з клавіатури координати точки x та y. /
Написати програму, яка визначить, лежить ця точка всередині кола чи ні."""
import math
x = int(input('input x: '))
y = int(input('input y: '))
radius = int(input('input radius: '))
gipotenuza = math.sqrt(x**2 + y**2)
if gipotenuza <= radius:
    print("YES")
else:
    print("NO")


