def add_fruit(inventory, fruit, quantity):
    if inventory.get(fruit)==None:
        inventory[fruit]=quantity
    else:
        inventory[fruit]=quantity+inventory.get(fruit)#
new_inventory={}
add_fruit(new_inventory,'strawberries',10)
print('strawberries' in new_inventory)
print(new_inventory['strawberries'])
add_fruit(new_inventory,'strawberries',25)
print(new_inventory['strawberries'])

# make these tests work...
# new_inventory = {}
# add_fruit(new_inventory, 'strawberries', 10)
# test('strawberries' in new_inventory, True)
# test(new_inventory['strawberries'], 10)
# add_fruit(new_inventory, 'strawberries', 25)
# test(new_inventory['strawberries'] , 35)
