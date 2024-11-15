from sqlmodel import Field, SQLModel, create_engine


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    age: int | None = None
    secret_name: str


db_name = "database.db"

url = f"sqlite:///{db_name}"
engine = create_engine(url, echo=True)


def create_db_and_table():
    SQLModel.metadata.create_all(engine)
