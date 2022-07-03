import sqlite3 as sq
from loader import base, cur
import datetime, pandas


def export_pandas(xls_file):
    print(f"Записи удалены из таблицы {cur.execute('DELETE FROM operation').rowcount}")
    time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
    sqlite_insert_query = """INSERT INTO operation
                                 (op_id, detail, op_number,
                                 op_name, machine, op_time, update_date)
                                 VALUES (NULL, ?, ?, ?, ?, ?, time);"""
    machine_time_data = pandas.read_excel(xls_file, sheet_name='Time',
                                          usecols=['Деталь', 'номер операции', 'название операции', 'станок',
                                                   'время от БТЗ', 'учет'])
    df_filter = machine_time_data.dropna(subset=['учет'])
    df_filter.to_sql('details_operation', base, schema=None, if_exists='replace', index=True)
    base.commit()

#file = './MachineTime.xlsx'

#export_pandas(file)
