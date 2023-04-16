from typing import Union

import pandas as pd

from . import config
from .rest_client import RestClient


class Client:
    def __init__(self):
        self.rest_client = RestClient()
    
    def json_response_to_dataframe(self, json_response: any, key: str):
        columns = json_response[key]['columns']
        data = json_response[key]['data']
        return pd.DataFrame(
            [{column: values[i] for i, column in enumerate(columns)} for values in data]
        )

    def get_candles(
        self,
        date_begin: str,
        date_end: str,
        interval: Union[int, str],
        engine: str = config.ENGINE,
        market: str = config.MARKET,
        board: str = config.BOARD,
        security: str = config.SECURITY,
        **kwargs,
    ):
        variables = vars()
        del variables['self']
        json_candles = self.rest_client.get_candles(**variables)
        return self.json_response_to_dataframe(json_candles, key=config.JSON_CANDLES_KEY)
