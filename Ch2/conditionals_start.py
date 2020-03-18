#
# Example file for working with conditional statements
#

def main():
  x, y = 10, 10
  
  # conditional flow uses if, elif, else
  if (x > y):
    st = "x > y"
  elif ( x == y):
    st = "x == y"
  else:
    st = "y < x"

  print(st)

  # conditional statements let you use "a if C else b"
  st = "x > y" if (x > y) else "x < = y"
  print(st)

if __name__ == "__main__":
  main()
