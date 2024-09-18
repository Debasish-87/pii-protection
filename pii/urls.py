from django.urls import path
from .views import index, index2, login_show, signup_view, manager_view, process_image, check_image,process_user_id,image_show

urlpatterns = [
    path('', index, name='index'),
    path('index2/', index2, name='index2'),
    path('login/', login_show, name='login'),
    path('signup/', signup_view, name='signup'),
    path('manager/', manager_view, name='manager'),
    path('process_image/', process_image, name='process_image'),
    path('check_image/', check_image, name='check_image'),
    path('process/<int:user_id>/',process_user_id, name='process-user-id'),
    path('image/',image_show, name='image_show'),
    # path('image/<int:user_id>/', image_show, name='image_show'),
]

