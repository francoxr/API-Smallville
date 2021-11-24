from django.urls import path
from . import views

urlpatterns = [
    # path('', views.HelloWorld),
    path('authors/',views.AuthorList.as_view()),
    path('authors/<int:pk>/', views.AuthorOneList.as_view()),
    path('authors/create/', views.AuthorCreateAPIView.as_view()),
    path('quotes/', views.QuotesList.as_view()),
    path('quotes/<int:pk>/', views.QuotesOneList.as_view()),
    path('quotes/create/', views.QuotesCreateApiView.as_view()),
    path('quotesp/<int:pk>/', views.QuotesOneListEspecial.as_view()),
]