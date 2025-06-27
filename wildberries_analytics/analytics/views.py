from django.shortcuts import render
from django.http import JsonResponse
from .models import Product


def dashboard(request):
    return render(request, "analytics/dashboard.html")


def products_list(request):
    products = Product.objects.all()

    min_price = request.GET.get("min_price")
    if min_price:
        products = products.filter(price__gte=int(min_price))

    min_rating = request.GET.get("min_rating")
    if min_rating:
        products = products.filter(rating__gte=float(min_rating))

    min_feedbacks = request.GET.get("min_feedbacks")
    if min_feedbacks:
        products = products.filter(feedbacks__gte=int(min_feedbacks))

    data = list(
        products.values("name", "price", "sale_price", "rating", "feedbacks")
    )
    return JsonResponse(data, safe=False)
