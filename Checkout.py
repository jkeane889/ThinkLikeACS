def checkout():
    total = 0
    count = 0
    moreItems = True
    while moreItems:
        price = float(input('Enter price of your next item (0 when done): '))
        if price < 0:
            print("Error. Please try re-entering the price.")
        elif price != 0:
            count = count + 1
            total = total + price
            print('Subtotal: $', total)
        else:
            moreItems = False
    average = total / count
    print('Total items:', count)
    print('Total $', total)
    print('Average price per item: $', average)

checkout()
