import datetime
import pandas
from data_base import sql_db


def export_pandas(xls_file):

    machine_time_data = pandas.read_excel(xls_file, sheet_name='Time',
                                          usecols=['Деталь', 'номер операции', 'название операции', 'станок',
                                                   'время от БТЗ', 'учет'])
    df_filter = machine_time_data.dropna(subset=['учет'])
    df_filter.to_sql('details_operation', con=sql_db.base, schema=None, if_exists='replace', index=True)
    #sql_db.base.commit()

#file = './MachineTime.xlsx'

#export_pandas(file)
