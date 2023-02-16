### Extract Function  
"Extract Function" is a refactoring technique that involves taking a section of code from within a larger function and turning it into its own separate function. This can improve the readability, maintainability, and reusability of the code by making it more modular and easier to understand.
    
        def calculate_total_price(cart_items, discount_percent):
            total_price = 0
            for item in cart_items:
                item_price = item['price'] * item['quantity']
                total_price += item_price
            discount_amount = total_price * (discount_percent / 100)
            final_price = total_price - discount_amount
            return final_price
      
        def calculate_item_price(item):
            return item['price'] * item['quantity']
        def calculate_total_price(cart_items, discount_percent):
            total_price = sum(calculate_item_price(item) for item in cart_items)
            discount_amount = total_price * (discount_percent / 100)
            final_price = total_price - discount_amount
            return final_price

### Replace Temp with Query  
"Replace Temp with Query" is a refactoring technique in which temporary variables used to store intermediate results within a function are replaced with a function call that calculates the same result. This can improve the clarity and maintainability of the code by making it easier to understand the intent of the code and reducing the number of variables that need to be tracked.
  
        def calculate_total_price(product_price, tax_rate, shipping_rate):
            tax_amount = product_price * tax_rate
            total_price = product_price + tax_amount
            shipping_amount = total_price * shipping_rate
            total_price = total_price + shipping_amount
            return total_price
        
        def calculate_tax(product_price, tax_rate):
            return product_price * tax_rate
        def calculate_shipping(product_price, shipping_rate):
            return product_price * shipping_rate
        def calculate_total_price(product_price, tax_rate, shipping_rate):
            total_price = product_price + calculate_tax(product_price, tax_rate)
            total_price = total_price + calculate_shipping(total_price, shipping_rate)
            return total_price

### Inline Variable  
"Inlining Variables" is a refactoring technique in which a variable used to store a value is replaced with the actual value itself. This can simplify the code and make it easier to understand by reducing the number of variables that need to be tracked.
  
        def calculate_rectangle_area(length, width):
            area = length * width
            return area

        def calculate_rectangle_area(length, width):
            return length * width

### Change Function Declaration  
"Change Function Declaration" is a refactoring technique that involves modifying the parameters or return type of a function to better reflect its purpose or make it more flexible. 
  
        def calculate_rectangle_area(length, width):
            area = length * width
            return str(area)

        def calculate_rectangle_area(length, width):
            return length * width

### Split Loop  
"Split Loop" is a refactoring technique that involves breaking up a loop that performs multiple tasks into separate loops, each of which performs a single task. 
  
        def calculate_average_score(students):
            total_score = 0
            count = 0
            for student in students:
                total_score += student['score']
                count += 1
                student['average_score'] = total_score / count
            return students
        
        def calculate_average_score(students):
            total_score = 0
            count = 0
            for student in students:
                total_score += student['score']
                count += 1   
            average_score = total_score / count
            for student in students:
                student['average_score'] = average_score
            return students

### Slide Statements  
"Slide Statements" is a refactoring technique that involves reordering the statements in a block of code to improve its readability and maintainability.   
  
            a = 0;
            b = 1;
            ...a bunch of other code...
            def add_numbers(a, b):
                result = a + b
                return result
  
            ...a bunch of other code...
            a = 0;
            b = 1;
            def add_numbers(a, b):
                result = a + b
                return result
  
### Extract Temp with Query  
"Extract Temp with Query" is a refactoring technique that involves replacing a temporary variable in a method with a query that calculates the value of that variable.
  
        def calculate_total_cost(order):
            base_cost = order['quantity'] * order['price']
            if base_cost > 1000:
                discount_rate = 0.05
            else:
                discount_rate = 0.01
            discount = base_cost * discount_rate
            total_cost = base_cost - discount
            return total_cost
        
        def calculate_base_cost(order):
            return order['quantity'] * order['price']
        def calculate_discount_rate(order):
            if calculate_base_cost(order) > 1000:
                return 0.05
            else:
                return 0.01
        def calculate_discount(order):
            return calculate_base_cost(order) * calculate_discount_rate(order)
        def calculate_total_cost(order):
            return calculate_base_cost(order) - calculate_discount(order)
  
### Split Phase  
"Split Phase" is a refactoring technique that involves splitting a complex method into two or more smaller methods, each of which performs a single, focused task.
  
        def process_order_and_send_email(order):
            # Step 1: Process the order
            if order['quantity'] * order['price'] > 1000:
                discount_rate = 0.05
            else:
                discount_rate = 0.01
            discount = order['quantity'] * order['price'] * discount_rate
            total_cost = order['quantity'] * order['price'] - discount
            # Step 2: Send email notification
            email_text = f"Dear {order['customer_name']}, your order has been processed. " \
                        f"The total cost is ${total_cost:.2f}. Thank you for your business."
            send_email(order['customer_email'], email_text)
        
        def process_order(order):
            if order['quantity'] * order['price'] > 1000:
                discount_rate = 0.05
            else:
                discount_rate = 0.01
            discount = order['quantity'] * order['price'] * discount_rate
            total_cost = order['quantity'] * order['price'] - discount
            return total_cost
        def send_order_confirmation_email(order, total_cost):
            email_text = f"Dear {order['customer_name']}, your order has been processed. " \
                        f"The total cost is ${total_cost:.2f}. Thank you for your business."
            send_email(order['customer_email'], email_text)
        total_cost = process_order(order)
        send_order_confirmation_email(order, total_cost)

