def has_QOCD(b):
 letters=["O","Q","C","D"]
 for i in b:
  if i in letters:
       return True
 else:
  return False



if __name__ == "__main__":
  assert has_QOCD("Quick") == True
  assert has_QOCD("Odd") == True
  assert has_QOCD("MAC") == True
  assert has_QOCD("WiLD") == True
  assert has_QOCD("MATH") == False
  assert has_QOCD("comp123") == False
  print("All tests passed!")
