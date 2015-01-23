#GLOBAL VARIABLE
choice = 'none'

#GLOBAL CONSTANT FOR PRICE
SNICKERS = 0.89
MNM = 1.39
KITKAT = 1.39
LAYS = 0.50
DORITOS = 0.50
CHEETOS = 1.49
TICTAC = 1.04
STARBURST = 0.79
SKITTLES = 2.49
ITEMPRICE = 0.0

def main():
   #Create a variable to control the loop.
   keep_going = 'y'
   
   while keep_going == 'y':
      displayMenu()
      mychoice =  input('\nPlease enter any one of the options above:\n')
      if mychoice not in {'a1','A1','a2','A2','a3','A3','b1','B2',
                    'b3','B3','c1','C1','c2','C2','c3','C3'}: 
         print ("Bad Choice,please enter valid choice to continue")
         keep_going = input('Do you want to re-enter your choice ?(Enter y for YES & n for NO):')
      else: 
         displayPrice(mychoice)
         keep_going = 'n'
         
def displayMenu():
   print('Welcome to Amruta\'s Vending machine!!')
   print('Snickers M&Ms KitKat\n $0.89\t$1.39\t $1.39\t\n A1 \tA2 \tA3\n')
   print('Lays    Doritos Cheetos\n $0.50\t$0.50\t $1.49\t\n B1 \tB2 \tB3\n')
   print('TicTac   Starburst Skittles\n $1.04\t $0.79\t $2.49\t\n C1 \tC2 \tC3')

def displayPrice(choice):
      if choice in {'a1','A1'}:
              print ('Price for Snickers = ',SNICKERS)
              ITEMPRICE=SNICKERS
              transaction(ITEMPRICE,choice)
      elif choice in {'a2','A2'}:
           print ('Price for M&M = ',MNM)
           ITEMPRICE=MNM
           transaction(ITEMPRICE,choice)  
      elif choice in {'a3','A3'}:
           print ('Price for KitKat = ',KITKAT)
           ITEMPRICE=KITKAT
           transaction(ITEMPRICE,choice)  
      elif choice in {'b1','B1'}:
           print ('Price for Lays = ',LAYS) 
           ITEMPRICE=LAYS 
           transaction(ITEMPRICE,choice)
      elif choice in {'b2','B2'}:
           print ('Price for Doritos = ',DORITOS) 
           ITEMPRICE=DORITOS 
           transaction(ITEMPRICE,choice)
      elif choice in {'b3','B3'}:
           print ('Price for Cheetos = ',CHEETOS)
           ITEMPRICE=CHEETOS 
           transaction(ITEMPRICE,choice)
      elif choice in {'c1','C1'}:
           print ('Price for TicTac = ',TICTAC)  
           ITEMPRICE=TICTAC
           transaction(ITEMPRICE,choice)
      elif choice in {'c2','C2'}:
           print ('Price for Starburst = ',STARBURST) 
           ITEMPRICE=STARBURST 
           transaction(ITEMPRICE,choice)
      elif choice in {'c3','C3'}:
           print ('Price for Skittles = ',SKITTLES)
           ITEMPRICE=SKITTLES
           transaction(ITEMPRICE,choice)
      else: 
           print('Not a valid choice!!!')

def transaction(ITEMPRICE,choice):
    #LOCAL VARIABLES
    user_money = 0.0
    temp_money =0.0
    #change_due = 0.0
    reenter = 'y'
    #while reenter == 'y' :
    while temp_money < ITEMPRICE and reenter == 'y':
    	user_money = float(input('Enter $1 bill for your transaction\n'))
    	if (user_money != 1.0):
    		reenter = input('INVALID AMMOUNT,Do you want to continue the transaction?(y/n)')
    		transactionexit(reenter,temp_money,choice,ITEMPRICE)
    	else:
    		temp_money = temp_money + user_money
    		reenter = 'y'
    transactionexit(reenter,temp_money,choice,ITEMPRICE)
    #change_due = temp_money - ITEMPRICE
    #print ('Item dispensed:',choice,'\nChange Due:',format(change_due,'.2f'))

def transactionexit(reenter,temp_money,choice,ITEMPRICE):
	change_due = 0.0
	if(reenter =='n' and temp_money == 0.0):
		print ("Thank you, have a good day")
	else:
		#print (temp_money)
		#print (ITEMPRICE)
		change_due = temp_money - ITEMPRICE
		print ('Item dispensed:',choice,'\nChange Due:',format(change_due,'.2f'))
		              
         
main()



