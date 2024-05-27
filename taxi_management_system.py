from tabulate import tabulate, SEPARATING_LINE                                                          # importing tabulate module

rate_chart = {'standard' : 23.5, 'peak' : 28.2, 'weekends' : 31.26, 'holiday' : 39.25}                  # rate chart
customers = []                                                                                          # list of customers
locations = []                                                                                          # locations list

customer_history = {}                                                                                   # customer booking history dictionary

def main():
    global rate_chart, customers, locations, customer_history                                           # declaring the constants as globals for further manipulation
    
    while True:                                                                                         # run the entire code indefinitely on the system until exited through dedicated menu options
        menu = f_menu()                                                                                 # showing the menu and getting the preference
        if menu == 1:                                                                                   # booking a trip
            while True:                                                                                 # reprompting loop
                customer_name = input("Enter your name: ").strip().title()                              # asking for customer's name
                try:                                                                                    # exception bloc to check for alphabets only in customer name
                    if customer_name.isalpha() is False:
                        raise ValueError                                                                # raising error if criteria not satisfied
                except ValueError:                                                                      # handling the error
                    print("Enter only your name.")
                else:                                                                                   # breaking the validation loop if alright
                    break

            while True:                                                                                 # reprompting loop
                departure = input("Enter departure location: ").strip().lower()                         # asking for departure location
                if departure not in locations: locations.append(departure)                              # adding the location to locations list

                destination = input("Enter destination location: ").strip().lower()                     # asking for destination location
                if destination not in locations: locations.append(destination)                          # adding the location to locations list
                try:                                                                                    # exception bloc to validate the condition for location
                    if destination == departure:
                        raise ValueError                                                                # raise error in case they are same
                except ValueError:                                                                      # handling the error
                    print("Destination location should be different than Departure location.")
                else:                                                                                   # breaking the validation loop if alright
                    break

            while True:                                                                                 # reprompting loop
                try:                                                                                    # exception bloc to validate the condition for distance
                    distance = float(input("Enter the distance travelled in km: "))                     # asking the distance between departure and destination locations
                    if distance <= 0:
                        raise ValueError
                except ValueError:                                                                      # handling error if conditions not met, or if conversion to float is not possible
                    print("Enter a valid distance.")
                else:                                                                                   # break out the validation loop if alright
                    break
                
            rate = f_rate(menu)                                                                         # getting the rate

            basic_fee = 41                                                                              # static base fee
            distance_fee = round(distance * rate)                                                       # calculating the distance fee

            if customer_name in customers:                                                              # validating the criteria for discount
                discount = round(distance_fee * 0.20)                                                   # calculating the discount
                print("A discount of", discount, "INR has been applied to the taxi fare")               # declaration of discount amount
            else:
                customers.append(customer_name)                                                         # adding the customer to the customers list, if new
                print("Welcome to the Suvradri's Taxi Service")                                         # welcome message for new customers
                discount = 0                                                                            # zero discount for new customers

            total_cost = round(basic_fee + distance_fee - discount)                                     # calculating total cost for the customer

            receipt(customer_name, departure, destination, rate, distance, basic_fee, distance_fee, discount, total_cost) # generating receipt

            if customer_name in customer_history:                                                       # saving customer booking history for old customers
                customer_history[customer_name].append([departure, destination, total_cost])
            else:
                customer_history[customer_name] = []                                                    # initialising new list for a new customer
                customer_history[customer_name].append([departure, destination, total_cost])            # saving the booking history as a list
       
        elif menu == 2:                                                                                 # adding/updating rate
            f_rate(menu)

        elif menu == 3:                                                                                 # display existing customers
            print("Customers availing the Taxi Management Service.")
            for i in customers:
                print(i)

        elif menu == 4:                                                                                 # display existing locations
            for i in locations:
                print(i)

        elif menu == 5:                                                                                 # display existing rates
            for i in rate_chart:
                print(i, "=", rate_chart[i])

        elif menu == 6:                                                                                 # add new locations
            location = input("Enter a location to add: ")                                               # asking for location to add
            locations.append(location)                                                                  # adding location to locations list


        elif menu == 7:                                                                                 # display a customer booking history
            n = 0
            customer_name = input("Enter the name of the customer: ")                                   # asking for the customer to look up
            print("This is the booking history of", customer_name)
            print("-----------------------------")
            while n < len(customer_history[customer_name]):                                             # looping through the customers booking history dictionary
                key = customer_history[customer_name]
                booking = key[n]
                Departure = booking[0]
                Destination = booking[1]
                Fare = booking[2]
                print(f"Booking {n+1}")
                print("Departure: ", Departure)
                print("Destination: ", Destination)
                print("Fare: ", Fare, "INR")
                print("###########################")
                n = n + 1   

        elif menu == 0:                                                                                 # exits the program
            break


