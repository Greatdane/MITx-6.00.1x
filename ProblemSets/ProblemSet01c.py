#Problem set 1c

order = "salad water hamburger salad hamburger" #example

def item_order(order):
    salad = int(order.count('salad')) #counting the string in order variable
    burger = int(order.count('hamburger'))
    water = int(order.count('water'))
    return "salad:" +str(salad) + " hamburger:" + str(burger) + " water:" + str (water)
    
print(item_order(order)) #testing!

    