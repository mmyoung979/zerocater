# Python Imports
from datetime import datetime, timedelta

# Check Vendor Availability For Meal Delivery
def is_vendor_available(vendor_id, date_time):
	# Driver information per vendor (should be in database)
	vendors = {
			'results': [
			{
					'vendor_id': 1,
					'drivers': 1
			},
			{
					'vendor_id': 2,
					'drivers': 3
			}
		]
	}

	# A list of meals to be delivered (should be in database)
	meals = {
			'results': [
			{
					'vendor_id': 1,                    # Vendor 1 will be serving
					'client_id': 10,                   # Client 10 on
					'datetime': '2017-01-01 13:30:00'  # January 1st, 2017 at 1:30 pm
			},
			{
					'vendor_id': 1,
					'client_id': 40,
					'datetime': '2017-01-01 14:30:00'
			},
			{
					'vendor_id': 2,
					'client_id': 20,
					'datetime': '2017-01-01 13:30:00'
			}
		]
	}

	if vendor_id not in [x['vendor_id'] for x in vendors['results']]:
		raise ValueError('Vendor ID not found')

	# Convert string to datetime
	def time(x):
		return datetime.strptime(x, '%Y-%m-%d %H:%M:%S')

	# In a real project, these would be database queries
	# Identify relevant amount of drivers and meal time deliveries
	drivers = vendors['results'][vendor_id - 1]['drivers']
	meal_times = [x['datetime'] for x in meals['results'] if x['vendor_id'] == vendor_id]

	# Check against all scheduled meals, 30 minutes before and 10 minutes after
	for meal in meal_times:
		before = time(meal) - timedelta(minutes=30)
		after = time(meal) + timedelta(minutes=10)

		# If within blackout period with no other drivers, vendor is not available
		if drivers > 0:
			return True
		if (date_time > before and date_time < after):
			return False

	return True
