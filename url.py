"""
Script to introduce the cryptocompare API
"""

def get_daily_pair_ohlcv_url(fsym: str, tsym: str, limit: int, api_key: str) -> str:
    """
    Function to contruct the url to fetch daily OHLCV data of a cryptocurrency pair from 
    cryptocompare API

    Args:
        fsym (str): The symbol of the cryptocurrency to retrieve data for (e.g., 'BTC' for Bitcoin).
        tsym (str, optional): The symbol of the currency to compare against (default is 'USD').
        limit (int, optional): The maximum number of data points to retrieve (default is 2000).
        api_key (str): The API key to use for authentication.

    Returns:
        str: The url to fetch the data from.
    """

    # TODO: contruct the url to fetch the data from cryptocompare API
    # Please follow the sequence of the url components as the function doc 
    # (fsym -> tsym -> limit -> api_key)

    return url
