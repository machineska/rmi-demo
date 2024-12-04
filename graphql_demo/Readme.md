{
  allBooks {
    title
    author
    publishedYear
  }
}


mutation {
  createBook(title: "1984", author: "George Orwell", publishedYear: 1949) {
    book {
      title
      author
      publishedYear
    }
  }
}
