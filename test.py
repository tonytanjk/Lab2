#Code done by Tony With Aid of ChatGPT
temps = []
import time
def calc_average(min_temp, max_temp):
    average = (min_temp + max_temp) / 2
    print("Average temperature:", average)

def get_user_input():
    temps_str = input("Enter temperatures separated by commas: ")
    try:
        temps = [float(temp) for temp in temps_str.split(",")]
    except ValueError:
        print("Invalid Input. Try Again")
        return []
    return temps

def find_min_max(temps):
    if temps:
        min_temp = min(temps)
        max_temp = max(temps)
        print("Minimum temperature:", min_temp)
        print("Maximum temperature:", max_temp)
    else:
        print("Temperatures not recorded yet. Please enter temperatures first.")

def clear_temp():
    global temps
    temps = []
    print("Temperature list cleared.")

def display_main_menu():
    print("\nMain Menu:")
    print("1. Enter Temperature Recordings")
    print("2. Find Min_Max Temperature")
    print("3. Calculate Average Temperature")
    print("4. Show Temperature List")
    print("5. Clear Temperature List")
    print("6. Exit")

def main():
    while True:
        display_main_menu()
        valid_selection = False
        while not valid_selection:
            selection = input("Enter your choice: ")
            if selection.isdigit():
                selection = int(selection)
                valid_selection = True
            else:
                print("Invalid Input, Please enter a valid integer")
                time.sleep(0.5)
        if valid_selection == True:
            if selection == 1:
                global temps
                temps += get_user_input()
            elif selection == 2:
                find_min_max(temps)
                time.sleep(1)
            elif selection == 3:
                if temps:
                    min_temp = min(temps)
                    max_temp = max(temps)
                    calc_average(min_temp, max_temp)
                    time.sleep(1)
                else:
                    print("Temperatures not recorded yet. Please enter temperatures first.")
            elif selection == 4:
                print("List of Temperatures: ", temps)
                time.sleep(1)
            elif selection == 5:
                clear_temp()
            elif selection == 6:
                print("Exiting program.")
                break
            else:
                print("Invalid selection. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()