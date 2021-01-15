from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    # path('about/', views.about, name='about'),
    path('planets/', views.planets_index, name="planets_index"),
    path('planets/<int:planet_id>', views.planets_show, name='planets_show'),
    path('planets/add/', views.PlanetAdd.as_view(), name="planets_add"),
    path('planets/<int:pk>/update/', views.PlanetUpdate.as_view(), name='planets_update'),
    path('planets/<int:pk>/delete/', views.PlanetDelete.as_view(), name="planets_delete"),
    # path('user/<username>/', views.profile, name="profile")
]
