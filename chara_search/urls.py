from django.urls import path
from . import views

app_name = 'chara_search'
urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('<int:character_id>/', views.sheet, name='sheet'),
    path('search/', views.SearchResultsView.as_view(), name='search_results')
]