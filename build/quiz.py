user=input("ENTER YOUR NAME :")
print("HELLO ",user,"WELCOME TO KAUN BANEGA CROREPATI")
print(" ")
print("LETS BEGIN KAUN BANEGA CROREPATI")
print(" ")
FINALAMOUNT=0

QUESTION_1=["Q1. WHAT IS CAPITAL OF DENMARK? "]
print(QUESTION_1)
ANSWER_1=["copenhagen"]
x=input("ENTER THE ANSWER:")
if x.lower()=='copenhagen':
    print("YOU WON 1000 DOLLARS")
    FINALAMOUNT+=1000
else:
    print("YOU LOSE")
    print("FINAL AMOUNT YOU TAKE HOME:", FINALAMOUNT, "DOLLARS")
    quit()

QUESTION_2=["Q2. What is the longest river in the world? "]
print(QUESTION_2)
ANSWER_2=["nile"]
y=input("ENTER THE ANSWER :")
if y.lower()=="nile":
    print("YOU WON 2000 DOLLARS")
    FINALAMOUNT+=2000
else:
    print("YOU LOSE")
    print("FINAL AMOUNT YOU TAKE HOME:", FINALAMOUNT, "DOLLARS")
    quit()


QUESTION_3=["Q3. What is the smallest continent by land area? "]
print(QUESTION_3)
ANSWER_3=["australia"]
z=input("ENTER THE ANSWER :")
if z.lower()=="australia":
    print("YOU WON 5000 DOLLARS")
    FINALAMOUNT+=5000
else:
    print("YOU LOSE")
    print("FINAL AMOUNT YOU TAKE HOME:", FINALAMOUNT, "DOLLARS")
    quit()

QUESTION_4=["Q4. Which desert is the largest hot desert in the world? "]
print(QUESTION_4)
ANSWER_4=["sahara"]
a=input("ENTER THE ANSWER :")
if a.lower()=="sahara":
    print("YOU WON 10000 DOLLARS")
    FINALAMOUNT+=10000
else:
    print("YOU LOSE")
    print("FINAL AMOUNT YOU TAKE HOME:", FINALAMOUNT, "DOLLARS")
    quit()

QUESTION_5=["Q5. What is the highest mountain in the world? "]
print(QUESTION_5)
ANSWER_5=["mounteverest"]
b=input("ENTER THE ANSWER :")
if b.lower()=="mounteverest":
    print("YOU WON 20000 DOLLARS")
    FINALAMOUNT+=20000
else:
    print("YOU LOSE")
    print("FINAL AMOUNT YOU TAKE HOME:", FINALAMOUNT, "DOLLARS")
    quit()

print("CONGRATULATIONS!, YOUR TOTALLY WINNING IS:",FINALAMOUNT)   
print("SEE YOU AGAIN :)") 