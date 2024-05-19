x = 38

print('Здравствуйте!')
if x < 0:
    print('Меньше нуля')
print('Досвидания!')

##################################

a, b = 10, 5

if a > b:
    print('a > b')

if a > b and 0 < a:
    print('успех')

if (a > b) and (0 < a or b < 1000):
    print('успех')

if 5 > b and b < 10:
    print('успех')

if '34' > '123':
    print('успех')

if '123' > '12':
    print('успех')

if [1, 2] > [1, 1]:
    print('успех')

if '6' > 5:
    print('успех')

if [5, 6] > 5:
    print('успех')

if '6' != 5:
    print('успех')
