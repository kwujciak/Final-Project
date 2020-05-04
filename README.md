# Final-Project-ES2
 
Travel Tool: How to travel with ease!
 
Short Description of Project: This travel tool helps the user with some problems one may run into when traveling. Based on the user's destination and location, it converts currency, the time change, flight duration to destination, population attractions at the destination, and the statistics on tourism for each destination. 

Instructions for running main.py:
1. Run the main.py file and interact using the console. 
2. For the first question, input keywords (listed in main.py).
	- time and timezone runs the time change file.
	- currency, exchange, money run the currency exchange file.
	- attraction(s), popular, place(s), location run attractions file.
	- flight, duration, airtime, plane run flight duration file.
	- tourist, statistics, stats, year, tourism run tourism file.
3. For the next question input one of the compatible destinations listed.
4. Based on the user inputs, the code runs accordingly. The rest of the questions are straightforward.

File List:
FP_time.py - gives the local time at the desired destination.
FP_attractions.py - gives a couple popular attractions at destination.
FP_FlightTime.py - gives the flight duration from origin to destination.
FP_currency.py - converts desired currency to currency at destination.
FP_tourism.py - graphs the statistics of tourism for each location. Specifically, annual international tourists to London, Rome, and Tokyo, and annual total tourists in the US locations.
main.py - main console that runs each of the files as needed.

Libraries:
- numpy
- pandas
- time
- matplotlib.pyplot

Design:
- The core of this project is using the user-inputted strings throughout many different functions. This is to avoid asking the user any unnecessary questions. CSV files are important in this project. Parsing through these CSV files is important in getting the specific information for each location.