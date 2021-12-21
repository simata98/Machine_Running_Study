x = '00081CFA'
y = '06391A30FFD1A163'
def convert(x):
  if len(x) < 16:
    while len(x) < 16:
      print(x)
      x = '00' + x
      print(x)
  return x

print(convert(x))
print(convert(y))