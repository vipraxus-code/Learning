message = ""

while message != "quit":
    try:
        message = int(input("input your age and I tell you how much your ticket will cost: "))   
        if message == "quit":
            break
        elif message != "quit":
            if message > 0 and message <= 3:
                print("Your ticket will be free.")
                continue
            elif message > 3 and message <= 12:
                print("Ticket will cost you 10 dollars.")
                continue
            elif message > 12:
                print("Ticket will cost you 15 dollars.")
    except:
        print("Error")
        continue