# GraphQL (dengan Django)

**GraphQL** bukanlah RPC dalam pengertian tradisional, tetapi sebuah *Query Language* untuk API. Namun, dalam konteks sistem terdistribusi modern, GraphQL sering menggantikan peran RPC (dan REST) untuk komunikasi antara Client (Frontend/Mobile) dan Server.

## Konsep Utama

### 1. Ask for what you need
Dalam REST API biasa, Anda mungkin punya endpoint `/users/1` yang mengembalikan *semua* data user. Di GraphQL, client bisa meminta: "Saya hanya butuh `nama` dan `email` dari user ID 1". Server hanya akan mengirimkan data itu. Ini menghemat bandwidth secara drastis.

### 2. Single Endpoint
Tidak ada lagi ribuan URL seperti `/api/v1/users`, `/api/v1/posts`, dll. GraphQL hanya punya satu endpoint (biasanya `/graphql`), dan Anda mengirim query ke sana.

### 3. Schema & Types
GraphQL memiliki sistem tipe yang kuat. Anda mendefinisikan skema (Schema) data Anda, dan GraphQL memvalidasi query terhadap skema tersebut.

## Implementasi dalam Demo

Demo ini menggunakan framework **Django** dan library **Graphene-Django**.
File demo terdapat di folder `graphql_demo/`.

### Model Django (`books/models.py`)

Kita mulai dengan model database biasa:

```python
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    # ...
```

### Schema GraphQL (`graphql_demo/schema.py`)

Kita memetakan Model Django ke `DjangoObjectType` GraphQL:

```python
class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ("id", "title", "author", "published_year")

class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)

    def resolve_all_books(root, info):
        return Book.objects.all()
```

### Menjalankan Server

```bash
python manage.py runserver
```

Akses `http://127.0.0.1:8000/graphql` di browser. Anda akan melihat antarmuka **GraphiQL**, sebuah IDE interaktif untuk mencoba query.

### Contoh Query

Coba masukkan ini di GraphiQL:

```graphql
query {
  allBooks {
    title
    author
  }
}
```

### Contoh Mutation (Menambah Data)

```graphql
mutation {
  createBook(title: "Laskar Pelangi", author: "Andrea Hirata", publishedYear: 2005) {
    book {
      id
      title
    }
  }
}
```

## Kelebihan dan Kekurangan

**Kelebihan:**
*   **Efisien**: Tidak ada over-fetching atau under-fetching data.
*   **Fleksibel**: Frontend developer bisa mengubah kebutuhan data tanpa minta Backend developer mengubah API.
*   **Tools Hebat**: GraphiQL memudahkan eksplorasi API.

**Kekurangan:**
*   **Kompleksitas Caching**: Karena semua request POST ke satu URL, caching HTTP standar tidak bisa digunakan dengan mudah.
*   **N+1 Problem**: Jika tidak hati-hati mendesain resolver, performa database bisa jeblok karena terlalu banyak query kecil.
