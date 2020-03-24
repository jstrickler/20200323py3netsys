while True:
    temp_input = input("what is the temperature in Celsius?")
    if temp_input == "q":
        break
    if temp_input == "":
        continue
    celsius = float(temp_input)
    fahrenheit = ((9 * celsius) / 5) + 32.
    print ("The Farenheit temperature is {}".format(fahrenheit))
