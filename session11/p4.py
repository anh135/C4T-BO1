price = {
    "hp": 600, 
    "macbook": 500,
    "asus": 400,
    "acer": 350,
    "toshiba": 600,
    "fujitsu": 900,
    "alienware": 1000,
}

# print(price[input("brand: ")])

x = price[input("brand: ")]
s = x * int(input("numbers: "))
print("total price: ", s)


