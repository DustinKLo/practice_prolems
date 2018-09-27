from datetime import datetime, timedelta, time


def time_spent_between_8pm_8am(start_date, end_date):
	'''
	calculate the total minutes between the specified start date and end date objects
	loop through the date range 1 minute at a time
		if the hour is between 8pm and 8am (greater than hour 20 and less then hour 8) 
		then one minute will be added to time_spent
	'''
	minutes_spent = 0
	EIGHT_AM = time(8, 0, 0)
	EIGHT_PM = time(20, 0, 0)

	if start_date > end_date:
		return minutes_spent

	date_counter = start_date
	while True:
		date_counter += timedelta(minutes=1)

		# if the time is greater than 8pm and less than 8am then count that minute
		if date_counter.time() >= EIGHT_PM or date_counter.time() <= EIGHT_AM:
			minutes_spent += 1

		if date_counter > end_date:
			break

	return minutes_spent


if __name__ == '__main__':
	# 6/01/2017 19:12:35  6/02/2017 09:12:35
	START_DATE = datetime(2017, 6, 3, 23, 12, 35)
	END_DATE = datetime(2017, 6, 4, 7, 12, 35)

	minutes_spent_between_8pm_8am = time_spent_between_8pm_8am(START_DATE, END_DATE)
	print('{} minutes spent in this location'.format(minutes_spent_between_8pm_8am))
