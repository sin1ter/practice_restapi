from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


from accounts.api.views import *

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    # path('login/', obtain_auth_token, name='login')
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', registration_view, name='register'),
    # path('logout/', logout_view, name='logout'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('userinfo/', User_info.as_view(), name='user_info'),
    path('changepassword/', Update_password.as_view(), name='change_password'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
