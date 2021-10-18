from typing import Any
from typing import Dict

import pandas as pd
import psycopg2

from .data_source import DataSource


class DBSource(DataSource):
    def __init__(self, name: str, config: Dict[str, Any]):
        super().__init__(name)

        try:
            url = config['url']
            port = config['port']
            database = config['database']
            user = config['user']
            password = config['password']

            self.connection = psycopg2.connect(
                host=url,
                port=port,
                database=database,
                user=user,
                password=password
            )

            self.features_query = config['query']['features']
            self.target_query = config['query']['target']
        except KeyError as ke:
            print(f"Failed to create a new DB connection: {ke}")

    def fetch_features(self) -> Any:
        with self.connection.cursor() as cursor:
            cursor.execute(self.features_query)
            column_names = [desc[0] for desc in cursor.description]
            tuples = cursor.fetchall()
            return pd.DataFrame(tuples, columns=column_names)

    def fetch_target(self) -> Any:
        with self.connection.cursor() as cursor:
            cursor.execute(self.target_query)
            tuples = cursor.fetchall()
            return [t[0] for t in tuples]

    def shutdown(self) -> None:
        print(f"Shutting down {self.name()} DB source")
        if self.connection is not None:
            self.connection.close()
