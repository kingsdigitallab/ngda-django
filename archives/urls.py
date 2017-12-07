# from django.conf import settings
# from django.conf.urls import include, url
from django.conf.urls import url
# from django.contrib import admin
from archives.views import home, fullTransactionRecord

urlpatterns = [
    url(r'^full-record/(\d+)$', fullTransactionRecord,
        name='full_transaction_record'),
    url(r'', home, name='home_page'),
]
