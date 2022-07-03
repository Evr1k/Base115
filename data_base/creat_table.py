import datetime
import pandas
import sqlite3 as sq

base = sq.connect('db.db')
cur = base.cursor()


# def export_operation_to_db(xls_file):
#     file_to_read = openpyxl.load_workbook(xls_file, read_only=True, data_only=True)
#     sheet = file_to_read.active
#     data = []
#     for row in range(2, sheet.max_row + 1):
#         record = []
#         for col in range(1, 6):
#             value = sheet.cell(row, col).value
#             record.append(value)
#         record.append(datetime.datetime.now().strftime("%d-%m-%Y %H:%M"))
#         data.append(record)
#         print(f'app end {row}')
#
#     insert_to_base = """INSERT INTO operation VALUES (NULL, ?, ?, ?, ?, ?, ?);"""
#     print('2 - ok')
#
#     cur.executemany(insert_to_base, data)
#     print('3 - ok')
#     base.commit()


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
    df_filter.to_sql('operation', base, schema=None, if_exists='replace', index=True)
    base.commit()

file = './MachineTime.xlsx'

export_pandas(file)
