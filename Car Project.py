Car_dict = {
    "Make": {
        "Audi": {
            "Average price": "$35,654",
            "Average maintenance cost": "$987"
        },
        "Mercedes": {
            "Average price": "$54,250",
            "Average maintenance cost": "$908"
        },
        "Bmw": {
            "Average price": "$35,203",
            "Average maintenance cost": "$750 to $1,200"
        },
        "Chevy Truck": {
            "Price range": "$29,300  to $35,600",
            "Average maintenance cost": "$649"
        },
        "Ford": {
            "Price range": "$32,765 to $36,675",
            "Average maintenance cost": "$775"
        },
        "Honda": {
            "Price range": "$21,700 to $22,900",
            "Average maintenance cost": "$428"
        },
        "Nissan": {
            "Price range": "$24,350 to $34,150",
            "Average maintenance cost": "$500"
        },
        "Porsche": {
            "Price range": "$101,200 to $121,300",
            "Average maintenance cost": "$1,192"
        },
        "Lexus": {
            "Price range": "$35,000 to $90,000",
            "Average maintenance cost": "$551"
        }
    }
}
Name = input("What Make are you looking for?")
if Name == 'Bmw' or 'bmw':
    print(Car_dict['Make']['Bmw'], )

if Name == 'Nissan' or 'nissan':
    print(Car_dict['Make']['Nissan'])