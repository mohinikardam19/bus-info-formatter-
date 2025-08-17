import pandas as pd
from tabulate import tabulate

class BusInfoFormatter:
    def _init_(self, data):
        self.df = pd.DataFrame(data)
    def clean_data(self):
        # Format route codes
        self.df['route'] = self.df['route'].str.upper().str.strip()
        
        # Format stop names
        self.df['start'] = self.df['start'].str.title().str.strip()
        self.df['end'] = self.df['end'].str.title().str.strip()
        
        # Format times
        self.df['time'] = pd.to_datetime(self.df['time'], errors='coerce').dt.strftime('%H:%M')
    
    def display_table(self):
        print(tabulate(self.df, headers='keys', tablefmt='pretty'))
    
    def export(self, filename, format_type="csv"):
        if format_type == "csv":
            self.df.to_csv(filename, index=False)
        elif format_type == "json":
            self.df.to_json(filename, orient="records", indent=4)
        print(f"Data exported to {filename}")

# Example usage
raw_data = [
    {"route": "15a", "start": "main st.", "end": "central park", "time": "08:30"},
    {"route": "15a", "start": "main st.", "end": "central park", "time": "14:15"},
    {"route": "7B", "start": "airport", "end": "downtown", "time": "09:00"}
]

tool = BusInfoFormatter(raw_data)
tool.clean_data()
tool.display_table()
tool.export("bus_schedule.csv", "csv")