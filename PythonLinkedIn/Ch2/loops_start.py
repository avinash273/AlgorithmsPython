#
# Example file for working with loops
#

def main():
  x = 0

  # define a while loop
  while (x < 5):
    print("While: ",x)
    x = x+1

  # define a for loop
  for x in range(5,10):
    print("For: ",x)

  # use a for loop over a collection
  days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

  for x in days:
    print("All Days: ",x)
 
  # use the break and continue statements
  for x in range(5,10):
    #if(x==7): break
    if(x%2 == 0): continue
    #continue just means that, you need to continue and do nothing is the value satisfies
    print(x)

  #using the enumerate() function to get index 
  days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

  for i,x in enumerate(days):
    print(i,",All Days: ",x)

if __name__ == "__main__":
  main()
