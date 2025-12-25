# -*- coding: utf-8 -*-
"""
Created on Wed Dec 24 00:27:59 2025

@author: dries
"""

# cli.py
from services.shopping_service import ShoppingService


def print_drinks(drinks):
    if len(drinks) == 0:
        print("No drinks found.\n")
        return

    print("ID | Brand | Drink | Qty | Bought")
    print("-------------------------------")

    for d in drinks:
        bought_txt = "YES" if d.is_bought() else "NO"
        print(f"{d.get_id():>2} | {d.get_brand_name()[:12]:<12} | {d.get_name()[:20]:<20} | {d.get_quantity():>3} | {bought_txt}")

    print()


def run_menu():
    service = ShoppingService()

    while True:
        print("=== Shopping List (Drinks) ===")
        print("1) List all")
        print("2) Add drink")
        print("3) Search")
        print("4) Mark bought")
        print("5) Mark NOT bought")
        print("6) Change quantity")
        print("7) Export CSV")
        print("0) Exit")

        choice = input("> ").strip()
        print()

        try:
            if choice == "1":
                drinks = service.list_all()
                print_drinks(drinks)

            elif choice == "2":
                name = input("Drink name: ")
                brand = input("Brand name: ")
                qty = int(input("Quantity: "))
                service.add_item(name, brand, qty)
                print("Added.\n")

            elif choice == "3":
                text = input("Search (drink or brand): ")
                drinks = service.search(text)
                print_drinks(drinks)

            elif choice == "4":
                drink_id = int(input("Drink id: "))
                ok = service.mark_bought(drink_id)
                if ok:
                    print("Updated.\n")
                else:
                    print("Drink not found.\n")

            elif choice == "5":
                drink_id = int(input("Drink id: "))
                ok = service.mark_not_bought(drink_id)
                if ok:
                    print("Updated.\n")
                else:
                    print("Drink not found.\n")

            elif choice == "6":
                drink_id = int(input("Drink id: "))
                qty = int(input("New quantity: "))
                ok = service.change_quantity(drink_id, qty)
                if ok:
                    print("Updated.\n")
                else:
                    print("Drink not found.\n")

            elif choice == "7":
                filename = service.export_csv()
                print(f"Exported to {filename}\n")

            elif choice == "0":
                print("Goodbye!")
                break

            else:
                print("Unknown option.\n")

        except ValueError as e:
            print(f"Error: {e}\n")
