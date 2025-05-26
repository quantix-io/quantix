"""Basic tests to ensure the package works."""

from datetime import date

import quantix as qx


def test_import():
    """Test that the package can be imported."""
    assert qx.__version__ == "0.1.0"


def test_strategy_decorator():
    """Test the strategy decorator."""

    @qx.strategy
    def test_strategy(bar):
        return qx.hold()

    assert hasattr(test_strategy, "_is_strategy")
    assert test_strategy._is_strategy is True


def test_signals():
    """Test trading signals."""
    buy_signal = qx.buy()
    assert buy_signal["action"] == "buy"
    assert buy_signal["size"] == 1.0

    sell_signal = qx.sell(size=0.5)
    assert sell_signal["action"] == "sell"
    assert sell_signal["size"] == 0.5

    hold_signal = qx.hold()
    assert hold_signal["action"] == "hold"


def test_load_placeholder():
    """Test data loading (placeholder)."""
    data = qx.load("AAPL", start=date(2020, 1, 1))
    assert "AAPL" in data["symbols"]
    assert data["start"] == date(2020, 1, 1)


def test_backtest_placeholder():
    """Test backtesting (placeholder)."""

    @qx.strategy
    def dummy_strategy(bar):
        return qx.hold()

    data = qx.load("AAPL")
    result = qx.backtest(data, dummy_strategy)

    assert hasattr(result, "total_return")
    assert hasattr(result, "sharpe_ratio")
    assert hasattr(result, "plot")
