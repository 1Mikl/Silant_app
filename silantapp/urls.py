from django.urls import path
from .views import *


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('index', Index.as_view()),

    path('info', Info.as_view(), name='info'),
    path('info/<int:pk>', InfoItem.as_view()),
    path('info/<int:pk>/edit', EditCar.as_view()),
    path('info/<int:pk>/delete', DeleteCar.as_view()),
    path('create_car', CreateCar.as_view(), name='create_car'),

    path('maintenance', MaintenanceList.as_view(), name='technicalmaintenance'),
    path('maintenance/<int:pk>', MaintenanceItem.as_view()),
    path('maintenance/<int:pk>/edit', MaintenanceEdit.as_view()),
    path('maintenance/<int:pk>/delete', MaintenanceDelete.as_view()),
    path('create_maintenance', CreateMaintenances.as_view(), name='create_maintenance'),

    path('complaints', ComplaintsList.as_view(), name='complaints'),
    path('complaints/<int:pk>', ComplaintsItem.as_view()),
    path('complaints/<int:pk>/edit', ComplaintsEdit.as_view()),
    path('complaints/<int:pk>/delete', ComplaintsDelete.as_view()),
    path('create_complaints', CreateComplaints.as_view(), name='create_complaints'),

    path('reference_book/', reference_book, name='reference_book'),
    path('reference_book/<int:pk>/', ReferenceBookList.as_view()),
    path('reference_book/1/create/', TechniqueModeCreate.as_view()),
    path('reference_book/1/<int:pk>/edit/', TechniqueModelEdit.as_view()),
    path('reference_book/2/create/', EngineModelCreate.as_view()),
    path('reference_book/2/<int:pk>/edit/', EngineModelEdit.as_view()),
    path('reference_book/3/create/', TransmissionModelCreate.as_view()),
    path('reference_book/3/<int:pk>/edit/', TransmissionModelEdit.as_view()),
    path('reference_book/4/create/', DriveBridgeModelCreate.as_view()),
    path('reference_book/4/<int:pk>/edit/', DriveBridgeModelEdit.as_view()),
    path('reference_book/5/create/', SteerableBridgeModelCreate.as_view()),
    path('reference_book/5/<int:pk>/edit/', SteerableBridgeModelEdit.as_view()),
    path('reference_book/6/create/', ServiceCompanyCreate.as_view()),
    path('reference_book/6/<int:pk>/edit/', ServiceCompanyEdit.as_view()),
    path('reference_book/7/create/', TypeMaintenanceCreate.as_view()),
    path('reference_book/7/<int:pk>/edit/', TypeMaintenanceEdit.as_view()),
    path('reference_book/8/create/', DescriptionFailureCreate.as_view()),
    path('reference_book/8/<int:pk>/edit/', DescriptionFailureEdit.as_view()),
    path('reference_book/9/create/', RecoveryMethodCreate.as_view()),
    path('reference_book/9/<int:pk>/edit/', RecoveryMethodEdit.as_view()),

]
