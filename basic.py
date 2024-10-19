 # print("hello world")

# print("   /|")
# print("  / |")
# print(" /  |")
# print("/___|")


# a = 100 + 3j #so phuc
# # print(type(a))
# print(a.real)#phan thuc
# print(a.imag)#phan ao

#in so thuc vs luong chu so sau dau phay xac dinh
# a = 28.0412341414443
# print("%.2f" %a)
# print(round(a,2))
# print("{:.2f}".format(a))
#muon bao nhieu so thi ...f

# character_name = "Huy"
# character_age = 18
#is_male = True
#tap rong se la false, 0 cung vay

# print("There once was a man name " + character_name + ",")
# print("He was about " + character_age + " years old. ")
# character_name = "Tom"
# character_age = 20
# print("He really like the name " + character_name + ",")
# print("But he want to be " + character_age + ".")

# print("Tom\nAcademy")
# print("Tom Academy")
# print("Tom\"Academy")

# phrase = "Tom Academy"
# print(phrase + " is cool")

# phrase = "Tom Academy"
# print(phrase.upper())
# phrase = "Tom Academy"
# print(phrase.lower())

# phrase = "Tom Academy"
# print(phrase.lower().isupper())

# phrase = "Tom Academy"
# print(len(phrase))

# phrase = "Tom Academy"
#         #01235678910
# print(phrase[0])
# print(phrase.index(" "))
# print(phrase.index("Academy"))
# print(phrase.replace("Tom", "Huy"))
#Tom replace by Huy

#print("28tech", "programming", sep = '--')
#--> 28tech--programming
#print("28tech", "programming", end = '--')
#-->28tech programming--

#work with number
# print(2)
# print(-2.2788728772)
# print(3 + 4.5)
# print(10 % 3)
# print(10 / 3)

# my_num = -5
# print(my_num)
# print(str(my_num) + " Tommy ")

# print(abs(my_num))
# print(pow(3,2))

# print(max(4,5))
# print(min(4,6))
# from math import *
# #allow to more math functions
# print(round(3.7))
# #4 
# print(floor(3.7))
# #3
# print(ceil(3.1))
# #4 always round up
# print(sqrt(36))

#Ham toan hoc
#import math
# from math import *
# #print(help(math))#xem cac ham cua toan
# #sqrt: square root --> tra ve so thuc
# print(sqrt(36))#6.0
# #isqrt
# print(isqrt(16))#lay so nguyen --> 6.3616642 = 6
# print(pow(2,10))#--> 1024.0

# #ceil --> lam tron len
# print(ceil(2.3))#3
# print(ceil (7.8))#8

#floor --> lam tron xuong
#print(floor(2.4))#2
#print(floor(7.8))#7

#factorial --> giai thua
#print(factorial(10))
#perm: giai thua / giai thua
#print(perm(5,3))

#gcd: greatest common division --> ucln
#print(gcd(10,20))
#ucln: smallest common --> bcnn = a * b / gcd(a,b)
#print(10 * 20 / gcd(10,20))


#Get input from users
# name = input ("Enter your name: ")
# age = input ("Enter your age: ")
# print("hello " + name + ", Your age is " + age) 

#build basic calculator
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))
# result = num1 + num2

# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# result = float(num1) + float(num2)
# print(result)

#Lists
#people = ["Huy", "Lương", "Thiện","Thọ","Đông"]
#012
#-3-2-1 0 với 0 là k có giá trị
# people[1] = "Phát"
# print(people[2])
# print(people[-2])
# print(people[1:]) # lấy tất cả về phía sau từ vị trí 1
# print(people[1:3]) #lấy tất cả từ 1 đến trong khoảng 1 đến 3, k lấy 3
# lucky_numbers = [4, 6, 2, 10, 252]
# people = ["Huy", "Lương", "Thiện","Thọ","Dông","Dông"]
# people.extend(lucky_numbers) #mở rộng list
#people.append("Bảo") #Mở rộng list thêm về phía sau
#people.insert( 1, "Quân")
#people.remove("Quân")
#people.clear()
#people.pop() #remove the last element in the list
#print(people) 
#print(people.index("Huy"))#vi tri cua index trong list
#print(people.count("Đông" ))
#lucky_numbers.sort()
# lucky_numbers.reverse()
# print(lucky_numbers)
# people.sort()
# people1 = people.copy()
# print(people1)
 
