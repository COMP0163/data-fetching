"""
Pytest test cases for the URL construction function.
"""
from url import get_daily_pair_ohlcv_url


def test_url_construction_correctness():
    """
    Test to check if the URL is constructed correctly with valid inputs.
    """
    fsym = "BTC"
    tsym = "USD"
    limit = 2000
    api_key = "mock_api_key"

    url = get_daily_pair_ohlcv_url(fsym, tsym, limit, api_key)

    expected_url = "https://min-api.cryptocompare.com/data/v2/histoday?\
fsym=BTC&tsym=USD&limit=2000&allData=true&api_key=mock_api_key"

    assert url == expected_url, "URL construction failed."