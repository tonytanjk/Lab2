#Code done by Tony
global temps
temps = []
import time
def calc_average(min_temp,max_temp):
    average = print("calc_average="+(min_temp+max_temp/2))
    return average

def get_user_input():
    temps_list = input("Enter temperature readings seperated by commas\n")
    temps = (float(temps) for temps in temps_list.split(",")) #Str list to float conversion
    return(temps)

def find_min_max(temps):
    if temps:
        min_temp = min(temps)
        max_temp = max(temps)
        print("\nMinimum Temperature: "+(min_temp))
        print("Maximum Temperature: "+(max_temp))
        time.sleep(1)
        return min_temp, max_temp
    else:
        print("temps not recorded yet, pls do temperature entry first")
        return display_main_menu()

def display_main_menu():
    print("Main Menu:")
    print("1.Enter Temperature Recordings")
    print("2.Find Min_Max Temperature")
    print("3.Calculate Average Temperature")
    print("4.Show Temperature List")
    print("5.Clear Temperature List")
    print("6.Exit Program")

def main():
    print("ET0375 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    while True:
        display_main_menu()
        selection = int(input())
        if selection == 1:
            temps = get_user_input()
            print(temps)
            
        elif selection == 2:
            find_min_max(temps)
            
        elif selection == 3:
            min_temp = min(temps)
            max_temp = max(temps)
            calc_average(min_temp,max_temp)
            
        elif selection == 4:
            print(temps)

        elif selection == 5:
            temps = []
            
        elif selection == 6:
            print("Exiting Program")
            time.sleep(1)
            break
        else:
            print("Please select between values 1 to 5")
            time.sleep(1)

if __name__ == "__main__":
    main()
