import csv
import datetime

##############################DISTANCE FILES##############################

# Create a CSV file for all the distances in WGU file
# and separate with a comma through the reader
with open('Distance_Table_Data.csv') as file_csv:
    read_mile = csv.reader(file_csv, delimiter=',')
    read_mile = list(read_mile)

# Create a CSV file for all the distance names in WGU file
# and separate with a comma through the reader
with open('Distance_Table_Name.csv') as file_names:
    read_name= csv.reader(file_names, delimiter=',')
    read_name = list(read_name)

##############################DISTANCE FUNCTIONS##############################

    # Define a function to get the values in rows and columns store values
    # Iterate through the location distances
    # Calculate the distances and return the total distance
    # The space-time complexity O(1)
    def inspect_distances(value_of_rows, value_of_columns, total_distance):
        dist = read_mile[value_of_rows][value_of_columns]
        if dist is '':
            dist = read_mile[value_of_columns][value_of_rows]
        total_distance += float(dist)
        return total_distance


    # Define a function to get the values in rows and columns store values
    # Iterate through the current distances
    # Calculate the distances and return the total distance
    # The space-time complexity O(1)
    def current_distance(value_of_rows, value_of_columns):
        dist = read_mile[value_of_rows][value_of_columns]
        if dist is '':
            dist = read_mile[value_of_columns][value_of_rows]
        return float(dist)

##############################TRUCK FUNCTIONS##############################

    # Variables for Truck
    truck_time_1 = ['8:00:00']
    truck_time_2 = ['9:10:00']
    truck_time_3 = ['11:00:00']

    # Define function for first truck
    # Get the total distance of first truck
    # The space-time complexity O(n)
    # Repeat for second and third trucks
    def first_truck(distance):
        times = distance / 18 # Calculate the distance of the truck "distance/18"
        # Format time using divmod() which returns a tuple Sources "www.w3schools.com/python/ref_func_divmod.asp"
        dist_mins = '{0:02.0f}:{1:02.0f}'.format(*divmod(times * 60, 60)) # divmod give mins and secs
        end_time = dist_mins + ':00'
        truck_time_1.append(end_time)
        sum = datetime.timedelta()
        for i in truck_time_1:
            (h, m, s) = i.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            sum += d
        return sum

    def second_truck(distance):
        times = distance / 18
        dist_mins = '{0:02.0f}:{1:02.0f}'.format(*divmod(times * 60, 60))
        end_time = dist_mins + ':00'
        truck_time_2.append(end_time)
        sum = datetime.timedelta()
        for i in truck_time_2:
            (h, m, s) = i.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            sum += d
        return sum

    def third_truck(distance):
        times = distance / 18
        dist_mins = '{0:02.0f}:{1:02.0f}'.format(*divmod(times * 60, 60))
        end_time = dist_mins + ':00'
        truck_time_3.append(end_time)
        sum = datetime.timedelta()
        for i in truck_time_3:
            (h, m, s) = i.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            sum += d
        return sum

##############################ADDRESS FUNCTIONS##############################

    # Define a function to return information for the packages in Package_Main
    # Space-time complexity is O(1)
    def check_address():
        return read_name

##############################STATE OF TRUCK FUNCTIONS##############################
    # Variables for state of trucks
    truck_state_1 = []
    truck_state_1L = []
    truck_state_2 = []
    truck_state_2L = []
    truck_state_3 = []
    truck_state_3L = []

    # Truck states all have a space - time complexity of O(1)
    truck_state_1L.insert(0, '0')

    def truck_1_state_index():
        return truck_state_1L

    def truck_1_state_list():
        return truck_state_1

    truck_state_2L.insert(0, '0')

    def truck_2_state_index():
        return truck_state_2L

    def truck_2_state_list():
        return truck_state_2

    truck_state_3L.insert(0, '0')

    def truck_3_state_index():
        return truck_state_3L

    def truck_3_state_list():
        return truck_state_3


    # Define Greedy algorithm for shortest path
    # Set an initial value for the distance and check every distance against the initial value
    # Add packages to correct trucks after the routes have been determined, packages need to be added to list
    # Remove package from list with the smallest value
    # Space - time Complexity is O(N^2)
    def calculate_shortest_distance(truck_miles, truck_id, location):
        if len(truck_miles) == 0:  # Initial start of list size
            return truck_miles
        else:
            try:
                initial_val = 100.0
                latest_locate = 0
                for index in truck_miles:
                    if current_distance(location, int(index[1])) <= initial_val:
                        initial_val = current_distance(location, int(index[1]))
                        latest_locate = int(index[1])
                for index in truck_miles:
                    if current_distance(location, int(index[1])) == initial_val:
                        if truck_id == 1:
                            truck_state_1.append(index)
                            truck_state_1L.append(index[1])
                            pop_value = truck_miles.index(index)
                            truck_miles.pop(pop_value)
                            location = latest_locate
                            calculate_shortest_distance(truck_miles, 1, location)
                        elif truck_id == 2:
                            truck_state_2.append(index)
                            truck_state_2L.append(index[1])
                            pop_value = truck_miles.index(index)
                            truck_miles.pop(pop_value)
                            location = latest_locate
                            calculate_shortest_distance(truck_miles, 2, location)
                        elif truck_id == 3:
                            truck_state_3.append(index)
                            truck_state_3L.append(index[1])
                            pop_value = truck_miles.index(index)
                            truck_miles.pop(pop_value)
                            location = latest_locate
                            calculate_shortest_distance(truck_miles, 3, location)
            except IndexError:
                pass