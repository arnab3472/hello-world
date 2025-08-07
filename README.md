# Stockscanner

This package provides a small utility to download stock price data and
compute simple moving averages.

## Installation

```bash
pip install -e .
```

## Usage

Use the command line interface to fetch the latest closing price and a
simple moving average:

```bash
stockscanner AAPL MSFT --window 5 --period 1mo
```

Within Python you can also call the function directly:

```python
from stockscanner import moving_stock_prices

data = moving_stock_prices(["AAPL", "MSFT"], window=5)
```
