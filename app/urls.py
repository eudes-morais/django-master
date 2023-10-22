from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import CarsListView, CarCreateView, CarDetailView, CarUpdateView, CarDeleteView
from .views import index
from accounts.views import register_view, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('', index),
    path('cars/', CarsListView.as_view(), name='cars_list'), # Quando se utiliza a CBV tem que especificar que a classe é uma view (.as_view)
    path('new_car/', CarCreateView.as_view(), name='new_car'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('car/<int:pk>/update/', CarUpdateView.as_view(), name='car_update'),
    path('car/<int:pk>/delete/', CarDeleteView.as_view(), name='car_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
