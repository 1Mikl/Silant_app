from django import forms
from .models import *


class FactoryNumber(forms.Form):
    factory_number = forms.CharField(label='Заводской номер', widget=forms.TextInput(attrs={'size': 8}),
                                     max_length=10)


class CreateCarForm(forms.ModelForm):
    client = forms.ModelChoiceField(
        queryset=ClientUser.objects.filter(groups__name='client').order_by('first_name')
    )

    class Meta:
        model = Car
        widgets = {'factory_number': forms.Textarea(attrs={'rows': 1}),
                   'engine_number': forms.Textarea(attrs={'rows': 1}),
                   'transmission_number': forms.Textarea(attrs={'rows': 1}),
                   'drive_bridge_number': forms.Textarea(attrs={'rows': 1}),
                   'controlled_bridge_number': forms.Textarea(attrs={'rows': 1}),
                   'delivery_agreement': forms.Textarea(attrs={'rows': 1}),
                   'consignee': forms.Textarea(attrs={'rows': 1}),
                   'delivery_address': forms.Textarea(attrs={'rows': 2}),
                   'equipment': forms.Textarea(attrs={'rows': 5}),
                   'date_of_shipment_from_the_factory': forms.NumberInput(attrs={'type': 'date'}),
                   }
        fields = '__all__'


class CreateMaintenancesForm(forms.ModelForm):
    class Meta:
        model = TechnicalMaintenance
        fields = '__all__'
        widgets = {'order': forms.Textarea(attrs={'rows': 1}),
                   'maintenance_date': forms.NumberInput(attrs={'type': 'date'}),
                   'order_date': forms.NumberInput(attrs={'type': 'date'}),
                   'car': forms.HiddenInput(),

                   }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        service_company = kwargs.pop('initial')['service_company']
        self.fields['service_company'].initial = service_company


class UpdateMaintenancesForm(forms.ModelForm):
    class Meta:
        model = TechnicalMaintenance
        fields = '__all__'
        widgets = {'order': forms.Textarea(attrs={'rows': 1}),
                   'maintenance_date': forms.NumberInput(attrs={'type': 'date'}),
                   'order_date': forms.NumberInput(attrs={'type': 'date'}),
                   'car': forms.HiddenInput(),
                   # 'service_company': forms.widgets.Select(attrs={'disabled': 'disabled'})
                   'service_company': forms.HiddenInput()
                   }


class CreateComplaintsForm(forms.ModelForm):
    class Meta:
        model = Complaints
        fields = '__all__'
        widgets = {'date_of_refusal': forms.NumberInput(attrs={'type': 'date'}),
                   'parts_used': forms.Textarea(attrs={'rows': 1}),
                   'description_failure': forms.Textarea(attrs={'rows': 2}),
                   'date_of_restoration': forms.NumberInput(attrs={'type': 'date'}),
                   'equipment_downtime': forms.Textarea(attrs={'rows': 1}),
                   'car': forms.HiddenInput(),
                   'service_company': forms.HiddenInput(),
                   }

    def __init__(self, *args, **kwargs):
        super(CreateComplaintsForm, self).__init__(*args, **kwargs)


class UpdateComplaintsForm(forms.ModelForm):
    class Meta:
        model = Complaints
        fields = '__all__'
        widgets = {'date_of_refusal': forms.NumberInput(attrs={'type': 'date'}),
                   'parts_used': forms.Textarea(attrs={'rows': 1}),
                   'date_of_restoration': forms.NumberInput(attrs={'type': 'date'}),
                   'equipment_downtime': forms.Textarea(attrs={'rows': 1}),
                   'car': forms.HiddenInput(),
                   'service_company': forms.HiddenInput()
                   }


class UpdateTechniqueModelForm(forms.ModelForm):
    class Meta:
        model = Technique_model
        fields = '__all__'
        widgets = {'name': forms.Textarea(attrs={'rows': 1}),}


class UpdateEngineModelForm(forms.ModelForm):
    class Meta:
        model = Engine_model
        fields = '__all__'
        widgets = {'name': forms.Textarea(attrs={'rows': 1}),}


class UpdateTransmissionModelForm(forms.ModelForm):
    class Meta:
        model = Transmission_model
        fields = '__all__'
        widgets = {'name': forms.Textarea(attrs={'rows': 1}),}


class UpdateDriveBridgeModelForm(forms.ModelForm):
    class Meta:
        model = Drive_bridge_model
        fields = '__all__'
        widgets = {'name': forms.Textarea(attrs={'rows': 1}),}


class UpdateSteerableBridgeModelForm(forms.ModelForm):
    class Meta:
        model = Steerable_bridge_model
        fields = '__all__'
        widgets = {'name': forms.Textarea(attrs={'rows': 1}),}


class CreateServiceCompanyForm(forms.ModelForm):
    class Meta:
        model = Service_company
        fields = '__all__'
        widgets = {'name': forms.Textarea(attrs={'rows': 1}),}


class UpdateServiceCompanyForm(forms.ModelForm):
    class Meta:
        model = Service_company
        fields = '__all__'
        # exclude = ('user',)
        widgets = {'name': forms.Textarea(attrs={'rows': 1}), 'user': forms.HiddenInput(),}


class UpdateTypeMaintenanceForm(forms.ModelForm):
    class Meta:
        model = Type_maintenance
        fields = '__all__'
        widgets = {'name': forms.Textarea(attrs={'rows': 1}),}


class UpdateDescriptionFailureForm(forms.ModelForm):
    class Meta:
        model = Failure_node
        fields = '__all__'
        widgets = {'name': forms.Textarea(attrs={'rows': 1}),}


class UpdateRecoveryMethodForm(forms.ModelForm):
    class Meta:
        model = Recovery_method
        fields = '__all__'
        widgets = {'name': forms.Textarea(attrs={'rows': 1}), }



