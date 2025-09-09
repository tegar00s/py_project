import pandas as pd
import sqlalchemy
from urllib.parse import quote_plus

username = "root"
password = quote_plus("P@ssw0rd")
engine = sqlalchemy.create_engine(f"mysql+pymysql://{username}:{password}@localhost:3306/db_dummy")

query = "SELECT * FROM users"
df = pd.read_sql(query,engine)

print(df.head())

df.to_csv("data_dummy.csv",index=False,encoding='utf-8')