##Tuples --> Lưu trữ dữ liệu không thể thay đổi được như hằng số Khac voi List
# my_tuples = (4, 5, 6, 100, 250)
# print(my_tuples[1])
# my_tuples1 = [(4,5), (10,15), (80,34)]
# print(my_tuples1[2])

# Empty tuple
# my_tuple = ()
# print(my_tuple)
 
# Tuple having integers
# my_tuple = (1, 2, 3)
# print(my_tuple)
 
# tuple with mixed data types
# my_tuple = (1, "Hello", 3.4)
# print(my_tuple)
 
# nested tuple
# my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
# print(my_tuple)

#Tuple không cần sd dấu ngoặc đơn gọi là tuple packing
# my_tuple = "mouse", [8, 4, 6], (1, 2, 3)
# print(my_tuple)
# a,b,c = my_tuple
# print(a)
# print(b)
# print(c)

# my_tuple = ("hello")
# print(type(my_tuple))  # <class 'str'>
 
#Creating a tuple having one element
# my_tuple = ("hello",)
# my_tuple = "hello",
# print(type(my_tuple))  # <class 'tuple'>

#Truy cập phần tử trong tuple
#nested tuple
# n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
 
#nested index
# print(n_tuple[0][3])       # 's'
# print(n_tuple[1][1])       # 4

#Slicing
#Access tuple elements using slicing
# my_tuple = ('p','r','o','g','r','a','m','i','z')

# print(my_tuple[4:]) # r a m i z
# print(my_tuple[1:4]) # r o g 
# print(my_tuple[:-6]) # p r o --> tính lui thì lấy 3 vị trí bỏ vị trí số -6
# print(my_tuple[:]) # all

#Change tuple values --> no change 
#Can change the value inside the mutable elements
# my_tuple = (4,2,5,6,[17, 28])
# my_tuple[1] = 9 # type error

# my_tuple[4][0] = 10
# print(my_tuple)

# Concatenation
# Output: (1, 2, 3, 4, 5, 6)
# print((1, 2, 3) + (4, 5, 6))
 
# Repeat
# Output: ('Repeat', 'Repeat', 'Repeat')
# print(("Repeat",) * 3 )

#delete tuple
# my_tuple = ('p','r','o','g','r','a','m','i','z')
# del my_tuple
# del my_tuple[3] # can delete items

# my_tuple = ('p','r','o','g','r','a','m','i','z')
# print(my_tuple.index('a')) #5
# print(my_tuple.count('r')) #2

# #IN operation
# print('h' in my_tuple)
# print('a' in my_tuple)

#Not IN operation
# print('g' not in my_tuple)

#for loop in python --> for loop use : at the end of for loop
# for alphabet in my_tuple:
#     print("Hello", alphabet)


#Functions
# def tutorial():
#     print("hello Huy")
    
# def say_hi(name):
#     print(name)
# tutorial()
# say_hi("Huy")

#Return statement
# def cube(num):
#     return num * 3 # return the value and break the function
# result = cube(7)
# print(result)

#IF function
# is_male = True
# is_tall = True
# if is_male and is_tall:
#     print("You are a tall male")
# elif is_male and not(is_tall):
#     print("You are a short male")
# elif not(is_male) and is_tall:
#     print("You are not a male but tall")
# else:
#     print("You are not a tall male")

#IF functions and comparisons
# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
# print(max_num(30,25,100))

#Shorthand if and toan tu ba ngoi
# a,b = 100, 200
# if a < b: print(a, "less than", b)

#variable = statement if condition else statement
# a, b = 100, 200
# res = "Huy" if a < b else "Minh"
# print(res)

#Build a simple calculator
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# op = input("Enter operator: ")

# if op == "+":
#     print(num1 + num2)
# elif op == "-":
#     print(num1 - num2)
# elif op == "*":
#     print(num1*num2)
# elif op == "/":
#     print(num1 / num2)
# else:
#     print("Invalid operator")
   
