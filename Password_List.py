import os
import sys
import time
import colorama
import winsound
from colorama import Fore

Frequency = 2500
Duration = 1000
winsound.Beep(Frequency,Duration)

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

def main():

    print("""
  †††††††††††††††††††††††††††††††††††††††††††††††††††††††††
  | Usage =>                                              |         
  |                                                       |
  |     Command :       Description:                      |
  |                                                       |
  |     (1234 of ...)   Value for generate                |
  |                                                       |
  |     Example >                                         |
  |                     *12340987*                        |
  |               *And wait for create*                   |
  |            ~~~~~~~~~~~~~~~~~~~~~~~~~~~                |
  |               Coded By : @Ac3ess                      |
  |               For : @BlackHatsIR                      |
  |            Tools : @BlackHatsIRTools                  |
  |               GP = @DarkSecurity                      |
  |                   Join Us :)                          |
  †††††††††††††††††††††††††††††††††††††††††††††††††††††††††

""")
main()

User_List = []

def Generate_pass():
    try:
        Quess = int(input("\n[-] Set your digits for gerenate pass list (1234 of ...)  >  "))

        for Generator in range(0,Quess+1):
            User_List.append(Generator)
            len (User_List)
            print (User_List[Generator])

        time.sleep(2)
        CPU = os.cpu_count()
        print ("\n\a[!] CPU Usage > ",int(CPU))
        print ("\n\a[*] Press (Ctrl + C) for exit :)")

    except KeyboardInterrupt:
        print("\n\a[!] Shutting down...")
        time.sleep(3)
        sys.exit()

    except KeyError:
        print("\n[x] Error code | 0xc0000005")
        print("\n[x] Pressed digit not found!")
        time.sleep(4)
        sys.exit()

    except:
        print("\n[x] Error code | 0x90")
        print("\n[x] No pressed found!")
        time.sleep(4)
        sys.exit()

while True:
    Generate_pass()
