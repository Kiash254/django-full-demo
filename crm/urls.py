from django.urls import path
from django.contrib.auth import views as auth_views 
from .views import home,products,customers,createOrder,updateOrder,Account,deleteOrder,Register,Login,Userpage,Logoutview
app_name = 'crm'

urlpatterns = [

    path('register/',Register,name='register'),
    path('login/',Login,name='login'),
    path('logout/',Logoutview,name='logout'),
    path('account/',Account,name='account'),
    path('',home,name='home'),
    path('user/',Userpage,name='user'),
    path('products/',products,name='products'),
    path('customers/<int:pk>/',customers,name='customers'),
    path('create_order/<int:pk>/',createOrder,name='create_order'),
    path('update_order/<int:pk>/',updateOrder,name='update_order'),
    path('delete_order/<int:pk>/',deleteOrder,name='delete_order'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='reset_password.html'),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='reset_password_sent.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_form.html'),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='reset_password_complete.html'),name='password_reset_complete'),
]