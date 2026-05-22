Step 1
In this workshop, you are going to create a media catalogue. Start by defining a class named Movie.

Give your class an __init__ method with the following parameters: self, title, year, director, and duration. Inside the __init__ method, assign title, year, director, and duration parameters to instance attributes with the same name.

Step 2
You want a readable display for debugging and printing. Create a __str__ method that returns a string with the format title (year) - duration min, director (where title, year, duration, and director should be replaced with the values of the corresponding attributes) so that printing a movie gives a nice summary.

Step 3
Now, create an instance of Movie passing in arguments of your choice and assign it to a variable named movie1. Then, print movie1 to the console.

Step 4
In the previous steps, you created a basic movie object. Now, you'll add some validation to make sure that movies cannot be instantiated with invalid attributes.

At the beginning of the __init__ method, create an if statement that checks if the title is either empty or contains whitespace only (you can use the strip method to build the condition).

If so, raise a ValueError with the message Title cannot be empty.

Step 5
The first movie was made in 1895. Create another if statement that checks if year is less than 1895 and raise a ValueError with the message Year must be 1895 or later.

Step 6
Create another if statement to check if director is either empty or contains whitespace only and raise a ValueError with the message Director cannot be empty.

Step 7
Finally, create one last if statement to verify if duration is not greater than 0 and raise a ValueError with the message Duration must be positive.

Step 8
Now delete your print(movie1) line. Then, put your movie1 assignment in a try block and create an except clause that catches ValueError as e and uses an f-string to print Validation Error: followed by a space and the error message.

Feel free to change the arguments passed to instantiate movie1 to see the different error messages.

Step 9
Now create a new class named MediaCatalogue, and give it an __init__ method that sets an items attribute to an empty list. This will represent the list of items in the catalogue.

Step 10
The MediaCatalogue class needs a method to add media items to the catalogue. Create an add method that accepts an item media_item and appends it to the items list.

Step 11
You'll need a proper way to visually represent the catalogue. So create a __str__ method in your MediaCatalogue class.

If the items list is empty, make sure the __str__ method returns Media Catalogue (empty).

Step 12
After the if statement, create a variable named result. This will be the string to return from the method.

So assign it an f-string with the format Media Catalogue (N items):. Replace N with the number of items in the items list and make the string end with two newline characters.

Step 13
Right after declaring the result variable, create a for loop that uses enumeration to iterate over the items in the catalogue and appends to result a string with the following format: N. movie where N is a numeric index starting from 1 and movie is the string representation of the item.

Make the string end with a newline character and return result after the loop.

Step 14
Before the try block, create an instance of MediaCatalogue and assign it to a variable named catalogue.

Then, use the add method to append movie1 to the catalogue. Finally print catalogue to the console.

Step 15
Create another variable named movie2 and assign it a Movie object instantiated with arguments of your choice. Then append movie2 to the catalogue.

Step 16
What if you want to represent a different type of media item, such as a TV series? You could create another class and make it inherit from Movie to have access to all of its methods and attributes.

Create an empty class named TVSeries and make it inherit from Movie. Here's how to make a Child class inherit from a Parent class.

class Parent:
    ...

class Child(Parent):
    ...

Step 17
A TVSeries object will be instantiated with additional attributes with respect to its parent Movie. Therefore, create an __init__ method with the following parameters: self, title, year, director, duration, seasons, and total_episodes.

Inside the __init__ method, assign seasons and total_episodes to attributes with the same name.

Step 18
The super function is used to refer to the parent class without naming it explicitly. For example, super().__init__(arg1, arg2, ...) calls the __init__ method defined in the parent class.

At the moment, you have effectively overridden the __init__ method inherited from Movie. This means that a TVSeries object will have only a seasons attribute and a total_episodes attribute. This is not what you want.

To keep all the code defined in the Movie class' __init__, use super to call the parent's __init__. Note that you'll need to pass in the arguments required by the method. In this case, title, year, director, and duration.

Step 19
Now, complete your __init__ method by validating seasons and total_episodes. Create an if statement that checks if seasons is less than 1 and raises a ValueError with the message Seasons must be 1 or greater.

Then, do the same to validate total_episodes. This time use the message Total episodes must be 1 or greater.

Step 20
Now that the __init__ method is complete, create a variable named series1 inside the try block. Assign it an instance of TVSeries passing in arguments of your choice. Then, print series1 to the console.