#Dictionaries
# monthConversions = {
#     "Jan": "January",
#     "Feb": "February",
#     "Mar": "March",
#     "Apr": "April",
#     "May": "May",
#     "Jun": "June",
#     "Jul": "July",
#     "Aug": "August",
#     "Sep": "September",
#     "Oct": "October",
#     "Nov": "November",
#     "Dec": "December",
# }

# print(monthConversions.get("Dec"))
# print(monthConversions["Dec"])
# print(monthConversions.get("Luv","Dec"))#pass the default value-->get


#While loop
#while condition:
#statement
#else:
#statement

# i = 10
# n = int(input("Nhap so n: "))
# while i <= n:
#     print(i)
#     i += 1 # i = i + 1
# else:
#     print("Vong while ket thuc khi i: ", i)

# n = 5
# i = 1
# while i <= n:
#     print(i)
#     continue #lap lai ngay i = 1
#     i += 1 
#--> vo han so 1
#break is the same --> demand the condition --> break

#BT: in ra n co bao nhieu chu so
# n = 1234
# dem = 0
# while n != 0:
#     dem += 1
#     n //= 10 #chia nguyen cho 10
# print("So chu so cua n: ", dem)

#BT: tong cac chu so cua so n
# n = 1234
# Tong = 0
# while n != 0:
#     Tong += n % 10
#     n //= 10 #chia nguyen cho 10
# print("Tong chu so cua n: ", Tong)

#BT: lat nguoc 1 so nguyen
# n = 1234
# a = 0
# b = 0 
# while n != 0:
#     #b = n % 10
#     a = a * 10 + n % 10
#     n //= 10
# print("So nghich dao cua n: ",a)

#Building a guess game
# secret_word = "Huy"
# guess = ""
# guess_count = 0
# guess_limit = 5
# out_of_guesses = False
# while guess != secret_word and not out_of_guesses:
#     if guess_count < guess_limit:
#      guess = input("enter guess:")
#      guess_count += 1
#     else:
#        out_of_guesses = True

# if out_of_guesses:
#    print("Out of guesses, You lose!")
# else:
#    print("You win!")

#For loops
#for var in iterable:
#range(start, stop, step) --> iterable

# for letter in "Gia Huy":
#     print(letter)
# friends = ["Jim", "Karen", "Kevin"]
# for name in friends:
#     print(name)
# for index in range(10):#not 10
#     print(index) 
# for index in range(3,10): # from 3 to 9
#     print(index)
# len(friends)
# for index in range(len(friends)):
#     print(friends[index])
# for index in range(5):
#     if index == 0:
#         print("First index")
#     else:
#         print("Not first")

# n = 10
# S = 1
# for i in range(1, n + 1):
#     S *= i
# print(S)
# for i in range (1, 7):#i chi lay gia tri trong range de chay
#     print(i)
#     i += 100
#--> 1 2 3 4 5 6

#Break and Continue
# for i in range (1, 21):
#     print(i, end = ' ')
#     if i % 7 == 0:
#         break
# print("Break")

# for i in range(5):
#     print(i)
#     continue #turn back for loops here
#     print("Huy")

#Nested loops
# for i in range(3):
#     for j in range(2):
#         print(i, j)


#Exponent function
# def raise_to_power(base_num, pow_num):
#     result = 1
#     for index in range(pow_num):
#         result = result * base_num
#     return result
# print(raise_to_power(3, 4))

#2D lists and nested loops
# number_grid = [
#     [1, 2, 3], 
#     [4, 5, 6],
#     [7, 8, 9],
#     [0]
# ]
# print(number_grid[0][1])#2
# print(number_grid[2][1])#8
# print(number_grid[2],[1])#[7, 8, 9], [1]
#print(number_grid)

# for i in range(len(number_grid)):
#     for j in range(len(number_grid[i])):
#         print(f"Hàng {i}, Cột {j}: ", number_grid[i][j])

#Build a translator
# def translate(phrase):
#     translation = ""
#     for letter in phrase:
#         if letter.lower() in "aeiou":
#             if letter.isupper():
#                 translation = translation + "G"
#             else:
#                 translation = translation + "g"
#         else:
#             translation = translation + letter
#     return translation

# print(translate(input("Enter a phrase: ")))

