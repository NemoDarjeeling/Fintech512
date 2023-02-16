### Extract Function  
"Extract Function" is a refactoring technique that involves taking a section of code from within a larger function and turning it into its own separate function. This can improve the readability, maintainability, and reusability of the code by making it more modular and easier to understand.
'''def calculate_total_price(cart_items, discount_percent):
    total_price = 0
    for item in cart_items:
        item_price = item['price'] * item['quantity']
        total_price += item_price
    discount_amount = total_price * (discount_percent / 100)
    final_price = total_price - discount_amount
    return final_price'''
'''def calculate_item_price(item):
    return item['price'] * item['quantity']'''
'''def calculate_total_price(cart_items, discount_percent):
    total_price = sum(calculate_item_price(item) for item in cart_items)
    discount_amount = total_price * (discount_percent / 100)
    final_price = total_price - discount_amount
    return final_price'''

### Replace Temp with Query  

### Inline Variable  

### Change Function Declaration  

### Split Loop  

### Slide Statements  

### Extract Temp with Query  

### Inline Variable  

### Split Phase  

### Move Function  

### Replace Loop with Pipeline  

### Replace Conditional with Polymorphism  

### Change Function Declaration  

### Replace Type Code with Subclasses  

### Replace Constructor with Factory Function  
