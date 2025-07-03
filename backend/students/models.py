from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

class HocSinh(models.Model):
    Ho = models.CharField(max_length=50)
    Ten = models.CharField(max_length=50)
    GioiTinh = models.CharField(max_length=10)
    NgaySinh = models.DateField()
    DiaChi = models.CharField(max_length=255)
    Email = models.EmailField(unique=True, null=True, blank=True)
    IDNienKhoaTiepNhan = models.ForeignKey('configurations.NienKhoa', on_delete=models.PROTECT)

    def __str__(self): 
        return f"{self.Ho} {self.Ten}"

    class Meta: 
        db_table = 'HOCSINH'
        verbose_name = 'Học sinh'
        verbose_name_plural = 'Học sinh'

    def clean(self):
        super().clean()  # Gọi clean() của lớp cha
        
        today = date.today()
        age = today.year - self.NgaySinh.year - ((today.month, today.day) < (self.NgaySinh.month, self.NgaySinh.day))
        min_age = 15
        max_age = 20
        
        if age < min_age or age > max_age:
            raise ValidationError(f"Học sinh phải từ {min_age} đến {max_age} tuổi.")

        if self.IDNienKhoaTiepNhan:
            try:
                nien_khoa_start_year = int(self.IDNienKhoaTiepNhan.TenNienKhoa.split('-')[0])
                # Giả sử học sinh phải ít nhất 15 tuổi khi vào niên khóa
                if (nien_khoa_start_year - self.NgaySinh.year) < 15:
                    raise ValidationError("Năm sinh không phù hợp với niên khóa.")
            except (ValueError, IndexError):
                raise ValidationError("Định dạng niên khóa không hợp lệ.")