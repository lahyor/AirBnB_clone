0x00. AirBnB clone - The console

Background Context
Welcome to the AirBnB clone project!
Before starting, please read the AirBnB concept page.

First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
create the first abstracted storage engine of the project: File storage.
create all unittests to validate all our classes and storage engine
What’s a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

Create a new object (ex: a new User or a new Place)
Retrieve an object from a file, a database etc…
Do operations on objects (count, compute stats, etc…)
Update attributes of an object
Destroy an object

Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
How to create a Python package
How to create a command interpreter in Python using the cmd module
What is Unit testing and how to implement it in a large project
How to serialize and deserialize a Class
How to write and read a JSON file
How to manage datetime
What is an UUID
What is *args and how to use it
What is **kwargs and how to use it
How to handle named arguments in a function

TASK
Write a class BaseModel that defines all common attributes/methods for other classes:

Create BaseModel from dictionary
mandatory
Previously we created a method to generate a dictionary representation of an instance (method to_dict()).

Now it’s time to re-create an instance with this dictionary representation.

Store first object
mandatory
Now we can recreate a BaseModel from another one by using a dictionary representation:

Console 0.0.1
mandatory
Write a program called console.py that contains the entry point of the command interpreter:

Console 0.1
mandatory
Update your command interpreter (console.py) to have these commands:

Write a class User that inherits from BaseModel:

More classes!
mandatory
Write all those classes that inherit from BaseModel:

Console 1.0
mandatory
Update FileStorage to manage correctly serialization and deserialization of all our new classes: Place, State, City, Amenity and Review
