from django.urls import path, include

urlpatterns = [
    path('foo/', include('myapp.foo.urls'))
]
