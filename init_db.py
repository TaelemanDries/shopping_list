# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 22:13:56 2025

@author: dries
"""

# init_db.py
import sqlite3
import settings


def init_db():
    connection = sqlite3.connect(settings.DB_PATH)
    try:
        cursor = connection.cursor()

        cursor.execute("PRAGMA foreign_keys = ON;")

        with open("schema.sql", "r", encoding="utf-8") as f:
            schema = f.read()
            cursor.executescript(schema)

        brands = ["Coca-Cola", "Jupiler", "Spa", "Red Bull"]
        for brand in brands:
            cursor.execute(
                "INSERT INTO brands(name) VALUES (?);",
                (brand,)
            )

        cursor.execute("SELECT id, name FROM brands;")
        rows = cursor.fetchall()

        brand_ids = {}
        for row in rows:
            brand_ids[row[1]] = row[0]

        drinks = [
            ("Cola Zero", "Coca-Cola", 6, 0),
            ("Cola Regular", "Coca-Cola", 2, 0),
            ("Jupiler 33cl", "Jupiler", 12, 0),
            ("Spa Reine", "Spa", 6, 1),
            ("Red Bull", "Red Bull", 4, 0),
        ]

        for name, brand_name, qty, bought in drinks:
            cursor.execute(
                """
                INSERT INTO drinks(name, brand_id, quantity, bought)
                VALUES (?, ?, ?, ?);
                """,
                (name, brand_ids[brand_name], qty, bought)
            )

        connection.commit()
        print("Database created and sample data inserted.")

    finally:
        connection.close()


if __name__ == "__main__":
    init_db()
