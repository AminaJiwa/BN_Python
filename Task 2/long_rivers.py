class longRivers:
    rivers = [
    {"name": "Nile", "length": 4157},
    {"name": "Yangtze", "length": 3434},
    {"name": "Murray-Darling", "length": 2310},
    {"name": "Volga", "length": 2290},
    {"name": "Mississippi", "length": 2540},
    {"name": "Amazon", "length": 3915}
 ]
    #Task 1
    for r in rivers:
        for key in r:
            if key == "name":
                print(r[key])
    
    #Task 2
    totalLength = 0
    for r in rivers:
        for key in r:
            if key == "length":
                totalLength += r[key]
    print(totalLength)

    #Task 3
    for r in rivers:
        for key in r:
            if key == "name" and r[key][0] == "M":
                print(r[key])
    
    #Task 4
    for r in rivers:
        for key in r:
            if key == "length":
                length = float(r[key]) * 1.6
                print(length)
