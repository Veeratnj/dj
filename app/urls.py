from app import views
from django.urls import path

app_name='app'

urlpatterns = [
    path('home/', views.views_demo, name='home'),
    path('dynamic/url/<int:post_id>/', views.views_dynamic_url_path, name='dynamic_url-path'),
    path('comments/', views.views_dynamic_urla_query, name='dynamic_url-query'),
    path('old/url',views.views_redirect_old,name='old-url'),
    path('new/url',views.views_redirect_new,name='new-url'),
    path('index/',views.views_index,name='index'),
    path('another/page',views.another_page,name='another_page'),
    path('form/',views.form_page,name='form_page')

]
