from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Talaba(models.Model):
    ism = models.CharField(max_length=255)
    guruh = models.CharField(max_length=100)
    kurs = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], default=1
    )
    kitob_soni = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.ism


class Muallif(models.Model):
    JINS_CHOICES = (
        ('Erkak', 'Erkak'),
        ('Ayol', 'Ayol'),
    )

    ism = models.CharField(max_length=255)
    jins = models.CharField(max_length=20, choices=JINS_CHOICES)
    t_sana = models.DateField(null=True)
    kitob_soni = models.PositiveSmallIntegerField(null=True)
    tirik = models.BooleanField(default=False)

    def __str__(self):
        return self.ism


class Kitob(models.Model):
    nom = models.CharField(max_length=255)
    janr = models.CharField(max_length=50)
    sahifa = models.PositiveSmallIntegerField()
    muallif = models.ForeignKey(Muallif, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        if self.muallif:
            return f"{self.muallif}: {self.nom}"
        return self.nom


class Kutubxonachi(models.Model):
    ism = models.CharField(max_length=255)
    ish_vaqti = models.TimeField()

    def __str__(self):
        return self.ism


class Record(models.Model):
    talaba = models.ForeignKey(Talaba, on_delete=models.SET_NULL, null=True)
    kitob = models.ForeignKey(Kitob, on_delete=models.CASCADE)
    kutubxonachi = models.ForeignKey(Kutubxonachi, on_delete=models.SET_NULL, null=True)
    olingan_sana = models.DateField(auto_now_add=True)
    qaytargan_sana = models.DateField(blank=True, null=True)
    qaytardi = models.BooleanField(default=False)

    def __str__(self):
        if self.talaba:
            return f"{self.talaba}: {self.kitob.nom}"
        return f"[Record] {self.kitob.nom}"
