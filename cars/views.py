from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

# Reescrevendo as views utilizando CBV. A vantagem é a organização do código.
# Que agora se assemelha a uma classe e tem um método que será executado
class CarsListView(ListView):
    # Os nomes MODEL, TEMPLATE_NAME e CONTEXT_OBJECT_NAME devem ser respeitado e
    # digitados corretamente, pois são ATRIBUTOS de LISTVIEW que devem ser passados!
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')

        if search:
            cars = cars.filter(model__icontains=search).order_by('model')
        
        return cars

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'


# O decorator abaixo serve para adicionar uma nova funcionalidade na classe que
# ele está sendo declarado. Neste caso, o decorator login_required verifica se o
# usuário está logado. Caso não esteja ele é redirecionado para a tela de login
@method_decorator(login_required(login_url='login'), name='dispatch')
class CarCreateView(CreateView):
    # Como esta classe herda as propriedades de CREATEVIEW, cabe a propria classe,
    # na hora em que ela é requisitada, 'descobrir' se é uma operação GET ou POST
    model = Car
    form_class = CarModelForm 
    template_name = 'new_car.html'
    success_url = '/cars'
    # Ou se usa o atributo FORM_CLASS ou FIELDS, os dois atributos não podem ser utilizados ao mesmo tempo
    # fields = ["brand_id", "model", "factory_year", "model_year", "value", "plate", "photo"]

    # Aqui também ocorre que todas as informações quando forem carregadas no template (aqui no caso é o NEW_CAR.HTML),
    # Vem no contexto FORM, por isso, lá no template, deve-se colocar apenas 'form'. No case do template new_car.html,
    # Será criado uma tabela, logo, é passado o contexto {{ form.as_table }}

@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'
    # No lugar do sucess_url abaixo, será usada a função get_success_url
    # success_url = '/cars' 

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})
    
@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'
    