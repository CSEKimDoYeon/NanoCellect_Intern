import sqlalchemy
from sqlalchemy import create_engine
import pandas as pd

#import plotly.express as px
#plotly 아직 쓸 필요 없음.

def extract_Underfifty(engine) :
    connection = engine.connect() # 데이터베이스 연결
    df = pd.read_sql_query("select company, count(*) from \"demo\" where \"A\"<50 and \"B\"<50 and \"C\"<50 group by company", engine)
    #print(df)

    connection.close() # 수행 후 데이터베이스 연결 종료
    return df



engine = create_engine('postgresql+psycopg2://postgres:rnsan-4226@localhost/postgres')
connection = engine.connect()
result = connection.execute("select * from demo")


df_base = pd.read_sql("select * from demo", connection)


connection.close()
extract_Underfifty(engine)


