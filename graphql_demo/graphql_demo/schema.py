import graphene
from graphene_django.types import DjangoObjectType
from books.models import Book


# Define a GraphQL type for the Book model
class BookType(DjangoObjectType):
    class Meta:
        model = Book


# Define Query class
class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)

    def resolve_all_books(self, info):
        # Query all books from the database
        return Book.objects.all()

class CreateBook(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        author = graphene.String(required=True)
        published_year = graphene.Int(required=True)

    book = graphene.Field(BookType)

    def mutate(self, info, title, author, published_year):
        book = Book(title=title, author=author, published_year=published_year)
        book.save()
        return CreateBook(book=book)


class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
