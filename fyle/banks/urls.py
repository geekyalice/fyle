from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^get_bank_details/', views.BankDetails.as_view(), name='bank_details'),
    url(r'^get_branch_bank_data/', views.BankBranchDetails.as_view(), name='bank_branch_details')
]