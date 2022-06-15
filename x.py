from lib2to3.pytree import convert
import pandas as pd
import sqlite3 as sql
import matplotlib.pyplot as plt

#trace a graph of the greenhouse gas during the last 30 years from the data base DB in the table country_informations for the country with the name WORLD for the attribute GHG
def generate_population(countryCode):
    try:
        conn = sql.connect('./bd/DB.db')
        request='SELECT Year,Population FROM CountryInformations WHERE countryCode = '+countryCode
        df = pd.read_sql_query(request,conn) 
        df.columns = ['Year','Population'] 
    except:
        print('Error: File "DB.db" not found')
        return 'Error: File "DB.db" not found'
    df.plot(x='Year', y='Population', kind='line')
    plt.title('Population for ')
    plt.show()
    conn.close()
    return df


generate_population("'WLD'")