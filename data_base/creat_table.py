import sqlite3 as sq
import pandas


def insert_detail_operation(records):
    con = sq.connect("data/database.db")
    cur = con.cursor()
    print(f"Записи удалены из таблицы {cur.execute('DELETE FROM details_operation').rowcount}")
    sqlite_insert_query = """INSERT INTO details_operation
                             (id, detal_name, operation_number,
                             operation_name, machine, working_time)
                             VALUES (?, ?, ?, ?, ?, ?);"""
    cur.executemany(sqlite_insert_query, records)
    con.commit()

    print("Записи успешно вставлены в таблицу", cur.rowcount)
    con.commit()
    cur.close()


machine_time_data = pandas.read_excel('E:\Base115\MachineTime.xlsx', sheet_name='Time',
                                      usecols=['Деталь', 'номер операции', 'название операции', 'станок',
                                               'время от БТЗ', 'учет'])

df_filter = machine_time_data.dropna(subset=['учет'])

con = sq.connect("data/database.db")
cur = con.cursor()
df_filter.to_sql('details_operation', con, schema=None, if_exists='replace', index=True)
con.commit()
cur.close()