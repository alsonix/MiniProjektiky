encod = "UTF-8"

encod = input("Encoding UTF-8, UTF-16, UTF-32 (DEFAULT UTF-8): ")
baud = int(input("Baud: "))

calcutf8bytes = (8*baud)/8
calcutf16bytes = (16*baud)/8
calcutf32bytes = (32*baud)/8

if encod == "UTF-8" or encod == "utf-8":
  print()
  print(8*baud, "bit/s")
  print(calcutf8bytes, "B/s")
  print()
  
elif encod == "UTF-16" or encod == "utf-16":
  print()
  print(16*baud, "bit/s")
  print(calcutf16bytes, "B/s")
  print()
  
elif encod == "UTF-32" or encod == "utf-32":
  print()
  print(32*baud, "bit/s")
  print(calcutf32bytes, "B/s")
  print()
  
else:
  print()
  print(8*baud, "bit/s")
  print(calcutf8bytes, "B/s")
  print()
  
  end = input()
