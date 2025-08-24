#FUNCTION TO PERFORM ARITHMETIC OPERATION
def cal(x,y,c):
    match c:
        case '+':
            print('ADDITION RESULT =',x+y)
        case '-':
             print('SUBTRACTION RESULT =',x-y)
        case '*':
              print('MULTIPLICATION RESULT =',x*y)
        case '/'if y!=0:
              print('DIVISION RESULT =',x/y)
        case '/':
            print ("ERROR:Y SHOULD NOT BE ZERO")
        case _ :
            print('CHOOSE VALID OPERATION')

print('WELCOME TO THE SIMPLE CALCULATOR')

#TAKING USER INPUT
a=int(input("ENTER THE FIRST NUMBER="))
b=int(input("ENTER THE SECOND NUMBER="))

#DISPLAYING CALCULATOR MENU
while True:
     print('''
    MENU=>
         TO ADD ENTER "+"
         TO SUBTRACT ENTER "-"
         TO MULTIPLY ENTER "*"
         TO DIVIDE ENTER "/"
         TO CHANGE NUMBER ENTER "CHANGE"
         TO EXIT CLICK "EXIT" 
           
        ''')
    #TAKING USER CHOICE AND CALLING FUNTION TO PERFORM OPRATION
     Choice=input('TELL THE OPERATION TO PERFORM=').lower()
     if Choice=="exit":
          print('THANK YOU FOR USING')
          break
     elif Choice=="change" :
          a=int(input("ENTER THE FIRST NUMBER="))
          b=int(input("ENTER THE SECOND NUMBER="))
     else:
          cal(a,b,Choice)

        
        