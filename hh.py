product_price=int(input("Enter the price of product:"))
if product_price >3000 :
  print("your price after 20% discount is {}".format(product_price*0.8))
elif  product_price >=2000 and product_price<=3000 :
  if product_price==2999:
      print("congragulation you will get extra gift")
  print("your price after 30% discount is {}".format(product_price*0.7))

elif  product_price >=100 and product_price<=2000 :
  print("your price after 40% discount is {}".format(product_price*0.6))
else:
  print("Lets drink tea")