import sqlite3, config

connection = sqlite3.connect(config.DB_FILE)

cursor = connection.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS school (
    id INTEGER PRIMARY KEY,
    ope8_id INTEGER NOT NULL UNIQUE,
    name TEXT NOT NULL UNIQUE
    )
    """
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS location (
    id INTEGER PRIMARY KEY,
    school_id INTEGER,
    city TEXT NOT NULL,
    zipcode TEXT NOT NULL,
    state TEXT NOT NULL,
    region TEXT NOT NULL,
    locale TEXT,
    latitude REAL,
    longitude REAL
    )
    """
)

connection.commit()
