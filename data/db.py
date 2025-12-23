# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 23:26:04 2025

@author: dries
"""

# db.py
import sqlite3
import settings


def open_connection():
    connection = sqlite3.connect(settings.DB_PATH)
    return connection
