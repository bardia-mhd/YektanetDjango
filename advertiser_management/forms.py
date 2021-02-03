from django import forms


class AdForm(forms.Form):
    advertiser_id = forms.IntegerField()
    img = forms.ImageField()
    title = forms.CharField()
    link = forms.CharField()


class AdDetailForm(forms.Form):
    ad_id = forms.IntegerField()
