import os, glob
import pandas as pd

# Combines all parsed csv files into one csv file to insert the data to the database

path = "/media/datalab1/Data1/serenay/rio_tweets_using_R/data/rio_parsed_csvs2"

all_files = glob.glob(os.path.join(path, "*.csv"))
df_from_each_file = [pd.read_csv(f, lineterminator="\n") for f in all_files]
df_merged = pd.concat(df_from_each_file, ignore_index=True)
df_merged.to_csv("/media/datalab1/Data1/serenay/rio_project/rio_stream/data/merged_all_parsed2.csv")