#Try except
# try:
#     a = 10/0
#     number = int(input("Enter a number: "))
#     print(number)
# except ZeroDivisionError as err:
#     print(err)
# except ValueError:
#     print("invalid input")

#Reading files
# license_file = open("LICENSE.txt", "r")#read

# print(license_file.read())
# print(license_file.readlines()[])#read all lines and put it in array
# for license in license_file.readlines():
#     print(license)

# print(license_file.readline())#read the individual line --> first line
# print(license_file.readline()) #-->second line
# print(license_file.readable()) #show that we can read or not
# license_file.close()

# open("LICENSE.txt", "w")#write
# license_file = open("LICENSE.txt", "w")#-->write new not storage the latest
# license_file.write("\nGia Huy")

# hello_file = open("hello.html", "w")
# hello_file.write("<p>This is HTML<p>")
# hello_file.close()

# open("LICENSE.txt", "a")#append
# license_file = open("LICENSE.txt", "a")
# license_file.write("\nGia Huy")#--> write in text file
#\n: underline
# open("LICENSE.txt", "r+")#read and write

#Modules and Pips
# import useful_tools

# print(useful_tools.roll_dice(10))
# print(useful_tools.beatles)
# print(useful_tools.feet_in_mile)
# print(useful_tools.meters_in_kilometer)

#Classes and Objects
# class student:

#     def __init__(self, name, major, gpa, is_on_probation):
#         self.name = name
#         self.major = major
#         self.gpa = gpa
#         self.is_on_probation = is_on_probation


# from student import People
# import student as student
# student1 = People("Huy", "Software engineer", 4.0, False )
# student2 = People("Minh", "AI", "4.0", True)
# print(student1.name)
# print(student2.name)

# import student
# print(dir(student)) #check function in class

#Building a multiple choice quiz
# from Question import Question
# question_prompts = [
#     "what color are Apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n/\n",
#     "what color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n/\n",
#     "what color are Strawberry?\n(a) Yellow\n(b) Red\n(c) Blue\n/\n"
# ]
# questions = [
#     Question(question_prompts[0], "a"),
#     Question(question_prompts[1], "c"),
#     Question(question_prompts[2], "b"),
# ]
# def run_test(question):
#     score = 0
#     for question in questions:
#         answer = input(question.prompt)
#         if answer == question.answer:
#             score += 1
#     print("You got " + str(score) + "/" + str(len(questions)) + "Correct")

# run_test(questions)

#Object function
# from student import People
# student1 = People("Huy", "Software engineer", 4.0, False )
# student2 = People("Mu", "AI", 3.4, True)
# student3 = People("Kh", "Engineer", 3.8, True)
# print(student1.on_honor_roll())
# print(student2.on_honor_roll())
# print(student3.on_honor_roll())
#Inheritance
# from Chef import Chef

# myChef = Chef()
# myChef.make_special_dish()

# def tong(a, b):#Tham so hinh thuc: Parameter
#     res = a + b
#     return res

# def change(n):
#     n *= 2

#Ham tinh giai thua
# def gt(n):
#     res = 1
#     for i in range(1, n + 1):
#         res *= i
#     return res
    
#BT kiem tra so chia het cho 3 va 5
# def solve(a):
#     if n % 3 == 0 and n % 5 == 0:
#         return True
#     else:
#         return False


#Code để chạy chương trình
# if __name__ == '__main__': #like ham main 
#     #code cần chạy
#     n = int(input())
#     if solve(n):
#         print('YES')
#     else:
#         print('NO')
        
    # print(gt(10))
    #   a = 1000
    #   change(a)
    #   print(a)#--> 1000 because change() no returns value a
    # x, y = map(int, input().split())
    # print(tong(x,y))
    #x, y: tham so chinh thuc: Argument
# input() đọc chuỗi '10 20'.
# .split() tách chuỗi này thành danh sách ['10', '20'].
# map(int, ['10', '20']) 
# chuyển đổi các chuỗi này thành số nguyên, tạo ra các giá trị 10 và 20.

