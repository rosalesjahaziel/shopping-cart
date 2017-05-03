def get_order():
    print "[command] [item] (command is a to add, d to delete, q t quit)"
    line = raw_input()

    command = line[:1]
    item = line[2:]

    return command, item

def process_order(order, cart):
    command, item = order

    if command == "a":
        cart.append(item)
    elif command == "d" and item in cart:
        cart.remove(item)
    elif command == "q":
        return False
    
    return True

def go_shopping():
    cart = []
    
    while True:
        order = get_order()
        if not process_order(order, cart):
            break 

    print cart
    print "Finished!"

go_shopping()