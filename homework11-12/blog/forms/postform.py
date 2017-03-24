from wtforms_alchemy import ModelForm
from models.post import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        include = [
            'user_id',
        ]
        exclude = [
            'visible',
        ]
