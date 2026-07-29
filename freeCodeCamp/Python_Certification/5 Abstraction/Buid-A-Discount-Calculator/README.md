Build A Discount Calculator

Technologies
Uses Python3.

Deployment
Copy main.py into the text editor of your choice. If using terminal, use the command python3 main.py to run the code.

Credits
Acknowledgements
FreeCodeCamp
-------------------------------------------------------------------------------------------------------------

Step 1

In this workshop, you are going to build a discount calculator that can apply different discount strategies to products. The system will determine the best price for a customer based on multiple discount rules.


Start by defining a class named Product. Give your class an __init__ method with the following parameters: self, name, and price. Inside the __init__ method, assign name and price parameters to instance attributes with the same name.


Step 2

In Python, type hints are optional signals that tell other developers what the data type of a variable or function is expected to be. Here is an example that adds the type hint str to the name parameter.



Example Code

def greet(name: str):
	return 'Hello, ' + name

For the __init__ method parameters, update the name parameter to have the type hint str and the price parameter to have the type hint float.


Step 3

Right now, if you create an instance of Product and print it, you'll see a default object representation that isn't very informative. For example, it might look something like <__main__.Product object at 0x7f9b8c2d1d30>.



To convert the default object representation into a readable string, create a __str__ method in your Product class that returns a string with the format name - $price (where name and price should be replaced with the values of the corresponding attributes).


Step 4

In Python, a return type hint indicates the expected return type of a function or method. You do this by adding -> return__type after the parameter list in the method definition.



Here is an example of a method with both parameter and return type hints whose return type is bool:



Example Code

def example_method(self, value: int) -> bool:
	pass

Other return type hints you might use include str, None, float and more.



In the existing __init__ method, add a return type hint of None since constructors do not return a value.


Step 5

Just like the previous Step, in your __str__ method, add a return type hint of str since this method returns a string representation of the object.


Step 6

Now, create an instance of Product with the name Wireless Mouse and a price of 50.0. Assign it to a variable named product. Then, print product to the console to see what it looks like


Step 7

Now you'll start building the discount system interface. Python provides a way to define abstract classes that serve as blueprints for other classes. This is done using the ABC class (Abstract Base Class) of the abc module.



At the top of your code, add the following import statement:



Example Code

from abc import ABC, abstractmethod

This imports the ABC class and the abstractmethod decorator, which you'll use to define methods that must be implemented by any class that inherits from your abstract class.


Step 8

Create a class named DiscountStrategy that inherits from ABC. This will be an abstract base class that defines the interface for all discount strategies.



For now, just use pass in the class body to create an empty class.


Step 9

As discussed in the previous lesson, abstract methods are methods that must be implemented by any class that inherits from the abstract base class. They serve as a contract, ensuring that all discount strategies will have certain required methods.



Inside your DiscountStrategy class, define a method named is__applicable. Use the @abstractmethod decorator above the method definition. The method should have the following parameters: self, product, and user__tier. Use the pass statement in the method body.



Add type hints to make the method signature clear: product should be of type Product, user__tier should be of type str.


Step 10

Add a return type hint of bool to the is__applicable method so that it clearly indicates it returns a bool.


Step 11

Now add a second abstract method named apply__discount to your DiscountStrategy class. Use the @abstractmethod decorator and give it parameters self and product.



Add type hints: product should be of type Product, and the method should return a float. Use pass in the method body.


Step 12

Now it's time to create a concrete implementation of your abstract class. Create a class named PercentageDiscount that inherits from DiscountStrategy.



Give it an __init__ method that takes self and percent as parameters. Give a type hint of int to percent and set the return type of the method to None. Inside the __init__ method, store percent as an instance attribute.


Step 13

Since PercentageDiscount inherits from an abstract class, you must implement all abstract methods. Start by implementing the is__applicable method. The is__applicable method should take self, product: Product, and user__tier: str as parameters. It should have a return type hint of bool.



This method should determine whether a percentage discount is valid. Return True if self.percent is less than or equal to 70, otherwise return False. This prevents unrealistic discounts like 90% off.


Step 14

Now implement the apply__discount method in your PercentageDiscount.



This method should calculate and return the discounted price.



