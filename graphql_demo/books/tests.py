from django.test import TestCase
from graphql_demo.schema import schema
from books.models import Book


class GraphQLBookTests(TestCase):
    def setUp(self):
        Book.objects.create(title="A", author="Author1", published_year=2001)
        Book.objects.create(title="B", author="Author2", published_year=2002)

    def test_query_all_books(self):
        query = """
        {
          allBooks {
            title
            author
            publishedYear
          }
        }
        """
        result = schema.execute(query)
        self.assertIsNone(result.errors)
        self.assertEqual(len(result.data["allBooks"]), 2)

    def test_create_update_delete_book(self):
        create = """
        mutation {
          createBook(title: "C", author: "Author3", publishedYear: 2003) {
            book { id title author publishedYear }
          }
        }
        """
        result = schema.execute(create)
        self.assertIsNone(result.errors)
        created = result.data["createBook"]["book"]
        uid = created["id"]

        update = f"""
        mutation {{
          updateBook(id: "{uid}", title: "C2") {{
            book {{ id title }}
          }}
        }}
        """
        result = schema.execute(update)
        self.assertIsNone(result.errors)
        self.assertEqual(result.data["updateBook"]["book"]["title"], "C2")

        delete = f"""
        mutation {{
          deleteBook(id: "{uid}") {{
            ok
          }}
        }}
        """
        result = schema.execute(delete)
        self.assertIsNone(result.errors)
        self.assertTrue(result.data["deleteBook"]["ok"])

# Create your tests here.
