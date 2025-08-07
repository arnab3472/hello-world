import pandas as pd
from unittest.mock import patch

from stockscanner.scanner import moving_stock_prices


def test_moving_stock_prices_computes_sma():
    fake_df = pd.DataFrame({"Close": [1, 2, 3, 4, 5]})
    with patch("yfinance.download", return_value=fake_df):
        data = moving_stock_prices(["FAKE"], window=3, period="5d")
    df = data["FAKE"]
    expected = [2.0, 3.0, 4.0]
    assert list(df["SMA_3"].dropna()) == expected
