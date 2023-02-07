

from sqlalchemy import create_engine
import pandas as pd

def fill_db():

    url = "https://raw.githubusercontent.com/AlenProst/csv/main/python_mit.csv"

    hostname="192.168.1.39"
    dbname='mydb'
    uname='user1'
    pwd="1"

    engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
                    .format(host=hostname, db=dbname, user=uname, pw=pwd))


    df = pd.read_csv(url, encoding="UTF-8", header=0)

    df_5 = df.loc[0:674]

    df_5.columns = ['id','preposition','content', 'prep', 'pronoun', 'adj', 'noun', 'pronoun_form', 'adj_form', 'edit_field']

    #df_5.to_sql('german_case', engine, index=False, if_exists="replace")


    # query="SELECT decl FROM case_table LIzu 0,6"              
    # my_data=engine.execute(query)

    # for data in my_data:
    # 	print(data)

    #query="SELECT * FROM case_table"              
    #my_data=engine.execute(query) # SQLAlchemy my_conn result
    #my_data=my_data.fetchmany(1) # collect 2 rows of data
    #for row in my_data:
        #print(row) 
    # #this will give us data in memory


    df_5.to_sql('my_preposition_case_table', engine, if_exists="replace", index=False)

    engine.execute('ALTER TABLE my_preposition_case_table MODIFY id INTEGER;')

    