### Move Function  
"Move Function" is a refactoring technique that involves moving a method from one class to another. The goal is to improve the organization and maintainability of the code by placing related methods together in a single class.
  
        class Order:
            def __init__(self, customer, quantity, price):
                self.customer = customer
                self.quantity = quantity
                self.price = price
            def calculate_total_cost(self):
                if self.quantity * self.price > 1000:
                    discount_rate = 0.05
                else:
                    discount_rate = 0.01
                discount = self.quantity * self.price * discount_rate
                total_cost = self.quantity * self.price - discount
                return total_cost
        class Customer:
            def __init__(self, name, email):
                self.name = name
                self.email = email
        
        class Order:
            def __init__(self, customer, quantity, price):
                self.customer = customer
                self.quantity = quantity
                self.price = price
        class Customer:
            def __init__(self, name, email):
                self.name = name
                self.email = email
            def calculate_total_cost(self, order):
                if order.quantity * order.price > 1000:
                    discount_rate = 0.05
                else:
                    discount_rate = 0.01
                discount = order.quantity * order.price * discount_rate
                total_cost = order.quantity * order.price - discount
                return total_cost

### Replace Loop with Pipeline  
"Replace Loop with Pipeline" is a refactoring technique that involves replacing a loop that performs a series of operations on a collection with a pipeline of function calls. The goal is to improve the readability and maintainability of the code by breaking down the loop into smaller, composable functions.
*pipeline:* a "pipeline" generally refers to a sequence of processing steps that are applied to a set of data, typically in a streaming or batch processing context. Each step in the pipeline takes some input, performs some processing or transformation, and produces some output, which is then passed on to the next step in the pipeline.  
  
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        total = 0
        for number in numbers:
            if number % 2 == 0:
                continue
            doubled = number * 2
            total += doubled
        print(total)
        
        from functools import reduce
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        total = reduce(lambda x, y: x + y, map(lambda x: x * 2, filter(lambda x: x % 2 != 0, numbers)))
        print(total)

### Replace Conditional with Polymorphism  
polymorphism allows objects of different classes to be treated as if they were objects of the same class. This means that you can create a set of related classes that implement the same methods but behave differently, depending on their specific implementation.  
  
        class Animal:
            def make_sound(self):
                pass
        
        class Cat(Animal):
            def make_sound(self):
                return "Meow"  
        class Dog(Animal):
            def make_sound(self):
                return "Woof"

### Change Function Declaration  
"Change Function Declaration" is a refactoring technique that involves modifying the signature of a function to make it more clear, expressive, or flexible. This technique is useful when the original signature of a function no longer meets the needs of the code, such as when new functionality is added or the function's context changes.  
  
        def calculate_total_price(item_price):
            tax_rate = 0.1  # 10% tax rate
            total_price = item_price + (item_price * tax_rate)
            return total_price
        
        def calculate_total_price(item_price, tax_rate):
            total_price = item_price + (item_price * tax_rate)
            return total_price

### Replace Type Code with Subclasses  
"Replace Type Code with Subclasses" refactoring technique, which involves replacing a type code (a variable that is used to represent a specific type) with a set of subclasses that implement different behaviors for that type.  
  
        class Shape:
            def __init__(self, type):
                self.type = type
            def draw(self):
                if self.type == "circle":
                    print("Drawing a circle...")
                elif self.type == "square":
                    print("Drawing a square...")
                elif self.type == "triangle":
                    print("Drawing a triangle...")
                else:
                    raise ValueError("Unknown shape type")
        
        class Shape:
            def draw(self):
                pass
        class Circle(Shape):
            def draw(self):
                print("Drawing a circle...")        
        class Square(Shape):
            def draw(self):
                print("Drawing a square...")        
        class Triangle(Shape):
            def draw(self):
                print("Drawing a triangle...")

### Replace Constructor with Factory Function  
The "Replace Constructor with Factory Function" refactoring technique involves replacing a class constructor with a factory function. The factory function is responsible for creating new objects of the class, but it can also perform additional logic or validation before creating the object, which can make the code more maintainable and flexible.
  
        class Product:
            def __init__(self, name, price, category):
                self.name = name
                self.price = price
                self.category = category
        book = Product("Book", 10.0, "Stationery")
        shirt = Product("Shirt", 20.0, "Clothing")

        class Product:
            def __init__(self, name, price, category):
                self.name = name
                self.price = price
                self.category = category  
        def create_product(name, price, category):
            if price < 0:
                raise ValueError("Price must be non-negative")
            if not category:
                raise ValueError("Category must be provided")
            return Product(name, price, category)
        book = create_product("Book", 10.0, "Stationery")
        shirt = create_product("Shirt", 20.0, "Clothing")

