def calculate_discount(price, discount_rate):
    #Ensure the price is a valid number
    try:
        price = float(price)
    except ValueError:
        raise ValueError(f"Invalid price: {price}. Price must be a valid number.")

    #Calculate the discount amount based on the price and discount rate.
    discount_amount = price * discount_rate
    return discount_amount

def apply_discount(price, discount_amount):
    #Ensure price and discount_amount are valid numbers
    try:
        price = float(price)
        discount_amount = float(discount_amount)
    except ValueError:
        raise ValueError(f"Invalid value for price or discount amount: {price} and {discount_amount}.")

    #Apply the discount amount to the original price and return the new price.
    new_price = price - discount_amount
    return new_price

def main():

    products = [
        {"name": "Laptop", "price": 1000, "discount_rate": 0.1},
        {"name": "Smartphone", "price": 800, "discount_rate": 0.15},
        {"name": "Tablet", "price": "500", "discount_rate": 0.2},
        {"name": "Headphones", "price": 200, "discount_rate": 0.05}
    ]

    for product in products:
        price = product["price"]
        discount_rate = product["discount_rate"]

        try:
            #Calculate discount amount
            discount_amount = calculate_discount(price, discount_rate)
            final_price = apply_discount(price, discount_amount)

            #Print the results
            print(f"Product: {product['name']}")
            print(f"Original Price: ${price}")
            print(f"Discount Amount: ${discount_amount}")
            print(f"Final Price: ${final_price}")
            print()
        except ValueError as e:
            print(f"Error with product {product['name']}: {e}")
            print()


if __name__ == "__main__":
    main()


