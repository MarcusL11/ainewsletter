from django.contrib.auth import login
from django.contrib.auth.tokens import default_token_generator
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.utils.http import urlsafe_base64_decode
from django.views import View

from .forms import CreateUserForm
from .models import Subscription, User
from .services import decode_uid, get_user_by_uid, send_sign_in_email


def verify_email(request: HttpRequest, uidb64: str, token: str) -> HttpResponse:
    """
    Verify user email after the user clicks on the email link.
    """
    uid = decode_uid(uidb64)
    user = get_user_by_uid(uid) if uid else None

    if user and default_token_generator.check_token(user, token):
        user.has_verified_email = True
        user.save()
        subscription, created = Subscription.objects.get_or_create(email=user)
        subscription.save()        
        login(request, user)
        return redirect('home')

    print("Email verification failed")    
    return redirect('sign_in')


class SendSignInEmail(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        if not request.user.is_anonymous and request.user.has_verified_email:
            return redirect('home')
        form = CreateUserForm()
        return render(request, 'authapp/sign_in.html', {'form': form})

    def post(self, request: HttpRequest) -> HttpResponse:
        data = {
            'username': request.POST['email'],
            'email': request.POST['email'],
            'password': request.POST['email']
        }
        user, created = User.objects.get_or_create(
            email=data['email'],
            defaults={'username': data['email'], 'password': data['email']}
        )

        return self._send_verification_and_respond(user)

    @staticmethod
    def _send_verification_and_respond(user: User) -> HttpResponse:
        send_sign_in_email(user)
        message = (
            f"We've sent an email ✉️ to "
            f'<a href=mailto:{user.email}" target="_blank">{user.email}</a> '
            "Please check your email to verify your account"
        )
        return HttpResponse(message)


def sign_out(request: HttpRequest) -> HttpResponse:
    request.session.flush()
    return redirect('sign_in')


def dashboard(request: HttpRequest) -> HttpResponse:
    if not request.user.is_anonymous and request.user.has_verified_email:
        return render(request, 'authapp/dashboard.html')
    else:
        return redirect('sign_in')

def unsubscribe(request: HttpRequest) -> HttpResponse:
    if not request.user.is_anonymous and request.user.has_verified_email and request.method == 'POST':  # noqa: E501
        user = request.user
        user.subscription.status = False
        user.subscription.save()

        message = (
            "You have successfully unsubscribed from our newsletter."
        )
        return HttpResponse(message)

def subscribe(request: HttpRequest) -> HttpResponse:
    if not request.user.is_anonymous and request.user.has_verified_email and request.method == 'POST':  # noqa: E501
        user = request.user
        user.subscription.status = True
        user.subscription.save()

        message = (
            "You have successfully subscribed to our newsletter."
        )
        return HttpResponse(message)
    
def subscribe_only(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        email = request.POST.get('email', '')
        
        try:
            validate_email(email)
        except ValidationError:
            message = "Invalid email address."
            return HttpResponse(message)

        user, created = User.objects.get_or_create(
            email=email,
            defaults={'username': email, 'password': email}
        )        
        
        subscriber, subscriber_created = Subscription.objects.get_or_create(email=user)
        subscriber.status = True
        subscriber.save()
        
        message = "You have subscribed to our newsletter."
        
        return HttpResponse(message)
