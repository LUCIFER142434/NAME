# Урок position arguments function ,/
# def name(argument):
#     print(argument)
# name("text")
# def name(greg,der,/,*,ted,red,):
#     print(greg,der,ted,red)
# name(5,3,ted = 2,red = 4)

# def text(*name):
#     print(name[1])
# text("text1","text2")

# def text(**name):
#     print(name["red"])
# text(red = "text1", ted = "text2")




# a = ("ee",1)
# print(type(a))



# def recursiy(red):
#     if(red > 0):
#         ted = red + recursiy(red - 1)
#         print(ted)
#     else:
#         ted = 0
#     return ted
# print("recursiy metod")
# recursiy(10)






# def my_function(ted,red):
#     print(ted)
# my_function("Hello from a function")



# def name(x):
#     x += 5
#     print(x)
# name(5)

# *
# **

















#1
# a = {
#     'a':1,
#     'b':2,
#     'c':3
# }
# for i in a:
#     print(a[i] * 2)
#2
# a = ['textss']

# for i in a:
#     print(i[::2])
#3
# a = [1,2,3,4,5]
# a.reverse()
# print(a)
#4
# for i in range(10,100,5):
#     print(i)
#5
# a = "asddsadadasa"
# print(set(a))
#6
# a = [1,2,3,-4,-5]
# for i in a:
#     if i > 0:
#         print(i)
#7
# a = [1.9,2.99,3,4.7,5.3]
# for i in a:
#     print(round(i))
# for i in a:
#     i = int(i)
#     print(i)
#8
# a = {
#     'a':1,
#     'b':2,
#     'c':3
# }
# for i in a:
#     print(a[i])

















#1
# a = [1,2,3,4,5,6]
# print(a)
#2
# a =[1,2,3]
# b =[4,5,6]
# c = a + b
# print(c)
#3
# a =(1,2,3)
# b =(4,5,6)
# c = a + b
# print(c)
#4
# a = {
#     'a':1,
#     'b':2
# }
# b = {
#     'c':3,
#     'd':4
# }
# a.update(b)
# print(a)
#5
# a = {1,2,4}
# b = {1,3,4}
# print(a.intersection(b))
#6
# a = {1,2,4}
# b = {1,3,4}
# print(a.symmetric_difference(b))
#7
# a = '12347'
# b = '12390'
# for i in a:
#     for x in b:
#         if i == x:
#             print(i)




# for x in range(1,10,2):
#     print(' ' * ((9 - x) // 2) + '*' * x)




# a = [
#     [11,12,13,14,15],
#     [21,22,23,24,25],
#     [31,32,33,34,35]
# ]
# for i in a:
#     print(i[2])


# a = [
#     'a':[
#         'b':[
#             'c':'+++'
#         ]
#     ]
# ]




#1
# for i in range(1,5):
#     print('*' * i)
#2

#3
# for i in range(2,10,2):
#     print('*' * i)
#4
# for i in range(1,10):
#     print('*', i,i,i)
#5
# x = 5
# while x >= 1:
#     x -=1
#     print('z' * x)
#6
# x = 10
# while x >= 1:
#     x -=1
#     print(str(x) * x)




# events = [
#   {
#     'date':  '2019-12-29',
#     'event': 'name1'
#   },
#   {
#     'date':  '2019-12-31',
#     'event': 'name2'
#   },
#   {
#     'date':  '2019-12-29',
#     'event': 'name3'
#   },
#   {
#     'date':  '2019-12-30',
#     'event': 'name4'
#   },
#   {
#     'date':  '2019-12-29',
#     'event': 'name5'
#   },
#   {
#     'date':  '2019-12-31',
#     'event': 'name6'
#   },
#   {
#     'date':  '2019-12-29',
#     'event': 'name7'
#   },
#   {
#     'date':  '2019-12-30',
#     'event': 'name8'
#   },
#   {
#     'date':  '2019-12-30',
#     'event': 'name9'
#   },
# ]
# b = {}
# for i in events:
#     data = i['date']
#     eve = i['event']
#     if data not in b:
#         b[data] = [eve]
#     else:
#         b[data].append(eve)
#     print(b)




# events = [
#     {
#         'date': '2019-12-529',
#         'event': 'name1'
#     },
#     {
#         'date': '2019-12-3641',
#         'event': 'name1',
#     },
#     {
#         'date': '2019-12-329',
#         'event': 'name3',
#     },
#     {
#         'date': '2019-12-30',
#         'event': 'name1'
#     },
#     {
#         'date': '2019-12-229',
#         'event': 'name3'
#     },
#     {
#         'date': '2019-12-131',
#         'event': 'name3'
#     },
#     {
#         'date': '2019-12-129',
#         'event': 'name7'
#     },
#     {
#         'date': '2019-12-230',
#         'event': 'name7'
#     },
#     {
#         'date': '2019-12-430',
#         'event': 'name9'
#     },
# ]
# b = {}
# for i in events:
#     data = i['event']
#     eve = i['date']
#     if data not in b:
#         b[data] = [eve]
#     else:
#         b[data].append(eve)
#     print(b)

# a = [1,2,3,4,5,6,7]
# b = filter(lambda num: num % 2 == 0,a)
# print(list(b))
# for i in a:
#     if i % 2 == 0:
#         print(i)

#1
# aaa = ['aab','aas','dq','df','re','wqeq']
# b = filter(lambda num: len(num) == 2, aaa)
# print(list(b))
# for i in aaa:
#     if len(i) == 2:
#         print(i)
#2
# num = 5
# def text():
    # global num
#     num *= 2
#     return num
# print(text())
#3
# num = 10
# def text():
#     global num
#     num -= 3
#     return num
# print(text())