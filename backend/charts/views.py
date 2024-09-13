from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime

def candlestick_data(request):
    data = {
        "data": [
            {"x": datetime(2023, 1, 2).strftime('%Y-%m-%d'), "open": 35, "high": 45, "low": 30, "close": 40},
            {"x": datetime(2023, 1, 3).strftime('%Y-%m-%d'), "open": 40, "high": 50, "low": 35, "close": 45},
            {"x": datetime(2023, 1, 4).strftime('%Y-%m-%d'), "open": 50, "high": 58, "low": 42, "close": 55},
            {"x": datetime(2023, 1, 5).strftime('%Y-%m-%d'), "open": 55, "high": 60, "low": 48, "close": 57},
            {"x": datetime(2023, 1, 6).strftime('%Y-%m-%d'), "open": 57, "high": 63, "low": 52, "close": 61},
            {"x": datetime(2023, 1, 7).strftime('%Y-%m-%d'), "open": 61, "high": 65, "low": 58, "close": 63},
            {"x": datetime(2023, 1, 8).strftime('%Y-%m-%d'), "open": 63, "high": 68, "low": 60, "close": 66},
            {"x": datetime(2023, 1, 9).strftime('%Y-%m-%d'), "open": 66, "high": 70, "low": 62, "close": 64},
            {"x": datetime(2023, 1, 10).strftime('%Y-%m-%d'), "open": 64, "high": 67, "low": 59, "close": 65}
        ]
    }
    return JsonResponse(data)

def line_chart_data(request):
    data = {
        "labels": ["Jan", "Feb", "Mar", "Apr"],
        "datasets": [
            {
                "data": [10, 20, 30, 40]
            }
        ]
    }
    return JsonResponse(data)

def bar_chart_data(request):
    data = {
        "labels": ["Product A", "Product B", "Product C"],
        "datasets": [
            {
                "label": "Products",
                "data": [100, 150, 200]
            }
        ]
    }
    return JsonResponse(data)

def pie_chart_data(request):
    data = {
        "labels": ["Red", "Blue", "Yellow"],
        "datasets": [
            {
                "data": [300, 50, 100]
            }
        ]
    }
    return JsonResponse(data)
