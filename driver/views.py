import datetime

import magic
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import AnonymousUser, User
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View

from driver.forms import LoginForm, RegistrationForm, EditUserForm
from driver.models import Advice
from driver.utils import create_email_message


class Home(View):
    def get(self, request):
        weeks_advice = Advice.objects.filter(weeks_advice=True).latest(field_name="created_date")
        if not weeks_advice:
            weeks_advice = Advice.objects.latest(field_name="created_date")
        if request.user.is_anonymous:
            advices_not_passed_list = Advice.objects.exclude(pk=weeks_advice.pk)
        else:
            advices_not_passed_list = Advice.objects.exclude(passed=request.user).exclude(pk=weeks_advice.pk)
        paginator = Paginator(advices_not_passed_list, 3)
        page = request.GET.get('page')
        advices_not_passed = paginator.get_page(page)
        context = {'weeks_advice': weeks_advice, 'advices_not_passed': advices_not_passed}
        return render(request, 'driver/home.html', context)

    def post(self, request):
        message = request.POST.get('message')
        user_help = User.objects.filter(username="user_help", is_staff=True)
        if user_help.exists():
            send_mail(subject=str(request.user)+''+str(datetime.date.today()),
                      message=message,
                      from_email=request.user.email,
                      recipient_list=[user_help[0].email])
        else:
            messages.warning(request, 'Twoja wiadomość nie została wysłana! Spróbuj później.')
        return redirect(reverse_lazy('home'))


class AdviceView(View):
    """todo: likes system, quiz (not with radio select!)."""
    def get(self, request, slug):
        try:
            advice = Advice.objects.get(slug=slug)
        except Advice.DoesNotExist:
            return Http404
        return render(request, 'driver/advice.html', context={'advice': advice})
    
    def post(self, request, slug):
        ans = request.POST.getlist('answer')
        print(ans)
        return HttpResponse('k')


class LoginView(View):
    def get(self, request):
        return render(request, 'driver/login.html', context={'form': LoginForm().as_p(),
                                                             'submit': 'Zaloguj'})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('user_login')
            user_password = form.cleaned_data.get('user_password')
            user = authenticate(username=user_name, password=user_password)
            if user is not None:
                login(request, user)
                next_ = request.GET.get('next')
                if next_ is not None:
                    return redirect(next_)
                else:
                    return redirect(reverse_lazy('home'))
            else:
                message = 'Niepoprawne dane logowania'
                return render(request, 'driver/login.html', context={'form': LoginForm().as_p(),
                                                                     'submit': 'Zaloguj',
                                                                     'message': message})


@login_required(redirect_field_name='next', login_url=reverse_lazy('login'))
def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('home'))


class RegisterView(View):
    def get(self, request):
        form = RegistrationForm().as_p()
        context = {'form': form}
        return render(request, 'driver/register.html', context)

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = create_email_message("Witamy na portalu Driver",
                                         "driver/welcome_email.html",
                                         user,
                                         {'user': user})
            email.send()
            return redirect(reverse_lazy('login'))
        else:
            context = {'form': form}
            return render(request, 'driver/register.html', context)


@login_required(redirect_field_name='next', login_url=reverse_lazy('login'))
def user_profile(request):
    return render(request, 'driver/user_profile.html', context={'user': request.user})


class EditProfileView(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name = 'next'

    def get(self, request):
        form = EditUserForm(instance=request.user).as_p()
        return render(request, 'driver/uni_form.html', context={'form': form, 'submit': 'Zapisz'})

    def post(self, request):
        form = EditUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('profile'))
        else:
            form = EditUserForm(instance=request.user).as_p()
            return render(request, 'driver/uni_form.html', context={'form': form, 'submit': 'Zapisz'})


class ChangePasswordView(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name = 'next'

    def get(self, request):
        form = PasswordChangeForm(user=request.user)
        return render(request, 'driver/uni_form.html', context={'form': form, 'submit': 'Zapisz'})

    def post(self, request):
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse_lazy('profile'))
        else:
            message = "Hasło niepoprawne"
            form = PasswordChangeForm(user=request.user)
            return render(request, 'driver/uni_form.html', context={'form': form, 'submit': 'Zapisz', 'message': message})
