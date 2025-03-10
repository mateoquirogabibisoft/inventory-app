# Import required functions and classes from Flask and SQLAlchemy.
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize the Flask application.
app = Flask(__name__)

# Configure the database connection (MySQL with PyMySQL).
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable an unnecessary feature for this project.

# Initialize SQLAlchemy with the Flask application.
db = SQLAlchemy(app)

# Define the Inventory model representing the 'Inventory' table.
class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Integer column as the primary key.
    name = db.Column(db.String(100))              # String column (up to 100 characters).
    price = db.Column(db.Float)                   # Float column for price (decimal number).
    mac_address = db.Column(db.String(100))       # Column for storing MAC address.
    serial_number = db.Column(db.String(100))     # Column for storing serial number.
    manufacturer = db.Column(db.String(100))      # Column for storing manufacturer name.
    description = db.Column(db.Text)              # Column for storing a longer description.

    def __repr__(self):
        # Special method for object representation, useful for debugging.
        return f'<Inventory {self.name}>'

# Route for the main page: displays the list of items.
@app.route('/')
def index():
    # Retrieve all records from the Inventory table.
    items = Inventory.query.all()
    # Render the index.html template and pass the list of items.
    return render_template('index.html', items=items)

# Route for adding a new item to the database.
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # If the form is submitted, create a new Inventory object with form data.
        new_item = Inventory(
            name=request.form['name'],
            price=request.form['price'],
            mac_address=request.form['mac_address'],
            serial_number=request.form['serial_number'],
            manufacturer=request.form['manufacturer'],
            description=request.form['description']
        )
        # Add the new object to the database session.
        db.session.add(new_item)
        # Commit the changes to the database.
        db.session.commit()
        # Redirect the user to the main page after adding the item.
        return redirect(url_for('index'))
    # If the request is GET, render the form for adding an item.
    return render_template('add.html')

# Route for editing an existing item.
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    # Find the item by its ID; if not found, return a 404 error.
    item = Inventory.query.get_or_404(id)
    if request.method == 'POST':
        # Update the item fields with form data.
        item.name = request.form['name']
        item.price = request.form['price']
        item.mac_address = request.form['mac_address']
        item.serial_number = request.form['serial_number']
        item.manufacturer = request.form['manufacturer']
        item.description = request.form['description']
        # Commit the changes to the database.
        db.session.commit()
        # Redirect to the main page.
        return redirect(url_for('index'))
    # If the request is GET, render the form preloaded with item data.
    return render_template('edit.html', item=item)

# Route for deleting an item.
@app.route('/delete/<int:id>')
def delete(id):
    # Find the item to delete.
    item = Inventory.query.get_or_404(id)
    # Remove the item from the database session.
    db.session.delete(item)
    # Commit the changes to the database.
    db.session.commit()
    # Redirect the user to the main page.
    return redirect(url_for('index'))

# Main block to run the application.
if __name__ == '__main__':
    # Use app.app_context() to ensure the application context is available,
    # which is required for database operations.
    with app.app_context():
        # Create database tables if they do not exist.
        db.create_all()
    # Start the application on port 5000, accessible from any IP (host '0.0.0.0').
    app.run(host='0.0.0.0', port=5000, debug=True)
