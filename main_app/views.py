from django.shortcuts import render
from .models import Planet
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User

# def profile(request, username):
#     user = User.objects.get(username=username)
#     Planets = Planet.objects.filter(user=user)
#     return render(request, 'profile.html', {'username': username, 'planets': planets})

def index(request):
    return render(request, 'index.html')

# def about(request):
#     return render(request, 'about.html')

def planets_index(request):
    planets = Planet.objects.all()
    return render(request, 'planets/index.html', {'planets': planets})
def planets_show(request, planet_id):
    planets = Planet.objects.get(id=planet_id)
    return render(request, 'planets/show.html', {'planet': planet})

class PlanetAdd(CreateView):
    model = Planet
    fields = '__all__'
    success_url = '/planet'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/planets')

class PlanetUpdate(UpdateView):
    model = Planet
    fields = ['name', 'type', 'description', 'mass', 'distance', 'parent_star', 'dist_from_star']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/planets')

class PlanetDelete(DeleteView):
    model = Planet
    success_url = '/planets'