Step 21
As you can see, series1 is displayed in the same format of a Movie object because it's inheriting its parent's __str__ method. In the next step, you'll override the __str__ method to provide a custom string representation.

For now, delete the print(series1) line from your code.

Step 22
Within the TVSeries class, create a __str__ method that returns a string with the following format: title (year) - S seasons, N episodes, duration min avg, director, where title, year, S, N, duration, and director should be replaced by title, year, seasons, total_episodes, duration and director attributes, respectively.


Step 23
Use the add method of catalogue to append series1 to the items list.

Then, create another variable series2. Assign another instance of TVSeries to it and append series2 to the catalogue as well.

Step 24
A docstring is a string placed as the first statement in a class or function, and it's used to provide documentation for that class or function. Docstrings are typically enclosed by triple double quotes:

def add(x, y):
    """A function that returns the sum of two numbers."""
    return x + y
Complete your Movie class by adding the following docstring to it: Parent class representing a movie.

Step 25
Docstrings can be accessed through the __doc__ attribute, which is set to None by default.

Verify it by printing movie1.__doc__ and series1.__doc__. Note that the __doc__ attribute is not inherited by any child class.

Step 26
Now complete the TVSeries class by adding the docstring Child class representing an entire TV series.

Step 27
Now remove the two print calls from your code.

Step 28
Going back to the MediaCatalogue class, add a docstring to it saying A catalogue that can store different types of media items.

Step 29
It would be nice to validate the item passed to the add method before adding it to the catalogue.

Create an if statement that uses isinstance to check if media_item is an instance of Movie and raise a TypeError with the message Only Movie or TVSeries instances can be added.

Note that isinstance(obj, ClassName) returns True if obj is an instance of ClassName or any of its subclasses, because it considers the full inheritance chain.

Step 30
In a previous module, you learned that you can build your own custom exceptions by inheriting from the Exception built-in class:

class CustomError(Exception):
    ...
Create a class named MediaError. Make it inherit from the Exception class and add to it a docstring saying Custom exception for media-related errors..


Step 31
Give your MediaError class an __init__ method with the following parameters: self, message, and obj.

Inside it, call super().__init__(message) to ensure the mechanisms for storing and displaying the error message, which is already present in the Exception class, can work properly.

After that, assign obj to self.obj.

Step 32
Now that the MediaError class is complete, modify the if statement in the add method. Replace the TypeError with a MediaError using the same message.

Also, pass in media_item as the second argument after the message. This will allow you to store the item causing the error in the exception object.

Step 33
Create another except clause that catches MediaError as e. Within the except block, use an f-string to print Media Error: followed by a space and the error message.

Step 34
To see your custom exception in action, turn the line catalogue.add(series2) into catalogue.add('series2').

Step 35
Since you are storing the object causing the exception in the exception object, you can make some use of it.

After your existing print call, add print(f'Unable to add {e.obj}: {type(e.obj)}').

This kind of messages can be extremely useful when you are trying to debug your code.

Step 36
Remove the quotes around series2 to restore the line you modified before.

Step 37
Currently, both movies and TV series are displayed all together when you print the catalogue. In the next steps, you'll take care of filtering the items in two categories to display separately.

Inside the MediaCatalogue class, create a method named get_movies and make it return a list containing only instances of the parent class Movie that can be found in self.items.

Use the approach you prefer to do so, but remember to use the type function since isinstance won't be able to discriminate between parent and child classes.

Step 38
Create another method named get_tv_series and make it return a list with all the instances of TVSeries you can found in self.items.

Step 39
After the if statement in your __str__ method, create two variables named movies and series and assign it a call to the get_movies method and a call to the get_tv_series method, respectively.


Step 40
Before your for loop, create an if statement that adds the string === MOVIES === (ending with a newline character) to the current value of result when the movies list is not empty.

Step 41
Indent your existing for loop by one level so that it runs when the catalogue has movies in it. Then, replace self.items with movies to iterate over movies only.

Step 42
Using the same logic, create an if statement that runs when the series list is not empty. Inside it, concatenate the string === TV SERIES === (ending with a newline character) to the current value of result.

Then, create a for loop that uses enumeration to add the items in the series list to the result variable. As you did previously, start indexing the values from 1.

With that, the media catalogue workshop is complete.