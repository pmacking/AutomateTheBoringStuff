def addToInventory(inventory, addedItems):
    for i in dragonLoot:
        if i not in inv.keys():
            inv.setdefault(i, 1)
        else:
            inv[i]+=1
    print(inv)


def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print (str(v) + ' ' + k)
        item_total+=inventory[k]
    print("Total number of items: " + str(item_total))

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addToInventory(inv, dragonLoot)
displayInventory(inv)