# 1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield
# -------------Решение----------------

# Создаем функцию с генератором
def odd_nums(max_num):
    for num in range(1, max_num + 1, 2):
        yield num


# Проверяем
odd_to_15 = odd_nums(15)
print(next(odd_to_15))
print(next(odd_to_15))


# 2. * (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.
# -------------Решение----------------
# Создаем функцию с генератором
def gen(max_num):
    return (i for i in range(1, max_num + 1, 2))


# Проверяем
gen_to_15 = gen(15)
print(next(gen_to_15))
print(next(gen_to_15))
