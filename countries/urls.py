from django.urls import path
from countries.views import GetTopCountriesApiViews,GetCountriesApiViews, PostCountriesLikedApiViews
    
urlpatterns = [
    path('countries/', GetCountriesApiViews.as_view(), name='countries'),
    path('countries/top10/', GetTopCountriesApiViews.as_view(), name='countries-top10'),
    path('countries/assess/', PostCountriesLikedApiViews.as_view(), name="countries-assess")
]
