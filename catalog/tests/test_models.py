from django.test import TestCase
from catalog.models import Author, Book, BookInstance, Genre
from django.contrib.auth.models import User #Required to assign User as a borrower

class AuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        Author.authors.create(first_name='Big', last_name='Ben')

    def test_first_name_label(self):
        author=Author.authors.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label,'first name')
    
    def test_date_of_death_label(self):
        author=Author.authors.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEquals(field_label,'Died')

    def test_first_name_max_length(self):
        author=Author.authors.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEquals(max_length,100)

    def test_object_name_is_last_name_comma_first_name(self):
        author=Author.authors.get(id=1)
        expected_object_name = '%s, %s' % (author.last_name, author.first_name)
        self.assertEquals(expected_object_name,str(author))

    def test_get_absolute_url(self):
        author=Author.authors.get(id=1)
        #This will also fail if the urlconf is not defined.
        self.assertEquals(author.get_absolute_url(),'/catalog/author/1')

class GenreModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Genre.genres.create(name='SciFi')
    
    def test_genre_name(self):
        genre=Genre.genres.get(name='SciFi')
        field_label = genre._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'name')

    def test_genre_name_length(self):
        genre=Genre.genres.get(name='SciFi')
        max_length = genre._meta.get_field('name').max_length
        self.assertEquals(max_length,200)

class BookModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        author = Author.authors.create(first_name='Big', last_name='Ben')
        genre = Genre.genres.create(name='SciFi')
        Book.books.create(title='Gospodari', author=author, summary='Neki description', isbn='aef123gfa123')
    
    def test_book_name(self):
        book=Book.books.get(title='Gospodari')
        field_label = book._meta.get_field('title').verbose_name
        self.assertEquals(field_label,'title')
    
    def test_book_name_length(self):
        book=Book.books.get(title='Gospodari')
        max_length = book._meta.get_field('title').max_length
        self.assertEquals(max_length,200)

    def test_book_summary(self):
        book=Book.books.get(title='Gospodari')
        field_label = book._meta.get_field('summary').verbose_name
        self.assertEquals(field_label,'summary')
    
    def test_book_summary_length(self):
        book=Book.books.get(title='Gospodari')
        max_length = book._meta.get_field('summary').max_length
        self.assertEquals(max_length,1000)

    def test_book_isbn(self):
        book=Book.books.get(title='Gospodari')
        field_label = book._meta.get_field('isbn').verbose_name
        self.assertEquals(field_label,'ISBN')
    
    def test_book_isbn_length(self):
        book=Book.books.get(title='Gospodari')
        max_length = book._meta.get_field('isbn').max_length
        self.assertEquals(max_length,13)
