##define function
def card_counter():
##initial count set to 0
    count = 0
##while loop
    while True:
##enter card to start count
        card = input("Enter card value (2-10, J, Q, K, A) or type 'quit' to exit: ").upper()
##if type QUIT quit
        if card == 'QUIT':
            break
##7,8,9 have no value
        elif card in ['7', '8', '9']:
            print("7, 9, and 9, have no value")
##2-6 value +1
        elif card in ['2', '3', '4', '5', '6']:
            count += 1
##10 j q k a value -1
        elif card in ['10', 'J', 'Q', 'K', 'A']:
            count -= 1
        else:
            print("Invalid card value. Please enter a valid card value or 'quit' to exit.")
            continue
##print count
        print("Current count:", count)
    print("Final count:", count)

if __name__ == "__main__":
    card_counter()