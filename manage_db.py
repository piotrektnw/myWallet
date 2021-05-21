import sqlite3

db_connect = sqlite3.connect('db.db')
connection = db_connect.cursor()



def create_table():
    connection.execute('''CREATE TABLE IF NOT EXISTS account (
        id integer PRIMARY KEY,
        category text,
        name text,
        amount_spend integer,
        amount_income integer,
        added text
        )
        '''
)


def save_to_db(category, name, amount, added, current_func):
    if current_func == 'count_expenses':
        connection.execute('INSERT INTO account (category, name, amount_spend, added) VALUES (?,?,?,?)'
                        ,  (category, name, amount, added))
    else:
        connection.execute('INSERT INTO account (category, name, amount_income, added) VALUES (?,?,?,?)'
                           , (category, name, amount, added))
    db_connect.commit()



