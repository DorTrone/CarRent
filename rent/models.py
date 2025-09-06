from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    category_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.category_price}₸)"


class Cars(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    car_image = models.ImageField(upload_to='images/')
    year = models.IntegerField()
    mileage = models.IntegerField()
    individual_price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    car_notes = models.TextField(blank=True, null=True, default="")

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"


class Clients(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    driver_licence = models.BooleanField(default=False)
    client_notes = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return self.full_name


class Rents(models.Model):
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    rent_date = models.DateField()
    return_date = models.DateField()
    rent_price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    rent_notes = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Rent'
        verbose_name_plural = 'Rents'

    def __str__(self):
        return f"Rent: {self.client.full_name} - {self.car.brand} {self.car.model}"
