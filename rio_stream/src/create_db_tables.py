from sqlalchemy import create_engine
import pandas as pd
import json
import glob


def create_tables(engine):
    """Function creates all needed table in the database.
    @type engine: object
    """

    engine.execute('''

                                            CREATE TABLE users (
                                            user_id text PRIMARY KEY,
                                            screen_name text,
                                            name text,
                                            location text,
                                            description text,
                                            url text,
                                            account_created_at date,
                                            profile_url text,
                                            followers_count bigint,
                                            friends_count bigint,
                                            listed_count bigint,
                                            favourites_count bigint,
                                            statuses_count bigint,
                                            verified boolean)
    ''')

    engine.execute('''

                                                CREATE TABLE tweets (
                                                status_id text NOT NULL PRIMARY KEY,
                                                user_id text,
                                                reply_to_status_id text,
                                                mention_id text,
                                                status_url text,
                                                created_at date,
                                                text text,
                                                source text,
                                                is_quote boolean,
                                                is_retweet boolean,
                                                favorite_count bigint,
                                                retweet_count bigint,
                                                hashtags text,
                                                urls_url text,
                                                lang varchar(255),
                                                FOREIGN KEY (user_id)
                                                    REFERENCES users (user_id)

        )''')

    engine.execute('''

                                                CREATE TABLE retweets (
                                                retweet_status_id text PRIMARY KEY NOT NULL,
                                                status_id text,
                                                retweet_text text,
                                                retweet_created_at date,
                                                retweet_source text,
                                                retweet_favorite_count bigint,
                                                retweet_retweet_count bigint,
                                                retweet_user_id text,
                                                retweet_screen_name text,
                                                retweet_name text,
                                                retweet_followers_count bigint,
                                                retweet_friends_count bigint,
                                                retweet_statuses_count bigint,
                                                retweet_location text,
                                                retweet_description text,
                                                retweet_verified boolean,
                                                 FOREIGN KEY (status_id)
                                                    REFERENCES tweets (status_id))
                                                ''')

    engine.execute('''

                                        CREATE TABLE mentions_users (
                                        mention_id serial PRIMARY KEY NOT NULL,
                                        status_id text,
                                        mentions_user_id text,
                                        mentions_screen_name text,
                                        FOREIGN KEY (status_id)
                                                    REFERENCES tweets (status_id))
''')

    engine.execute('''

                                                    CREATE TABLE replies (
                                                    reply_id serial PRIMARY KEY NOT NULL, 
                                                    reply_to_status_id text,
                                                    status_id text,
                                                    reply_to_user_id text,
                                                    reply_to_screen_name text,
                                                    FOREIGN KEY (status_id)
                                                        REFERENCES tweets (status_id))
    ''')

    engine.execute('''

                                                CREATE TABLE quotes (
                                                quoted_status_id text PRIMARY KEY NOT NULL,
                                                status_id text,
                                                quoted_text text,
                                                quoted_source text,
                                                quoted_created_at date,
                                                quoted_favorite_count bigint,
                                                quoted_retweet_count bigint,
                                                quoted_user_id text,
                                                quoted_screen_name text,
                                                quoted_name text,
                                                quoted_followers_count bigint,
                                                quoted_friends_count bigint,
                                                quoted_statuses_count bigint,
                                                quoted_location text,
                                                quoted_description text,
                                                quoted_verified boolean,
                                                FOREIGN KEY (status_id)
                                                    REFERENCES tweets (status_id))
''')

    engine.execute('''

                                                CREATE TABLE media (
                                                media_id serial PRIMARY KEY NOT NULL,
                                                status_id text,
                                                media_url text,
                                                media_type varchar(100),
                                                FOREIGN KEY (status_id)
                                                    REFERENCES tweets (status_id))
''')

    engine.execute('''

                                        CREATE TABLE places (
                                        place_id serial PRIMARY KEY NOT NULL,
                                        status_id text,
                                        place_url text,
                                        place_name text,
                                        place_full_name text,
                                        place_type text,
                                        country text,
                                        country_code varchar(255),
                                        FOREIGN KEY (status_id)
                                                    REFERENCES tweets (status_id))
''')
