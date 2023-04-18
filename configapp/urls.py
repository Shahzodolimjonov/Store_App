from django.urls import path
from .views import *

urlpatterns = [
    # path('index/', index, name='home'),
    path('index/',HomeNews.as_view(),name='home'),
    path('add_category/', add_category, name='add_category'),
    path('boss/', boss, name='boss'),
    path('add/', BlogCreateView.as_view(), name='add'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='update'),
    path('opp/', catego, name='opp'),
    path('moss/<int:pk>/', moss, name='moss'),
    # path('category/<int:pk>/', categories, name='category'),
    path('category/<int:pk>/',HomeCategory.as_view(),name='category'),
    path('detail/<int:pk>/', BlogDeleteView.as_view(), name='detail'),
    path('search/', moon, name='search'),
]
