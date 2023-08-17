# myapp/models.py

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    # def __str__(self):
    #     return self.author

def __str__(self):
    return f"{self.title} by {self.author}"

# new_book = Book(title='Django for Beginners', author='John Smith', isbn='9781234567890', price=29.99)
# new_book.save()


# READ 
#filter
# book = book.objects.all() //show all

# for book in Book:
#      print(f"name is {book['title']}")

# book = book.objects.get(id = 1)  //find by id
# book = Book.objects.filter(id = 1)  
# book 


# CREATE 
# book = Book(title="abc" , author = "amir")
# book 

#Book.objects.create(title= "abc" , author="amir")

# UPDATE 
# book = Book.objects.filter(id=1)
# book.title = "abc"
# book.author = "ravi visnoi"

# Book.object.filter(id=1).update(title="Ramayna")


# DELETE 

# Book.objects.get(id=1).delete()
# Book.objects.all().delete()