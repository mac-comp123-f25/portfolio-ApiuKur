def has_q(a):

 q="q"
 if q in a:
    return True
 else:
   return False
has_q("Mary")

if __name__ == "__main__":
  assert has_q("quick") == True
  assert has_q("math") == False
  print("All tests passed!")


