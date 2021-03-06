"""b2s URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from users import views as user_views
from .views import home,profile

if settings.DEBUG:
    import debug_toolbar
    
    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home ,name="home"),
    path('profile/', profile, name="profile"),
    path('products/', include('products.urls', namespace='products')),
    path('register/',user_views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.htm'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.htm'), name="logout"),
    path('__debug__/', include(debug_toolbar.urls)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)