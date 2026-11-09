
import logging
from database import (
    initialize_database,
    add_product,
    get_all_products,
    search_product,
    update_product,
    delete_product
)

logging.basicConfig(
    filename="inventory.log",
    level=logging.ERROR
)


def main():
    initialize_database()

    while True:
        print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Exit")

        try:
            choice = input("Enter your choice: ")

            if choice == "1":
                pid = input("Enter Product ID: ")
                name = input("Enter Product Name: ")
                qty = int(input("Enter Quantity: "))
                add_product(pid, name, qty)

            elif choice == "2":
                products = get_all_products()

                if products:
                    for product in products:
                        print(product)
                else:
                    print("No products found")

            elif choice == "3":
                pid = input("Enter Product ID: ")
                product = search_product(pid)
                print(product if product else "Product not found")

            elif choice == "4":
                pid = input("Enter Product ID: ")
                qty = int(input("Enter New Quantity: "))
                update_product(pid, qty)

            elif choice == "5":
                pid = input("Enter Product ID: ")
                delete_product(pid)

            elif choice == "6":
                print("Thank you!")
                break

            else:
                print("Invalid choice. Try again.")

        except ValueError:
            print("Please enter a valid number.")

        except Exception:
            logging.exception("An error occurred")
            print("Something went wrong. Check the input and try again.")


if __name__ == "__main__":
    main()
              
