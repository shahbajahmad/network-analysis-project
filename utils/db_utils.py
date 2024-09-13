import sqlalchemy

def get_database_connection(db_url: str):
    """
    Get a SQLAlchemy database connection engine.

    Args:
        db_url (str): The database connection URL.

    Returns:
        sqlalchemy.engine.Engine: The database connection engine.
    """
    return sqlalchemy.create_engine(db_url)
