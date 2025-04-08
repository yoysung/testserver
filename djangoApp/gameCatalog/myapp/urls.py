from django.urls import path, re_path
from . import views

urlpatterns = [
    # API endpoints
    path("api/items/", views.get_items, name="get_items"),
    path("api/items/create/", views.create_item, name="create_item"),
    path("api/items/<int:item_id>/", views.manage_item, name="manage_item"),
    path("api/items/search/", views.search_items, name="search_items"),
    
    # Frontend routes
    path("", views.home, name="home"),
    path("add/", views.add_data, name="add_data"),
    path("choice/", views.choice, name="choice"),
    path("consoles/", views.consoles_peripherals, name="consoles_peripherals"),
    path("create-console/", views.create_console, name="create_console"),
    path("database-display/", views.database_display, name="database_display"),
    path("signup/", views.database_signup, name="database_signup"),
    path("database/", views.database_functionality, name="database_functionality"),
    path("game-copies/", views.game_copies, name="game_copies"),
    
    # Catch-all pattern for React router
    re_path(r'^.*$', views.serve_react_app, name='react-app'),
]
