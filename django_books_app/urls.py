from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPageView.as_view(), name='main_page'),
    path('book/<int:pk>/', views.BookDetailedView.as_view(), name='book_detail'),
    path('book/create/', views.BookCreateView.as_view(), name='book_create'),
    path('book/delete/<int:pk>', views.BookDeleteView.as_view(), name='book_delete'),
    path('book/update/<int:pk>', views.BookUpdateView.as_view(), name='book_update'),
    path('book/list/', views.BookListView.as_view(), name='book_list'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('book/<int:pk>/reviews/', views.ReviewListPerBookView.as_view(), name='review_per_book_list'),
    path('review/', views.ReviewListView.as_view(), name='review_list'),
    path('review/<int:pk>/', views.ReviewView.as_view(), name='review_detail'),
    path('review/delete/<int:pk>/', views.ReviewDeleteView.as_view(), name='review_delete'),
    path('review/update/<int:pk>/', views.ReviewUpdateView.as_view(), name='review_update'),
    path('book/<int:pk>/review/create/', views.ReviewCreateView.as_view(), name='review_create'),
    path('author/create/', views.AuthorCreateView.as_view(), name='author_create'),
]
