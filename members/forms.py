from django import forms

from .models import Member


class MemberForm(forms.ModelForm):

    class Meta:
        model = Member
        fields = ("full_name", "email", "title", "bio", "city", "github",
                  "twitter", "linkedin", "facebook", "instagram", "website", "picture",)
        widgets = {
            'full_name': forms.TextInput(
                attrs={
                    'placeholder': 'Prénom et Nom',
                    'class': 'w-full px-3 py-2 outline-none text-black',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Adresse Email',
                    'class': 'w-full px-3 py-2 outline-none text-black',
                }
            ),
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Titre',
                    'class': 'w-full px-3 py-2 outline-none text-black',
                }
            ),
            'bio': forms.Textarea(
                attrs={
                    'placeholder': 'Bio',
                    'class': 'w-full px-3 py-2 outline-none text-black',
                    'rows': 4,
                }
            ),
            'city': forms.TextInput(
                attrs={
                    'placeholder': 'Ville',
                    'class': 'w-full px-3 py-2 outline-none text-black',
                }
            ),
            'github': forms.TextInput(
                attrs={
                    'placeholder': 'Compte Github',
                    'class': 'w-full px-3 py-2 outline-none text-black',
                }
            ),
            'linkedin': forms.TextInput(
                attrs={
                    'placeholder': 'Compte Linkedin',
                    'class': 'w-full px-3 py-2 outline-none text-black',
                }
            ),
            'facebook': forms.TextInput(
                attrs={
                    'placeholder': 'Compte Facebook',
                    'class': 'w-full px-3 py-2 outline-none text-black',
                }
            ),
            'instagram': forms.TextInput(
                attrs={
                    'placeholder': 'Compte Instagram',
                    'class': 'w-full px-3 py-2 outline-none text-black',
                }
            ),
            'website': forms.TextInput(
                attrs={
                    'placeholder': 'Site Web',
                    'class': 'w-full px-3 py-2 outline-none text-black',
                }
            ),
            'twitter': forms.TextInput(
                attrs={
                    'placeholder': 'Compte Twitter',
                    'class': 'w-full px-3 py-2 outline-none text-black',
                }
            ),
        }
