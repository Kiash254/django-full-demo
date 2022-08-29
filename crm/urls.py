from django.urls import path
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

]