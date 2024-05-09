import pandas as pd
from pathlib import Path
from pydantic import BaseModel


class FileInput(BaseModel):
    file_path: Path

    @classmethod
    def validate_file_path(cls, value: Path) -> Path:
        if not value.exists():
            raise ValueError(f"File '{value}' does not exist.")
        if value.suffix.lower() not in {'.csv', '.xlsx'}:
            raise ValueError(f"Unsupported file format. Please provide a CSV or Excel file.")
        return value


class DemandLoader:
    def __init__(self, file_path: Path):
        validated_file_path = FileInput(file_path=file_path).file_path
        self.demand_data = self.load_demand_data(validated_file_path)

    @staticmethod
    def load_demand_data(file_path: Path) -> dict:
        demand_data = {}

        if file_path.suffix.lower() == '.csv':
            demand_df = pd.read_csv(file_path)
        else:
            demand_df = pd.read_excel(file_path)

        # Drop rows where demand is 0
        demand_df = demand_df[demand_df['demand'] != 0]

        for _, row in demand_df.iterrows():
            product_id = row['product_id']
            week_id = row['week_id']
            demand = row['demand']
            demand_data.setdefault(product_id, {})[week_id] = demand

        return demand_data


class StateLoader:
    def __init__(self, file_path: Path):
        validated_file_path = FileInput(file_path=file_path).file_path
        self.state_data = self.load_state_data(validated_file_path)

    @staticmethod
    def load_state_data(file_path: Path) -> dict:
        state_data = {}

        if file_path.suffix.lower() == '.csv':
            state_df = pd.read_csv(file_path)
        else:
            state_df = pd.read_excel(file_path)

        for _, row in state_df.iterrows():
            ms_id = row['ms_id']
            product_id = row['product_id']
            machine_id = row['machine_id']

            if machine_id not in state_data:
                state_data[machine_id] = {}

            state_data[machine_id].setdefault(ms_id, set()).add(product_id)

        return state_data


class CapacityLoader:
    def __init__(self, file_path: Path):
        validated_file_path = FileInput(file_path=file_path).file_path
        self.capacity_data = self.load_capacity_data(validated_file_path)

    @staticmethod
    def load_capacity_data(file_path: Path) -> dict:
        capacity_data = {}

        if file_path.suffix.lower() == '.csv':
            capacity_df = pd.read_csv(file_path)
        else:
            capacity_df = pd.read_excel(file_path)

        # Drop rows where capacity is 0
        capacity_df = capacity_df[capacity_df['week_cap'] != 0]

        for _, row in capacity_df.iterrows():
            machine_id = row['machine_id']
            product_id = row['product_id']
            week_cap = row['week_cap']
            capacity_data.setdefault(machine_id, {})[product_id] = week_cap
        return capacity_data


class TranstimeLoader:
    def __init__(self, file_path: Path):
        validated_file_path = FileInput(file_path=file_path).file_path
        self.transtime_data = self.load_transition_times(validated_file_path)

    @staticmethod
    def load_transition_times(file_path: Path) -> dict:
        transition_times = {}

        if file_path.suffix.lower() == '.csv':
            transition_df = pd.read_csv(file_path)
        else:
            transition_df = pd.read_excel(file_path)

        # Drop rows where transition times are 0
        transition_df = transition_df[transition_df['trans_time_days'] != 0]

        for _, row in transition_df.iterrows():
            machine_id = row['machine_id']
            from_state = row['from']
            to_state = row['to']
            trans_time_days = row['trans_time_days']

            if machine_id not in transition_times:
                transition_times[machine_id] = {}

            transition_times[machine_id].setdefault((from_state, to_state), trans_time_days)

        return transition_times


class DowntimeLoader:
    def __init__(self, file_path: Path):
        validated_file_path = FileInput(file_path=file_path).file_path
        self.downtime_data = self.load_downtime_data(validated_file_path)

    @staticmethod
    def load_downtime_data(file_path: Path) -> dict:
        downtime_data = {}

        if file_path.suffix.lower() == '.csv':
            downtime_df = pd.read_csv(file_path)
        else:
            downtime_df = pd.read_excel(file_path)

        # Drop rows where downtime is 0
        downtime_df = downtime_df[downtime_df['downtime_days'] != 0]

        for _, row in downtime_df.iterrows():
            machine_id = row['machine_id']
            week_id = row['week_id']
            downtime_days = row['downtime_days']
            downtime_data.setdefault(week_id, {})[machine_id] = downtime_days

        return downtime_data
