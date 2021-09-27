import psycopg2
from typing import Any
from typing import Dict

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
            self.cursor = self.connection.cursor()

            self.features_query = config['query']['features']
            self.target_query = config['query']['target']
        except KeyError as ke:
            print(f"Failed to create a new DB connection: {ke}")

    def fetch_features(self) -> Any:
        self.cursor.execute(self.features_query)
        return self.cursor.fetchall()

    def fetch_target(self) -> Any:
        self.cursor.execute(self.target_query)
        return self.cursor.fetchall()

    def shutdown(self) -> None:
        print(f"Shutting down {self.name()} DB source")
        if self.cursor is not None:
            self.cursor.close()
        if self.connection is not None:
            self.connection.close()