import random
def main():
   pointes=0
   mistakes = 0
   questions=10
   lev = get_level()
   for i in range (questions):
       x = generate_integer(lev)
       y = generate_integer(lev)
       while True:
           print(f"{x} + {y} =",end=" ")
           solve =input()
           try:
               solve = int(solve)
           except ValueError:
               pass
           if solve == x+y:
               pointes+=1
               break
           else:
               print("EEE")
               mistakes +=1
           if mistakes == 3:
               print(f"{x} + {y} =",x+y)
               break
       mistakes = 0
   print("score:" , pointes)
def get_level():
   while True:
       try:
           level = int(input("Level: "))
           if level in [1, 2, 3]:
               return level
       except ValueError:
           pass
def generate_integer(level):
   if level==1:
       return random.randint(0, 9)
   elif level==2:
       return random.randint(10, 99)
   else:
       return random.randint(100, 999)
if __name__ == "__main__":
   main()
