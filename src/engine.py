import pandas as pd
from ortools.sat.python import cp_model

class RailwayEngine:
    def __init__(self, timetable_path):
        self.df = pd.read_csv(timetable_path)

    def detect_conflicts(self, block_id):
        """Finds trains that overlap in the same track block."""
        conflicts = []
        # Sort by entry time to compare adjacent trains
        sorted_trains = self.df.sort_values('entry_time')
        
        for i in range(len(sorted_trains) - 1):
            t1 = sorted_trains.iloc[i]
            t2 = sorted_trains.iloc[i+1]
            
            # Simple check: Does Train 2 enter before Train 1 leaves?
            if t2['entry_time'] < t1['target_exit_time']:
                conflicts.append((t1['train_no'], t2['train_no']))
        
        return conflicts

    def solve_precedence(self, train_a, train_b):
        """Uses Google OR-Tools to decide who waits."""
        model = cp_model.CpModel()
        
        # Priority-based logic: High priority (Rank 1) gets a 'bonus'
        # In a full project, you'd use CP-SAT solver variables here
        if train_a['priority'] < train_b['priority']:
            return f"Action: Hold {train_b['train_no']}, Pass {train_a['train_no']}"
        else:
            return f"Action: Hold {train_a['train_no']}, Pass {train_b['train_no']}"

# Example Usage:
# engine = RailwayEngine('data/timetable.csv')
# print(engine.detect_conflicts('Block_S1'))
