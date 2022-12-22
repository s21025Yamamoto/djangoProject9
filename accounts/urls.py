from django.urls import path
# viewsモジュールをインポート
from . import views
# viewsをインポートしてauth_viewという名前で利用する
from django.contrib.auth import views as auth_views

# URLパターンを逆引きできるように名前をつける
app_name = 'accounts'

# URLパターンを登録するための変数
urlpatterns = [
    # サインアップページのビューの呼び出し
    # 「http(s)://<ホスト名>/signup/」へのアクセスに対して、
    # viewsモジュールのSignUpViewをインスタンス化する
    path('signup/',
         views.SignUpView.as_view(),
         name='signup'
         ),

    path('signup_success/',
         views.SignUpSuccessView.as_view(),
         name='signup_success'
         ),
    path('login/',
             auth_views.LoginView.as_view(template_name='login.html'),
             name='login'
             ),

        path('logout/',
             auth_views.LogoutView.as_view(template_name='logout.html'),
             name='logout'
             ),

    ]