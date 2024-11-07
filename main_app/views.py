from django.shortcuts import render, redirect
from .models import Musician
from .forms import MusicForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class MusicianCreate(LoginRequiredMixin, CreateView):
    model = Musician
    fields = ['name', 'description', 'age']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class MusicianUpdate(LoginRequiredMixin, UpdateView):
    model = Musician
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = ['description', 'age']

class MusicianDelete(LoginRequiredMixin, DeleteView):
    model = Musician
    success_url = '/musicians/'

class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')


@login_required
def musicians_index(request):
    #search psql all cats
    musician = Musician.objects.filter(user=request.user)
    return render(request, 'musicians/index.html', {'musicians': musician})


def musicians_detail(request, musician_id):
    musician = Musician.objects.get(id=musician_id)
    music_form = MusicForm()
    return render(request, 'musicians/detail.html', {'musician': musician, 'music_form': music_form})


@login_required
def add_music(request, musician_id):
    form = MusicForm(request.POST)
    if form.is_valid():
        new_music = form.save(commit=False)
        new_music.musician_id =  musician_id
        new_music.save()
    return redirect('musician-detail', musician_id = musician_id)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in
            login(request, user)
            return redirect('musician-index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)