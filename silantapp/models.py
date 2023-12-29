from django.db import models
from django.contrib.auth.models import User


class Technique_model(models.Model):
    name = models.TextField(unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Модель техники'
        verbose_name_plural = 'Модели техники'


class Engine_model(models.Model):
    name = models.TextField(unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Модель двигателя'
        verbose_name_plural = 'Модели двигателей'


class Transmission_model(models.Model):
    name = models.TextField(unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Модель трансмиссии'
        verbose_name_plural = 'Модели трансмиссий'


class Drive_bridge_model(models.Model):
    name = models.TextField(unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Модель ведущего моста'
        verbose_name_plural = 'Модели ведущих мостов'


class Steerable_bridge_model(models.Model):
    name = models.TextField(unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Модель управляемого моста'
        verbose_name_plural = 'Модели управляемых мостов'


class ClientUser(User):
    class Meta:
        proxy = True

    def __str__(self):
        return self.first_name


class Service_company(models.Model):
    user = models.OneToOneField(ClientUser, on_delete=models.CASCADE, verbose_name='Имя пользователя')
    name = models.TextField(unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Сервисные компании'
        verbose_name_plural = 'Сервисные компании'


class Car(models.Model):
    factory_number = models.TextField(max_length=20, unique=True, db_index=True, verbose_name='Заводской номер')
    technique_model = models.ForeignKey(Technique_model, on_delete=models.CASCADE, db_index=True, verbose_name='Модель техники')
    engine_model = models.ForeignKey(Engine_model, on_delete=models.CASCADE, db_index=True, verbose_name='Модель двигателя')
    engine_number = models.TextField(max_length=20, verbose_name='Номер двигателя')
    transmission_model = models.ForeignKey(Transmission_model, on_delete=models.CASCADE, db_index=True, verbose_name='Модель трансмиссии')
    transmission_number = models.TextField(max_length=20, verbose_name='Номер трансмиссии')
    drive_bridge_model = models.ForeignKey(Drive_bridge_model, on_delete=models.CASCADE, db_index=True, verbose_name='Модель ведущего моста')
    drive_bridge_number = models.TextField(max_length=20, verbose_name='Номер ведущего моста')
    controlled_bridge_model = models.ForeignKey(Steerable_bridge_model, on_delete=models.CASCADE, db_index=True, verbose_name='Модель управляемого моста')
    controlled_bridge_number = models.TextField(max_length=20, verbose_name='Номер управляемого моста')
    delivery_agreement = models.TextField(max_length=40, blank=True, verbose_name="Договор поставки №, дата")
    date_of_shipment_from_the_factory = models.DateField(db_index=True, verbose_name="Дата отгрузки с завода")
    consignee = models.TextField(max_length=40, blank=True, verbose_name="Грузополучатель")
    delivery_address = models.TextField(max_length=150, blank=True, verbose_name='Адрес поставки (эксплуатации)')
    equipment = models.TextField(blank=True, verbose_name='Комплектация (доп. опции)')
    client = models.ForeignKey(ClientUser, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Клиент')
    service_company = models.ForeignKey(Service_company, null=True, on_delete=models.CASCADE, blank=True, verbose_name='Сервисная компания')

    def __str__(self):
        return f'{self.factory_number}'

    class Meta:
        verbose_name = 'Машины'
        verbose_name_plural = 'Машины'
        ordering = ['date_of_shipment_from_the_factory']


class Type_maintenance(models.Model):
    name = models.TextField(verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Вид ТО'
        verbose_name_plural = 'Вид ТО'


class TechnicalMaintenance(models.Model):
    type_maintenance = models.ForeignKey(Type_maintenance, on_delete=models.CASCADE, verbose_name='Вид ТО')
    maintenance_date = models.DateField(verbose_name='Дата проведения ТО')
    operating_time = models.IntegerField(verbose_name='Наработка м/час')
    order = models.TextField(max_length=40, verbose_name='Номер заказа-наряда')
    order_date = models.DateField(verbose_name='Дата заказа-наряда')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Машина')
    service_company = models.ForeignKey(Service_company, on_delete=models.CASCADE, verbose_name='Сервисная компания')

    def __str__(self):
        return f'{self.car, self.type_maintenance}'

    class Meta:
        verbose_name = 'ТО'
        verbose_name_plural = 'ТО'
        ordering = ['maintenance_date']


class Failure_node(models.Model):
    name = models.TextField(verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Узел отказа'
        verbose_name_plural = 'Узел отказа'


class Recovery_method(models.Model):
    name = models.TextField(verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Способ восстановления'
        verbose_name_plural = 'Способ восстановления'


class Complaints(models.Model):
    date_of_refusal = models.DateField(verbose_name='Дата отказа')
    operating_time = models.IntegerField(verbose_name='Наработка м/час')
    failure_node = models.ForeignKey(Failure_node, on_delete=models.CASCADE, verbose_name='Узел отказа')
    description_failure = models.TextField(verbose_name='Описание отказа')
    recovery_method = models.ForeignKey(Recovery_method, on_delete=models.CASCADE, verbose_name='Способ восстановления')
    parts_used = models.TextField(blank=True, verbose_name='Используемые запасные части')
    date_of_restoration = models.DateField(verbose_name='Дата восстановления')
    equipment_downtime = models.TextField(verbose_name='Время простоя техники')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Машина')
    service_company = models.ForeignKey(Service_company, on_delete=models.CASCADE, verbose_name='Сервисная компания')

    def __str__(self):
        return f'{self.car, self.failure_node}'

    class Meta:
        verbose_name = 'Рекламации'
        verbose_name_plural = 'Рекламации'
        ordering = ['date_of_refusal']