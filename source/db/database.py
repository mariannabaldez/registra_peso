import sqlalchemy
import databases


SQLALCHEMY_DATABASE_URL = "postgresql://postegres:development@localhost/registra-peso-db"
# "postgresql://user:password@postgresserver/db"

database = databases.Database(SQLALCHEMY_DATABASE_URL)s
metadata = sqlalchemy.MetaData()



