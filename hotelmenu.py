Menu={
    'pizza':40,
    'pasta':50,
    'burger':60,
    'coffee':80,
}
#print(Menu)
print("welcome to restaurant")
order_total=0
item_1=input("enter name of item")
if item_1 in Menu:
    order_total+=Menu[item_1]
    print(f"your item{item_1}")

else:
    print(f"item{item_1} not found")

another_order=input("do you want to add item?")
if another_order=="yes":
    item_2=input("enter second item")
    if item_2 in Menu:
        order_total+=Menu[item_2]
        print(f"item{item_2}")
    else:
        print(f"order{item_2} is not available")
print(f"total{order_total}")