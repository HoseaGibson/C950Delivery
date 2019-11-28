# WGUPS Package Delivery C950
# Hosea Gibson Student ID = 000749816
# Delivery Application that shows the total miles of the shortest path,
# also allows the user to lookup individual packages by id or by time

#########################IMPORTS####################################
import json

from Project_Main.Package_Main import total_distance
import datetime
from Project_Main.Reader import get_hash_map

#########################MAIN####################################

# Create user interface
# Show user the total miles
# Add the ability for user to have a lookup feature
# Allow look up through id or by time frames
# Display information to user
class Main:
    global convert_time_1, time_1, convert_time_2, time_2
    print('Solution is executed!')
    print('WGUPS Tracking System!')
    print('Shortest path route was completed in', "{0:.2f}".format(total_distance(), 2), 'miles.') # Format shortest path
    # Allow user input to search packages and to exit program
    start = input("Please type 'lookup' to search for an individual package or "
                  "\ntype 'timestamp' to view delivery status at a give time: "
                  "\n or type 'all' to show all packages: "
                  "\n or type 'exit' to exit program!")
    # Shows all packages
    if start == 'all':
        # Open packageTables.json and read the file
        with open("packageTables.json", 'r') as f:
            var = json.load(f)
        # Used a json file because I could retrieve certain data from the file to
        # get all information needed for program and print out in console
        # Print status which is in route
        allPackages = [(p['id'], p['address'], p['city'], p['state'], p['zip'], p['deadline'], p['kg'], 'IN_ROUTE')
                       for p in
                       var]
        [print(p) for p in allPackages]
    # Space-time complexity is O(N)
    while start is not 'exit':

        # If start for timestamp display all packages during the timeframe
        # Runtime of this process is O(N)
        if start == 'timestamp':
            try:
                package_time = input('Please enter a time in the HH:MM:SS format: ')
                (h, m, s) = package_time.split(':')
                convert_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                # Space-time complexity is O(N^2)
                for count in range(1,41):
                    try:
                        time_1 = get_hash_map().get(str(count))[9]
                        time_2 = get_hash_map().get(str(count))[10]
                        (h, m, s) = time_1.split(':')
                        convert_time_1 = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                        (h, m, s) = time_2.split(':')
                        convert_time_2 = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                    except ValueError:
                        pass
                    # Check all times
                    # Check if they are at the hub
                    # Display results
                    if convert_time_1 >= convert_time:
                        get_hash_map().get(str(count))[10] = 'At Hub'
                        get_hash_map().get(str(count))[9] = 'Leaves at ' + time_1
                        print('Package ID:', get_hash_map().get(str(count))[0], '   Street address:',
                              get_hash_map().get(str(count))[2], get_hash_map().get(str(count))[3],
                              get_hash_map().get(str(count))[4], get_hash_map().get(str(count))[5],
                              '  Required delivery time:', get_hash_map().get(str(count))[6],
                              ' Package weight:', get_hash_map().get(str(count))[7], '  Truck status:',
                              get_hash_map().get(str(count))[9], '  Delivery status:',
                              get_hash_map().get(str(count))[10])
                    elif convert_time_1 <= convert_time:
                        # Then checks to see which packages have left the hub but have not been delivered yet
                        if convert_time < convert_time_2:
                            get_hash_map().get(str(count))[10] = 'In transit'
                            get_hash_map().get(str(count))[9] = 'Left at ' + time_1
                            print('Package ID:', get_hash_map().get(str(count))[0], '   Street address:',
                                  get_hash_map().get(str(count))[2], get_hash_map().get(str(count))[3],
                                  get_hash_map().get(str(count))[4], get_hash_map().get(str(count))[5],
                                  '  Required delivery time:', get_hash_map().get(str(count))[6],
                                  ' Package weight:', get_hash_map().get(str(count))[7], '  Truck status:',
                                  get_hash_map().get(str(count))[9], '  Delivery status:',
                                  get_hash_map().get(str(count))[10])
                        # Check if the packages have been delivered
                        # Display times of packages and status
                        else:
                            get_hash_map().get(str(count))[10] = 'Delivered at ' + time_2
                            get_hash_map().get(str(count))[9] = 'Left at ' + time_1
                            print('Package ID:', get_hash_map().get(str(count))[0], '   Street address:',
                                  get_hash_map().get(str(count))[2], get_hash_map().get(str(count))[3],
                                  get_hash_map().get(str(count))[4], get_hash_map().get(str(count))[5],
                                  '  Required delivery time:', get_hash_map().get(str(count))[6],
                                  ' Package weight:', get_hash_map().get(str(count))[7],'  Truck status:',
                                  get_hash_map().get(str(count))[9],'  Delivery status:',
                                  get_hash_map().get(str(count))[10])
            except IndexError:
                print(IndexError)
                exit()
            except ValueError:
                print('Invalid entry!')
                exit()
        # Check if "Lookup"
        # Check the id user entered
        # Check the time user has entered
        # Display user results to information entered
        elif start == 'lookup':
            try:
                count = input('Please enter a package ID to lookup: ')
                time_1 = get_hash_map().get(str(count))[9]
                time_2 = get_hash_map().get(str(count))[10]
                package_time = input('Please enter a time in the HH:MM:SS format: ')
                (h, m, s) = package_time.split(':')
                convert_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                (h, m, s) = time_1.split(':')
                convert_time_1 = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                (h, m, s) = time_2.split(':')
                convert_time_2 = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                # Check if package left the hub
                # Check if package has left the hub but still waiting delivery
                # Check if package has been delivered if has then display information
                if convert_time_1 >= convert_time:
                    get_hash_map().get(str(count))[10] = 'At Hub'
                    get_hash_map().get(str(count))[9] = 'Leaves at ' + time_1
                    print('Package ID:', get_hash_map().get(str(count))[0], '   Street address:',
                          get_hash_map().get(str(count))[2], get_hash_map().get(str(count))[3],
                          get_hash_map().get(str(count))[4], get_hash_map().get(str(count))[5],
                          '  Required delivery time:', get_hash_map().get(str(count))[6],
                          ' Package weight:', get_hash_map().get(str(count))[7], '  Truck status:',
                          get_hash_map().get(str(count))[9], '  Delivery status:',
                          get_hash_map().get(str(count))[10])
                elif convert_time_1 <= convert_time:
                    if convert_time < convert_time_2:
                        get_hash_map().get(str(count))[10] = 'In transit'
                        get_hash_map().get(str(count))[9] = 'Left at ' + time_1
                        print('Package ID:', get_hash_map().get(str(count))[0], '   Street address:',
                              get_hash_map().get(str(count))[2], get_hash_map().get(str(count))[3],
                              get_hash_map().get(str(count))[4], get_hash_map().get(str(count))[5],
                              '  Required delivery time:', get_hash_map().get(str(count))[6],
                              ' Package weight:', get_hash_map().get(str(count))[7], '  Truck status:',
                              get_hash_map().get(str(count))[9], '  Delivery status:',
                              get_hash_map().get(str(count))[10])
                    else:
                        get_hash_map().get(str(count))[10] = 'Delivered at ' + time_2
                        get_hash_map().get(str(count))[9] = 'Left at ' + time_1
                        print('Package ID:', get_hash_map().get(str(count))[0], '   Street address:',
                              get_hash_map().get(str(count))[2], get_hash_map().get(str(count))[3],
                              get_hash_map().get(str(count))[4], get_hash_map().get(str(count))[5],
                              '  Required delivery time:', get_hash_map().get(str(count))[6],
                              ' Package weight:', get_hash_map().get(str(count))[7], '  Truck status:',
                              get_hash_map().get(str(count))[9], '  Delivery status:',
                              get_hash_map().get(str(count))[10])
            except ValueError:
                print('Invalid entry')
                exit()
        elif start == 'exit':
            exit()
        else:
            print('Invalid entry!')
            exit()

