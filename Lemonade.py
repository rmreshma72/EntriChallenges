#Lemonade Change

def change(bills,ch):   #Function for checking 
    index=bills.index(ch)
    bills.pop(index)
    return bills

pay=[5,10,20]
bills=[] #To take the bills from the customers

while True:
    try:
        print('\n👦Customer👧 Buying Lemonade🍋..')
        earn=int(input('Amount paying 💲: '))

        if earn not in pay:     #If customer not entering proper amount 
            raise ValueError
        elif earn == 5:         
            bills.append(earn)
        elif earn == 10:        #If customer paying $10 change $5 should be given
            if 5 in bills:
                bills.append(10)
                bills=change(bills,5)   
                print('\n$5 change given.. Thank you...')
            else:
                raise IndexError #If customer is paying $20
        elif earn == 20:
            
            if (5 in bills):
                bills=change(bills,5)
                if (10 in bills):   # If change $10 and $5 changes available.. $20 is added
                    bills.append(20)
                    bills=change(bills,10)  
                    print('\n$5 and $10 given as change.. Thank you..')
                elif (5 in bills):
                    bills=change(bills,5)
                    if (5 in bills):    #if three $5 changes available.  $20 is added
                        index5=bills.index(5)
                        bills=change(bills,5)   
                        print('\n3 x 5$ given as change .. Thank you...') 
                    else:
                        raise IndexError
                else:
                    raise IndexError
            elif ((10 in bills) or (20 in bills)):     #If $10 or $20 only available in the list
                raise IndexError
        else:
                raise IndexError
        
        print('\nBills:',bills)
    except IndexError:      #If changes are not available
        print('\nSorry...Change not available..\n')
        break
    except ValueError:      #If entered amount is invalid
        print('\nInvalid amount.. Amount can be paid is $5,$10,$20.')
        