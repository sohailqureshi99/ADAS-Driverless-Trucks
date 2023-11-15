# Finidng-IPM-for-ADAS-System-in-Driverless-Trucks
Calculating IPM100 (disengagement per 100 miles) for specific issue in Driverless trucks specific to ISSUE-18 using real time data 

Step 1: Imported necessary libraries, including pandas and numpy
Step 2: Created a function, calc_ipm, to calculate Incidents Per Mile (IPM). This function takes two parameters, dis (disengagement) and distance, and converts the distance from meters to miles before performing the calculation.
Step 3: Loaded data from a JSON file using the read_json function into a pandas DataFrame named 'data'.
Step 4: Extracted the count of disengagement events and filtered rows where the ticket_id is 'ISSUE-18'.
Step 5: Added a new column named 'distance' to the DataFrame and extracted the distance values from the 'cruise' column.
Step 6: Dropped rows where the distance value is missing.
Step 7: Calculated IPM 100 using the calc_ipm function.
Step 8: Calculated IPM 100 specifically for 'ISSUE-18' using the calc_ipm function.
Step 9: Calculated the mean and standard error using the sqrt function in numpy.
Step 10: Calculated the confidence interval using poisson distribution for critical value 1.96.
Step 11: Calculated the lower and upper bounds of the confidence interval.