from sqlalchemy import create_engine, text

engine = create_engine("mysql_pymysql://root:12345678@localhost:3306/PYTHON", echo=True)

with engine.connect() as connection:
    result = connection.execute(text('select "Hello"'))
    print(result.all())
