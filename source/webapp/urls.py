from webapp.views import index_view, cat_stats_view
from django.urls import path

urlpatterns = [
    path('', index_view),
    path('cat_stats/', cat_stats_view),
]