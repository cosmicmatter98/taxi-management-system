# Taxi Management System

## Brief introduction and scope of the program
This is a Python project where an individual can run the program to do any and all of the following:-
1. Book a taxi ride and get a receipt for the ride
2. See existing customers' booking history
3. Add locations before booking
4. Update existing rates
5. Add new taxi rates
6. See all the locations stored in the system

## Uses
### Running the program
run the program from the terminal
```
[path of the interpreter] taxi_management_system.py
```

### Menu
On running the program, it shows a general greeting, shows a menu to the user, and prompts for an option.
```
Welcome to Taxi Management System

#######################################################
You can choose from the following options:
1. Book a trip
2. Add/Update a rate
3. Display existing customers
4. Display existing locations
5. Display existing rates
6. Add new locations
7. Display a customer booking history
0. Exit the program
#######################################################

Choose one option:
```

### Booking a ride
Booking for a ride is done using the first option in the main menu at the prompt for choosing an option.

Following is a general scheme of booking a ride
```
Choose one option: 1
Enter your name: Rahul   
Enter departure location: Dumdum
Enter destination location: Barasat
Enter the distance travelled in km: 11.2
Enter the rate type: standard
Welcome to the the Taxi Service
Taxi           Receipt
-------------  ---------------
Name:          Rahul
Departure:     dumdum
Destination:   barasat
Rate:          23.5 INR per km
Distance:      11.2 km
-------------  ---------------
Basic Fee:     41 INR
Distance Fee:  263 INR
Discount:      0 INR
-------------  ---------------
Total cost:    304 INR
```
The program prompts the user to enter the `departure`, `destination`, `distance travelled` and the `rate type`, and then calculates the fare (in INR) and prints the receipt in the terminal itself, as shown. The program also shows the menu again.

#### rate type
Only four types of rating are hard coded - standard, peak, weekends, holidays

#### discount mechanism
Discount is only applicable for returning customers, and not one-time customers.

For the above customer `Rahul`, this would be the receipt for a subsequent ride. Notice the `discount` statement before the receipt is printed.
```
Choose one option: 1
Enter your name: Rahul
Enter departure location: Dumdum
Enter destination location: Barasat
Enter the distance travelled in km: 11.2
Enter the rate type: standard
A discount of 53 INR has been applied to the taxi fare
Taxi           Receipt
-------------  ---------------
Name:          Rahul
Departure:     dumdum
Destination:   barasat
Rate:          23.5 INR per km
Distance:      11.2 km
-------------  ---------------
Basic Fee:     41 INR
Distance Fee:  263 INR
Discount:      53 INR
-------------  ---------------
Total cost:    251 INR
```

### Add/Update a rate
This is done using the second option from the main menu. A separate menu for updating the rate chart opens and the user is prompted to select an option from the menu.
```
Choose one option: 2
Update rate chart menu.

Select one option:
1. Update existing rate.
2. Enter new rate.
3. Exit rate chart menu.

Choose an option:
```

#### Updating existing rate
General scheme for updating an existing rate. This is done with option `1`.
```
Choose an option: 1
Enter the rate type you want to update. standard
Enter updated rate. 25.0
```
For the purpose of illustration I have updated `standard` to a value of `25.0`. The program then exits the rate menu and prompts the main menu.

#### Adding a new rate
General scheme for adding a new rate. This is done with option `2`.
```
Choose an option: 2
Enter new rate type. deluxe
Enter the new rate. 40.00
```
For the purpose of illustration I have added a new rate `deluxe` with a value of `40.00`. The program then exits the rate menu and prompts the main menu.

### Display existing rates
Using the fifth option in the main menu, the user can see the existing four rates. Or after updating existing rates/adding new ones, this menu option can be used to check the rate types and their values.
```
Choose one option: 5
standard = 25.0
peak = 28.2
weekends = 31.26
holiday = 39.25
deluxe = 40.0
```
For the purpose of illustration I have, using the menu options, updated the `standard` rate type and added a `deluxe` rate type. This list is followed by the main menu, as usual.

### Display existing customers
Existing customers can be listed using the third option from the main menu.
```
Choose one option: 3
Customers availing the Taxi Management Service.
Rahul
Anuska
Rohan
```
The names are listed in separate lines as shown. For the purpose of illustration I have hardcoded some names. Names are only stored after a ride is booked and receipt generated. The program then shows the main menu.

### Display existing locations
Existing locations can be listed using the fourth option from the main menu.
```
Choose one option: 4
Locations that the cab has went to already.
```
After this it lists all the locations where the rides previously has been booked, followed by the main menu.

### Add new locations
New locations can be added to the Taxi Management System, without booking a ride. This is done using the sixth option in the main menu. Following is the scheme.
```
Choose one option: 6
Enter a location to add: Dumdum
```
I have added the location `Dumdum` here. The location gets added to the existing locations list. This can be verified using the fourth menu option.
```
Choose one option: 4
Locations that the cab has went to already.
Dumdum
```
As usual, after this activity, the main menu is prompted.

### Customer Booking History
Booking history of a particular customer can be seen using the seventh option in the main menu.
```
Choose one option: 7
Enter the name of the customer: Rahul
This is the booking history of Rahul
-----------------------------
Booking 1
Departure:  abc
Destination:  xyz
Fare:  104 INR
###########################
Booking 2
Departure:  lmn
Destination:  olk
Fare:  123 INR
###########################
```
Two bookings are shown for the sample customer `Rahul`. After this the main menu gets prompted, as usual.

### Exiting the program
To exit the program select the last option, which is option `0`.

## Error handling
Some examples of error handling

### in the main menu
On choosing a non-existent option
```
Choose one option: 8
Enter option from the available list of options.
Choose one option:
```

### in the rate menu
On choosing a non existent rate type to update
```
Choose an option: 1
Enter the rate type you want to update. deluxe
Enter one of the already existing rates
```

## Author
- Name - Suvradri Maitra
- GitHub profile - [cosmicmatter98](https://www.github.com/cosmicmatter98)
- LinkedIn profile - [Suvradri Maitra](https://www.linkedin.com/in/suvradri-maitra)
- You can mail me [here](mailto:suvradri98@outlook.com)
