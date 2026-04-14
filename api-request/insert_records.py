import psycopg2
from api_request import mock_fetch_data, fetch_data
from dotenv import load_dotenv
import os
load_dotenv()

db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")


def connect_to_db():
    print("Connecting to the PostgreSQL database")
    try:
        conn = psycopg2.connect(
            host="db",
            port=5432,
            dbname=db_name,
            user=db_user,
            password=db_password
        )
        return conn
    except psycopg2.Error as e:
        print(f"Database connection failed: {e}")
        raise


def create_table(conn):
    print("Create a table if not exists")
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE SCHEMA IF NOT EXISTS dev;
            CREATE TABLE IF NOT EXISTS dev.raw_weather_data (
                id SERIAL PRIMARY KEY,
                city TEXT,
                temperature FLOAT,
                weather_descriptions TEXT,
                wind_speed FLOAT,
                wind_dir TEXT,
                cloud_cover INT,
                feels_like FLOAT,
                time TIMESTAMP,
                inserted_at TIMESTAMP,
                utc_offset TEXT
            );
            """
        )
        conn.commit()
        print("Table was created successfully")
    except psycopg2.Error as e:
        print(f"Failed to create a table: {e}")


def insert_records(conn, data):
    print("Inserting data into the table")
    try:
        weather = data["current"]
        location = data["location"]
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO dev.raw_weather_data (
                city,
                temperature,
                weather_descriptions,
                wind_speed,
                wind_dir,
                cloud_cover,
                feels_like,
                time,
                inserted_at,
                utc_offset
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, NOW(), %s)
            """, (
                location["name"],
                weather["temperature"],
                weather["weather_descriptions"][0],
                weather["wind_speed"],
                weather["wind_dir"],
                weather["cloudcover"],
                weather["feelslike"],
                location["localtime"],
                location["utc_offset"]
            )
        )
        conn.commit()
        print("Data was successfully inserted")
    except psycopg2.Error as e:
        print(f"Failed to insert data into the table: {e}")
        raise

def main():
    try:
        # data = mock_fetch_data()
        data = fetch_data(["Lviv"])
        conn = connect_to_db()
        create_table(conn)
        for city_data in data:
            insert_records(conn, city_data)
    except Exception as e:
        print(f"An error occured during execution: {e}")
    finally:
        if "conn" in locals() and conn is not None:
            conn.close()
            print("Database connection closed")


if __name__ == "__main__":
    main()