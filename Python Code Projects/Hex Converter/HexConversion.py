# Simple Hexadecimal to ASCII conversion program
# Joshua Pantoja 
# Last Edited 4/8/2022
print("Hexadecimal to ASCII Converter")
print()

i = False
while not i:

  Input = input("Insert Hex format for decoding: ")
  decoded = bytes.fromhex(Input)
  decoded = decoded.decode("ascii")
  print('Here is the decoded format:',decoded)
  print()

  i = input("Press 0 to Exit or any key to continue: ")
  if i == "0":
    i = True
  else: 
    i = False