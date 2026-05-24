Build a Salary Tracker

Technologies
Uses Python3.

Deployment
Copy main.py into the text editor of your choice. If using terminal, use the command python3 main.py to run the code.

Credits
Acknowledgements
FreeCodeCamp
-------------------------------------------------------------------------------------------------------------

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

Step 15
Create a class attribute named _base_salaries and assign it the following dictionary:

Example Code
{
    'trainee': 1000,
    'junior': 2000,
    'mid-level': 3000,
    'senior': 4000
}

Step 16
The level used to instantiate an employee should be chosen among specific levels. You'll use _base_salaries to validate the level and set the right salary for the employee.

After your existing if statement, create another if that checks if level is not in Employee._base_salaries.

Inside the new if statement, raise a ValueError with the message Invalid value '{level}' for 'level' attribute., where {level} should be replaced by the value of the level argument.

Step 17
Finally, at the bottom of the __init__ method, set the _salary attribute to the value corresponding to level inside the _base_salaries dictionary.

Step 18
Now that you have a new attribute, you're going to create a getter for it.

Create a method named salary with a self parameter and use the @property decorator on it. Inside the method, return self._salary.

Step 19
At the bottom of your code, use an f-string to print Base salary: $ followed by the amount of charlie_brown's salary.

Step 20
A setter is a method used to set the value of an attribute, allowing for validation checks and restrictions. You can create a setter using the @propertyName.setter decorator, where propertyName should match the name of the property to set:

Example Code
class Person:
    def __init__(self, name):
        self.name = name  # Calling the setter

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

p = Person('Alice')
p.name = 'Abigail' # Calls the setter
print(p.name) # Abigail
After your getter method, create a name method with parameters self and new_name. Decorate the method with @name.setter. Inside the method, set self._name to new_name.

Step 21
Now that the name setter is created, update __init__ to use self.name = name instead of self._name = name. This delegates name assignment through the setter, and validation will be added to it in the next step.

Also, adjust the if condition to only check level, and update the TypeError message accordingly:

Step 22
As you learned in a previous lesson, a setter offers a way to control how an attribute can be modified. To ensure that new_name is the right type, create an if statement that raises a TypeError with the message 'name' must be a string. when new_name is not an instance of str.

Step 23
Right after setting the _name attribute to new_name, print 'name' updated to 'new_name'., where new_name should be replaced by the new value of _name.

Step 24
Now you have a setter method for the _name attribute that exposes the name property.

So try to update charlie_brown's name to a different name as you would normally do with any attribute. This will call the setter method under the hood.

Step 25
Feel free to set the name property to something that is not a string to see the validation process in action. After that, restore charlie_brown's name by removing any line of code that changes its name.

Step 26
Now you'll create a setter for the _level attribute. Create a method named level with parameters self and new_level. Decorate the method with @level.setter.

Inside the method, set self._level to new_level.

Step 27
Now that the level setter is created, update __init__ to use self.level = level instead of self._level = level. This delegates level assignment through the setter, and validation will be added to it in the next step.

Also, remove the if not isinstance(level, str) check from __init__ since the setter will handle that validation in the next step.


Step 28
To ensure that new_level is the right type, create an if statement that raises a TypeError with the message 'level' must be a string. when new_level is not an instance of str.


Step 29
Now that the level setter handles the validation for invalid levels, remove the if level not in Employee._base_salaries check from __init__. This will be handled by the setter in the next step.

Step 30
The new level cannot be set without checking if it's a valid level. After the isinstance check, create an if statement that raises a ValueError when new_level is not a key of Employee._base_salaries.

For the error message, use Invalid value '{new_level}' for 'level' attribute., where {new_level} should be replaced by the argument passed to the setter.

Step 31
After the existing if statements, create another one to raise a ValueError when new_level is already the selected level.

Note that _level doesn't exist yet during initialization, so use hasattr(self, '_level') to check if it exists before comparing. This avoids an AttributeError when the object is first created.

For the message, use '{level}' is already the selected level., where {level} should be replaced by the current level.

Step 32
Finally, create a fourth if statement that raises a ValueError with the message Cannot change to lower level. when the base salary of the new level is less than the base salary of the current level.

Use hasattr(self, '_level') to avoid an AttributeError during initialization.

Step 33
When the level is modified, you need to update the salary as well.

Before setting self._level, set self._salary to the base salary for the new level.

Step 34
Complete the setter by printing '{name}' promoted to '{new_level}'. inside your method. Replace {name} and {new_level} with the employee's name and new level, respectively.

Step 35
It's time to test your new setter. Try to assign invalid values such as a random string or the current level (trainee) to charlie_brown.level and see the error messages in the console.

Once you've done, remove the lines raising errors and set charlie_brown.level to the string junior.

Step 36
Now you'll focus on coding a salary setter. After the salary getter, create a simple setter for the salary property that sets self._salary to the value passed to the method as its argument. After that, print Salary updated to $ followed by the new salary and a period.

You'll take care of validating the new salary in the next few steps.

Step 37
Now that the salary setter is created, update __init__ to call it instead of assigning directly to self._salary. Change self._salary = Employee._base_salaries[level] to self.salary = Employee._base_salaries[level].

Step 38
At the beginning of your setter, create an if statement that raises a TypeError with the message 'salary' must be a number. when new_salary is not either an integer or a float.

Step 39
After your existing if statement, create another one for when the new salary is less than the base salary for the current level. Use hasattr(self, '_level') to avoid an AttributeError during initialization.

Inside the if statement, raise a ValueError with the message Salary must be higher than minimum salary $ followed by the base salary for the current level and a period.

Step 40
Finally, now that you have completed the salary setter, you can call it within the level setter.

Modify the line self._salary = Employee._base_salaries[new_level] so that it calls the salary setter instead of modifying directly the _salary attribute.

With that the salary tracker workshop is complete.