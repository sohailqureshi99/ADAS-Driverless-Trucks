import pandas as pd
import numpy as np

def calc_ipm(dis,distance):
    dist_miles=distance*0.000621371
    ipm100 = dis/dist_miles * 100  
    return ipm100

# Load the data from the JSON file
data = pd.read_json('takehome.json')
disengagements=data['type'].value_counts()['disengage']
issue_18s=data[data['ticket_id'] == "ISSUE-18"]

data['distance'] = data['cruise'].apply(lambda x: x.get('distance') if isinstance(x, dict) else None)

# Drop rows where the 'distance' is not available
data = data.dropna(subset=['distance'])

# Calculate total distance
total_distance = data['distance'].sum()


ipm100=calc_ipm(disengagements,total_distance)
ipm100_for_issue18=calc_ipm(len(issue_18s),total_distance)
print("IPM-100 :",ipm100)
print("IPM-100 for ISSUE-18 :",ipm100_for_issue18)


#poisson distribution
mean_ipm100 = ipm100
std_error = np.sqrt(mean_ipm100)

# Calculating the 95% confidence interval
confidence_interval = 1.96 * std_error
lower_bound = mean_ipm100 - confidence_interval
upper_bound = mean_ipm100 + confidence_interval

print("Confidence interval:",lower_bound, upper_bound)
