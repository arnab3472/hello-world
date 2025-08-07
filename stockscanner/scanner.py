"""Utilities to scan stock prices and compute moving averages."""

from typing import Iterable, Dict
import pandas as pd
import yfinance as yf


def moving_stock_prices(tickers: Iterable[str], window: int = 5, period: str = "1mo") -> Dict[str, pd.DataFrame]:
    """Fetch closing prices for ``tickers`` and compute simple moving averages.

    Parameters
    ----------
    tickers:
        Iterable of stock ticker symbols (e.g. ``["AAPL", "MSFT"]``).
    window:
        Window size for the simple moving average.
    period:
        Data period passed to :func:`yfinance.download` (e.g. ``"1mo"``).

    Returns
    -------
    Dict[str, pd.DataFrame]
        A mapping from ticker symbol to a DataFrame containing the closing
        price and the computed simple moving average.
    """
    results: Dict[str, pd.DataFrame] = {}
    for ticker in tickers:
        data = yf.download(ticker, period=period, progress=False)
        close = data["Close"].dropna()
        sma = close.rolling(window=window).mean()
        results[ticker] = pd.DataFrame({"close": close, f"SMA_{window}": sma})
    return results
