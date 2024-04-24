def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    temps = input()
    user_input = [float(user) for user in temps.split(",")]
    return user_input

def calc_average(list):
    calc = sum(list) / len(list)
    print("\ncalc_average", calc)

def find_min_max(user_input):
    min_temp = min(user_input)
    max_temp = max(user_input)
    print("\nMinimum Temperature: ", min_temp)
    print("\nMaximum Temperature: ", max_temp)

def sort_temperature(user_input):
    sorted_temp = user_input.sort()
    print("\nSorted Temperature :\n", user_input)

def calc_median_temperature():
    print("median floats")


def main():
    display_main_menu()
    user_temp = get_user_input()
    sort_temperature(user_temp)
    find_min_max(user_temp)
    calc_average(user_temp)




if __name__ == "__main__":
    main()