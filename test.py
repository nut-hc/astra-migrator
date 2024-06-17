from amenity import createAmenities, publishAmenities
from collection import createCategories, publishCategories
from destination import createDestinations, publishDestinations
from hotelClass import createHotelClasses, publishHotelClasses
from readFile import readFile

strapi_domain = "http://localhost:1337"
error_destinations_items = []
error_destinations_publish_items = []
error_categories_items = []
error_categories_publish_items = []
error_amenities_items = []
error_amenities_publish_items = []
error_hotel_classes_items = []
error_hotel_classes_publish_items = []
destinations, categories, amenities, hotel_classes = readFile()

# Destinations
destinations_results, error_destinations_items = createDestinations(
    strapi_domain, destinations, error_destinations_items
)
destinations_publish_results, error_destinations_items = publishDestinations(
    strapi_domain, destinations_results, error_destinations_publish_items
)

# Categories
categories_results, error_categories_items = createCategories(
    strapi_domain, categories, error_categories_items
)
categories_publish_results, error_categories_items = publishCategories(
    strapi_domain, categories_results, error_categories_publish_items
)

# Amenities
amenities_results, error_amenities_items = createAmenities(
    strapi_domain, amenities, error_amenities_items
)
amenities_publish_results, error_amenities_items = publishAmenities(
    strapi_domain, amenities_results, error_amenities_publish_items
)

# Hotel Class
hotel_classes_results, error_hotel_classes_items = createHotelClasses(
    strapi_domain, hotel_classes, error_hotel_classes_items
)
hotel_classes_publish_results, error_hotel_classes_items = publishHotelClasses(
    strapi_domain, hotel_classes_results, error_hotel_classes_publish_items
)
