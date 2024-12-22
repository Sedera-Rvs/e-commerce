from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from accounts.views import login_user, logout_user, signup
from shop import settings
from store.views import add_to_cart, cart, delete_cart, detail_prod, index

urlpatterns = [
    path('', index, name='index'),
    path('signup', signup, name='signup'),
    path("login", login_user, name="login"),
    path('logout', logout_user, name='logout'),
    path('product/<str:slug>/', detail_prod, name='product'),
    path('product/<str:slug>/add-to-cart', add_to_cart, name='add-to-cart'),
    path('cart', cart, name='cart'),
    path('cart/delete/', delete_cart, name='delete-cart'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 