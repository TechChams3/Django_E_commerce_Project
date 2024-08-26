from django.shortcuts import render
from django.shortcuts import redirect,render
# Create your views here.
from django.views import generic
from .models import OrderItem
from .forms import CheckoutForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import JsonResponse




class Checkout(LoginRequiredMixin,generic.View):
    login_url = reverse_lazy('login')
    def get(self,*args,**kwargs):
        form = CheckoutForm()
        context = {
            'form':form
        }
        return render(self.request,'order/cheackout.html',context)
    

    def post(self,*args,**kwargs):
        form = CheckoutForm(self.request.POST)

        if form.is_valid():
            data = form.cleaned_data
            print(data)
            return JsonResponse({
                "success":True,
                "errors":None
            })
        else:
            return JsonResponse({
                "success":False,
                "errors":dict(form.errors)
            })




