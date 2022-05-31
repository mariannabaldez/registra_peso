from msilib import Table
import sqlalchemy
import databases


SQLALCHEMY_DATABASE_URL = "postgresql://postegres:development@localhost/registra-peso-db"
# "postgresql://user:password@postgresserver/db"

database = databases.Database(SQLALCHEMY_DATABASE_URL)s
metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(
    SQLALCHEMY_DATABASE_URL,
    execution_options={
        "isolation_level": "REPEATABLE READ"
    }
)


metadata.create_all(engine)
