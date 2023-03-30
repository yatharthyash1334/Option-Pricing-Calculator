from django.shortcuts import render
from django.http import HttpResponse
from .forms import two_stepForm
from .forms import n_stepForm
from .forms import black_scholesForm

#import maths lib required
import numpy as np
import math
from scipy.stats import norm

# put call parity function
# calculating put from call
def parity(c, K, r, T, S):
    return c + K*np.exp(-1*r*T) - S

# calculation
def twoStep(S, K, r, T, u, d):
    prob = (np.exp(r*T/2) - d)/(u-d)
    Cuu = max(S*u*u-K, 0)
    Cud = max(S*u*d - K, 0)
    Cdd = max(S*d*d - K, 0)
    C = ((prob**2)*Cuu + ((1-prob)**2)*Cdd + 2*prob*(1-prob)*Cud)*np.exp(-1*r*T)
    return C

def nStep(n, S, K, r, T, u, d):
    t = T/n
    prob = (np.exp(r*t) - d)/(u-d)
    Cud = []
    for i in range(n+1):
        c = max(S*(u**i)*(d**(n-i)) - K, 0)
        p = (prob**i)*((1-prob)**(n-i))
        Cud.append(math.comb(n,i)*p*c)
    ans = 0
    for i in Cud:
        ans += i
    return ans*np.exp(-r*T)

def blackScholes(S, K, sd, r, T):
    B = K*np.exp(-r*T)
    lg = np.log(S/B)
    x1 = lg/(sd*(T**0.5)) + 0.5*sd*(T**0.5)
    x2 = lg/(sd*(T**0.5)) - 0.5*sd*(T**0.5)
    x1 = norm.cdf(x1)
    x2 = norm.cdf(x2)
    print(x1, " ", x2)
    return S*x1 - B*x2

# Create your views here.
def home_view(request):
    return render(request, "home.html")

def two_step(request):
    form = two_stepForm()
    context = {}
    context['two'] = form
    if request.method == "POST":
        form = two_stepForm(request.POST)
        if form.is_valid():
            S = float(form.data['stock_price'])
            K = float(form.data['spot_price'])
            r = float(form.data['risk_free_interest_rate'])
            T = float(form.data['maturity_time'])
            u = float(form.data['stock_up_rate'])
            d = float(form.data['stock_down_rate'])
            T = T/12
            r = r/100
            d = 1-d/100
            u = 1+u/100
            print(r, " ", d, " ", u)
            call = twoStep(S, K, r, T, u, d)
            put = parity(call, K, r, T, S)
            context['call'] = call
            context['put'] = put
            return render(request, 'two_step.html', context)
    else:
        return render(request, 'two_step.html', context)

def n_step(request):
    form = n_stepForm()
    context = {}
    context['n'] = form
    if request.method == "POST":
        form = n_stepForm(request.POST)
        if form.is_valid():
            n = int(form.data['steps'])
            S = float(form.data['stock_price'])
            K = float(form.data['spot_price'])
            r = float(form.data['risk_free_interest_rate'])
            T = float(form.data['maturity_time'])
            u = float(form.data['stock_up_rate'])
            d = float(form.data['stock_down_rate'])
            T = T/12
            r = r/100
            d = 1-d/100
            u = 1+u/100
            call = nStep(n, S, K, r, T, u, d)
            put = parity(call, K, r, T, S)
            context['put'] = put
            context['call'] = call
            return render(request, 'n_step.html', context)
    else:
        return render(request, 'n_step.html', context)

def black_scholes(request):
    form = black_scholesForm()
    context = {}
    context['bs'] = form
    if request.method == "POST":
        form = black_scholesForm(request.POST)
        if form.is_valid():
            S = float(form.data['stock_price'])
            K = float(form.data['spot_price'])
            sd = float(form.data['standard_deviation'])
            r = float(form.data['risk_free_interest_rate'])
            T = float(form.data['maturity_time'])
            T = T/12
            r = r/100
            sd = sd/100
            call = blackScholes(S, K, sd, r, T)
            put = parity(call, K, r, T, S)
            context['call'] = call
            context['put'] = put
            return render(request, 'black_schole.html', context)
    else:
        context.pop('put', None)
        return render(request, 'black_schole.html', context)

 

