
import math

print("Illia Basalukk, IT-31")

# Розміри кімнати
LENGTH = 5
WIDTH = 4
HEIGHT = 3

# Розміри дверей і вікна
DOOR_WIDTH = 0.9
DOOR_HEIGHT = 2.1
WINDOW_WIDTH = 1.5
WINDOW_HEIGHT = 1.4

# Плитка
TILE_SIZE = 0.3
TILE_PRICE = 42.30

# Площа
floor_area = LENGTH * WIDTH
wall_area = 2 * (LENGTH + WIDTH) * HEIGHT
wall_area -= DOOR_WIDTH * DOOR_HEIGHT
wall_area -= WINDOW_WIDTH * WINDOW_HEIGHT

# Діагоналі
floor_diag = math.hypot(LENGTH, WIDTH)
room_diag = math.dist(
    (0, 0, 0),
    (LENGTH, WIDTH, HEIGHT)
)

# Кількість плиток
tile_area = TILE_SIZE ** 2
tiles_exact = floor_area / tile_area

print(f"room:          {LENGTH} x {WIDTH} x {HEIGHT} m")
print(f"floor area:    {floor_area:.2f} m2")
print(f"wall area:     {wall_area:.2f} m2")
print(f"floor diag:    {floor_diag:.2f} m")
print(f"room diag:     {room_diag:.2f} m")

print(f"\ntiles exact:   {tiles_exact:.2f}")
print(f"  round:       {round(tiles_exact)}")
print(f"  floor:       {math.floor(tiles_exact)}")
print(f"  ceil:        {math.ceil(tiles_exact)}")

tiles_to_buy = math.ceil(tiles_exact * 1.1)
print(f"tiles to buy:  {tiles_to_buy}")

# Фарба
paint = wall_area * 2 / 10
cans = math.ceil(paint / 2.5)

print(f"paint:         {paint:.2f} l -> {cans} cans")

# Вартість плитки
cost_mul = tiles_to_buy * TILE_PRICE

cost_sum = 0
for _ in range(tiles_to_buy):
    cost_sum += TILE_PRICE

print(f"\ntiles cost:    {cost_mul:.2f} UAH")
print(f"sum == mul:    {cost_sum == cost_mul}")
print(f"isclose:       {math.isclose(cost_sum, cost_mul)}")
print(f"difference:    {abs(cost_sum - cost_mul)}")
