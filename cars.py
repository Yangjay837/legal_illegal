car=float(input("Enter the Base price of Maybach C Class:"))
Tax=float(input("Enter the Tax pricr of the Maybach:"))
license=float(input("Enterthe license of the Maybach:"))
Dealer_prep=float(input("Enter the Dealer_prep of the car:"))
DestinationCharge=float(input("Enter the Destination_charge:"))
actual_price=Tax + license  + Dealer_prep  + DestinationCharge  +car
print("Your Totalprice is",actual_price)


