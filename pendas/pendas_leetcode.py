import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    # Pivot the DataFrame so each (machine_id, process_id) pair has its start and end times
    pivot_df = activity.pivot(index=['machine_id', 'process_id'], 
                              columns='activity_type', 
                              values='timestamp').reset_index()
    
    # Calculate the processing time for each process
    pivot_df['processing_time'] = pivot_df['end'] - pivot_df['start']
    
    # Compute the average processing time per machine
    avg_time = pivot_df.groupby('machine_id', as_index=False)['processing_time'].mean()
    
    # Round the average processing time to 3 decimal places
    avg_time['processing_time'] = avg_time['processing_time'].round(3)
    
    return avg_time

# Example usage:
data = [
    [0, 0, 'start', 0.712], [0, 0, 'end', 1.52],
    [0, 1, 'start', 3.14], [0, 1, 'end', 4.12],
    [1, 0, 'start', 0.55], [1, 0, 'end', 1.55],
    [1, 1, 'start', 0.43], [1, 1, 'end', 1.42],
    [2, 0, 'start', 4.1], [2, 0, 'end', 4.512],
    [2, 1, 'start', 2.5], [2, 1, 'end', 5]
]
activity = pd.DataFrame(data, columns=['machine_id', 'process_id', 'activity_type', 'timestamp'])
activity = activity.astype({'machine_id':'Int64', 'process_id':'Int64', 'activity_type':'object', 'timestamp':'Float64'})

result = get_average_time(activity)
print(result)
