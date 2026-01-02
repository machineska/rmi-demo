import graphene
from graphene_django.types import DjangoObjectType
from books.models import Book


# Define a GraphQL type for the Book model
class BookType(DjangoObjectType):
    class Meta:
        model = Book


# Define Query class
class Query(graphene.ObjectType):
    all_books = graphene.List(
        BookType,
        author=graphene.String(),
        title_contains=graphene.String(),
        year_gte=graphene.Int(),
        year_lte=graphene.Int(),
        limit=graphene.Int(),
        offset=graphene.Int(),
    )

    def resolve_all_books(
        self,
        info,
        author=None,
        title_contains=None,
        year_gte=None,
        year_lte=None,
        limit=None,
        offset=None,
    ):
        qs = Book.objects.all()
        if author:
            qs = qs.filter(author__iexact=author)
        if title_contains:
            qs = qs.filter(title__icontains=title_contains)
        if year_gte is not None:
            qs = qs.filter(published_year__gte=year_gte)
        if year_lte is not None:
            qs = qs.filter(published_year__lte=year_lte)
        if offset is not None:
            qs = qs[offset:]
        if limit is not None:
            qs = qs[:limit]
        return qs

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


class UpdateBook(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String()
        author = graphene.String()
        published_year = graphene.Int()

    book = graphene.Field(BookType)

    def mutate(self, info, id, title=None, author=None, published_year=None):
        try:
            book = Book.objects.get(pk=id)
        except Book.DoesNotExist:
            raise Exception("Book not found")
        if title is not None:
            book.title = title
        if author is not None:
            book.author = author
        if published_year is not None:
            book.published_year = published_year
        book.save()
        return UpdateBook(book=book)


class DeleteBook(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()

    def mutate(self, info, id):
        try:
            book = Book.objects.get(pk=id)
        except Book.DoesNotExist:
            raise Exception("Book not found")
        book.delete()
        return DeleteBook(ok=True)


class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()
    delete_book = DeleteBook.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
