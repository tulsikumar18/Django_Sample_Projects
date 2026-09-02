from CBVapp.models import Company
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponse
from django.shortcuts import render


from django.views.generic import View , TemplateView
# Create your views here.


# this is Class Based Views.. 
# It needs less code to write and it is easy to write , however the function BASED views are easy to understand.. 
# 
class myClass(View):

    def get(self, request):

        return HttpResponse('<h1> Helloo Sulululu.. </h1>')


        
class home_view(TemplateView):
    template_name = 'home.html'



# internally ListView will look for modelname_list.html page ('company_list.html') inside the CBVapp/templates/
class allCompany(ListView):

    model = Company




class CompanyDetails(DetailView):

    model = Company # it will look for company_detail.html page in the template of CBVapp in CBVapp

    context_object_name = 'company_detail'



class AddCompany(CreateView):

    model = Company
    fields = '__all__'  # in the createview, it automatically creates the object  and renders it in the form.
                        # It will look for the modelname.form.html file (i.e company_form.html in templates/CBVap/html_file)
    