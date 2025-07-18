from django.urls import path
from .views import (
    LopHocListCreateView,
    LopHocDeleteView,
    LopHocUpdateView,
    KhoiDropdownView,
    NienKhoaDropdownView,
    ToHopDropdownView,
    ThemHocSinhVaoLopView,        
    XuatDanhSachLopView            
)

urlpatterns = [
    path('', LopHocListCreateView.as_view()),                         # UC06-01, UC06-04
    path('<int:pk>/', LopHocUpdateView.as_view()),                    # UC06-03
    path('delete/<int:pk>/', LopHocDeleteView.as_view()),            # UC06-02
    path('dropdown/khoi/', KhoiDropdownView.as_view()),              # UC06-05
    path('dropdown/nienkhoa/', NienKhoaDropdownView.as_view()),      # UC06-06
    path('dropdown/tohop/', ToHopDropdownView.as_view()),            # UC06-07

   
    path('<int:pk>/them-hocsinh/', ThemHocSinhVaoLopView.as_view()),     # UC06-08
    path('<int:pk>/xuat-danh-sach/', XuatDanhSachLopView.as_view()),     # UC06-09
]
