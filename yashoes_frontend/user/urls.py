from django.urls import path
from yashoes_frontend.user.views import profile,transaction, transactiondetail
urlpatterns = [
    path('user/profile/', profile, name="profile"),
    path('user/transactions/', transaction, name="transaction"),
    path('user/transactions/<int:id>/', transactiondetail, name="transactiondetail"),
]

