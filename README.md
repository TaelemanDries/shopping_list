# Purpose

- This project is a simple command-line application to make shopping lists for drinks. The user can add drinks, brands to the drinks, mark them as bought or not bought, update quantity and export it as an csv-file. 

# Technology

- Python 3
- SQLite
- Git (GitHub)

# Libraries

- SQLite3
- csv

No external libraries required.

# Functions

- Add a drink with a brand and quantity
- Automatically create brands if they do not exist
- Show a list of all drinks
- Search drinks by name or brand
- Mark a drink as bought or not bought
- Update the quantity of a drink
- Export the shopping list to a CSV file

# Planned Functions

- Delete a drink from the shopping list
- Add prices to drinks
- Export the shopping list to Excel format

# Database name

The application uses an SQLite database.

Default database file:

shopping_list.db

The database file location is configured in `settings.py`.

# How to execute

1. Clone the repository from GitHub
2. Create and activate a virtual environment

```bash
python -m venv .venv


# Structure of database

The database consists of two tables with a one-to-many relationship.

Table: brands

id – INTEGER, primary key
name – TEXT, unique

Each brand represents a drink brand (e.g. Coca-Cola, Jupiler).

Table: drinks

id – INTEGER, primary key
name – TEXT
brand_id – INTEGER, foreign key referencing brands.id
quantity – INTEGER
bought – INTEGER (0 = not bought, 1 = bought)

Each drink belongs to exactly one brand.
A brand can be linked to multiple drinks.

Relationship

One brand → many drinks
Enforced using a foreign key on drinks.brand_id