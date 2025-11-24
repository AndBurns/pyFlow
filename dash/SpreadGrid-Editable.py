# Import packages
from dash import Dash, html, dash_table
import pandas as pd

from dash_spread_grid import DashSpreadGrid

app = Dash(__name__)

app.layout = DashSpreadGrid(
  data={
    "John": {"name": "John", "age": 25, "score": 100, "registered": True, "team": "red"},
    "Alice": {"name": "Alice", "age": 24, "score": 70, "registered": False, "team": "blue"},
    "Bob": {"name": "Bob", "age": 26, "score": 35, "registered": True, "team": "blue"},
    "Charlie": {"name": "Charlie", "age": 27, "score": 60, "registered": False, "team": "red"},
    "David": {"name": "David", "age": 18, "score": 60, "registered": True, "team": "red"},
    "Eve": {"name": "Eve", "age": 29, "score": 80, "registered": False, "team": "green"},
    "Frank": {"name": "Frank", "age": 30, "score": 50, "registered": True, "team": "blue"}
  },
  columns=[{"type": "DATA-BLOCK", "width": 70}],
  formatting=[
    {
      "column": [{"id": "name"}],
      "edit": True,
    }
  ],
)

if __name__ == "__main__":
  app.run()


