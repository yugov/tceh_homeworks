from wtforms_alchemy import ModelForm
from models.user import User


class UserForm(ModelForm):
    class Meta:
        model = User
