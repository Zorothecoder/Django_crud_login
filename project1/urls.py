from django.contrib import admin
from django.urls import path
from app1 import views as app1_views
from app2 import views as app2_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('register', app1_views.Register, name = "register"),
    path('', app1_views.Login, name = "login"),
    path('logout', app1_views.Logout, name = "logout"),
    
    path('home', app2_views.Home, name = "home"),
    path('update/<int:id>', app2_views.Update, name = "update"),
    path('delete/<int:id>', app2_views.Delete, name = "delete")
]
