import pandas as pd
from datetime import datetime
import os

class PaperTradingJournal:
    def __init__(self, starting_capital=20000, dry_powder=5000):
        self.starting_capital = starting_capital
        self.dry_powder = dry_powder
        self.cash = starting_capital - dry_powder
        self.positions = {}
        self.trades = []
        self.portfolio_value = starting_capital

    def log_trade(self, asset, direction, entry, exit_price, size, notes="", source="IronClaw"):
        pnl = (exit_price - entry) * size if direction.lower() == "long" else (entry - exit_price) * size
        trade = {
            "Date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "Asset": asset,
            "Direction": direction,
            "Entry": entry,
            "Exit": exit_price,
            "Size": size,
            "PNL": round(pnl, 2),
            "Notes": notes,
            "Source": source
        }
        self.trades.append(trade)
        if direction.lower() == "long":
            self.cash -= size * entry
        print(f"Trade logged: {direction} {size} {asset} @ {entry} -> PNL: ${pnl:.2f}")

    def get_portfolio_summary(self):
        total_pnl = sum(t["PNL"] for t in self.trades)
        win_rate = len([t for t in self.trades if t["PNL"] > 0]) / len(self.trades) * 100 if self.trades else 0
        return {
            "Total Capital": self.starting_capital,
            "Current Cash": round(self.cash, 2),
            "Dry Powder": self.dry_powder,
            "Total P&L": round(total_pnl, 2),
            "Win Rate %": round(win_rate, 1),
            "Total Trades": len(self.trades)
        }

    def export_to_csv(self, filename="trades.csv"):
        if not self.trades:
            print("No trades to export.")
            return
        df = pd.DataFrame(self.trades)
        df.to_csv(filename, index=False)
        print(f"Exported to {filename}")

    def export_to_excel(self, filename="trades.xlsx"):
        if not self.trades:
            print("No trades to export.")
            return
        df = pd.DataFrame(self.trades)
        df.to_excel(filename, index=False, engine="openpyxl")
        print(f"Exported to {filename}")

    def import_from_ironclaw_csv(self, filepath):
        df = pd.read_csv(filepath)
        self.trades.extend(df.to_dict("records"))
        print(f"Imported {len(df)} trades from IronClaw")

if __name__ == "__main__":
    journal = PaperTradingJournal()
    print("IronClaw Paper Trading Journal ready!")
    print("Use journal.log_trade(...) or import from your agent.")