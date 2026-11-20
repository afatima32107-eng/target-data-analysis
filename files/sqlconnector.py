import pandas as pd
from sqlalchemy import create_engine
engine=create_engine(
    f"mysql+pymysql://root:fatima@localhost:3306/ecommerce"
)
list_csv=[
    ('customers','customers.csv'),
    ('geolocation','geolocation.csv'),
    ('order_items','order_items.csv'),
    ('orders','orders.csv'),
    ('payments','payments.csv'),
    ('products','products.csv'),
    ('sellers','sellers.csv')
] 
for table,file in list_csv:
    filepath=f'./Files/{file}'
    df = pd.read_csv(filepath)
    df.columns=df.columns.str.replace(" ","_")
    df.to_sql(
        name=table,
        con=engine,
        if_exists='replace',
        index=False
    )
    print(f"Imported{file} successfully into {table}")
engine.dispose()    
