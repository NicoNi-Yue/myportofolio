import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone #melengkapi fungsi is_ongoing yang masih inaccurate

class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='full-time')
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(default=timezone.now) #(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        if self.ended_at is None: 
            return True
        
        return self.ended_at > timezone.now()
    
    @property
    def image(self):
        if self.thumbnail is None:
            return False
        else:
            return True
    
class Education(models.Model):
    EDUCATION_CHOICES = [
        ('SD', 'Elementary School'),
        ('SMP', 'Junior High School'),
        ('SMA', 'Senior High School'),
        ('Kuliah', 'College'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=10, choices=EDUCATION_CHOICES, default='full-time')
    logo = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(default=timezone.now())
    ended_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        if self.ended_at is None: 
            return True
        
        return self.ended_at > timezone.now()
    
    @property
    def image(self):
        if self.logo is None:
            return False
        else:
            return True
    
class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    tech_stack = models.CharField(max_length=255)
    project_url = models.URLField(blank=True)
    project_image_url = models.URLField(blank=True, max_length=500)
    starred_by = models.ManyToManyField(
        User, related_name="starred_projects", blank=True
    )
    
    def __str__(self):
        return self.title
    
#Blank Template
#thumbnail="https://placehold.co/600x400",
#Penjelasan Kode:

# models.Model adalah kelas dasar yang digunakan untuk mendefinisikan model dalam Django.
# Experience adalah nama model yang kamu definisikan.
# EXPERIENCE_CHOICES adalah tuple yang mendefinisikan pilihan kategori pengalaman yang tersedia.
# id adalah field bertipe UUIDField yang digunakan sebagai primary key dan nilainya di-generate otomatis menggunakan uuid.uuid4.
# title adalah field bertipe CharField untuk judul pengalaman, dengan panjang maksimal 255 karakter.
# description adalah field bertipe TextField untuk deskripsi pengalaman yang dapat menampung teks panjang.
# category adalah field bertipe CharField dengan pilihan terbatas sesuai EXPERIENCE_CHOICES, dengan nilai default 'full-time'.
# thumbnail adalah field bertipe URLField untuk menyimpan URL gambar thumbnail pengalaman (opsional).
# started_at adalah field bertipe DateTimeField yang otomatis berisi tanggal dan waktu saat data dibuat.
# ended_at adalah field bertipe DateTimeField yang dapat dibiarkan kosong dan nilainya dapat diatur ke None.
# Method __str__ digunakan untuk mengembalikan representasi string dari objek (dalam hal ini judul pengalaman).
# Decorator @property digunakan untuk membuat atribut read-only yang nilainya merupakan hasil perhitungan dari atribut lain. Dalam kasus ini, is_ongoing akan bernilai True jika ended_at adalah None.

#Full Template
# Experience.objects.create(
#     title="Test C",
#     description="Description of Test C",
#     category="full-time",
#     thumbnail="https://wallpapercave.com/wp/wp9414303.jpg",
#     started_at="2025-11-01",
#     ended_at="2025-12-01"
# )

# Education.objects.create(
#     title="SDs YPPI Perawang",
#     description="",
#     category="SD",
#     logo="https://tse2.mm.bing.net/th/id/OIP.uqMdAol64tmutBk2IJqnZwAAAA?r=0&pid=Api&P=0&h=180",
#     started_at="2013-07-01",
#     ended_at="2019-06-01"
# )