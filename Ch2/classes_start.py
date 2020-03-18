#
# Example file for working with classes
#
class myClass():
  def method1(self):
    print("myClass Method1")

  def method2(self,someString):
    print("myClass Method1 " + someString )

def main():
  c = myClass()
  c.method1()
  c.method2("String obj")
  
if __name__ == "__main__":
  main()
