from django import forms
from .models import NippoModel

class NippoModelForm(forms.ModelForm):
    class Meta:
        model = NippoModel
        fields = "__all__"
    def __init__(self, *args, **kwargs):
        for field in self.base_fields.values():
            field.widget.attrs["class"] = "form-control"
        super().__init__(*args, **kwargs)


class NippoFormClass(forms.Form):
    title = forms.CharField(max_length=100, label="タイトル")
    content = forms.CharField(widget = forms.Textarea(), max_length=1000, label="内容")
    def __init__(self, *args, **kwargs):
        for field in self.base_fields.values():
            field.widget.attrs["class"] = "form-control"
        super().__init__(*args, **kwargs)




class NippoModelForm(forms.ModelForm):
    class Meta:
        model = NippoModel
        exclude = ["user"]
        # fields = "__all__"
    def __init__(self, *args, **kwargs):
        for key, field in self.base_fields.items():
            if key != "public":
                field.widget.attrs["class"] = "form-control"
            else:
                field.widget.attrs["class"] = "form-check-input"
        super().__init__(*args, **kwargs)
                