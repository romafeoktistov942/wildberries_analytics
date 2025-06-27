import requests
from analytics.models import Product


def parse_products(query):
    url = "https://search.wb.ru/exactmatch/ru/common/v4/search"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {
        "query": query,
        "resultset": "catalog",
        "limit": 100,
        "page": 1,
    }

    response = requests.get(url, headers=headers, params=params)
    print("Status code:", response.status_code)
    print("Response text:", response.text)
    data = response.json()

    products = data.get("data", {}).get("products", [])
    print("Найдено товаров:", len(products))

    for item in products:
        print(item)
        Product.objects.update_or_create(
            name=item.get("name"),
            defaults={
                "price": item.get("priceU", 0) // 100,
                "sale_price": item.get("salePriceU", 0) // 100,
                "rating": item.get("reviewRating") or 0,
                "feedbacks": item.get("feedbacks") or 0,
            },
        )
