from django.db import models
#I put the order of the models in a way so that no dependecy issues when 
#you make migrations

#Sales Person Model with salesperson_id as a primary_key
class Salesperson(models.Model):
    salesperson_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)

    
#Mechanic Model with machanic_id as a primary key
class Mechanic(models.Model):
    mechanic_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)

 
#Car Model with car ID as a primary key
class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    serial_number = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    colour = models.CharField(max_length=50)
    year = models.IntegerField()
    car_for_sale = models.BooleanField()

 
#Customer model with customer_id as a primary key
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

 
#Service model with service_id as primary key
class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=100)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)


#Parts model with parts_id as a primary key
class Parts(models.Model):
    parts_id = models.AutoField(primary_key=True)
    part_number = models.CharField(max_length=100)
    description = models.TextField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    retail_price = models.DecimalField(max_digits=10, decimal_places=2)


#SalesInvoice model with invoice_id as a primary key 
#car,customerand salesperson attributes as foreign keys
class SalesInvoice(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    invoice_number = models.CharField(max_length=100)
    date = models.DateField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    salesperson = models.ForeignKey(Salesperson, on_delete=models.CASCADE)

  
#   ServiceTicket model with service_ticket_id as a primary key
#car customer and attributes as foreign key
class ServiceTicket(models.Model):
    service_ticket_id = models.AutoField(primary_key=True)
    service_ticket_number = models.CharField(max_length=100)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_received = models.DateField()
    comments = models.TextField(blank=True, null=True)
    date_returned_to_customer = models.DateField(blank=True, null=True)

#Service Mechanic Model with service_mechanic_id as a primary key
#service_ticket, service and mechanic attributes as foreign key 
class ServiceMechanic(models.Model):
    service_mechanic_id = models.AutoField(primary_key=True)
    service_ticket = models.ForeignKey(ServiceTicket, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    mechanic = models.ForeignKey(Mechanic, on_delete=models.CASCADE)
    hours = models.DecimalField(max_digits=5, decimal_places=2)
    comment = models.TextField(blank=True, null=True)
    rate = models.DecimalField(max_digits=10, decimal_places=2)

  
#PartsUsed Model with parts_used_id as a primary key 
#part and service_ticket attributes as foreign keys
class PartsUsed(models.Model):
    parts_used_id = models.AutoField(primary_key=True)
    part = models.ForeignKey(Parts, on_delete=models.CASCADE)
    service_ticket = models.ForeignKey(ServiceTicket, on_delete=models.CASCADE)
    number_used = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

  
