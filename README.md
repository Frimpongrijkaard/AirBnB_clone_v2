#HBNB STORAGE AND CONSOLE

This repository about Airbnb clone website with the update version of the Hbnb storage and console. This stage implements a backend interface or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.

##The task Content

|      Task         |          Files          |     Descriptions        |
|                   |                         |                         |
|-------------------|-------------------------|-------------------------|
|Author/README      |                         |                         |
| File              |       AUTHORS           |     Project authors     |
|                   |                         |                         |
|                   |                         |                         |
|-------------------|-------------------------|-------------------------|
|                   |                         |                         |
|  Unit Testing     |      /test              |   All class-defining    |
|                   |                         |   module are unittested |
|                   |                         |                         |
|-------------------|-------------------------|-------------------------|
|                   |                         |                         |
|  Make             |                         | Define a parent class   |
|  BaseModel        |   /models/base_mode.py  | to be inherited by all  |
|                   |                         |    model class          |  
|                   |                         |                         |
|-------------------|-------------------------|-------------------------|
|                   |                         |                         |
|                   |                         |   Add functionality to  |
| Update            |                         |  recreate an instance of|
| BaseModel/        |   /models/base_model.py |  a class from a         |
| Kwargs            |                         |   dictionary            |
|                   |                         |   representation        |
|                   |                         |                         |
|-------------------|-------------------------|-------------------------|
|                   |                         |                         |
|                   |  /models/engine/        |   define a class to     |
|                   |  file_storage.py        |   manage persistent     |
| Create            |  /models/_init_.py      |   file storage          |
| Filestorage       |  /models/base_mode.py   |   system                |   
| class             |                         |                         |
|-------------------|-------------------------|-------------------------|
|                   |                         |                         |
|                   |                         |   Add basic functionlity|
| console 0.0.1     |      console.py         |   to console program    |
|                   |                         |   allowing it to quit,  |
|                   |                         |   handle empty lines    |
|                   |                         |   and ^D                | 
|-------------------|-------------------------|-------------------------|
|                   |                         |                         |
|                   |                         |    Update the console   |
|                   |                         |    with methods allowing| 
| Console 0.1       |       console.py        |    the user to create   |
|                   |                         |    destory, show, and   |
|                   |                         |    update stored data   |
|-------------------|-------------------------|-------------------------|
|                   |                         |                         |
|                   |   console.py            |    Implements a user    |
| Create User       |   /models/engine        |    class dynamically    |
| class             |   /file_storage.py      |                         |
|                   |   /models/user.py       |                         |
|                   |                         |                         |
|-------------------|-------------------------|-------------------------|
|                   |                         |                         |
|                   |  /models/user.py        |                         |
| More Classes      |  /models/place.py       |      Implement more     |
|                   |  /models/city.py        |      classes dynamically|  
|                   |  /models/amenity.py     |                         |
|                   |  /models/state.py       |                         |
|                   |  /models/review.py      |                         |
|                   |                         |                         |
|-------------------|-------------------------|-------------------------|
|                   |                         |                         |
|                   |                         |    update the console   |
|                   |   console.py            |    and file storage     |
| Console 1.0       |   /models/engine/       |    system to work       |
|                   |   file_storage.py       |   dynamically           |
|                   |                         |    with all classes     |
|                   |                         |    update file storage  |
|                   |                         |                         |
|-------------------|-------------------------|-------------------------|

#General Use

1.First clone this repository.
2.Once the repository is cloned locate the "console.py" file and run it as follows:
 
 /AirBnB_clone$ ./console.py

3.When this command is run the following prompt should appear:
 
 (hbnb)

4.This prompt designates you are in the "HBnB" console. There are a variety of commands available within the console program.

###Commands

* create - Creates an instance based on given class

* destroy - Destroys an object based on class and UUID

* show - Shows an object based on class and UUID

* all - Shows all objects the program has access to, or all objects of a given class

* update - Updates existing attributes an object based on class name and UUID

* quit - Exits the program (EOF will as well)

###Alternative Syntax
Users are able to issue a number of console command using an alternative syntax:

Usage: <class_name>.<command>([<id>[name_arg value_arg]|[kwargs]])
Advanced syntax is implemented for the following commands:

* all - Shows all objects the program has access to, or all objects of a given class

* count - Return number of object instances by class

* show - Shows an object based on class and UUID

* destroy - Destroys an object based on class and UUID

* update - Updates existing attributes an object based on class name and UUID


###Examples
Primary Command Syntax
Example 0: Create an object
Usage: create <class_name>

(hbnb) create BaseModel
(hbnb) create BaseModel
3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb)
###Example 1: Show an object
Usage: show <class_name> <_id>

(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
[BaseModel] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96959),
'updated_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96971)}
(hbnb)
###Example 2: Destroy an object
Usage: destroy <class_name> <_id>

(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
** no instance found **
(hbnb)
###Example 3: Update an object
Usage: update <class_name> <_id>

(hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"
(hbnb) show BaseModel b405fc64-9724-498f-b405-e4071c3d857f
[BaseModel] (b405fc64-9724-498f-b405-e4071c3d857f) {'id': 'b405fc64-9724-498f-b405-e4071c3d857f', 'created_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729889),
'updated_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729907), 'first_name': 'person'}
(hbnb)
Alternative Syntax
###Example 0: Show all User objects
Usage: <class_name>.all()

(hbnb) User.all()
["[User] (99f45908-1d17-46d1-9dd2-b7571128115b) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92071), 'id': '99f45908-1d17-46d1-9dd2-b7571128115b', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92056)}", "[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
###Example 1: Destroy a User
Usage: <class_name>.destroy(<_id>)

(hbnb) User.destroy("99f45908-1d17-46d1-9dd2-b7571128115b")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
###Example 2: Update User (by attribute)
Usage: <class_name>.update(<_id>, <attribute_name>, <attribute_value>)

(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", name "Todd the Toad")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'name': 'Todd the Toad', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
###Example 3: Update User (by dictionary)
Usage: <class_name>.update(<_id>, )

(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", {'name': 'Fred the Frog', 'age': 9})
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'name': 'Fred the Frog', 'age': 9, 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]

