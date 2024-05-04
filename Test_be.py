import BE
#test_BE.py

def test_find_min_max():
   test_temps = [12,23,25,10,5,15,20]
   test_arr = [5, 25]
   result = BE.find_min_max(test_temps)
   assert (result == test_arr)

def test_calc_average():
   test_temps = [12,23,25,10,5,15,20]
   result = BE.calc_average(test_temps)

   assert (result == (sum(test_temps) / len(test_temps)))

def test_calc_median_temperature():
   import statistics
   test_temps = [12,23,25,10,5,15,20]
   result = BE.calc_median_temperature(test_temps)

   assert (result == statistics.median(test_temps))