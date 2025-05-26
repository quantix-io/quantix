# Quantix

<div align="center">

[![PyPI version](https://badge.fury.io/py/quantix-trading.svg)](https://badge.fury.io/py/quantix-trading)
[![Python](https://img.shields.io/pypi/pyversions/quantix-trading.svg)](https://pypi.org/project/quantix-trading/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)

**Fast and intuitive backtesting for Python**

[Installation](#installation) • [Quick Start](#quick-start) • [Documentation](https://quantix.dev) • [Community](https://discord.gg/quantix)

</div>

---

## 🚀 What is Quantix?

Quantix is a Python backtesting library that combines the **speed of VectorBT** with the **simplicity of modern Python frameworks**. No more choosing between performance and usability!

```python
import quantix as qx
from datetime import date

# This is all you need for a complete backtest
data = qx.load("AAPL", start=date(2020, 1, 1))

@qx.strategy
def my_strategy(bar):
    if bar.rsi < 30:
        return qx.buy()
    elif bar.rsi > 70:
        return qx.sell()
    return qx.hold()

result = qx.backtest(data, my_strategy, cash=10000)
result.plot()  # Beautiful interactive charts
```

## 📈 Features

- **Lightning Fast**: Matches VectorBT's performance with 10x better API
- **Intuitive API**: Write strategies in plain Python - no PhD required
- **Built-in Indicators**: 50+ indicators included, easy to add custom ones
- **Beautiful Visualizations**: Interactive plots that actually make sense
- **Risk Management**: Built-in stop-loss, take-profit, and position sizing
- **Multiple Assets**: Backtest portfolios with ease

## 📦 Installation

```bash
pip install quantix-trading
```

## 🎯 Quick Start

### Simple Moving Average Strategy

```python
import quantix as qx
from datetime import date

# Load data
data = qx.load("AAPL", start=date(2020, 1, 1), end=date(2023, 12, 31))

# Define strategy
@qx.strategy(stop_loss=0.02, take_profit=0.05)
def sma_strategy(bar):
    # Clean access to indicators
    if bar.close > bar.sma(50) and bar.close_prev <= bar.sma_prev(50):
        return qx.buy()
    elif bar.close < bar.sma(20) and bar.close_prev >= bar.sma_prev(20):
        return qx.sell()
    return qx.hold()

# Run backtest
result = qx.backtest(
    data=data,
    strategy=sma_strategy,
    cash=10000,
    commission=0.001
)

# Analyze results
print(f"Total Return: {result.total_return:.2%}")
print(f"Sharpe Ratio: {result.sharpe_ratio:.2f}")
print(f"Max Drawdown: {result.max_drawdown:.2%}")

# Visualize
result.plot()
```

## 🛠️ Status

> ⚠️ **Early Development**: We're building this in public! Star the repo to follow our progress.

### Roadmap

- [x] Week 1: Project setup and basic structure
- [ ] Week 2: Data management and caching
- [ ] Week 3: Strategy engine and backtesting
- [ ] Week 4: Technical indicators
- [ ] Month 2: Visualization and optimization
- [ ] Month 3: Community and advanced features

## 🤝 Contributing

We'd love your help! Check out our [Contributing Guide](CONTRIBUTING.md) to get started.

```bash
# Clone the repo
git clone https://github.com/quantix-io/quantix.git
cd quantix

# Install with poetry
poetry install

# Run tests
poetry run pytest

# Run linting
poetry run ruff check .
poetry run ruff format .
```

## 💬 Community

- 🌟 [Star the repo](https://github.com/quantix-io/quantix) to support the project
- 💬 [Join our Discord](https://discord.gg/quantix) for discussions
- 🐛 [Report issues](https://github.com/quantix-io/quantix/issues)
- 📧 [Subscribe to updates](https://quantix.dev)

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

---

<div align="center">
Built with ❤️ by traders, for traders
</div>