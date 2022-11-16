from django.contrib import admin
from django.urls import path
from MyPage.views import MyPagess, create, editar, back, update, delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MyPagess),
    path('back/', back, name='back'),
    path('create/', create, name='create'),
    path('editar/<int:id>/', editar, name='editar'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>/', delete, name='delete')
]
