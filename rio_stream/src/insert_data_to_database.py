from pangres import upsert
import numpy as np
import pandas as pd


def remove_x_from_id_columns(dataframe):
    column_with_id = [k for k in list(dataframe.columns) if 'id' in k]
    for column in column_with_id:
        dataframe[column] = dataframe[column].replace({'x': ''}, regex=True)


def insert_data(dataframe,
                engine):
    # users table
    users_table = dataframe[['user_id', 'screen_name', 'name', 'location', 'description', 'url',
                             'account_created_at', 'profile_url', 'followers_count', 'friends_count',
                             'listed_count', 'statuses_count', 'favourites_count', 'verified']]

    users_table = users_table[users_table['user_id'].notna()]
    users_table.drop_duplicates(subset=['user_id'], inplace=True, ignore_index=True)
    users_table.set_index('user_id', inplace=True)
    upsert(engine=engine,
           df=users_table,
           table_name='users',
           if_row_exists='update')
    print("---------------users_table was written in the database---------")

    # Tweets table
    tweets_table = dataframe[
        ['status_id', 'user_id', 'status_url', 'created_at', 'text', 'source', 'is_quote', 'is_retweet',
         'favorite_count',
         'retweet_count',
         'hashtags', 'urls_url', 'lang']]

    tweets_table = tweets_table[tweets_table['status_id'].notna()]
    pd.to_datetime(tweets_table['created_at'])
    tweets_table.drop_duplicates(subset=['status_id'], inplace=True, ignore_index=True)
    tweets_table.set_index('status_id', inplace=True)
    upsert(engine=engine,
           df=tweets_table,
           table_name='tweets',
           if_row_exists='update')

    print("---------------tweets_table was written in the database---------")

    # quotes_table
    quotes_table = dataframe[
        ['quoted_status_id', 'status_id', 'quoted_text', 'quoted_created_at', 'quoted_source',
         'quoted_favorite_count', 'quoted_retweet_count', 'quoted_user_id', 'quoted_screen_name',
         'quoted_name', 'quoted_followers_count', 'quoted_friends_count', 'quoted_statuses_count',
         'quoted_location', 'quoted_description', 'quoted_verified']]

    quotes_table = quotes_table[quotes_table['quoted_status_id'].notna()]
    quotes_table.drop_duplicates(subset=['quoted_status_id'], inplace=True, ignore_index=True)
    quotes_table.set_index('quoted_status_id', inplace=True)
    upsert(engine=engine, df=quotes_table, table_name='quotes', if_row_exists='update')
    print("---------------quotes_table was written in the database---------")

    # retweets_table
    retweets_table = dataframe[
        ['retweet_status_id', 'status_id', 'retweet_text', 'retweet_created_at', 'retweet_source',
         'retweet_favorite_count', 'retweet_retweet_count', 'retweet_user_id', 'retweet_screen_name',
         'retweet_followers_count', 'retweet_friends_count', 'retweet_statuses_count', 'retweet_location',
         'retweet_name', 'retweet_description', 'retweet_verified']]

    retweets_table = retweets_table[retweets_table['retweet_status_id'].notna()]
    retweets_table.drop_duplicates(subset=['retweet_status_id'], inplace=True, ignore_index=True)
    retweets_table.set_index('retweet_status_id', inplace=True)
    upsert(engine=engine, df=retweets_table, table_name='retweets', if_row_exists='update')
    print("---------------retweets_table was written in the database---------")

    # media_table
    media_table = dataframe[['media_url', 'status_id', 'media_type']]
    media_table = media_table.dropna(subset=['media_url', 'media_type'])
    media_table.to_sql('media', engine, if_exists='append', index=False, chunksize=100)
    print("---------------media_table was written in the database---------")

    # places_table
    places_table = dataframe[['status_id', 'place_url', 'place_name', 'place_full_name',
                              'place_type', 'country', 'country_code']]
    places_table = places_table.dropna(subset=['place_url', 'place_name'])
    places_table.to_sql('places', engine, if_exists='append', index=False, chunksize=100)
    print("---------------places_table was written in the database---------")

    # replies table
    replies_table = dataframe[['status_id', 'reply_to_status_id', 'reply_to_user_id', 'reply_to_screen_name']]
    replies_table = replies_table.dropna(subset=['reply_to_status_id', 'reply_to_user_id'])
    replies_table = replies_table[replies_table.status_id != 0]
    replies_table.to_sql('replies', engine, if_exists='append', index=False, chunksize=100)
    print("---------------replies table was written in the database---------")

    # mentions table
    mentions_user_table = dataframe[['mentions_user_id', 'status_id', 'mentions_screen_name']]
    mentions_user_table = mentions_user_table[mentions_user_table['mentions_user_id'].notna()]
    mentions_user_table.to_sql('mentions_users', engine, if_exists='append', index=False, chunksize=100)
    print("---------------mentions table was written in the database---------")
