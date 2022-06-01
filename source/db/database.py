import sqlalchemy
import databases


SQLALCHEMY_DATABASE_URL = "postgresql://postegres:development@localhost/registra-peso-db"
# "postgresql://user:password@postgresserver/db"

database = databases.Database(SQLALCHEMY_DATABASE_URL)
metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(
    SQLALCHEMY_DATABASE_URL,
    execution_options={
        "isolation_level": "REPEATABLE READ"
    }
)


tabela_login = sqlalchemy.Table(
    "login",
    metadata,
    sqlalchemy.Column(
        pass
    )
)

tabela_medidas = sqlalchemy.Table(
    "medidas",
    metadata,
    sqlalchemy.Column(
        'id',
        sqlalchemy.Integer,
        #sqlalchemy.Identity(start=42, cycle=True)
        primary_key=True,
    ),
    sqlalchemy.Column(
        'peso',
        sqlalchemy.Integer,
        nullable=False
    )
    sqlalchemy.Column(
        'altura',
        sqlalchemy.Integer,
        nullable=True
    )
    sqlalchemy.Column(
        "pescoço",
        sqlalchemy.String,
        nullable=True,
    ),
    sqlalchemy.Column(
        "cintura",
        sqlalchemy.String,
        nullable=True,
    ),
    sqlalchemy.Column(
        "quadril",
        sqlalchemy.String,
        nullable=True,
    ),
    #sqlalchemy.Column('medidas', String)
)


metadata.create_all(engine)
