from django.conf.urls import url
from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from driver.views import Home, LoginView, user_profile, EditProfileView, ChangePasswordView, RegisterView, \
    logout_view, ArticleView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('advice/<slug:slug>', ArticleView.as_view(), name='article'),
    path('login', LoginView.as_view(), name="login"),
    path('logout', logout_view, name='logout'),
    path('register', RegisterView.as_view(), name='register'),
    path('profile', user_profile, name='profile'),
    path('profile/edit', EditProfileView.as_view(), name='profile_edit'),
    path('profile/change-password', ChangePasswordView.as_view(), name='change_password'),
    url(r'^user/reset/password/$',
        auth_views.PasswordResetView.as_view(template_name='driver/reset_password.html',
                                             success_url=reverse_lazy('user_reset_password_done')),
        name='user_reset_password'),
    url(r'^user/reset/password/done/$', auth_views.PasswordResetDoneView.as_view(), name='user_reset_password_done'),
    url(r'^user/reset/password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^user/reset/password/complete/$', auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'),
]