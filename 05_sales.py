customerName = input("Enter your name:")
purchaseAmount = int(input("Enter purchaseAmount:"))
premiumMember = True

# discount
discount = 0
if(purchaseAmount >= 5000 or premiumMember):
    discount = purchaseAmount * 15 / 100
else:
    discount = purchaseAmount * 5 / 100

print("||---==== CUSTOMER INFO ==== ----||")
print("customerName:",customerName)
print("purchaseAmount:",purchaseAmount)
print("discount:",discount)
print("===================================")
print("Final Amount:",purchaseAmount - discount)