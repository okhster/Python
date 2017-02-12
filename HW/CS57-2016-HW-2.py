#1) Write the below programs with a while loop and a for loop
#a)Sum the even numbers from 0-100 (inclusive)
#a-whileLoop
x=0
tot=0
while x<100: #does it have to be x<=100 since it should include 100 at the end?
    x=x+2
    tot+=x
print tot

#a-forLoop
tot=0
for x in range(0, 101,2):
    tot+=x
print tot
    
#b)Sum the odd numbers from 0-100 (inclusive)
#b-whileLoop
x=1
tot=0
while x<100:
    tot+=x
    x+=2
print tot

#b-forLoop
tot=0
for x in range(1,100,2):
    tot+=x
print tot

    
#2)Write a program that counts the vowels in this sentence. 16
sentence="Write a program that counts the vowels in this sentence."
n=0
v=["a", "e", "i", "o", "u"]
for char in sentence:
    if char in v:
        n+=1
print n
    

#3)Asks a user to enter a temperature in celsius (via raw_input) and
#outputs the temperature in fahrenheight. (9x/5)+32

c=raw_input('Please enter a temperature in Celsius, ')
c=int(c)
c=float((9*c)/5+32)
print "The temperature in Fahrenheight is,",c

#4)Write a program that outputs the value of adding all numbers 1 to n.
##Example, n of 4, would result in 10 (1+2+3+4)
## a user will input n via raw_input. Assume n is a positive integer greater than 14
t=0
n=int(raw_input("Enter a number, "))
for x in range(0, n+1):
    t+=x
print t
    
    

