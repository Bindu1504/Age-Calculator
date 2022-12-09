# print("Enter the date in formats of dd-mm-yyyy")
# date1=[int(s) for s in input("Date1: ").split("-")]
# date2=[int(s) for s in input("Date2: ").split("-")]
# days=[31,28,31,30,31,30,31,31,30,31,30,31]
# d1=date1[0]
# d2=date2[0]
# m1=date1[1]
# m2=date2[1]
# y1=date1[2]
# y2=date2[2]
# a=0
# b=0
# count=0
# x=(y2-y1-1)*365
# #print("x",x)
# for i in range(y1+1,y2):
#     if (i%4==0 and i%100!=0) or (i%400==0):
#         count=count+1
#         #print(count,"c")
# for i in range(m1-1,12):
#     a=a+days[i]
#     #print(a,"a")
# for i in range(m2-1):
#     b=b+days[i]
#     #print(b,"b")
# n1=-d1+a+x+count+d2+b
# #print(n1)
# if  (y1%4==0 and y1%100!=0) or (y1%400==0):
#     if m1<=2:
#         n1=n1+1
# if  (y2%4==0 and y2%100!=0) or (y2%400==0):
#     if m2>2:
#         n1=n1+1
# print("no.of days:",n1)
# f=open("K22bs.txt","a")
# a=input("enter data")
# f.write(a)
# print("data saved in file")
# f.close()
#
# f=open("K22bs.txt","r")
# d=f.read()
# print(d)
# y=open("K22bs.txt","a")
# a=input("enter data")
# f.write(a)
# file1=open("myfile.txt","w")
# L=["This is Delhi \n","This is Paris \n","This is London \n"]
# file1.write("Hello \n")
# file1.writelines(L)
# file1.close()
# file1=open("myfile.txt","r+")
# print("Output of Read function is")
# print(file1.read(5))
# print()
# file1.seek(0)
# print("Output of Readline function is")
# print(file1.readline())
# print()
# file1.seek(0)
# print("Output of Read(9) function is")
# print(file1.read(9))
# print()
# file1.seek(0)
# print("Output of Readline(9) function is ")
# print(file1.readline(9))
# file1.seek(0)
# print("Output of Readlines function is ")
# print(file1.readlines())
# print()
# file1.close()
# f=open("Input.txt","w")
# f.write("Hello welcome to class \n Welcome \n Bye")
# f.close()
# fin=open('Input.txt','r')
# charCount=wordCount=lineCount=0
# for line in fin:
#     lineCount+=1
#     wordCount+=len(line.split())
#     charCount+=
# num1=int(input("num1: "))
# num2=int(input("num2: "))
# try:
#     num3=num1/num2
#     print(num3)
# except:
#     print("exception occured")
# try:
#     a=int(input("a: "))
#     b=int(input("b: "))
#     c=a+b
#     e=a/b
#     print("try successful")
# except ArithmeticError:
#     print("arithmetic error occured")
# except Exception:
#     print("expection occured")
# else:
#     print("hi")
# finally:
#     print("executed in any condition")
# try:
#     number1,number2=eval(input("Enter two numbers,separated by a comma"))
#     result=number1/number2
#     print("Result is",result)
# except ZeroDivisionError:
#     print("Division by zero")
# except SyntaxError:
#     print("A comma may be missing in the input")
# except:
#     print("No exception")
# finally:
#     print("The finally clause ")
# marks={'Rahul':50,'Harsh':60,'Suresh':70}
# name=input("enter name:")
# try:
#     print('marks:',marks[name])
# except KeyError:
#     print('name {} not in the list'.format(name))
# print("end ")
# try:
#     fh = open("testfile","r")
#     fh.write("This is my test file for exception handling")
# except IOError:
#     print("Error: can't find file or read data")
# else:
#     print("Content written successfully")
def checkage(age):
    if age<0:
        raise ValueError("age should be greater than or equal to zero")
    print("age is valid")
try:
    age=int(input("age: "))
    checkage(age)
except ValueError as err:
    print(err.args)
finally:
    print("excuted in any situation")