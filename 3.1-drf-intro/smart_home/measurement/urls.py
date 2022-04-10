from django.contrib import admin
from django.urls import path

from measurement.views import SensorView, MeasurementCreate, SensorDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sensors/', SensorView.as_view()),
    path('measurements/', MeasurementCreate.as_view()),
    path('sensors/<pk>/', SensorDetail.as_view()),

]
