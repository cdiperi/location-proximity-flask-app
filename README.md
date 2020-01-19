# location-proximity-flask-app

This app was developed to provide a simple and informative way to locate stores within a specified radius of a specified target store. The context of this app is within a large specialty retailer that is the parent of several smaller retail companies, together summing up to over 1,300 retail locations in the country. The app allows the user to filter the results by both distance and by company, which was derived from the first two characters of the unique store identifier in this case.

The steps I took to populate the database:
  1) Began with a report containing each open store along with their addresses.
  2) Using Google Maps Geocoding API, translated each address to a geographical coordinate.
  3) Using geopy, compared each store's location to every other store's location and calculated the straight-line distance for each instance.
  4) Filtered the above results to only instances where the straight-line distance was less than 50 miles.
  5) Using Google Maps Distance Matrix API, obtained the driving distance and duration for each instance.
  6) Filtered the above results to only instances where the driving distance was less than 50 miles.
  7) Imported this data into the database using pandas and sqlalchemy.
  
Originally built on pythonanywhere.com using their cloud-hosted MySQL database.

This app requires a Google Maps API key.
