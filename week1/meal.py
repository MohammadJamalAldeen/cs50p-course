def main():
     t = input("write your time: ")
     t = convert(t)
     if 7 <= t <= 8 :
          print("breakfast time")
     elif 12 <= t <= 13 :
          print("lunch time")
     elif 18 <= t <= 19 :
          print("dinner time")
def convert(time):
     time = time.strip()
     am = False
     pm = False
     if "p.m." in time :
          pm = True
          time = time.replace("p.m.","")
     elif "a.m." in time :
          am = True
          time = time.replace("a.m.","")
     hours, minutes = time.split(":")
     hours = int(hours)
     minutes = int(minutes)
     if pm and hours != 12 :
          hours = hours + 12
     elif am and hours == 12 :
          hours = hours - 12
     return(((((hours)*60) + (minutes))/60))

if __name__ == "__main__":
    main()

