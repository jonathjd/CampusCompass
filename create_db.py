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
    longitude REAL,
    FOREIGN KEY (school_id) REFERENCES school (id)
    )
    """
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS finance (
    id INTEGER PRIMARY KEY,
    school_id INTEGER,
    year DATE,
    cost4a REAL,
    in_state_tuition REAL,
    out_state_tuition REAL,
    FOREIGN KEY (school_id) REFERENCES school (id)
    )
    """
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS control (
    id INTEGER PRIMARY KEY,
    school_id INTEGER,
    under_investigation BOOLEAN,
    predominant_deg TEXT,
    highest_deg TEXT,
    control TEXT,
    FOREIGN KEY (school_id) REFERENCES school (id)
    )
    """
)

connection.commit()
