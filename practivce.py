# This Function Uses Global Variable

# def k():
#     s = "My Name Is Aagja Krish Mahendrabhai. "
#     print(s)
# k()

# def hello(name):
#     print("Hello, " , name)
# hello('bob')
# hello ('krish')

# def hello(name):
#     print("Hello, " ,name)
# hello(input("Enter the name : "))
# hello(input("Enter The Name : "))

# def func(name,job):
#     print(name,'Is A',job)
# func('Krish','Develop')

# def name(fname,job):
#     print(fname,'Is A',job)
# name('Krish','Develop')

# for char in 'python':
#     if (char == 'h'):
#         pass
#     print("Current Charecter: ",char)

# def enroll(a,b,c=110):
#     print("Serial Name: ",a)
#     print("Serial Name: ",b)
#     print("Serial Name: ",c)
# enroll(125,94)

# def f():
#     k = "Hello , I'm Aagja Krish Mahendrabhai"
#     print(k)
# f()

#define Parameter With Default Values

# def dis(x,y=0):
#     print('X: ',x)
#     print('Y: ',y)
# if__name__ == '__main__':
#     #function  Called And Passed Only One Argument
# dis(4)
# dis(4,5)

    # practical 9

# x = int(input('Enter the first number:  '))
# y = int(input("Enter the second number: "))
# z = int(input("Enter the third number: "))

# m = max(x,y,z)

# print(m)

                         #Practical 10

# i = 0
# while (i <= 10):
#     print(i)
#     i += 1

                    # Practical 12

# i = 1
# i2 = int(input("Enter the number  : "))

# while ( i <= i2):
#     if (  i% 2 ) == 0:
#         print(i,'Is An Even Number.')
#     else :
#         print(i,'Is An odd Number.')
#     i += 1

                    # Practical 13

# num = int(input("Enter the number : "))
# if num > 1:
#     for i in range (2,int(num/2+1)):
#         if (num% 1)== 0:
#             print(num,"Is Not A Prime Number.")
#         else :
#             print(num,"Is A Prime Number.")
# else :
#         print(num,"Is Not A Prime Number.")



            # FUNCITON


            # Calling Function
# def my_function():
#     print("Hello From A Function")
# my_function()
            # Arguments
# def my_function(fname):
#     print(fname + " Refsnes")
# my_function("Emil")
# my_function("Tobias")
# my_function("Krish")

        # Number Of Arguments

# def my_function(fname,lname):
#     print(fname +" "+ lname)
# my_function("Aagja","Krish")

            # Arbitrary  Arguments *args

# def my_function(*kids):
#     print("Hello Mine",kids[2])
# my_function("Jhon","Mark","Elvin")

            # KeyWord Arguments

# def my_function(child3,child2,child1):
#     print("The Youngster Child Is ",child3)
# my_function(child3="Krish",child1="Mark",child2="Jhon")

            # Arbitrary Keywords Arguments **kwargs

# def my_function(**kid):
#     print("His last name is " + kid['lname'])
# my_function(fname="Krish",lname="Aagja")

            # Default Parameters Value

# def my_function(country="Swedan"):
#     print("I Am From ",country)
# my_function("Austraila")
# my_function("India")
# my_function()
# my_function('Canada')


            # Passing A List as an Argument

# def dfood(food):
#     for x in food:
#         print(x)
# fruits = ["Apple","Banana","Cherry"]

# dfood(fruits)

            # Return Value

# def sum(x):
#     return 5 + x
# print(sum(3))
# print(sum(4))
# print(sum(5))


            # PASS
# def name(fname):
#     print("My Name is ",fname)
#     return fname + "aagja"
# name("Krish")