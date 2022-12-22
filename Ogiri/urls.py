from django.urls import path
from . import views

app_name = 'Ogiri'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('thema_category', views.ThemaCategory.as_view(), name='thema_category'),
    path('post/', views.CreateOgiriView.as_view(), name='post'),
    path('post_done/', views.PostSuccessView.as_view(), name='post_done'),
    path('answer_category', views.AnswerCategory.as_view(), name='answer_category'),
    path('reverse_post/', views.CreateReverseOgiriView.as_view(), name='reverse_post'),
    path('image_post/', views.CreateImageOgiriView.as_view(), name='image_post'),
    path('imitation_post/', views.CreateImitationOgiriView.as_view(), name='imitation_post'),





]