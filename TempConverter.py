#simple temperature converter
#https://courses.edx.org/courses/course-v1:MITx+6.00.1x_9+2T2016/discussion/forum/6.00.1x_General/threads/575d833135c79c0562000340

print("Welcome to the temperature scale conversion script\n") 
#note - the \n on the string. This is just an escape sequence and it's used on string formatting to print a new line
celsius = float(raw_input("Enter the value in C to convert:\n"))
#we are using Celsius as the default temperature and then convert it to Fahrenheit and Kelvin. raw_input() handles input as strings, 
#so we have to convert the input to a numerical value! We do this as follows variable = float(raw_input("msg")
while(celsius < -273.15):
    print("Enter a valid temperature input\n")
    celsius = float(raw_input("Enter the value in C to convert:\n"))
fahrenheit = celsius * 9.0 / 5.0 + 32 #F = C * 9/5 + 32
kelvin = celsius + 273.15 #celsius + 273.15 - This is why we check we don't have a number below -273.15!
print("%.2f C = %.2f F and %.2f K"% (celsius, fahrenheit, kelvin))
#Place holders in Python work as follows: %s for strings, %f for floats, etc and replaces the annoying task of converting the temperature 
#variables to strings in the print function. The .2 that lies between % symbol and the f means the decimal place i want my solution to display,
#in this case it will only show 2 decimal places.

# print("%f %s" %(variable1, variable2))
# where variable1 is a float and variable2 is a string.