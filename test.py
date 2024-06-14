from post import postWithRetry
from readFile import readFile

strapi_domain = "http://localhost:1337"
error_items = []
error_publish_items = []
destinations = readFile()

# Create collections
url = f"{strapi_domain}/content-manager/collection-types/api::destination.destination"
collection_results = []
for d in destinations:
    body = {
        "articles": {"disconnect": [], "connect": []},
        "hotels": {"disconnect": [], "connect": []},
        "name": d["name"],
        "taId": d["taId"],
        "slug": d["slug"],
    }
    result = postWithRetry(url, error_items, body)
    if result:
        collection_results.append(result)
if collection_results.__sizeof__() > 0:
    print("Successfully create collection.")
else:
    print("Failed to create collection after 3 retries.")
    print("Error on: ", error_items)

# Publish collections
publish_results = None
for c in collection_results:
    id = c["id"]
    url = f"{strapi_domain}/content-manager/collection-types/api::destination.destination/{id}/actions/publish"
    publish_results = postWithRetry(url, error_publish_items, retry_count=5)
if publish_results:
    print("Successfully publish collection.")
elif publish_results == None:
    print("Nothing to publish")
else:
    print("Failed to publish collection after 3 retries.")
    print("Error on: ", error_publish_items)
