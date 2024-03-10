# This just a test file.
# This tests to see if a database file has been created, and if it is, it prints the size of the file.

from datetime import datetime, timedelta

# Get the current date
current_date = datetime.now()

# Calculate the date 14 days from now
future_date = current_date + timedelta(days=14)

# Print the future date in DD-MM format
print("Today's date:", current_date.strftime('%d-%m'))
print("Date 14 days from now:", future_date.strftime('%d-%m'))