def f_rate(menu):                                                                                       # function to deal with all things related to rate
    global rate_chart                                                                                   # declaring rate chart as global for manipulation

    if menu == 1:                                                                                       # decision route when func is called to get rate
        while True:                                                                                     # reprompting loop
            rate_type = input("Enter the rate type: ")                                                  # ask for rate type
            try:                                                                                        # except bloc to validate if entered type in chart or not
                if rate_type not in rate_chart:                                                         # validating if rate type in rate chart or not
                    raise ValueError                                                                    # raising error if criteria invalid
            except ValueError:                                                                          # handling the error
                print("Enter a valid rate type.")
            else:
                return rate_chart[rate_type]                                                            # return rate and break out the loop
    
    elif menu == 2:                                                                                     # decision route when func is called for addition/updation
        print("Update rate chart menu.")
        print()
        print("Select one option: ")
        print("1. Update existing rate.")
        print("2. Enter new rate.")
        print("3. Exit rate chart menu.")
        print()
        while True:                                                                                     # reprompting loop
            try:                                                                                        # except bloc to restrict options to only one of the three
                option = int(input("Choose an option: "))                                               # ask for option
                if option == 1:                                                                         # decision route for updation of existing rate
                    rate_input = input("Enter the rate type you want to update. ").strip().lower()      # ask for the rate type to update
                    if rate_input in list(rate_chart):                                                  # checking if rate type in rate chart
                        while True:                                                                     # reprompting loop
                            try:                                                                        # exception bloc to validate entered rate is float
                                updated_rate = float(input("Enter updated rate. "))                     # ask for updated value
                            except ValueError:                                                          # handling error if non-floatable input is given
                                print("Enter only the updated rate.")
                            else:                                                                       # update rate type with the new value and break
                                rate_chart[rate_input] = updated_rate
                                break
                    else:                                                                               # if rate type not in rate chart raise an error
                        raise ValueError
                elif option == 2:                                                                       # decision route for addition to rate
                    new_type = input("Enter new rate type. ")                                           # asking for new rate type
                    while True:                                                                         # reprompting loop
                        try:                                                                            # exception bloc to validate entered rate is float
                            new_rate = float(input("Enter the new rate. ")).strip().lower()             # ask for value of new rate type
                        except ValueError:                                                              # handling error if non-floatable input is given
                            print("Enter a valid rate only. ")
                        else:                                                                           # update rate chart with new type and value and break
                            rate_chart[new_type] = new_rate
                            break
                elif option == 3:                                                                       # decision route for exiting rate menu by break
                    break
                else:                                                                                   # raise error when any other thing is entered in option prompt
                    raise ValueError
            except ValueError:                                                                          # handling error at options prompt at rate menu
                print("Enter one of the three options only. ")
            else:                                                                                       # breaking the loop when all things are done
                break


def receipt(name, dep, dest, r, d, b, distfee, dis, total):                                             # function to print receipt

    r = str(r) + " INR per km"
    d = str(d) + " km"
    b = str(b) + " INR"
    distfee = str(distfee) + " INR"
    dis = str(dis) + " INR"
    total = str(total) + " INR"

    table = [["Name:", name],
             ["Departure:", dep],
             ["Destination:", dest],
             ["Rate:", r],
             ["Distance:", d],
             SEPARATING_LINE,
             ["Basic Fee:", b],
             ["Distance Fee:", distfee],
             ["Discount:", dis],
             SEPARATING_LINE,
             ["Total cost:", total]]                                                                    # creating a table for the receipt

    headers = ["Taxi", "Receipt"]                                                                       # creating headers for the table

    print(tabulate(table, headers, tablefmt = "simple", stralign = "left", numalign = "right"))         # printing the receipt


def f_menu():                                                                                           # function to display menu when code runs
    print("Welcome to Suvradri's Taxi Management System")
    print()
    print("#######################################################")
    print("You can choose from the following options:")
    print("1. Book a trip")
    print("2. Add/Update a rate")
    print("3. Display existing customers")
    print("4. Display existing locations")
    print("5. Display existing rates")
    print("6. Add new locations")
    print("7. Display a customer booking history")
    print("0. Exit the program")
    print("#######################################################")
    print()
    
    while True:                                                                                         # reprompting loop
        try:                                                                                            # exception bloc to validate option is valid
            option = int(input("Choose one option: "))                                                  # asking for an option
            if option not in [1,2,3,4,5,6,7,0]:                                                         # validating criteria
                raise ValueError                                                                        # raising error if invalid option
        except ValueError:                                                                              # handling error
            print("Enter option from the available list of options.")
        else:                                                                                           # breaking out of loop if everything alright
            break
    
    return option                                                                                       # returning the option


if __name__ == "__main__":
    main()                                                                                              # run the entire code in main function only when this file is run