import java.util.ArrayList;
import java.util.Scanner;

class Book {
    String title;
    String author;

    Book(String title, String author) {
        this.title = title;
        this.author = author;
    }
}

class Library {
    ArrayList<Book> books;

    Library() {
        books = new ArrayList<>();
    }

    void addBook(String title, String author) {
        books.add(new Book(title, author));
        System.out.println("Book added successfully.");
    }

    void displayBooks() {
        System.out.println("Library Books:");
        for (Book book : books) {
            System.out.println("Title: " + book.title + ", Author: " + book.author);
        }
    }
}

public class LibraryManagementSystem {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Library library = new Library();

        int choice;
        do {
            System.out.println("Library Management System Menu:");
            System.out.println("1. Add a Book");
            System.out.println("2. Display Books");
            System.out.println("3. Exit");
            System.out.print("Enter your choice: ");

            choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    scanner.nextLine(); // Consume newline
                    System.out.print("Enter the title of the book: ");
                    String title = scanner.nextLine();
                    System.out.print("Enter the author of the book: ");
                    String author = scanner.nextLine();
                    library.addBook(title, author);
                    break;
                case 2:
                    library.displayBooks();
                    break;
                case 3:
                    System.out.println("Exiting Library Management System. Goodbye!");
                    break;
                default:
                    System.out.println("Invalid choice. Try again.");
            }
        } while (choice != 3);
    }
}










execute_this()




























Mene pehle hi kaha tha ki ye faltu hai isse mat kholna
kat gaya na tuhmhara

  koi nai agla file kholo
