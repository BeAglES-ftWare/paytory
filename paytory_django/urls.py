"""
URL configuration for paytory_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from paytory.views import submit_expense, submit_income, disable_developer, dev_options, confirm_developer, generate_token, manage_tokens, revoke_token, reset_score
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('submit/expense/', submit_expense),
    path('submit/income/', submit_income),
    path('accounts/', include("django.contrib.auth.urls")),
    path('accounts/', include("accounts.urls")),
    path("", include('paytory.urls')),
    path('devoptions/', dev_options, name='devoptions'),
    path('devoptions_enable', confirm_developer, name='devoptions_enable'),
    path('devoptions_disable/', disable_developer, name='disable_developer'),
    path('tokens/generate/', generate_token, name='generate_token'),
    path('tokens/manage/', manage_tokens, name='manage_tokens'),
    path('tokens/revoke/<int:token_id>/', revoke_token, name='revoke_token'),
    path('reset_score/', reset_score, name='reset_score'),
]
