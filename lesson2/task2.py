# Замените в пользовательской строке все появления буквы h на букву H,
# кроме первого и последнего вхождения.

a = input()
first_h = a.find('h')
last_h = a.rfind('h')

if first_h != -1 and last_h != -1 and first_h != last_h:
    b = a[:first_h + 1] + a[first_h + 1:last_h].replace('h', 'H') + a[last_h:]
    print(b)
