inventory = {
    'olma':10,
    'anor':15,
    'nok':23
}

product = input("mshsulotni kiriting : ").strip()
if product in inventory:
    print(inventory[product])
else:
    print('quantity = 0')