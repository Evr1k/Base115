import pandas
import sqlite3 as sq

base = sq.connect('database.db')
cur = base.cursor()

file_excel = 'E:\Base115\data\\files\MachineTime.xlsx'


def export_pandas(xls_file):
    machine_time_data = pandas.read_excel(xls_file, sheet_name='Time',
                                          usecols=['Деталь', 'номер операции', 'название операции', 'станок',
                                                   'время по станку', 'время по ТП', 'расценка', 'учет'])
    df_filter = machine_time_data.dropna(subset=['учет'])
    df_filter.to_sql('operation', base, schema=None, if_exists='replace', index=True)
    base.commit()


def select_answer():
    answer_bd = (str(i).split(".", 1)[0] for i in cur.execute('''SELECT DISTINCT Деталь 
                                                                FROM operation 
                                                                ORDER BY Деталь''').fetchall())
    for ret in set(answer_bd):
        det = cur.execute('''SELECT DISTINCT Деталь 
                            FROM operation 
                            WHERE Деталь LIKE ?
                            ORDER BY Деталь''', (ret[2:] + "%",)).fetchall()
        break


if __name__ == '__main__':
    select_answer()



