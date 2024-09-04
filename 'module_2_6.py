import random

def get_code() :

    numbers = list(range(3, 21))
    code = random.choice(numbers)
    return code

def get_password(n):
    password = {}

    password = password.get(n)
    return password

n = get_code()

print('Число   :', n)


pair1 = list(range(1, n))
pair2 = list(range(1, n))
pairs = []
result = ''

for i in pair1:
    for j in pair2:
        pn1 = i
        pn2 = j
        if pn1 >= pn2:
            continue
        else:

            if n % (pn1 + pn2) == 0:
                pairs.append([pn1, pn2])
                result = result + str(pn1) + str(pn2)
print('Пары чисел', *pairs)
print('Введите пароль', result, 'во вторую вставку')