#BT luyện viết hàm
# from math import *
# #Bai 1: Kiem tra n la so nguyen to. neu dung in 1, sai in 0
# def ham1(n):
#     if n < 2:
#         return 0
#     for i in range(2, isqrt(n)+1):
#         if n % i == 0:
#             return 0
#         else:
#             return 1
# #Tong cac chu so cua n  
# def ham2(n):
#     Tong = 0
#     while n != 0:
#         Tong = Tong + n % 10
#         n //= 10
#     return Tong
# #Tong chu so chan cua n
# def ham3(n):
#     Tong = 0
#     while n != 0:
#         if n % 10 % 2 == 0:
#             Tong += n % 10
#         n //= 10
#     return Tong
# #In ra Tong chu so n la snt
# def ham4(n):
#     # Tong = 0
#     # while n != 0:
#     #     if ham1(n) == True:
#     #         Tong += n % 10
#     #     n //= 10
#     # return Tong 
#     #C2:
#     Tong = 0
#     while n != 0:
#         r = n % 10
#         if r == 2 or r == 3 or r == 5 or r == 7:
#             Tong += r
#         n //= 10
#     return Tong 

# #In ra so lat nguoc cua n
# def ham5(n):
#     sln = 0
#     while n != 0:
#         sln = sln * 10 + n % 10
#         n //= 10
#     return sln

# #In so luong uoc cua n la snt
# def ham6(n):
#     dem = 0
#     for i in range(2, isqrt(n) + 1):
#         dem += 1
#         while n % i == 0:
#             n //= i
#     if n > 1:
#         dem += 1
#     return dem
# #In ra uoc snt lon nhat cua n --> thua so nguyen to cuoi cung
# def ham7(n):
#     res = -1
#     for i in range(2, isqrt(n) + 1 ):
#         if n % i == 0:
#             res = i
#             while n % i == 0:
#                 n //= i
#     if n > 1:
#         res = n
#     return res

# #Kiem tra neu n ton tai it nhat 1 so 6
# def ham8(n):
#     while n != 0:
#         if n % 10 == 6:
#             return 1
#         n //= 10
#     return 0

# #Kiem tra xem tong n co chia het cho 8 
# def ham9(n):
#     Tong = 0
#     while n != 0:
#         Tong += n % 10
#         n //= 10
#     if Tong % 8 == 0:
#         return 1
#     else:
#         return 0
    
# #Tong giai thua cac chu so cua n
# def ham10(n):
#     Tong = 0
#     while n != 0:
#         Tong += factorial(n%10)
#         n //= 10
#     return Tong

# #Kiem tra cac so cua n co giong nhau hay khong
# def ham11(n):
#     donvi = n % 10
#     while n != 0:
#         if donvi != n % 10:
#             return 0
#         n //= 10
#     return 1
# #Kiem tra so tan cung cua n lon nhat hay k
# def ham12(n):
#     donvi = n % 10
#     while n != 0:
#         if n % 10 > donvi:
#             return 0
#         n //= 10
#     return 1

# #Tong luy thua chu so cua n vs so mu la so chu so
# def ham13(n):
#     m = n 
#     count = 0
#     while n != 0:
#         count += 1
#         n //= 10
#     Tong = 0
#     while m != 0:
#         Tong += (m % 10) ** count #** : luy thua
#         m //= 10
#     return Tong

# if __name__ == '__main__':
#     n = int(input())
    # print(ham1(n))
    # print(ham2(n))
    # print(ham3(n))
    # print(ham4(n))
    # print(ham5(n))
    # print(ham6(n))
    # print(ham7(n))
    # print(ham8(n))
    # print(ham9(n))
    # print(ham10(n))
    # print(ham11(n))
    # print(ham12(n))
    # print(ham13(n))

#Recursion: Đệ quy
def A():
    print('A')
def B():
    A()
    print('B')
def C():
    B()
    print('C')

def S(n):
    if n == 0:
        return 0
    else:
        return n + S(n-1) #Recursion
    
#Tinh tong S(n) = 1 + 2 + 3 +...
def sum(n):
    if n == 0:
        return 0
    else:
        return  n + sum(n-1)
#Tinh giai thua F(n) = 1.2.3.4...
def fac(n):
    if n == 0:
        return 1
    return n * fac(n-1)
