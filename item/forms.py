from django import forms
from .models import Item, Profile
INPUT_CLASSES ='w-full py-4 px-6 rounded-xl border'
INPUT_PROFILE='w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model =Item

        fields =('category', 'name', 'description', 'price', 'image') 
        
        widgets ={
            'category': forms.Select(attrs={
                'class':INPUT_CLASSES
            }),
            
            'name': forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            
            'description': forms.Textarea(attrs={
                'class':INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            
            'image': forms.FileInput(attrs={
                'class':INPUT_CLASSES
            })
        }
        
        
class EditItemForm(forms.ModelForm):
    class Meta:
        model =Item

        fields =('name', 'description', 'price', 'image', 'is_sold') 
        
        widgets ={
            
            'name': forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            
            'description': forms.Textarea(attrs={
                'class':INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            
            'image': forms.FileInput(attrs={
                'class':INPUT_CLASSES
            })
        }        
        
        
        
class CreateprofileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields =['first_name', 'last_name', 'age', 'prof_image', 'degree', 'email', 'product_selling', 
                 'decription']
        
        widgets ={
            'first_name': forms.TextInput(attrs={
                'class':INPUT_PROFILE
            }),
            'last_name': forms.TextInput(attrs={
                'class':INPUT_PROFILE
            }),
            'age':forms.NumberInput(attrs={
                'class':INPUT_PROFILE
            }),
            'prof_image': forms.FileInput(attrs={
                'class':INPUT_PROFILE
            }),
            'degree': forms.TextInput(attrs={
                'class':INPUT_PROFILE
            }),
            'email':forms.EmailInput(attrs={
                'class':INPUT_PROFILE
            }),
            'product_selling':forms.Textarea(attrs={
                'class':INPUT_PROFILE
            }),
            'decription':forms.Textarea(attrs={
                'class':INPUT_PROFILE
            })
        }