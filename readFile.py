import csv
import json


def readFile():
    destinations = []
    categories = []
    amenities = []
    hotel_classes = []
    with open("source/ValidHotels.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Example: {"name":"Seven Mile Beach","slug":"seven-mile-beach","taId":"147367"}
            tempDestinations = json.loads(row["Destination"])
            for t in tempDestinations:
                destinations.append(t)

            # Example: {"name":"Kid-Friendly","slug":"kid-friendly"}
            tempCategories = json.loads(row["Category"])
            for t in tempCategories:
                categories.append(t)

            # Example: {"name":"Beach","slug":"beach"}
            tempAmenities = json.loads(row["Amenity"])
            for t in tempAmenities:
                amenities.append(t)

            # Example: {"name":"Upscale","slug":"upscale"}
            tempHotelClasses = json.loads(row["Hotel Class"])
            for t in tempHotelClasses:
                hotel_classes.append(t)
    return destinations, categories, amenities, hotel_classes
