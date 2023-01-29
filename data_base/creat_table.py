import pandas
import sqlite3 as sq

base = sq.connect('database.db')
cur = base.cursor()


def export_pandas(xls_file):
    machine_time_data = pandas.read_excel(xls_file, sheet_name='Time',
                                          usecols=['Деталь', 'номер операции', 'название операции', 'станок',
                                                   'время по станку', 'время по ТП', 'расценка', 'учет'])
    df_filter = machine_time_data.dropna(subset=['учет'])
    df_filter.to_sql('operation', base, schema=None, if_exists='replace', index=True)
    base.commit()


file = 'E:\Base115\data\\files\MachineTime.xlsx'

export_pandas(file)
