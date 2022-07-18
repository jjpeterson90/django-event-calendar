from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


# PasswordResetForm > send_mail, get_users, save
# SetPasswordForm > clean_new_password2, save
# PasswordChangeForm(SetPasswordForm) > clean_old_password


class CreateUser(UserCreationForm):
    password2 = None

    class Meta:
        model = get_user_model()
        fields = ("email",)
        