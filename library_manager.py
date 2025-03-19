import json
from rich.console import Console
from rich.table import Table
from rich.text import Text

# Console object for rich formatting
console = Console()

# File name for storing the library data
FILE_NAME = "library.json"

# Load existing library data from JSON file
def load_library():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save library data to JSON file
def save_library(library):
    with open(FILE_NAME, "w") as file:
        json.dump(library, file, indent=4)

# Add a new book
def add_book(library):
    console.print("[bold cyan]Enter book details:[/bold cyan]")
    title = input("Title: ")
    author = input("Author: ")
    year = input("Publication Year: ")
    genre = input("Genre: ")
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"

    book = {
        "title": title,
        "author": author,
        "year": int(year),
        "genre": genre,
        "read": read_status
    }
    library.append(book)
    save_library(library)
    console.print("[bold green]✔ Book added successfully![/bold green]")

# Remove a book
def remove_book(library):
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            save_library(library)
            console.print("[bold red]❌ Book removed successfully![/bold red]")
            return
    console.print("[bold yellow]⚠ Book not found![/bold yellow]")

# Search for a book
def search_book(library):
    choice = input("Search by (1) Title or (2) Author? Enter choice: ")
    keyword = input("Enter the search term: ").lower()
    results = [book for book in library if keyword in book["title"].lower() or keyword in book["author"].lower()]

    if results:
        console.print("\n[bold cyan]📚 Matching Books:[/bold cyan]")
        for book in results:
            status = "[bold green]Read[/bold green]" if book["read"] else "[bold yellow]Unread[/bold yellow]"
            console.print(f"[bold white]{book['title']}[/bold white] by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        console.print("[bold yellow]⚠ No matching books found![/bold yellow]")

# Display all books
def display_books(library):
    if not library:
        console.print("[bold yellow]📭 No books in your library.[/bold yellow]")
        return

    table = Table(title="📚 Your Library", style="bold blue")
    table.add_column("Title", style="cyan", justify="left")
    table.add_column("Author", style="magenta")
    table.add_column("Year", style="yellow")
    table.add_column("Genre", style="green")
    table.add_column("Read Status", style="bold")

    for book in library:
        status = "[green]✔ Read[/green]" if book["read"] else "[yellow]✖ Unread[/yellow]"
        table.add_row(book["title"], book["author"], str(book["year"]), book["genre"], status)

    console.print(table)

# Update book details
def update_book(library):
    title = input("Enter the title of the book to update: ")
    for book in library:
        if book["title"].lower() == title.lower():
            console.print("[bold cyan]Leave blank to keep the current value.[/bold cyan]")
            book["title"] = input(f"New title [{book['title']}]: ") or book["title"]
            book["author"] = input(f"New author [{book['author']}]: ") or book["author"]
            book["year"] = input(f"New publication year [{book['year']}]: ") or book["year"]
            book["genre"] = input(f"New genre [{book['genre']}]: ") or book["genre"]
            book["read"] = input(f"Have you read this book? (yes/no) [{book['read']}]: ").strip().lower() == "yes"
            save_library(library)
            console.print("[bold green]✔ Book updated successfully![/bold green]")
            return
    console.print("[bold yellow]⚠ Book not found![/bold yellow]")

# Display statistics
def display_statistics(library):
    total_books = len(library)
    read_books = sum(1 for book in library if book["read"])
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0

    console.print("\n📊 [bold cyan]Library Statistics:[/bold cyan]")
    console.print(f"📚 Total books: [bold white]{total_books}[/bold white]")
    console.print(f"📖 Books read: [bold green]{read_books}[/bold green]")
    console.print(f"📈 Percentage read: [bold yellow]{percentage_read:.2f}%[/bold yellow]")

# Main menu
def main():
    library = load_library()
    
    while True:
        console.print("\n[bold cyan]📖 Personal Library Manager[/bold cyan]", style="bold underline")
        console.print("[bold magenta]1.[/bold magenta] Add a book")
        console.print("[bold magenta]2.[/bold magenta] Remove a book")
        console.print("[bold magenta]3.[/bold magenta] Search for a book")
        console.print("[bold magenta]4.[/bold magenta] Display all books")
        console.print("[bold magenta]5.[/bold magenta] Update a book")
        console.print("[bold magenta]6.[/bold magenta] Display statistics")
        console.print("[bold magenta]7.[/bold magenta] Exit")

        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            update_book(library)
        elif choice == "6":
            display_statistics(library)
        elif choice == "7":
            save_library(library)
            console.print("[bold green]📂 Library saved successfully. Goodbye![/bold green]")
            break
        else:
            console.print("[bold red]❌ Invalid choice! Please try again.[/bold red]")

# Run the program
if __name__ == "__main__":
    main()
