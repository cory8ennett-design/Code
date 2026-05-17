Step 1
In this workshop, you are going to build a salary tracking system for employees.

Start by creating a class named Employee. Inside it create an __init__ method with self, name, and level parameters. Within the __init__ method, assign name and level to the instance attributes with the same name.

Step 2
Now create an instance of the Employee class passing in the strings Charlie Brown and trainee. Assign the instance to a variable named charlie_brown.

Step 3
In a previous lesson, you learned that an attribute prefixed with a single underscore is meant for internal use by convention.

Modify both name and level attributes into _name and _level, since these are not supposed to be modified from outside their class.

Note that this does not prevent the attribute from being accessed or modified outside the class. Also, in Python there's always a way to access private attributes (prefixed with a double underscore) as well.

Step 4
Add a __str__ method to the Employee class. Make it return an f-string with the format name: level, replacing name and level with the corresponding attributes.

After that, print charlie_brown to the console.

Step 5
The @property decorator is used in Python to turn a method into a property. It is typically used to define getter methods, which are methods used to retrieve the value of an attribute:

Example Code
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

p = Person('Alice')
print(p.name)  # Alice
Create a method named name with a self parameter and decorate it with @property. Inside the method, return self._name.

Step 6
Now that you defined a getter for name, you can access the _name attribute through the name property. So print charlie_brown.name to the console.

Step 7
Following what you did in the previous steps, create a getter for the _level attribute.

Step 8
Now print charlie_brown.level to the console.

Step 9
Now that you have getters for both _name and _level attributes, update the string returned by __str__ to use self.name and self.level. This will call the getters instead of directly accessing the attributes.

Step 10
Now remove the last two print calls.

Step 11
The __repr__ method is a special method that is supposed to return a string representation of the object that can be used to instantiate it.

For example, the __repr__ method of Employee('Charlie', 'developer') should return the string Employee('Charlie', 'developer'), which is the same string used to create the object.

Give your Employee class a __repr__ method with a self parameter, and make it return a string that can be used to instantiate the object.

Step 12
The __repr__ method is called under the hood when you call the repr function. To see it in action, print the result of calling repr(charlie_brown) at the bottom of your code.

Step 13
Remove the last print call from your code.

Step 14
Now it's time to add some validation to the __init__ method. At the beginning of the method, create an if statement that checks if either name or level are not instances of str.

Inside the if statement, raise a TypeError with the message 'name' and 'level' attribute must be of type 'str'.