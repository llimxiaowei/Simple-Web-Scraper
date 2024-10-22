
# Import necessary libraries
from bs4 import BeautifulSoup
import requests
import csv

# Function to scrape listing elements from Google Flights
def scrape_listings(soup):
    return soup.select('li.pIav2d')

# Function to scrape company name from a flight listing
def scrape_company_name(listing):
    airline_element = listing.select_one('div.Ir0Voe div.sSHqwe')
    return airline_element.text.strip() if airline_element else "N/A"

# Function to scrape flight duration from a flight listing
def scrape_flight_duration(listing):
    duration_element = listing.select_one('div.AdWm1c.gvkrdb')
    return duration_element.text.strip() if duration_element else "N/A"

# Function to scrape price from a flight listing
def scrape_price(listing):
    price_element = listing.select_one('div.U3gSDe div.FpEdX span')
    return price_element.text.strip() if price_element else "N/A"

# Function to scrape departure and arrival dates from a flight listing
def scrape_departure_arrival_dates(listing):
    departure_date_element = listing.select_one('span.mv1WYe span:first-child [jscontroller="cNtv4b"] span')
    arrival_date_element = listing.select_one('span.mv1WYe span:last-child [jscontroller="cNtv4b"] span')

    departure_date = departure_date_element.text.strip() if departure_date_element else "N/A"
    arrival_date = arrival_date_element.text.strip() if arrival_date_element else "N/A"
    return departure_date, arrival_date

# Function to scrape flight CO2 emission from a flight listing
def scrape_co2_emission(listing):
    co2_element = listing.select_one('div.V1iAHe div.AdWm1c')
    return co2_element.text.strip() if co2_element else "N/A"

# Function to scrape flight stops from a flight listing
def scrape_flight_stops(listing):
    stops_element = listing.select_one('div.EfT7Ae span.ogfYpf')
    return stops_element.text.strip() if stops_element else "N/A"

# Main function
def main():
    # Make a request to Google Flights URL and parse HTML
    url = 'https://www.google.com/travel/flights/search?tfs=CBwQAhoeEgoyMDI0LTEwLTIyagcIARIDS1VMcgcIARIDU0lOGh4SCjIwMjQtMTAtMjJqBwgBEgNTSU5yBwgBEgNLVUxAAUgBcAGCAQsI____________AZgBAQ&hl=en-US&curr=EUR'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Scrape flight listings
    listings = scrape_listings(soup)

    # Prepare CSV file to save the data
    with open('google_flights_data.csv', mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        # Write header row
        writer.writerow(['Company Name', 'Flight Duration', 'Price', 'Departure Date', 'Arrival Date', 'CO2 Emission', 'Stops'])

        # Iterate through each listing and extract flight information
        for listing in listings:
            company_name = scrape_company_name(listing)
            flight_duration = scrape_flight_duration(listing)
            price = scrape_price(listing)
            departure_date, arrival_date = scrape_departure_arrival_dates(listing)
            co2_emission = scrape_co2_emission(listing)
            stops = scrape_flight_stops(listing)

            # Write flight information to the CSV file
            writer.writerow([company_name, flight_duration, price, departure_date, arrival_date, co2_emission, stops])

    print("Flight data saved to google_flights_data.csv")

if __name__ == "__main__":
    main()