# Вам дано множество студентов:
#  students = {‘Schultz’, ‘Django’, ‘Brunhilde’, ‘Fritz’}
# А также множество рабочих:
#  employees = {‘Schultz’, ‘Django’, ‘Calvin’, ‘Butch’, ‘Fritz’}
# Кто-то из них учится и работает одновременно.
# Предстоит вывести в консоль:
#   Всех людей
#   Всех тех, кто одновременно учится и работает
#   Всех тех, кто только работает, но не учится
#   Всех тех, кто либо учится, либо работает, но не одновременно

study = {'Schultz', 'Django', 'Brunhilde', 'Fritz'}
work = {'Schultz', 'Django', 'Calvin', 'Butch', 'Fritz'}

all_people = study | work
studying_and_working = study & work
working_only = work - study
either_studying_or_working = study ^ work

print(all_people)
print(studying_and_working)
print(working_only)
print(either_studying_or_working)
