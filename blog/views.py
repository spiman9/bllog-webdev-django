
from email import message
from django.urls import reverse 
from django.shortcuts import render , get_object_or_404, redirect


# Create your views here.
from django.views.generic import (CreateView , DetailView , ListView , UpdateView , DeleteView)
from .models import Article
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User , auth

# forms import
from .forms import ArticleModelForm

class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article , id=id_)

    def get_success_url(self):
        return reverse('articles:article-list')

class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    model = Article
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def form_valid(self , form):
        form.save()
        print(form.cleaned_data)
        messages.success(self.request, "Blog Updated Successfully !!!" )
        return super().form_valid(form)

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article , id=id_)

class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    model = Article
    form_class = ArticleModelForm
    queryset = Article.objects.all()
    # success_url = '/'

    def form_valid(self , form):
        form.save()
        print(form.cleaned_data)
        messages.success(self.request, "Blog Created Successfully !!!" )
        return super().form_valid(form)


class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()    #<blog>/<modelsname>_list.html

    
class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article , id=id_)



def home_view(request , *args , **kwargs):
    context = {}
    return render(request , 'home.html' , context)


def about_view(request , *args , **kwargs):
    context = {
    }
    return render(request , 'about.html' , context)


def contact_view(request , *args , **kwargs):
    context = {
    }
    return render(request , 'contact.html' , context)




def loginuser(request):
    if request.method == 'POST':
        user = auth.authenticate(username = request.POST['uname'] , password = request.POST['password'])
        if user is not None:
            auth.login(request , user)
            print("Loogin")
            messages.success(request, "Successfully Login!!! " , {request.user}) 
            return redirect("/")
    return render(request , 'loginuser.html')

def logoutuser(request):
    auth.logout(request)
    messages.success(request, "Logout Succesfully!!! " ) 
    return redirect("/")

def register(request):
    if request.method == 'POST':
        if User.objects.filter(username=request.POST['uname']).exists():
            print("Username already exists!!!")
        elif User.objects.filter(email = request.POST['email']).exists():
            print("Email Already Exists !!!")
        else:
            u = User.objects.create_user(username = request.POST['uname'] , first_name=request.POST['fname'] , last_name = request.POST['lname'] , password=request.POST['password'] , email = request.POST['email'])
            u.save()
            messages.success(request, "Successfully Registered!!!" )
        return redirect("/")
    return render(request , 'register.html')