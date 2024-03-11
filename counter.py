# apple banana beer suryatr
shop_items = ["apple" , "banana" , "beer" , "surya"]
while True:
    shop = input(f"What would you like to purchase {shop_items}? ").lower().strip()
    if shop in shop_items:
        break
