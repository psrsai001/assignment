from main import cursor

cursor.execute(
    """
CREATE DATABASE IF  NOT EXISTS wipro;
"""
)

cursor.close()
