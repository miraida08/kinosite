from .views import *
from django.urls import path


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('profile/', ProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='product_list'),
    path('profile/<int:pk>/', ProfileViewSet.as_view({'get': 'retrieve',
                                                    'put': 'update',
                                                    'delete': 'destroy'}), name='product_detail'),

    path('country/', CountryViewSet.as_view({'get': 'list', 'post': 'create'}), name='product_list'),
    path('country/<int:pk>/', CountryViewSet.as_view({'get': 'retrieve',
                                              'put': 'update',
                                              'delete': 'destroy'}), name='product_detail'),

    path('director/', DirectorDetailViewSet.as_view({'get': 'list', 'post': 'create'}), name='product_list'),
    path('director/<int:pk>/', DirectorDetailViewSet.as_view({'get': 'retrieve',
                                              'put': 'update',
                                              'delete': 'destroy'}), name='product_detail'),



    path('actor/', ActorDetailViewSet.as_view({'get': 'list', 'post': 'create'}), name='product_list'),
    path('actor/<int:pk>/', ActorDetailViewSet.as_view({'get': 'retrieve',
                                              'put': 'update',
                                              'delete': 'destroy'}), name='product_detail'),

    path('janre/', JanreViewSet.as_view({'get': 'list', 'post': 'create'}), name='product_list'),
    path('janre/<int:pk>/', JanreViewSet.as_view({'get': 'retrieve',
                                              'put': 'update',
                                              'delete': 'destroy'}), name='product_detail'),

    path('', MovieListViewSet.as_view({'get': 'list', 'post': 'create'}), name='product_list'),
    path('<int:pk>/', MovieDetailViewSet.as_view({'get': 'retrieve',
                                              'put': 'update',
                                              'delete': 'destroy'}), name='product_detail'),

    path('movieLanguages/', MovieLanguagesViewSet.as_view({'get': 'list', 'post': 'create'}), name='product_list'),
    path('movieLanguages/<int:pk>/', MovieLanguagesViewSet.as_view({'get': 'retrieve',
                                              'put': 'update',
                                              'delete': 'destroy'}), name='product_detail'),

    path('moments/', MomentsViewSet.as_view({'get': 'list', 'post': 'create'}), name='product_list'),
    path('moments/<int:pk>/', MomentsViewSet.as_view({'get': 'retrieve',
                                              'put': 'update',
                                              'delete': 'destroy'}), name='product_detail'),

    path('rating/', RatingViewSet.as_view({'get': 'list', 'post': 'create'}), name='product_list'),
    path('rating/<int:pk>/', RatingViewSet.as_view({'get': 'retrieve',
                                              'put': 'update',
                                              'delete': 'destroy'}), name='product_detail'),

    path('favorite/', FavoriteViewSet.as_view({'get': 'list', 'post': 'create'}), name='product_list'),
    path('favorite/<int:pk>/', FavoriteViewSet.as_view({'get': 'retrieve',
                                              'put': 'update',
                                              'delete': 'destroy'}), name='product_detail'),

    path('favoriteMovie/', FavoriteMovieViewSet.as_view({'get': 'list', 'post': 'create'}), name='product_list'),
    path('<int:pk>/', FavoriteMovieViewSet.as_view({'get': 'retrieve',
                                              'put': 'update',
                                              'delete': 'destroy'}), name='product_detail'),

    path('history/', HistoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='product_list'),
    path('history/<int:pk>/', HistoryViewSet.as_view({'get': 'retrieve',
                                              'put': 'update',
                                              'delete': 'destroy'}), name='product_detail'),
    ]