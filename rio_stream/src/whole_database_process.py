
from sqlalchemy import create_engine
import pandas as pd

import create_db_tables as ct
import insert_data_to_database as idd
from config import config


engine = create_engine(f'postgresql://{config.REMOTE_USERNAME}:{config.PASSWORD}@\
{config.REMOTE_IP_ADDRESS}/{config.DATABASE_NAME_S}')


data_path = '/media/datalab1/Data1/serenay/rio_project/rio_stream/data/merged_all_parsed3.csv'

ct.create_tables(engine)

df = pd.read_csv(data_path, lineterminator='\n')
idd.remove_x_from_id_columns(df)
idd.insert_data(df, engine)


