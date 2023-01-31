import pandas
from data_base import sql_db


def export_pandas_from_admin_telegram(xls_file):
    data = pandas.read_excel(xls_file, sheet_name='Time',
                             usecols=['Деталь', 'номер операции', 'название операции', 'станок',
                                      'время по станку', 'время по ТП', 'расценка', 'учет'])
    df_filter = data.dropna(subset=['учет'])
    df_filter.to_sql('operation', con=sql_db.base, schema=None, if_exists='replace', index=True)


if __name__ == '__main__':
    file_excel = 'E:\Base115\data\\files\MachineTime.xlsx'
    export_pandas_from_admin_telegram(file_excel)