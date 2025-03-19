# 📚 Personal Library Manager

A command-line application to manage your personal book collection with a rich, colorful interface.

## Features

- **Add Books**: Store details like title, author, publication year, genre, and reading status
- **Remove Books**: Delete books from your collection
- **Search**: Find books by title or author
- **Display Library**: View your entire collection in a formatted table
- **Update Books**: Modify details of existing books
- **Statistics**: Get insights about your reading habits

## Requirements

- Python 3.6+
- Required packages:
  - rich (for beautiful terminal formatting)
  - json (included in Python standard library)

## Installation

1. Clone this repository or download the source code
2. Install the required packages:

```bash
pip install rich
```

## Usage

Run the application with:

```bash
python library_manager.py
```

### Main Menu Options

1. **Add a book**: Enter book details including title, author, year, genre, and read status
2. **Remove a book**: Delete a book by its title
3. **Search for a book**: Find books by title or author
4. **Display all books**: View your entire library in a formatted table
5. **Update a book**: Modify details of an existing book
6. **Display statistics**: View reading statistics (total books, books read, percentage)
7. **Exit**: Save and quit the application

## Data Storage

Your library data is stored in a JSON file named `library.json` in the same directory as the application. This allows your library data to persist between sessions.

## Example

```
📖 Personal Library Manager
1. Add a book
2. Remove a book
3. Search for a book
4. Display all books
5. Update a book
6. Display statistics
7. Exit
```

When displaying your library, you'll see a nicely formatted table with all your books and their details.

## Contributing

Feel free to fork this project and submit pull requests with improvements or additional features.

## License

This project is open source and available under the [MIT License](LICENSE).
