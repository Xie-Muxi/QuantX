# QuantX

A cryptocurrency quantitative trading system built on the Jesse framework.

## Project Structure

```
QuantX/
├── config/               # Configuration files
├── strategies/          # Trading strategies
├── storage/            # Data storage
├── notebooks/         # Research & Analysis
└── requirements.txt   # Dependencies
```

## Quick Start

### Environment Setup

```bash
# Create conda environment
conda create -n quantx python=3.9
conda activate quantx

# Install dependencies
pip install -r requirements.txt
```

### Basic Usage

```bash
# Backtesting
jesse backtest 2023-01-01 2024-01-01

# Live Trading
jesse live
```

## Development Status

- [x] Project structure setup
- [ ] Environment configuration
- [ ] Strategy development
- [ ] Backtesting system
- [ ] Live trading setup

## Features

- Built on Jesse framework
- Modular strategy development
- Comprehensive backtesting
- Risk management system
- Real-time market data processing

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/name`)
3. Commit changes (`git commit -m 'Add feature'`)
4. Push to branch (`git push origin feature/name`)
5. Open a Pull Request

## Risk Warning

Trading cryptocurrencies involves substantial risk of loss. Please ensure you understand the risks involved and never trade with money you cannot afford to lose.

## License

MIT License - see the LICENSE file for details

## Links

- [GitHub Repository](https://github.com/yourusername/quantx)
- [Jesse Documentation](https://docs.jesse.trade/)
```
```