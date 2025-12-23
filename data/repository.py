# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 23:37:52 2025

@author: dries
"""

# repository.py
from data.db import open_connection
from domain.models import Drink


class ShoppingRepository:

    def get_brand_id(self, brand_name):
        connection = open_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT id FROM brands WHERE name = ?;", (brand_name,))
            row = cursor.fetchone()
            if row is None:
                return None
            return row[0]
        finally:
            connection.close()

    def add_brand(self, brand_name):
        """
        Inserts a brand if it does not exist.
        Returns brand id.
        """
        existing_id = self.get_brand_id(brand_name)
        if existing_id is not None:
            return existing_id

        connection = open_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO brands(name) VALUES (?);", (brand_name,))
            connection.commit()
            return cursor.lastrowid
        finally:
            connection.close()

    def add_drink(self, drink_name, brand_id, quantity):
        connection = open_connection()
        try:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO drinks(name, brand_id, quantity, bought) VALUES (?, ?, ?, ?);",
                (drink_name, brand_id, quantity, 0)
            )
            connection.commit()
        finally:
            connection.close()

    def list_drinks(self):
        connection = open_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT d.id, d.name, b.name, d.quantity, d.bought
                FROM drinks d
                JOIN brands b ON b.id = d.brand_id
                ORDER BY d.bought ASC, b.name ASC, d.name ASC;
            """)
            rows = cursor.fetchall()

            drinks = []
            for row in rows:
                drink = Drink(row[0], row[1], row[2], row[3], row[4])
                drinks.append(drink)
            return drinks
        finally:
            connection.close()

    def search_drinks(self, text):
        like = "%" + text + "%"
        connection = open_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("""
                SELECT d.id, d.name, b.name, d.quantity, d.bought
                FROM drinks d
                JOIN brands b ON b.id = d.brand_id
                WHERE d.name LIKE ? OR b.name LIKE ?
                ORDER BY b.name ASC, d.name ASC;
            """, (like, like))
            rows = cursor.fetchall()

            result = []
            for row in rows:
                result.append(Drink(row[0], row[1], row[2], row[3], row[4]))
            return result
        finally:
            connection.close()

    def drink_exists(self, drink_id):
        connection = open_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT id FROM drinks WHERE id = ?;", (drink_id,))
            row = cursor.fetchone()
            return row is not None
        finally:
            connection.close()

    def set_bought(self, drink_id, bought):
        if not self.drink_exists(drink_id):
            return False

        connection = open_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("UPDATE drinks SET bought = ? WHERE id = ?;", (bought, drink_id))
            connection.commit()
            return True
        finally:
            connection.close()

    def set_quantity(self, drink_id, quantity):
        if not self.drink_exists(drink_id):
            return False

        connection = open_connection()
        try:
            cursor = connection.cursor()
            cursor.execute("UPDATE drinks SET quantity = ? WHERE id = ?;", (quantity, drink_id))
            connection.commit()
            return True
        finally:
            connection.close()
