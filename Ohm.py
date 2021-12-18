while (1):
    print("1. Calculate Voltage")
    print("2. Calculate Resistance")
    print("3. Calculate Current")
    print("4. Exit Program")
    ask = input("> ")
    if (ask == "1"):
        print("-- Calculating Voltage --")
        i = float(input("Current: "))
        r = float(input("Resistence: "))
        v = i * r
        print("Voltage = ", format(v, ".2f"))

    elif(ask == "2"):
        print("-- Calculating Resistance --")
        v = float(input("Voltage: "))
        i = float(input("Current: "))
        r = v / i
        print("Resistance = ", format(r, ".2f"))

    elif(ask == "3"):
        print("-- Calculating Current --")
        v = float(input("Voltage: "))
        r = float(input("Resistence: "))
        i = v / r
        print("Current = ", format(i, ".2f"))

    elif(ask == "4"):
        break
    else:
        print("Not an Input Try again")




