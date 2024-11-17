from sqlmodel import Field, SQLModel, create_engine, Session


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    age: int | None = None
    secret_name: str


db_name = "database.db"

url = f"sqlite:///{db_name}"
engine = create_engine(url)


def create_db_and_table():
    SQLModel.metadata.create_all(engine)


def hero_insert():
    hero_1 = Hero(name="deadpool", secret_name="dead")
    hero_2 = Hero(name="wolverine", secret_name="wolf", age=54)
    hero_3 = Hero(name="hulk", secret_name="disaster", age=55)

    with Session(engine) as session:
        session.add(hero_1)
        session.add(hero_3)
        session.add(hero_2)
        session.commit()

        print("values after commiting")
        print("Hero 1", hero_1)

        print("attributes after commiting changes")
        print("Hero1_name", hero_1.name)

        print("pring id of heros")
        print("Hero1_id", hero_1.id)


def main():
    create_db_and_table()
    hero_insert()


if __name__ == "__main__":
    main()
