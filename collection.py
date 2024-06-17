from post import postWithRetry


def createCategories(strapi_domain, categories, error_items):
    url = (
        f"{strapi_domain}/content-manager/collection-types/api::collection.collection"
    )
    collection_results = []
    for d in categories:
        body = {
            "articles": {"disconnect": [], "connect": []},
            "hotels": {"disconnect": [], "connect": []},
            "name": d["name"],
            "slug": d["slug"],
        }
        result = postWithRetry(url, error_items, body)
        if result:
            collection_results.append(result)
    if collection_results.__sizeof__() > 0:
        print("Successfully create category.")
    else:
        print("Failed to create category after 3 retries.")
        print("Error on: ", error_items)

    return collection_results, error_items


def publishCategories(strapi_domain, collection_results, error_publish_items):
    publish_results = None
    for c in collection_results:
        id = c["id"]
        url = f"{strapi_domain}/content-manager/collection-types/api::collection.collection/{id}/actions/publish"
        publish_results = postWithRetry(url, error_publish_items, retry_count=5)
    if publish_results:
        print("Successfully publish category.")
    elif publish_results == None:
        print("Nothing to publish")
    else:
        print("Failed to publish category after 3 retries.")
        print("Error on: ", error_publish_items)
    
    return publish_results, error_publish_items
