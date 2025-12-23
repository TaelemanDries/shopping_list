# -*- coding: utf-8 -*-
"""
Created on Wed Dec 24 00:O7:02 2025

@author: dries
"""

# shopping_service.py
import csv
from data.repository import ShoppingRepository


class ShoppingService:
    def __init__(self):
        self.repo = ShoppingRepository()

    def list_all(self):
        return self.repo.list_drinks()

    def add_item(self, drink_name, brand_name, quantity):
        drink_name = drink_name.strip()
        brand_name = brand_name.strip()

        if drink_name == "":
            raise ValueError("Drink name is required.")
        if brand_name == "":
            raise ValueError("Brand name is required.")
        if quantity < 0:
            raise ValueError("Quantity must be 0 or higher.")

        brand_id = self.repo.add_brand(brand_name)
        self.repo.add_drink(drink_name, brand_id, quantity)

    def search(self, text):
        text = text.strip()
        if text == "":
            return []
        return self.repo.search_drinks(text)

    def mark_bought(self, drink_id):
        return self.repo.set_bought(drink_id, 1)

    def mark_not_bought(self, drink_id):
        return self.repo.set_bought(drink_id, 0)

    def change_quantity(self, drink_id, quantity):
        if quantity < 0:
            raise ValueError("Quantity must be 0 or higher.")
        return self.repo.set_quantity(drink_id, quantity)

    def export_csv(self, filename="shopping_list.csv"):
        items = self.list_all()

        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "brand", "drink", "quantity", "bought"])

            for d in items:
                writer.writerow([
                    d.get_id(),
                    d.get_brand_name(),
                    d.get_name(),
                    d.get_quantity(),
                    d.get_bought()
                ])

        return filename
