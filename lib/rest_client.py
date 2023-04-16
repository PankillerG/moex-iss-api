from typing import Union
import urllib

import requests

from . import config


class RestClient:
    def __init__(self):
        pass
    
    def get_url(self, path: str, **kwargs):
        params = urllib.parse.urlencode(kwargs)
        return config.DEFAULT_REQUEST_TEMPLATE.format(path=path, params=params)

    def add_query_params_to_url(self, url: str, query_params: dict = None):
        query_params = {
            param: value if isinstance(value, list) else [value] for param, value in query_params.items()
        }
        url_parts = urllib.parse.urlparse(url)
        query_params_dict = urllib.parse.parse_qs(url_parts.query)
        query_params_dict.update(query_params)
        url_parts = url_parts._replace(query=urllib.parse.urlencode(query_params_dict, doseq=True))
        return urllib.parse.urlunparse(url_parts, )

    def get_response_portion(self, url: str, start: int = 0):
        updated_url = self.add_query_params_to_url(url, {'start': start})
        return requests.get(updated_url).json()

    def get_full_response(self, url: str):
        full_json_respone = None
        start = 0
        key = config.JSON_CANDLES_KEY
        while json_portion:= self.get_response_portion(url, start):
            if full_json_respone is None:
                full_json_respone = json_portion
            else:
                full_json_respone[key]['data'] += json_portion[key]['data']
            data_size = len(json_portion[key]['data'])
            start += data_size
            if data_size == 0:
                break
        return full_json_respone

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
        kwargs.update({
            'from': date_begin,
            'till': date_end,
            'interval': interval,
        })
        url = self.get_url(
            path=config.CANDLES_PATH.format(
                engine=engine,
                market=market,
                board=board,
                security=security,
            ),
            **kwargs,
        )
        return self.get_full_response(url)
