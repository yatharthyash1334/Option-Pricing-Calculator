from django import forms

#creating form
class two_stepForm(forms.Form):
    stock_price = forms.DecimalField()
    spot_price = forms.DecimalField()
    risk_free_interest_rate = forms.DecimalField()
    maturity_time = forms.DecimalField(help_text='in months')
    stock_up_rate = forms.DecimalField()
    stock_down_rate = forms.DecimalField()

class n_stepForm(forms.Form):
    steps = forms.IntegerField()
    stock_price = forms.DecimalField()
    spot_price = forms.DecimalField()
    risk_free_interest_rate = forms.DecimalField()
    maturity_time = forms.DecimalField(help_text='in months')
    stock_up_rate = forms.DecimalField()
    stock_down_rate = forms.DecimalField()

class black_scholesForm(forms.Form):
    stock_price = forms.DecimalField()
    spot_price = forms.DecimalField()
    standard_deviation = forms.DecimalField(help_text='in % per annum')
    risk_free_interest_rate = forms.DecimalField()
    maturity_time = forms.DecimalField(help_text='in months')
    
