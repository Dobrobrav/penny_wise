from django.contrib.auth import get_user_model, authenticate, login
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import View

User = get_user_model()


def home(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        template_name='penny_wise/index.html',
        context={'user': request.user},
    )


class SignupView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, template_name='registration/signup.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        creds = request.POST
        User.objects.create_user(username=creds['username'], password=creds['password'])

        # TODO: reuse login logic in LoginView
        user = authenticate(request, username=creds['username'], password=creds['password'])
        if user is None:
            return HttpResponse('Invalid credentials', status=401)

        login(request, user=user)
        return redirect(to='home')