The formula is: product.price \* (1 - self.percent / 100)


Step 15

After implementing the apply__discount method, test your discount strategy. Create an instance of PercentageDiscount with 10 percent and assign it to a variable named discount. Then apply the discount using discount.apply__discount(product), and print the result to see the discount in action.


Step 16

Now you'll create another discount strategy. Create a class named FixedAmountDiscount that inherits from DiscountStrategy.



Give it an __init__ method that takes self and amount as parameters. Give amount parameter a type hint of int and a return type hint of None for the method. Inside the __init__ method, store amount as an instance attribute.


Step 17

Implement the is__applicable method for your FixedAmountDiscount class. A fixed amount discount should only be applied if it makes sense economically.



Return True if product.price \* 0.9 is greater than self.amount, otherwise return False. This ensures the discount is less than 90% of the original price, so it's not unrealistic.


Step 18

Now implement the apply__discount method for FixedAmountDiscount. This method should subtract the fixed amount from the product price and return the new price.


Step 19

You can now test the new discount strategy. After the existing code, create an instance of FixedAmountDiscount with an amount of 5 and assign it to a variable named fixed__discount. Then apply this discount to the product and print the result.


Step 20

For the third discount strategy, create a class named PremiumUserDiscount that inherits from DiscountStrategy.



Unlike the previous strategies, this one doesn't need an __init__ method because it doesn't store any configuration. It will apply a fixed 20% discount to all premium users.



For now, just create the empty class that inherits from DiscountStrategy using pass.


Step 21

Implement the is__applicable method for PremiumUserDiscount. This method should check if the user is a premium member.



Return True if user__tier.lower() equals 'premium', otherwise return False. Using .lower() ensures the check is case-insensitive.


Step 22

Now implement the apply__discount method for PremiumUserDiscount. This should apply a 20% discount to premium users.



Return product.price \* 0.8 (which represents 80% of the original price, i.e., 20% off).


Step 23

Now you need a way to manage multiple discount strategies and find the best price.



Create a class named DiscountEngine. This class will manage all discount strategies and calculate the best price for a product.



Give it an __init__ method that takes self and strategies as parameters, where strategies has a type hint of list\[DiscountStrategy]. Using list\[DiscountStrategy] specifies that the parameter is a list containing DiscountStrategy objects. The return type of the method should be None. Inside the __init__ method, store strategies as an instance attribute.


Step 24

Now create a method named calculate__best__price in your DiscountEngine class. This method should take self, product, and user__tier as parameters, and return a float.



For now, just use pass in the method body. You'll implement the logic in the next Steps.


Step 25

Inside the calculate__best__price method, create a list named prices containing product.price. This ensures that if no discounts apply, the customer pays the full price.


Step 26

Now create a for loop that iterates over self.strategies. For each strategy, check if it's applicable using the is__applicable method. If it is, calculate the discounted price using apply__discount and store it in a variable named discounted. Then, append the discounted price to the prices list.


Step 27

Finally, return the minimum value from the prices list using the min() function. This will give you the best (lowest) price after considering all applicable discounts.


Step 28

Now, remove the following lines from the bottom of your code:



* print(product)
* discount = PercentageDiscount(10)
* print(discount.apply__discount(product))
* fixed__discount = FixedAmountDiscount(5)
* print(fixed__discount.apply__discount(product))




Step 29

It's time to test the complete discount system! Add an if statement checking if __name__ == '__main__' and move product = Product('Wireless Mouse', 50.0) inside it.



After that, inside the if block, create a variable user__tier and set it to the string Premium. Then create a variable strategies set to a list of strategies containing PercentageDiscount(10), FixedAmountDiscount(5), and PremiumUserDiscount().




Step 30

Create a DiscountEngine instance and store it in the variable engine. After that, calculate the best price using calculate__best__price method and store it in a variable named best__price.




Step 31

To complete the workshop, add a final print statement to display the best price with two decimal places using an f-string and this format: Best price for \[product.name] for \[user__tier] user: $\[best__price] where \[product.name], \[user__tier], and \[best__price] should be replaced with the actual variable values.



An example output could be: Best price for Wireless Buds for Premium user: $93.00. Note the two decimal places for the price.



With that, the discount calculator workshop is complete!

