# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 22:34:10 2025

@author: dries
"""

# models.py

class Brand:
    def __init__(self, brand_id, name):
        self.id = brand_id
        self.name = name

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def __str__(self):
        return f"{self.name}"


class Drink:
    def __init__(self, drink_id, name, brand_name, quantity, bought):
        self.id = drink_id
        self.name = name
        self.brand_name = brand_name
        self.quantity = quantity
        self.bought = bought

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_brand_name(self):
        return self.brand_name

    def get_quantity(self):
        return self.quantity

    def get_bought(self):
        return self.bought

    def is_bought(self):
        return self.bought == 1

    def __str__(self):
        bought_txt = "yes" if self.is_bought() else "no"
        return f"{self.id} - {self.brand_name} {self.name} (qty={self.quantity}, bought={bought_txt})"
