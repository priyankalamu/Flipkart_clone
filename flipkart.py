import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


# Function to display "Add to Cart" message
def add_to_cart(product_name):
    messagebox.showinfo("Cart", f"{product_name} has been added to your cart!")


# Function to handle login submission
def submit_login(username, email, password, phone):
    if username and email and password and phone:
        # Custom login success message with larger font
        login_success_popup(username)
    else:
        messagebox.showerror("Error", "Please fill in all fields!")


# Custom popup for login success
def login_success_popup(username):
    success_popup = tk.Toplevel()
    success_popup.title("Login Successful")
    success_popup.geometry("300x150")
    success_popup.configure(bg="white")

    # Message Label with large font
    success_message = tk.Label(success_popup, text=f"Welcome, {username}!", font=("Arial", 20, "bold"), bg="white", fg="green")
    success_message.pack(expand=True, pady=30)

    # Close Button
    close_button = tk.Button(success_popup, text="Close", font=("Arial", 12), bg="#2874f0", fg="white", command=success_popup.destroy)
    close_button.pack(pady=10)


# Function to create the Login page
def login_page():
    login_window = tk.Toplevel()
    login_window.title("Login")
    login_window.geometry("400x350")
    login_window.configure(bg="white")

    # Login Title
    login_title = tk.Label(login_window, text="Login", font=("Arial", 20, "bold"), bg="white")
    login_title.pack(pady=10)

    # Username Field
    username_label = tk.Label(login_window, text="Username", font=("Arial", 12), bg="white")
    username_label.pack(pady=5)
    username_entry = tk.Entry(login_window, font=("Arial", 12), width=30)
    username_entry.pack(pady=5)

    # Email Field
    email_label = tk.Label(login_window, text="Email (Gmail)", font=("Arial", 12), bg="white")
    email_label.pack(pady=5)
    email_entry = tk.Entry(login_window, font=("Arial", 12), width=30)
    email_entry.pack(pady=5)

    # Password Field
    password_label = tk.Label(login_window, text="Password", font=("Arial", 12), bg="white")
    password_label.pack(pady=5)
    password_entry = tk.Entry(login_window, font=("Arial", 12), width=30, show="*")
    password_entry.pack(pady=5)

    # Phone Number Field
    phone_label = tk.Label(login_window, text="Phone Number", font=("Arial", 12), bg="white")
    phone_label.pack(pady=5)
    phone_entry = tk.Entry(login_window, font=("Arial", 12), width=30)
    phone_entry.pack(pady=5)

    # Submit Button
    submit_button = tk.Button(login_window, text="Submit", font=("Arial", 12), bg="#2874f0", fg="white",
                              command=lambda: submit_login(username_entry.get(), email_entry.get(), password_entry.get(), phone_entry.get()))
    submit_button.pack(pady=10)

    login_window.mainloop()


# Create the Flipkart Clone Application
def flipkart_clone():
    root = tk.Tk()
    root.title("Flipkart Clone")
    root.geometry("1000x700")
    root.configure(bg="white")

    # Navbar
    navbar = tk.Frame(root, bg="#2874f0", height=60)
    navbar.pack(fill="x", side="top")

    # Logo
    logo = tk.Label(navbar, text="Flipkart", fg="white", bg="#2874f0", font=("Arial", 20, "bold"))
    logo.pack(side="left", padx=15)

    # Search Bar
    search_bar = tk.Entry(navbar, font=("Arial", 14), width=50)
    search_bar.pack(side="left", padx=20, pady=10)
    search_button = tk.Button(navbar, text="Search", font=("Arial", 12), bg="#ffe500", command=lambda: None)
    search_button.pack(side="left", padx=5)

    # Cart and Login Buttons
    login_button = tk.Button(navbar, text="Login", font=("Arial", 12), bg="white", fg="#2874f0", width=10,
                             command=login_page)
    login_button.pack(side="right", padx=10, pady=10)
    cart_button = tk.Button(navbar, text="🛒 Cart", font=("Arial", 12), bg="white", fg="#2874f0", width=10)
    cart_button.pack(side="right", padx=10, pady=10)

    # Product Grid
    product_grid = tk.Frame(root, bg="white")
    product_grid.pack(fill="both", expand=True, padx=20, pady=10)

    # Sample Product List
    products = [
        {"name": "Smartphone", "price": "₹15,000", "image": "smartphone.jpg"},
        {"name": "Laptop", "price": "₹50,000", "image": "laptop.jpg"},
        {"name": "Headphones", "price": "₹3,000", "image": "headphones.jpg"},
        {"name": "Smartwatch", "price": "₹5,000", "image": "smartwatch.jpg"},
    ]

    for product in products:
        product_frame = tk.Frame(product_grid, bd=2, relief="solid", padx=10, pady=10, bg="white")
        product_frame.pack(side="left", padx=15, pady=10)

        try:
            # Load product image
            product_image = Image.open(product["image"])
            product_image = product_image.resize((220, 220), Image.Resampling.LANCZOS)
            product_photo = ImageTk.PhotoImage(product_image)
            product_image_label = tk.Label(product_frame, image=product_photo, bg="white")
            product_image_label.image = product_photo
            product_image_label.pack()
        except FileNotFoundError:
            product_image_label = tk.Label(product_frame, text="No Image Available", bg="white")
            product_image_label.pack()

        # Product Name
        product_name_label = tk.Label(product_frame, text=product["name"], font=("Arial", 14), bg="white")
        product_name_label.pack()

        # Product Price
        product_price_label = tk.Label(product_frame, text=product["price"], font=("Arial", 12), fg="#2874f0", bg="white")
        product_price_label.pack()

        # Add to Cart Button
        add_to_cart_button = tk.Button(
            product_frame,
            text="Add to Cart",
            font=("Arial", 12),
            bg="#2874f0",
            fg="white",
            command=lambda name=product["name"]: add_to_cart(name),
        )
        add_to_cart_button.pack(pady=5)

    # Footer
    footer = tk.Frame(root, bg="#f1f1f1", height=50)
    footer.pack(fill="x", side="bottom")
    footer_label = tk.Label(footer, text="© 2024 Flipkart Clone. All rights reserved.", bg="#f1f1f1", fg="#555")
    footer_label.pack(pady=10)

    root.mainloop()


# Run the application
flipkart_clone()
