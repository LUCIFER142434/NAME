print('Hello World')
#1
# events = [
#     {
#         'date':  '2019-12',
#         'event': 'name1'
#     },
#     {
#         'date':  '2019-12',
#         'event': 'name2'
#     },
#     {
#         'date':  '2019-11',
#         'event': 'name3'
#     },
#     {
#         'date':  '2019-11',
#         'event': 'name4'
#     },
#     {
#         'date':  '2020-10',
#         'event': 'name5'
#     },
#     {
#         'date':  '2020-10',
#         'event': 'name6'
#     },
#     {
#         'date':  '2020-11',
#         'event': 'name5'
#     },
#     {
#         'date':  '2020-11',
#         'event': 'name6'
#     },
#     {
#         'date':  '2020-12',
#         'event': 'name7'
#     },
#     {
#         'date':  '2020-12',
#         'event': 'name8'
#     },
#     {
#         'date':  '2020-12',
#         'event': 'name9'
#     },
#     ]
# b = {}
# for i in events:
#     data = i['date']
#     eve = i['event']
#     if data not in b:
#         b[data] = [eve]
#     else:
#         b[data].append(eve)
# for x in b:
#     print(x,'{ \n', b[x], '\n }')











#2
# a = input('Напешите текст но не цифры :')
# b = 0
# num = ''
# for i in a:
#     # print(i)
#     if i == 'у' or i == 'е' or i == 'а' or i == 'о' or i == 'э' or i == 'ы' or i == 'я' or i == 'и' or i == 'ю' or i == 'ё':
#         b += 1
#     for x in range(1,10):
#         x = str(x)
#         if i == x:
#             num += f'Зачем тебе цафра {i} !? \n'

# print(f'Гласных букв {b} \n {num}')










#3
# a = input('Шифр')
# b = ['']
# for i in a:
#     if i == '1':
#         b += 'а'
#     elif i == '2':
#         b += 'б'
#     elif i == '3':
#         b += 'в'
#     elif i == '4':
#         b += 'г'
#     elif i == '5':
#         b += 'д'
#     elif i == '6':
#         b += 'е'
#     elif i == '7':
#         b += 'ё'
#     elif i == '8':
#         b += 'ж'
#     elif i == '9':
#         b += 'з'
#     print(i)
# print(b)












#4
# a = [1,2,1]
# b = a.reverse()

# if a == b:
#     print("da")
# else:
#     print('error')


# a = [1,2,3,4,5]
# a.reverse()
# print(a)






