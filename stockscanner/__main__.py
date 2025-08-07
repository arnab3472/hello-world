"""Command line interface for the stockscanner package."""

import argparse
from .scanner import moving_stock_prices


def main() -> None:
    parser = argparse.ArgumentParser(description="Scan stock tickers and report closing prices and moving averages.")
    parser.add_argument("tickers", nargs="+", help="Ticker symbols to scan, e.g. AAPL MSFT")
    parser.add_argument("--window", type=int, default=5, help="Window for the simple moving average")
    parser.add_argument("--period", default="1mo", help="Data period to retrieve")
    args = parser.parse_args()

    data = moving_stock_prices(args.tickers, window=args.window, period=args.period)
    for ticker, df in data.items():
        last = df.iloc[-1]
        sma_col = f"SMA_{args.window}"
        print(f"{ticker}: close={last['close']:.2f}, {sma_col}={last[sma_col]:.2f}")


if __name__ == "__main__":  # pragma: no cover
    main()
