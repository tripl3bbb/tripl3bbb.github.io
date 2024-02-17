from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Dummy data for products
products = [
    {'id': 1, 'name': 'Bread', 'price': 3.99},
    {'id': 2, 'name': 'Cake', 'price': 19.99},
    # Add more products as needed
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cart')
def cart():
    cart_items = session.get('cart', [])
    total_price = sum(item['price'] for item in cart_items)
    return render_template('shopping-cart.html', cart_items=cart_items, total_price=total_price)

@app.route('/add-to-cart/<int:product_id>')
def add_to_cart(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        cart_items = session.get('cart', [])
        cart_items.append(product)
        session['cart'] = cart_items
    return redirect('/cart')

@app.route('/wishlist')
def wishlist():
    # Retrieve wishlist items from session
    wishlist_items = session.get('wishlist', [])
    return render_template('wishlist.html', wishlist_items=wishlist_items)

@app.route('/add-to-wishlist/<int:product_id>')
def add_to_wishlist(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        wishlist_items = session.get('wishlist', [])
        wishlist_items.append(product)
        session['wishlist'] = wishlist_items
    return redirect('/wishlist')

@app.route('/checkout')
def checkout():
    cart_items = session.get('cart', [])
    total_price = sum(item['price'] for item in cart_items)
    return render_template('checkout.html', cart_items=cart_items, total_price=total_price)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Check username and password (e.g., in a database)
        # For simplicity, we'll use a hardcoded check
        if username == 'admin' and password == 'password':
            session['logged_in'] = True
            return redirect('/')
        else:
            return 'Invalid username or password'
    return render_template('login.html')

@app.route('/contact')
def contact():
    return render_template('contact-us.html')

@app.route('/product')
def product():
    return render_template('product-default.html')

@app.route('/blog')
def blog():
    return render_template('blog-detail.html')

@app.route('/about')
def about():
    return render_template('about-us.html')

if __name__ == '__main__':
    app.run(debug=True)
