#
# Example file for working with classes
#
class myClass():
  def method1(self):
    print("myClass Method1")

  def method2(self,someString):
    print("myClass Method2 " + someString )

class anotherClass(myClass):
  def method1(self):
    myClass.method1(self)
    print("anotherClass Method1")

  def method2(self,someString):
    myClass.method2(self,"Dummy value")
    print("anotherClass Method2 " + someString)

def main():
  c = myClass()
  c.method1()
  c.method2("String obj")

  c2 = anotherClass()
  c2.method1()
  c2.method2("Inherited method class2")
  
if __name__ == "__main__":
  main()
