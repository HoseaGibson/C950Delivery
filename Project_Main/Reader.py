###########################IMPORTS###############################
import csv
from Project_Main.Hashing_Table import Hash_Map

###########################FILES READER###############################
with open('Distance_Packages_Data.csv') as csvfile:
    read_CSV = csv.reader(csvfile, delimiter=',')

###########################VARIABLES###############################

    # Create a new object of hash map
    hash_table_insert = Hash_Map()
    # Create variable to hold a list for each truck deliveries
    truck_1 = []
    truck_2 = []
    trips_1_2 = []

###########################CSV FILE FOR HASHTABLE###############################

    # Loop through csv files and add them to each variable dictionary
    # Space-time complexity is O(N)
    for row in read_CSV:
        package_ID = row[0]
        address = row[1]
        city = row[2]
        state = row[3]
        zip = row[4]
        delivery = row[5]
        size = row[6]
        note = row[7]
        delivery_start = ''
        address_location = ''
        delivery_status = 'At Hub'
        iterate_value = [package_ID, address_location, address, city, state,
                         zip, delivery, size, note, delivery_start,
                         delivery_status]

###########################STATUS FOR DELIVERY AND NOTES###############################
        key = package_ID
        value = iterate_value

        # Check status from each truck
        # Add the packages of to list for trucks
        # We can use this data structure to look up and sorting the packages and
        # give status for each
        if value[6] != 'EOD':
            if 'Must' in value[8] or 'None' in value[8]:
                truck_1.append(value)
        if 'Can only be' in value[8]:
            truck_2.append(value)
        if 'Delayed' in value[8]:
            truck_2.append(value)
        # Moves wrong address info to the new corrected address
        if '84104' in value[5] and '10:30' not in value[6]:
            trips_1_2.append(value)
        if 'Wrong address listed' in value[8]:
            value[2] = '410 S State St'
            value[5] = '84111'
            trips_1_2.append(value)
        if value not in truck_1 and value not in truck_2 and value not in trips_1_2:
            if len(truck_2) > len(trips_1_2):
                trips_1_2.append(value)
            else:
                truck_2.append(value)
        # Insert values to hash table from the csv files
        hash_table_insert.insert(key, value)

###########################DEFINE FUNCTIONS###############################

    # Define function to return the list of values
    # Space-time complexity is O(1)
    def get_hash_map():
        return hash_table_insert

    # Define a function for truck 1 package load
    # Space-time complexity is O(1)
    def check_truck_1_trip():
        return truck_1

    # Define a function for truck 2 package load
    # Space-time complexity is O(1)
    def check_truck_2_trip():
        return truck_2

    # Define a function for truck 1 package load for 2nd trip
    # Space-time complexity is O(1
    def check_truck_1_trip_2():
        return trips_1_2

