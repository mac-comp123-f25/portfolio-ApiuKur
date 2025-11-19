def readfile(filename):
  file = open(filename, "r")
  text = file.read()
  file.close()
  return text

readme = readfile("../../ica/bike.py")

