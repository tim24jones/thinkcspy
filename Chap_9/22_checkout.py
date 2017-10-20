def checkout():
    total = 0
    count = 0
    moreItems = True
    while moreItems:
        price = float(input('Enter price of item (0 when done): '))
        if price != 0:
            count = count + 1
            total = total + price
            roundedtotal=round(total,2)
            print('Subtotal: $', roundedtotal)
        else:
            moreItems = False
    average = total / count
    roundedtotal=round(total,2)
    roundedaverage=round(average,2)
    print('Total items:', count)
    print('Total $', roundedtotal)
    print('Average price per item: $', roundedaverage)

checkout()
