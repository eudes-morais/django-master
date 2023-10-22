from django import forms
from cars.models import Brand, Car

# O que ocorre aqui, é algo parecido com a camada de controler. Esta camada (FORM)
# está entre os models (entidades) e o banco de dados
# Exemplo enxuto de como funciona a evolução do FORM, o MODELFORM
class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        labels = {'brand_id': 'Brand'}

    # Funções para validação de campos.OBRIGATORIAMENTE começam com a palavra CLEAN
    # O exemplo abaixo cria uma função que valida se o valor do carro é maior que 20k
    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value', 'Valor deve ser maior que 20k')
        return value
    
    # Função que valida a criação de carros com data de fabricação a partir de 1975
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1975:
            self.add_error('factory_year', 'Somente carros a partir de 1975')
        return factory_year
