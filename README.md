# IronClaw Paper Trading Journal

Advanced paper trading and portfolio manager built for training your IronClaw agent.

## Features
- Track $20k simulated portfolio with $5k dry powder
- Log paper trades with full reasoning
- Export to CSV and Excel
- Performance metrics (win rate, P&L, drawdown)
- Easy integration with IronClaw (just paste CSV output)

## Quick Start
1. Clone the repo
2. `pip install -r requirements.txt`
3. Run `python paper_trading_journal.py`

Your IronClaw agent can now export its journal and you can analyze it here.

## How to use with IronClaw
Tell your agent:
"Export journal as CSV"
Then paste the output into this tool or import the CSV.

Created for NEAR IronClaw training.