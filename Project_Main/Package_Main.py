# Class for packages
# The class calls functions from the distance functions in Distance_Main.py file

##############################IMPORTS##########################
import datetime
from Project_Main import Distance_Main
from Project_Main.Distance_Main import calculate_shortest_distance, truck_1_state_index, inspect_distances, \
    truck_1_state_list, first_truck, current_distance, truck_2_state_index, truck_2_state_list, second_truck, \
    truck_3_state_index, truck_3_state_list, third_truck
from Project_Main.Reader import check_truck_1_trip, get_hash_map, check_truck_2_trip, check_truck_1_trip_2

##############################VARIABLES##########################

# Define times when the truck left hub
times = '8:00:00'
times_2 = '9:10:00'
times_3 = '11:00:00'

deliver_1 = []
deliver_2 = []
deliver_3 = []
distance_truck_1 = []
distance_truck_2 = []
distance_truck_3 = []
##############################FORMAT TIMES##########################

# Format the times from each time variable
(h, m, s) = times.split(':')
convert_first_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
(h, m, s) = times_2.split(':')
convert_second_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
(h, m, s) = times_3.split(':')
convert_third_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

##############################TRUCK TRIPS AND DISTANCES AND PACKAGE DETAIL##########################
# Loop through each package for delivery status for the first truck
# Space-time complexity is O(N)
i = 0 # Set counter
for value in check_truck_1_trip():
    check_truck_1_trip()[i][9] = times
    deliver_1.append(check_truck_1_trip()[i])
    i += 1

# Loop through addresses
# Compare the address to list of all address
# Add address to an index
# Space-time complexity is O(N^2)
try:
    count_1 = 0
    for k in deliver_1:
        for j in Distance_Main.check_address():
            if k[2] == j[2]:
                distance_truck_1.append(j[0])
                deliver_1[count_1][1] = j[0]
        count_1 += 1
except IndexError:
    pass
# Algorithm to sort packages
calculate_shortest_distance(deliver_1, 1, 0)
calculates_truck_1 = 0

# Loop through all values for truck 1
# Calculates the total distance of truck 1
# Calculates the distances of the packages for truck_1
# Space-time complexity is O(N)
truck_1_p_id= 0
for index in range(len(truck_1_state_index())):
    try:
        # calculate the total distance of the truck
        calculates_truck_1 = inspect_distances(int(truck_1_state_index()[index]), int(truck_1_state_index()[index + 1]), calculates_truck_1)
        # calculate the distance of each package along the route
        deliver_package = first_truck(current_distance(int(truck_1_state_index()[index]), int(truck_1_state_index()[index + 1])))
        truck_1_state_list()[truck_1_p_id][10] = (str(deliver_package))
        get_hash_map().update(int(truck_1_state_list()[truck_1_p_id][0]), deliver_1)
        truck_1_p_id += 1
    except IndexError:
        pass
# Same steps in truck 1 are used for truck 2
# Same space-time-complexity for truck 1 is for truck 2
# Same algorithm used in truck 1 is used for truck 2
i = 0
for value in check_truck_2_trip():
    check_truck_2_trip()[i][9] = times_2
    deliver_2.append(check_truck_2_trip()[i])
    i += 1
try:
    count_2 = 0
    for k in deliver_2:
        for j in Distance_Main.check_address():
            if k[2] == j[2]:
                distance_truck_2.append(j[0])
                deliver_2[count_2][1] = j[0]
        count_2 += 1
except IndexError:
    pass

calculate_shortest_distance(deliver_2, 2, 0)
calculates_truck_2 = 0
truck_1_p_id = 0
for index in range(len(truck_2_state_index())):
    try:
        calculates_truck_2 = inspect_distances(int(truck_2_state_index()[index]), int(truck_2_state_index()[index + 1]), calculates_truck_2)
        deliver_package = second_truck(current_distance(int(truck_2_state_index()[index]), int(truck_2_state_index()[index + 1])))
        truck_2_state_list()[truck_1_p_id][10] = (str(deliver_package))
        get_hash_map().update(int(truck_2_state_list()[truck_1_p_id][0]), deliver_2)
        truck_1_p_id += 1
    except IndexError:
        pass

# for loop updates the delivery status of all packages in truck 1 (second delivery) to 'In transit'
# Same steps in truck 1 are used for truck 1 trip 2
# Same space-time-complexity for truck 1 is for truck 1 trip 2
# Same algorithm used in truck 1 is used for truck 1 trip 2
i = 0
for value in check_truck_1_trip_2():
    check_truck_1_trip_2()[i][9] = times_3
    deliver_3.append(check_truck_1_trip_2()[i])
    i += 1

try:
    count_2 = 0
    for k in deliver_3:
        for j in Distance_Main.check_address():
            if k[2] == j[2]:
                distance_truck_3.append(j[0])
                deliver_3[count_2][1] = j[0]
        count_2 += 1
except IndexError:
    pass

calculate_shortest_distance(deliver_3, 3, 0)
calculates_truck_3 = 0

truck_1_p_id = 0
for index in range(len(truck_3_state_index())):
    try:
        calculates_truck_3 = inspect_distances(int(truck_3_state_index()[index]), int(truck_3_state_index()[index + 1]), calculates_truck_3)
        deliver_package = third_truck(current_distance(int(truck_3_state_index()[index]), int(truck_3_state_index()[index + 1])))
        truck_3_state_list()[truck_1_p_id][10] = (str(deliver_package))
        get_hash_map().update(int(truck_3_state_list()[truck_1_p_id][0]), deliver_3)
        truck_1_p_id += 1
    except IndexError:
        pass

##############################TOTAL DISTANCES##########################

# Define a function to add all distance of each truck and return the total distance
# Space-time complexity is O(1)
def total_distance():
    total_distance = calculates_truck_1 + calculates_truck_2 + calculates_truck_3
    return total_distance

