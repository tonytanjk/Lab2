#Code done by Tony from ET0375 of DOAIOT @ SP
def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input(): #grabs user input from terminal
    temps = input()
    user_input = [float(user) for user in temps.split(",")]
    return user_input

def calc_average(list): # adds all values and divides by number of values
    calc = sum(list) / len(list)
    print("\ncalc_average", calc)
    return calc

def find_min_max(user_input): #identify min and max value given from get_user_input function
    min_temp = min(user_input)
    max_temp = max(user_input)
    print("\nMinimum Temperature: ", min_temp)
    print("\nMaximum Temperature: ", max_temp)
    return [min_temp,max_temp]

def sort_temperature(user_input):
    user_input.sort()
    print("\nSorted Temperature :", user_input)

def calc_median_temperature(list):
    import statistics
    median = statistics.median(list)
    print("Median of List:\n", median)
    return median


def main():
    display_main_menu()
    user_temp = get_user_input()
    sort_temperature(user_temp)
    find_min_max(user_temp)
    calc_average(user_temp)
    calc_median_temperature(user_temp)


if __name__ == "__main__":
    main()