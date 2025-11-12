import sqlite3

# Create dummy database
conn = sqlite3.connect('bookstore.db')
cursor = conn.cursor()

# Create required tables if they don't exist
# Tables to be created: customers, orders, products & order_products
cursor.execute('''
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    city TEXT,
    join_date TEXT
)''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    category TEXT,
    price REAL
)''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER,
    order_date TEXT,   
    total_amount REAL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
)''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS order_products (
    order_product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    subtotal REAL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
)''')

# Insert dummy data
# 1. Customers
customers = [
    ('James Carter', 'james.carter@example.com', 'San Francisco', '2024-01-03'),
    ('Maria Lopez', 'maria.lopez@example.com', 'Austin', '2024-01-25'),
    ('William Brown', 'william.brown@example.com', 'Portland', '2024-02-11'),
    ('Sophia Turner', 'sophia.turner@example.com', 'Orlando', '2024-03-05'),
    ('Noah Scott', 'noah.scott@example.com', 'Dallas', '2024-03-22'),
    ('Olivia Martinez', 'olivia.martinez@example.com', 'Phoenix', '2024-04-14'),
    ('Lucas Dean', 'lucas.dean@example.com', 'Atlanta', '2024-05-08'),
    ('Emma Brooks', 'emma.brooks@example.com', 'San Diego', '2024-06-02')
]
cursor.executemany("INSERT INTO customers (name, email, city, join_date) VALUES (?, ?, ?, ?)", customers)

# 2. Products
products = [
    ('The Silent Ocean', 'Fiction', 14.99),
    ('Mastering Python', 'Programming', 29.99),
    ('AI Revolution', 'Technology', 34.50),
    ('Cooking Made Easy', 'Lifestyle', 18.75),
    ('Travel Guide: Europe', 'Travel', 22.00),
    ('Leather Bookmark', 'Accessory', 3.99),
    ('Book Light', 'Accessory', 12.50),
    ('History of Space', 'Non-Fiction', 26.99),
    ('Notebook Journal', 'Stationery', 6.49),
    ('Mystery Tales Vol. 1', 'Fiction', 15.25)
]
cursor.executemany("INSERT INTO products (name, category, price) VALUES (?, ?, ?)", products)

# 3. Orders
orders = [
    (1, '2024-06-12', 44.98),
    (2, '2024-06-20', 33.49),
    (3, '2024-07-01', 65.74),
    (4, '2024-07-15', 37.24),
    (5, '2024-07-28', 57.50),
    (6, '2024-08-09', 29.99),
    (7, '2024-08-19', 41.24),
    (8, '2024-09-01', 25.75)
]
cursor.executemany("INSERT INTO orders (customer_id, order_date, total_amount) VALUES (?, ?, ?)", orders)

# 4. Order Products
order_products = [
    (1, 1, 2, 14.99 * 2),     # James bought 2 'The Silent Ocean'
    (1, 6, 1, 3.99),          # James bought 1 'Leather Bookmark'
    (2, 2, 1, 29.99),         # Maria bought 1 'Mastering Python'
    (2, 9, 1, 6.49),          # Maria bought 1 'Notebook Journal'
    (3, 3, 2, 34.50 * 2),     # William bought 2 'AI Revolution'
    (3, 7, 1, 12.50),         # William bought 1 'Book Light'
    (4, 4, 1, 18.75),         # Sophia bought 1 'Cooking Made Easy'
    (4, 6, 2, 3.99 * 2),      # Sophia bought 2 bookmarks
    (5, 5, 1, 22.00),         # Noah bought 'Travel Guide: Europe'
    (5, 8, 1, 26.99),         # Noah bought 'History of Space'
    (5, 9, 1, 6.49),          # Noah bought 'Notebook Journal'
    (6, 2, 1, 29.99),         # Olivia bought 'Mastering Python'
    (7, 10, 2, 15.25 * 2),    # Lucas bought 2 'Mystery Tales Vol. 1'
    (7, 6, 1, 3.99),          # Lucas bought a 'Bookmark'
    (8, 1, 1, 14.99),         # Emma bought 'The Silent Ocean'
    (8, 9, 1, 6.49)           # Emma bought 'Notebook Journal'
]
cursor.executemany("INSERT INTO order_products (order_id, product_id, quantity, subtotal) VALUES (?, ?, ?, ?)", order_products)

# Commit changes and close connection
conn.commit()
conn.close()

print("Bookstore dummy dataset inserted successfully!")