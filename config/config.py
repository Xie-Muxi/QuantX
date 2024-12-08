config = {
    # Database configuration
    'databases': {
        'postgres_host': '127.0.0.1',
        'postgres_name': 'jesse_db',
        'postgres_port': 5432,
        'postgres_username': 'jesse_user',
        'postgres_password': '',
    },

    # Debug mode
    'debug_mode': True,

    # Backtesting configuration
    'backtest': {
        # Fee rate (0.001 = 0.1%)
        'fee': 0.001,
        # Slippage rate
        'slippage': 0.001,
        # Initial capital
        'initial_capital': 10000,
        # Futures leverage
        'futures_leverage': 1,
        # Execution delay (milliseconds)
        'execution_delay': 0,
    },

    # Logging configuration
    'logging': {
        'order_submission': True,
        'order_cancellation': True,
        'order_execution': True,
        'position_opened': True,
        'position_increased': True,
        'position_reduced': True,
        'position_closed': True,
        'shorter_period_candles': False,
        'trading_candles': True,
        'balance_update': True,
    },

    # Exchange configuration
    'exchanges': {
        'Binance': {
            'fee': 0.001,
            'starting_balance': 10000,
        }
    },

    # Cache configuration
    'caching': {
        'driver': 'pickle',
        'warmup_candles': 240,
    },
}