def rgb_hex():
  invalid_msg = "You entered an invalid RGB value"
  red = int(input("Please enter a red value: "))
  if red < 0 or red > 255:
    print(invalid_msg)
    return
  green = int(input("Please enter a green value: "))
  if green < 0 or green > 255:
    print(invalid_msg)
    return
  blue = int(input("Please enter a blue value: "))
  if blue < 0 or blue > 255:
    print(invalid_msg)
    return
  val = (red << 16) + (green << 8) + blue
  print(hex(val).upper())
  
def hex_rgb():
  hex_val = input("Please enter a hex value: ")
  if len(hex_val) != 6:
    print("You entered an invalid hex value")
    return
  else:
    hex_val = int(hex_val, 16)
  two_hex_digits = 2**8
  blue = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  green = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  red = hex_val % two_hex_digits
  print("Your color in rgb is: RGB(%s, %s, %s)" % (red, green, blue))
  
def convert():
  while True:
    option = input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit:")
    if option == '1':
      print("RGB to Hex...")
      rgb_hex()
    elif option == '2':
      print("Hex to RGB...")
      hex_rgb()
    elif option.upper() == 'X':
      print("Exiting program")
      break;
    else:
      print("Error")
     
convert()

