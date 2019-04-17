from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'photologue'
urlpatterns = [
    path('', TemplateView.as_view(template_name="photologue/home.html"), name='home'),
    path('database/', views.database_list_view, name='database_list'),
    path('database/create/', views.database_create_view, name='database_create'),
    path('database/<slug:slug>/', views.database_detail_view, name='database_detail'),
    path('database/<slug:slug>/edit/', views.database_edit_view, name='database_edit'),

    # Info about indexes for concrete database. If no database parameter provided then show list of databases
    # parameter ?database=slug
    path('database/index/info/', views.database_index_info_view, name='database_index_info'),

    # Form to create new index for some database without deleting old ones.
    # Must provide option whether to use new index as default.
    # parameter ?database=slug
    path('database/index/create/', views.database_index_create_view, name='database_index_create'),

    # Management of indexes for concrete database. For example, change default.
    # If no database parameter provided then show list of databases
    # parameter ?database=slug
    path('database/index/management/', views.database_index_management_view, name='database_index_management'),

    # Info about concrete index: which database, how many objects indexed,
    # list of events which used this index...
    path('database/index/<slug:slug>/', views.database_index_detail_view, name='database_index_detail'),

    path('event/create/', views.event_create_view, name='event_create'),
    path('event/<slug:slug>/', views.event_detail_view, name='event_detail'),

]
