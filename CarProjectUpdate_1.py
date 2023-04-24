# all of the current dictionaries with 10 manufacturers
Bmw_dict = {
    'Bmw Models': {
        "1 Series": "$32,000 to $44,000",
        "2 Series": "$35,300",
        "3 Series": "$41,450 to $54,700",
        "4 Series": "$45,200 to $53,300",
        "5 Series": "$54,200 to $62,250",
        "6 Series": "$67,350 to 86,250",
        "7 Series": "$86,800 to 95,900",
        "8 Series": "$85,000 to $94,400",
    },
    'Maintenance': {
        "Average annual maintenance cost": '$750 to $1,200'
    }
}

Audi_dict = {
    'Audi Models': {
        "Audi A Class": "$34,945 to 87,545",
        "Audi Q Class": "$37,095 to $71,395",
        "Audi S Class": "$45,,945 to $131,945",
        "Audi RS Class": "$76,145 to $120,495",
        "Audi TT Class": "$51,545 to $73,545",
    },
    'Maintenance': {
        "Average annual maintenance cost": "$987"
    }
}

Benz_dict = {
    'Mercedes Models': {
        "A-Class": "$33,650 to $45,850",
        "C-Class": "$41,600 to $60,000",
        "E-Class": "$54,950 to $68,400",
        "B-Class": "$39,900 to $51,000",
        "G-Class": "$133,250 to $157,750"
    },
    'Maintenance': {
        "Average annual maintenance cost": "$908"
    }
}

Nissan_dict = {
    'Nissan Models': {
        "Nissan Versa": "$15,080",
        "Nissan Sentra": "$19,510",
        "Nissan Altima": "$24,550",
        "Nissan Rogue": "$26,050",
        "Nissan Pathfinder": "33,410",
        "Nissan GT-R": "$113,540 to $215,690"
    },
    'Maintenance': {
        "Average annual maintenance cost": "$500"
    }
}

Honda_dict = {
    'Honda Models': {
        "Honda Odyssey": "$33,040",
        "Honda Pilot": "$37,580",
        "Honda Accord": "$26,120",
        "Honda Civic": "$22,350",
        "Honda CR-V": "$26,400",
        "Honda Type R": "$37,895"
    },
    'Maintenance': {
        "Average annual maintenance cost": "$428"
    }
}

Ford_dict = {
    'Ford Models': {
        "Ford Bronco Sport": "$27,415 to $33,230",
        "Ford Expedition": "$68,150 to $76,765",
        "Ford Super Duty": "$34,035 to $46,930",
        "Ford Explorer": "$33,145 to $44,745",
        "Ford F-150": "$29,990 to $37,700",
        "Ford Ranger": "$25,500 to $27,900",
        "Ford Escort": "$22,040 to $28,205",
        "Ford Mustang": "27,205 to $32,705"
    },
    'Maintenance': {
        "Average annual maintenance cost": "$775"
    }
}

Chevy_dict = {
    'Chevy Models': {
        "Camaro": "$34,000 to $40,000",
        "Corvette": "$59,900 to $80,000",
        "Silverado": "$29,300 to $36,500",
        "Chevy Colorado": "$25,200 to $43,200",
        "Chevy Equinox": "$23,800 to $31,400",
        "Chevy Traverse": "$29,800 to $40,000",
        "Chevy Bolt EV": "$36,500 to $42,695",
        "Chevy Impala": "$28,000 to $38,000",
        "Chevy Malibu": "$24,400"
    },
    'Maintenance': {
        "Average annual maintenance cost": "$1,192"
    }
}

Porsche_dict = {
    'Porsche Models': {
        "Porsche Taycan": "$79,900 to $150,900",
        "Porsche Cayenne": "$67,500 to $107,300",
        "Porsche Macan": "$52,100 to $72,100",
        "Porsche 718 Cayman": "$59,900 to $71,900",
        "Porsche 718 Boxter": "$62,000 to $74,000",
        "Porsche 911": "$99,200 to $112,000"
    },
    'Maintenance': {
        "Average annual maintenance cost": "$1,192"
    }
}

"""prints dict in neat format"""
def PD(dic):
    for key, value in dic.items():
        print(key, ':')
        for Models, Price in value.items():
            print(Models, ':', Price)


"""this will keep on prompting the user to enter
a value till the user quits the dict"""
while True:
    i = input("What car make are you looking for? ")
    print("Enter 'q' to quit at any time")
    u = i.upper()
    if u == 'BMW':
        PD(Bmw_dict)
    elif u == 'PORSCHE':
        PD(Porsche_dict)
    elif u == 'NISSAN':
        PD(Nissan_dict)
    elif u == 'CHEVY':
        PD(Chevy_dict)
    elif u == 'CHEVROLET':
        PD(Chevy_dict)
    elif u == 'FORD':
        PD(Ford_dict)
    elif u == 'BENZ':
        PD(Benz_dict)
    elif u == 'MERCEDES':
        PD(Benz_dict)
    elif u == 'MERCEDES BENZ':
        PD(Benz_dict)
    elif u == 'AUDI':
        PD(Audi_dict)
    elif u == 'Q':
        break
