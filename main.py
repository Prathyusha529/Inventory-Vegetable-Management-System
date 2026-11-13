veg=[]
quantity=[]
price=[] 
sales_item=[]
sales_quantity=[]
sales_amt=[]
Name=input("Who you are SHOPKEEPER/CUSTOMER:")
if Name=='shopkeeper':
    while True:
        print("choose one option:")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Update Item")
        print("4. View Inventory")
        print("5. View Sales Report")
        print("6. Exit")
        ch=int(input("Enter your choice:"))
        if ch==1:
            add_item=input("Do yo want to add the item yes/no:")
            while add_item=='yes':
                vegetable=input("Enter vegetable name:")
                qty=int(input(f' Add the quantity of {vegetable}:'))
                pr=int(input(f' Add the price of {vegetable}:'))
                veg.append(vegetable)
                quantity.append(qty)
                price.append(pr)
                print(f' {vegetable} added successfully')
                add_item=input("Do you want to add more items yes/no:")
            
        #Remove item
        elif ch==2:
            remove_item=input("Do you want to remove the item yes/no:")
            while remove_item=='yes':
                r_veg=input("Enter the vegetable name:")
                if r_veg in veg:
                    idx=veg.index(r_veg)
                    veg.remove(r_veg)
                    quantity.pop(idx)
                    price.pop(idx)
                    print(f' {r_veg} is removed successfully')
                else:
                    print(f' {r_veg} not found')
                remove_item=input("Do you want to remove more items yes/no:")
        elif ch==3:
            update_item=input("Do you want to update an item yes/no:")
            if update_item=='yes':
                up_veg=input("Enter the vegetable name:")
                if up_veg in veg:
                    idx=veg.index(up_veg)
                    quantity[idx]=float(input("Enter the update quantity:"))
                    price[idx]=float(input("Enter the update price:"))
                    print(f' {up_veg} updated successfully')
                else:
                    print(f' {up_veg} not found')

        elif ch==4:
            print(" NAME",' '*8,'QUANTITY',' '*6,'PRICE')
            print('_'*40)
            for i in zip(veg,quantity,price):
                print(f' {i[0]: <15}{i[1]: <15}{i[2]}')

        elif ch==5:
            print(" ITEM",' '*8,'QUANTITY',' '*6,'AMOUNT')
            print('_'*40)
            for i in zip(sales_item,sales_quantity,sales_amt):
                print(f' {i[0]: <15}{i[1]: <15}{i[2]}')

        elif ch==6:
            break

        else:
            print("Choose correct option")
           
       
        
if Name=='customer':
    cart_items=[]
    cart_quantity=[]
    cart_amt=[]
    while True:
        item=input("What do yo want (type 'done' to finish):")
        if item=='done':
            view_cart=input("Do you want to view the cart yes/no:")
            if view_cart=='yes':
                print('*'*15, 'VCube Vegtable Bill','*'*15)
                print('ITEM',' '*5,'QUANTITY',' '*5,'AMOUNT')
                print('_'*40)
                for i in zip(cart_items,cart_quantity,cart_amt):
                    print(f' {i[0]: <10}{i[1]: <10}{i[2]: <10}')
                total_sum=sum(cart_amt)
                print(total_sum)
                print()
                print() 
                print("Happy Customer")
                print("Visit Again...")
            break
        elif item in veg:
            qty=float(input(f' Enter the quantity of {item} you want:'))
            idx=veg.index(item)
            if qty<=quantity[idx]:
                amount=qty*price[idx]
                quantity[idx]=quantity[idx]-qty
                cart_items.append(item)
                cart_quantity.append(qty)
                cart_amt.append(amount)
                sales_item.append(item)
                sales_quantity.append(qty)
                sales_amt.append(amount)
            else:
                print(f' {item} is out of stock')
        else:
            print(f' {item} is not available')