# Este arquivo é responsável por capturar e executar eventos dentro
# do banco de dados. Ele é divido em: PRÉ SAVE (antes de salvar/alterar/deletar no BD) 
# e POST SAVE (depois que salvar/alterar/deletar no BD)

from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from cars.models import Car, CarInventory
from django.db.models import Sum
from openai_api.client import get_car_ai_desc


def car_inventory_update():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value = Sum('value')
    )['total_value']
    CarInventory.objects.create(
        cars_count = cars_count,
        cars_value = cars_value
    )

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.description:
        ai_desc = get_car_ai_desc(instance.model, instance.brand_id, instance.model_year)
        instance.description = ai_desc

# Os parâmetros são obrigatórios
@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()
    

@receiver(post_delete, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()