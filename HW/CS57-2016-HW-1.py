#Homework 1

#1)Evaluate ((True and False) and True) or (True and False) or (True or True)
##Scratch-Start## (True and False) => False and True => False;
#### (True or True) => True
#### False or False or True
##Scratch-End## False or True
#Answer 1) True.

#2)If a="catsanddogs" what would the following evaluate to:
#2a) a[3:9]="sanddog"
#2b) a(2:]="tsanddogs"
#2c) a[-3]="o"

#3)Ask user to enter a word and output the length of the word.
w=raw_input("Please enter a word to find its length in this world: ")
lw= len(w)
print "the length of", w, "is", lw, "\n","Thank you for playing! :)"
#4)Ask a user to enter a number and output the cube of that number
num=float(raw_input("Welcome to Cube-Ur-Number Land, enter your number here: "));
nc=num**3
print "Alhacazam, it is now:", nc

#5)Ask a user to enter a radius and outputs the area of a circle with the associated radius.
r=float(raw_input("Lets find the area of a circle, enter a radius here: "))
a=3.14159*(r**2)
print a


  
