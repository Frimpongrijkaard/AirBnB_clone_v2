# AirBnB_clone - The Console
This is the first step towards building our first full web application: the AirBnB clone.

## This Interpreter Command Founctionalities
 * Create a new object (ex: a new User or a New place)
 * Retrieve an object from a file, a database etc...
 * Do operations on object (count, compute stats )
 * UPdate attribute of an object
 * Destroy an object
 
 # Environment
 
 This project This interpreted/tested on Ubuntu 14.04 LTS using python3 (version 3.4.3)
 
 # Installation
 
* Clone this repository: git clone
 (https://github.com/Frimpongrijkaard/AirBnB_clone.git)
* Access AirBnb directory: cd AirBnB_clone
* Run hbnb(interactively): ./console and enter command
* Run hbnb(non-interactively): echo "" | ./console.py
 
 # Description
 This is a team work project for an alx software Engineer Program.
 It's te first step toward building a first web application: (Airbnb clone).This
 fiest step consist of a custom command-line interface for the data management and the base
 classes for the storage of this data.
 
 # Console and Command Usage
 
 The console is a Unix shell-like command line user interface provided by the python CmdModule. It prints a prompt and waits for the user for input, for our project we used (hbnb)
 
 

  Command                 __          Example             
Display commands help     __        (hbnb) help        
Create object             __        (hbnb) create       
Destroy object            __        (hbnb) destroy      
Show object               __        (hbnb) show          
Show "all" objects        __        (hbnb) all            
Run console               __        ./console.py          
Quit console               __       (hbnb)quit            


Help command example

(hbnb) help
 # Document commands(type help):
 
 EOF all count create destroy help quit show update
 Class Models Used

File	  --      Description	   --       Attributes
base_model.py  --	The BaseModel class is inherited by other --	id, created_at, updated_at
user.py --	User class stores user-related info	-- email, password, first_name, last_name
city.py  --	City class stores city-specific information --	state_id, name
state.py  -- 	State class stores state-specific information	-- name
place.py	-- Place class stores full detailed outline	
of rental unit features --	city_id, user_id, name, description,number_rooms,
number_rooms, number_bathrooms, max_guest,
price_by_night, latitude, longitude, amenity_ids
review.py	 -- Review class stores previous customer reviews and opinions	-- 	place_id, user_id, text
	
amenity.py	--  Amenity class stores highlighted amenity
information	--  name 
 # Tests
 All the code is tested with the unittest module. The tset for
 the classes are inthetest_models folder.
 
 # Authors
* Frimpong Rijkaard - Frimpong
* Michael Mensah - Michael
