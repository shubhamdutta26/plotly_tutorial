import pandas as pd
import random
from datetime import datetime, timedelta

# Set a seed for reproducibility
random.seed(42)

# Generate sample scooter sharing data
num_entries = 100

data = []
start_time = datetime(2023, 10, 1, 6, 0, 0)

for i in range(num_entries):
    trip_id = f"T{i+1:04d}"
    scooter_id = f"SCOOT{random.randint(100, 199)}"
    user_id = f"USER{random.randint(1000, 1999)}"
    
    trip_start = start_time + timedelta(minutes=random.randint(0, 10000))
    trip_duration = timedelta(minutes=random.randint(5, 60))
    trip_end = trip_start + trip_duration
    
    start_location = f"Zone {random.randint(1, 5)}"
    end_location = f"Zone {random.randint(1, 5)}"
    distance_km = round(random.uniform(0.5, 5.0), 2)
    
    data.append({
        "trip_id": trip_id,
        "scooter_id": scooter_id,
        "user_id": user_id,
        "start_time": trip_start.strftime("%Y-%m-%d %H:%M:%S"),
        "end_time": trip_end.strftime("%Y-%m-%d %H:%M:%S"),
        "start_location": start_location,
        "end_location": end_location,
        "distance_km": distance_km
    })

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
csv_filename = "scooter_sharing_data.csv"
df.to_csv(csv_filename, index=False)

print(f"Dataset saved as {csv_filename}")

from PIL import Image
import numpy as np

# Load the image and ensure it's in RGB format
img = Image.open("logo/dsfe_256.png").convert("RGB")
arr = np.array(img)  # Shape: (height, width, 3), dtype typically uint8

# Save as .npy
np.save("humpy_logo_rgb.npy", arr)