#Tinh so Fibonacci
def fibo(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
#Tinh tong chu so nguyen duong n: SumDigit(n)
def SumDigit(n):
    if n < 10:
        return n 
    else:
        return n % 10 + SumDigit(n//10) 
#Tinh UCLN:
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
#Chuyen he 10 sang he 2 -> chia cho 2
def decToBin(n):
    if n < 2:
        print(n, end = '')
        return
    else:
        decToBin(n // 2)
        print(n % 2, end = '')


#List
def List():
    a = [1, 2, 3, 4, 30.50, '28tech', 'Gia Huy', True]
    # print(type(a))
    # print(len(a))
    # print(a[0])
    # print(a[-1]) #python co ho tro
    # print(a[10])

    # s ='Gia Huy'
    # b = list(s)
    # print(b)

    # c = list(range(20))
    # print(c)

    #Duyet list
    # for i in range(0, len(a)):
    #     print(a[i], end = ' ')
    
    # for i in range(len(a) - 1, -1, -1):
    #     print(a[i], end = ' ')

    # a[2] = 'Tuan Minh'

    #Them phan tu vao List
    # a.append(10)
    # a.append(100)
    #--> them vao cuoi

    # a.insert(2, 1000)
    #--> them 1000 vao vi tri 2 --> ham insert

    # a.insert(12, 101)
    #--> vi qua vi tri cuoi cung cua list nen se insert vao cuoi
    
    #Xoa phan tu khoi List thong qua vi tri
    # a.pop(2) #Xoa vi tri so 2
    # a.pop() #Xoa vi tri cuoi cung
#--> pop co the tra ve phan tu ma minh xoa
#--> del thi khong tra ve
    # del a[1]
    
    #Xoa phan tu khoi List thong qua gia tri
    # b = [1, 2, 1, 2, 3, 4, 5]
    # b.remove(1) #--> xoa di so 1 dau tien

    # b.clear()#-> xoa het nphan tu trong list
    
    # #Sao chep list
    # c = [1, 2, 3]
    # d = c * 2

    # print(d)

    # for item in b:
    #     print(item)  

    #Tim kiem phan tu trong list
    # a = [1, 2, 3, 4 , 5]
    # if 5 in a:
    #     print('yes')

    #Combine List
    # a = [1, 2, 3]
    # b = [6, 7, 8,9 , 10]
    # a.extend(b)
    # print(a)
    # a += b
    # print(a)

    #Copy list
    # a = [1, 2, 3]
    # b = a
    # print(b is a)# True
    # c = a.copy()#[1, 2, 3]
    # print(c)
    # print(c == a)#True
    # print(c is a)#False

    #Count() --> tra ve so lan xuat hien cua phan tu trong list
    # a = [1, 2, 3, 5, 2, 5, 2]
    # print(a.count(2))

    #Index() --> tra ve vi tri cua phan tu trong list, chi so dau tien
    # print(a.index(2))

    #Reverse() --> Lat nguoc list
    # a.reverse()
    # print(a)

    #Sort() --> Sap xep phan tu trong list
    # a.sort()
    # b = sorted(a)
    # print(a)
    # print(b) #--> A khong bi sort hung a trong b thi sort

    #All() --> tra ve true neu moi phan tu trong list la true
    #Any() --> True neu it nhat 1 phan tu la true
    #Max() --> Phan tu lon nhat != Min()
    #Sorted() --> List da xep cua list ban dau
    #Sum() --> Tong cac phan tu trong list

#List slicing --> list[start, stop, step]
def LS():
    a = [10, 20, 30, 40, 50, 60, 70, 80]
    a[2 : 5] = [1,2,3]
    a[1:2] = []
    a[:0] = ['Huy', 'Minh']# --> chen vao dau
    a[len(a):] = [1000] #Chen vao cuoi
    b = a[:]#Deep copy == a.copy()
    print(b)
    print(b == a) #True
    print(b is a) #False
    # b = a[2 : 5 : 1]
    # c = a[2 : -2]
    # print(b)
    # print(c)
    print(a)
    d = a[::-1] #--> cu phap nhanh de lat nguoc list == a.reverse
    print(d)




if __name__ == '__main__':
    # print(sum(5))
    # print(fac(4))
    # print(fibo(10))
    # print(SumDigit(111))
    # print(gcd(20, 10))
    # print(decToBin(19))
    # print(List())
    print(LS())













