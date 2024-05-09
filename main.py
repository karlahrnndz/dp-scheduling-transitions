from data_loader import DemandLoader, CapacityLoader, TranstimeLoader, DowntimeLoader, StateLoader
from pathlib import Path

# Example usage for loading demand data
demand_loader = DemandLoader(file_path=Path("input/demand.xlsx"))
print(demand_loader.demand_data)

# Example usage for loading capacity data
capacity_loader = CapacityLoader(file_path=Path("input/capacity.xlsx"))
print(capacity_loader.capacity_data)

# Example usage for loading transition times data
transtime_loader = TranstimeLoader(file_path=Path("input/transition_times.xlsx"))
print(transtime_loader.transtime_data)

# Example usage for loading scheduled downtime data
downtime_loader = DowntimeLoader(file_path=Path("input/scheduled_downtime.xlsx"))
print(downtime_loader.downtime_data)

# Example usage for loading state definition data
sate_loader = StateLoader(file_path=Path("input/state_def.xlsx"))
print(sate_loader.state_data)
