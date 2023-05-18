from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model, logout, login, authenticate
from .forms import RegistrationForm


User = get_user_model()

def register(request):
    if request.method == 'POST':
        # Process the registration form data
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            # Generate the validation link
            current_site = get_current_site(request)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            validation_link = f"{current_site}/validate/{uid}/{token}/"

            # Send validation email
            subject = 'Activate your account'
            message = render_to_string('validation_email.html', {
                'user': user,
                'validation_link': validation_link
            })
            send_mail(subject, message, 'noreply@example.com', [user.email])
            return redirect('registration_complete')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def validate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'validation_successful.html')
    else:
        return render(request, 'validation_failed.html')


def email_validation_view(request, username):
    user = User.objects.get(username=username)
    uid = urlsafe_base64_decode(request.GET.get('uid')).decode()
    token = request.GET.get('token')
    if default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'activation_successful.html')
    else:
        return render(request, 'activation_failed.html')

def logout_view(request):
    logout(request)
    return redirect('login') 


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or return HttpResponse
            return redirect('polls')  # Replace 'dashboard' with your desired URL name or path
        else:
            # Return an error message or render the login page with an error
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')