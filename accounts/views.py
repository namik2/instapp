from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from accounts.forms import LoginForm,RegistrationForm



# def login(request):
#     form=LoginForm()
#     context = {
#         'form':form
#     }
#     return render(request,'login.html',context)

# def registr(request):
#     form=RegistrationForm()
#     context = {
#         'form':form
#     }

#     return render(request,'register.html',context)

class CustomLoginView(LoginView):
    template_name ='login.html'
    form_class = LoginForm
    success_url = reverse_lazy('register')  # duzenlemek
   
class RegisterView(CreateView):
    template_name = 'registr.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    
   