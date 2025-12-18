<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>📚Kuchuu Devops ( LOVE)</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Arial', sans-serif;
            background: #f0f2f5;
            color: #202124;
        }

        /* Header */
        .header {
            background: #232f3e;	
            color: white;
            padding: 15px 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        }

        .logo {
            font-size: 20px;
            font-weight: bold;
            cursor: pointer;
        }

        .search-container {
            flex: 1;
            max-width: 600px;
            margin: 0 50px;
        }

        .search-box {
            display: flex;
            background: white;
            border-radius: 4px;
            overflow: hidden;
        }

        .search-input {
            flex: 1;
            padding: 10px 15px;
            border: none;
            font-size: 14px;
        }

        .search-btn {
            background: #ff9900;
            border: none;
            padding: 0 20px;
            cursor: pointer;
            font-size: 18px;
        }

        .header-actions {
            display: flex;
            gap: 15px;
            align-items: center;
        }

        .btn {
            background: #ff9900;
            color: black;
            border: none;
            padding: 10px 20px;
            border-radius: 4px;
            cursor: pointer;
            font-weight: bold;
            font-size: 14px;
            transition: background 0.3s;
        }

        .btn:hover {
            background: #ffad33;
        }

        .btn-secondary {
            background: #6c5ce7;
            color: white;
        }

        .btn-secondary:hover {
            background: #5849c7;
        }

        .cart-btn {
            background: transparent;
            color: white;
            font-size: 16px;
            padding: 8px 15px;
        }

        .cart-btn:hover {
            background: rgba(255,255,255,0.1);
        }

        /* Main Content */
        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
        }

        .welcome-banner {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            border-radius: 8px;
            text-align: center;
            margin-bottom: 30px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }

        .welcome-banner h1 {
            font-size: 32px;
            margin-bottom: 10px;
        }

        /* Book Grid */
        .books-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }

        .book-card {
            background: white;
            border-radius: 8px;
            padding: 15px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            transition: transform 0.3s, box-shadow 0.3s;
            cursor: pointer;
        }

        .book-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 16px rgba(0,0,0,0.2);
        }

        .book-cover {
            width: 100%;
            height: 200px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 4px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 14px;
            text-align: center;
            padding: 10px;
            margin-bottom: 10px;
            position: relative;
            overflow: hidden;
        }

        .book-title {
            font-weight: bold;
            margin-bottom: 5px;
            font-size: 14px;
            min-height: 40px;
        }

        .book-author {
            color: #666;
            font-size: 12px;
            margin-bottom: 8px;
        }

        .book-rating {
            color: #ff9900;
            font-size: 14px;
            margin-bottom: 8px;
        }

        .book-price {
            color: #b12704;
            font-weight: bold;
            font-size: 18px;
            margin-bottom: 10px;
        }

        .add-to-cart-btn {
            width: 100%;
            background: #1a73e8;
            color: white;
            border: none;
            padding: 10px;
            border-radius: 4px;
            cursor: pointer;
            font-weight: bold;
            transition: background 0.3s;
        }

        .add-to-cart-btn:hover {
            background: #1557b0;
        }

        /* Login Modal */
        .modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.5);
            z-index: 1000;
            align-items: center;
            justify-content: center;
        }

        .modal.active {
            display: flex;
        }

        .modal-content {
            background: white;
            padding: 30px;
            border-radius: 8px;
            max-width: 400px;
            width: 90%;
            box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        }

        .modal-header {
            background: #232f3e;
            color: white;
            padding: 20px;
            margin: -30px -30px 20px -30px;
            border-radius: 8px 8px 0 0;
            text-align: center;
        }

        .form-group {
            margin-bottom: 15px;
        }

        .form-group label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }

        .form-group input {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 14px;
        }

        .modal-actions {
            display: flex;
            gap: 10px;
            margin-top: 20px;
        }

        .guest-landing {
            text-align: center;
            padding: 60px 20px;
        }

        .guest-landing h2 {
            font-size: 28px;
            margin-bottom: 20px;
            color: #232f3e;
        }

        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-top: 40px;
        }

        .feature-card {
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }

        .feature-icon {
            font-size: 40px;
            margin-bottom: 15px;
        }

        .loading {
            text-align: center;
            padding: 40px;
            color: #666;
        }

        .hidden {
            display: none;
        }

        /* Cart Sidebar */
        .cart-sidebar {
            position: fixed;
            right: -400px;
            top: 0;
            width: 400px;
            height: 100%;
            background: white;
            box-shadow: -2px 0 10px rgba(0,0,0,0.2);
            transition: right 0.3s;
            z-index: 1001;
            overflow-y: auto;
        }

        .cart-sidebar.active {
            right: 0;
        }

        .cart-header {
            background: #232f3e;
            color: white;
            padding: 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .cart-items {
            padding: 20px;
        }

        .cart-item {
            background: #f8f9fa;
            padding: 15px;
            margin-bottom: 10px;
            border-radius: 4px;
        }

        .cart-total {
            padding: 20px;
            border-top: 2px solid #ddd;
            font-size: 18px;
            font-weight: bold;
        }

        @media (max-width: 768px) {
            .books-grid {
                grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
            }
            
            .search-container {
                margin: 0 20px;
            }

            .cart-sidebar {
                width: 100%;
                right: -100%;
            }
        }
    </style>
</head>
<body>
    <!-- Header -->
    <div class="header">
        <div class="logo" onclick="showHome()">📚Kuchuu Devops ( LOVE)</div>
        
        <div class="search-container">
            <div class="search-box">
                <input type="text" class="search-input" id="searchInput" placeholder="Search books, authors, genres...">
                <button class="search-btn" onclick="searchBooks()">🔍</button>
            </div>
        </div>

        <div class="header-actions">
            <button class="btn btn-secondary" onclick="showAIInsights()">🧠 AI Insights</button>
            <button class="btn cart-btn" onclick="toggleCart()">🛒 Cart (<span id="cartCount">0</span>)</button>
            <button class="btn" id="authBtn" onclick="showLogin()">👤 Sign In</button>
        </div>
    </div>

    <!-- Main Container -->
    <div class="container">
        <!-- Guest Landing -->
        <div id="guestLanding" class="guest-landing">
            <h2>📚 Welcome toKuchuu Devops ( LOVE)</h2>
            <p style="font-size: 18px; color: #666; margin-bottom: 30px;">Your Premium Online Book Shopping Destination</p>
            <p style="font-size: 16px; color: #ff9900; margin-bottom: 30px;">🔐 Please sign in to access our full catalog and features</p>
            <button class="btn" style="font-size: 18px; padding: 15px 40px;" onclick="showLogin()">👤 Sign In to Browse Books</button>

            <div class="features-grid">
                <div class="feature-card">
                    <div class="feature-icon">📚</div>
                    <h3>Browse Thousands of Books</h3>
                    <p>Access our complete catalog with 3D book previews</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🛒</div>
                    <h3>Shopping Cart & Checkout</h3>
                    <p>Add books to cart and secure checkout process</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">🎯</div>
                    <h3>Personalized Recommendations</h3>
                    <p>Get book suggestions based on your preferences</p>
                </div>
                <div class="feature-card">
                    <div class="feature-icon">⭐</div>
                    <h3>Reviews & Ratings</h3>
                    <p>Read and write book reviews and ratings</p>
                </div>
            </div>
        </div>

        <!-- Logged In Content -->
        <div id="loggedInContent" class="hidden">
            <div class="welcome-banner">
                <h1>📚 Welcome toKuchuu Devops ( LOVE)</h1>
                <p>Discover Your Next Great Read with AI-Powered Recommendations!</p>
            </div>

            <div class="books-grid" id="booksGrid"></div>
        </div>
    </div>

    <!-- Login Modal -->
    <div class="modal" id="loginModal">
        <div class="modal-content">
            <div class="modal-header">
                <h2>👤 Sign In to BookStore</h2>
            </div>
            <div class="form-group">
                <label>Username:</label>
                <input type="text" id="loginUsername" placeholder="Enter your username">
            </div>
            <div class="form-group">
                <label>Password:</label>
                <input type="password" id="loginPassword" placeholder="Enter your password">
            </div>
            <div class="modal-actions">
                <button class="btn" style="flex: 1;" onclick="handleLogin()">Sign In</button>
                <button class="btn" style="flex: 1; background: #6c757d;" onclick="closeModal()">Cancel</button>
            </div>
            <p style="text-align: center; margin-top: 15px;">
                <a href="#" onclick="showRegister()" style="color: #0066cc;">Create new account</a>
            </p>
        </div>
    </div>

    <!-- Register Modal -->
    <div class="modal" id="registerModal">
        <div class="modal-content">
            <div class="modal-header">
                <h2>📝 Create Account</h2>
            </div>
            <div class="form-group">
                <label>Username:</label>
                <input type="text" id="regUsername" placeholder="Choose a username">
            </div>
            <div class="form-group">
                <label>Email:</label>
                <input type="email" id="regEmail" placeholder="Enter your email">
            </div>
            <div class="form-group">
                <label>Password:</label>
                <input type="password" id="regPassword" placeholder="Choose a password">
            </div>
            <div class="modal-actions">
                <button class="btn" style="flex: 1;" onclick="handleRegister()">Create Account</button>
                <button class="btn" style="flex: 1; background: #6c757d;" onclick="closeModal()">Cancel</button>
            </div>
        </div>
    </div>

    <!-- Cart Sidebar -->
    <div class="cart-sidebar" id="cartSidebar">
        <div class="cart-header">
            <h2>🛒 Your Cart</h2>
            <button class="btn" style="background: transparent; padding: 5px 10px;" onclick="toggleCart()">✕</button>
        </div>
        <div class="cart-items" id="cartItems"></div>
        <div class="cart-total">
            Total: ₹<span id="cartTotal">0.00</span>
        </div>
        <div style="padding: 20px;">
            <button class="btn" style="width: 100%; padding: 15px;" onclick="checkout()">🛒 Proceed to Checkout</button>
        </div>
    </div>

    <script>
        // Sample book data
        const sampleBooks = [
            {id: 1, title: "The Great Gatsby", author: "F. Scott Fitzgerald", genre: "Fiction", rating: 4.5, price: 299},
            {id: 2, title: "To Kill a Mockingbird", author: "Harper Lee", genre: "Fiction", rating: 4.8, price: 349},
            {id: 3, title: "1984", author: "George Orwell", genre: "Science Fiction", rating: 4.7, price: 279},
            {id: 4, title: "Pride and Prejudice", author: "Jane Austen", genre: "Romance", rating: 4.6, price: 259},
            {id: 5, title: "The Hobbit", author: "J.R.R. Tolkien", genre: "Fantasy", rating: 4.9, price: 399},
            {id: 6, title: "Harry Potter", author: "J.K. Rowling", genre: "Fantasy", rating: 4.8, price: 449},
            {id: 7, title: "The Catcher in the Rye", author: "J.D. Salinger", genre: "Fiction", rating: 4.3, price: 289},
            {id: 8, title: "Brave New World", author: "Aldous Huxley", genre: "Science Fiction", rating: 4.4, price: 309}
        ];

        let currentUser = null;
        let cart = [];
        let allBooks = [...sampleBooks];

        // Initialize app
        function init() {
            const savedUser = localStorage.getItem('currentUser');
            if (savedUser) {
                currentUser = JSON.parse(savedUser);
                showLoggedInView();
            } else {
                showGuestView();
            }
            loadCart();
        }

        // Show guest view
        function showGuestView() {
            document.getElementById('guestLanding').classList.remove('hidden');
            document.getElementById('loggedInContent').classList.add('hidden');
            document.getElementById('authBtn').textContent = '👤 Sign In';
            document.getElementById('searchInput').disabled = true;
            document.getElementById('searchInput').placeholder = 'Sign in to search books...';
        }

        // Show logged in view
        function showLoggedInView() {
            document.getElementById('guestLanding').classList.add('hidden');
            document.getElementById('loggedInContent').classList.remove('hidden');
            document.getElementById('authBtn').textContent = '👤 ' + currentUser.username;
            document.getElementById('authBtn').onclick = logout;
            document.getElementById('searchInput').disabled = false;
            document.getElementById('searchInput').placeholder = 'Search books, authors, genres...';
            displayBooks(allBooks);
        }

        // Display books
        function displayBooks(books) {
            const grid = document.getElementById('booksGrid');
            grid.innerHTML = '';
            
            books.forEach(book => {
                const card = document.createElement('div');
                card.className = 'book-card';
                card.innerHTML = `
                    <div class="book-cover" style="background: linear-gradient(135deg, ${getRandomColor()} 0%, ${getRandomColor()} 100%);">
                        <strong>${book.title}</strong>
                    </div>
                    <div class="book-title">${book.title}</div>
                    <div class="book-author">by ${book.author}</div>
                    <div class="book-rating">${'★'.repeat(Math.floor(book.rating))}${'☆'.repeat(5-Math.floor(book.rating))} ${book.rating}</div>
                    <div class="book-price">₹${book.price}</div>
                    <button class="add-to-cart-btn" onclick="addToCart(${book.id})">🛒 Add to Cart</button>
                `;
                grid.appendChild(card);
            });
        }

        // Random color for book covers
        function getRandomColor() {
            const colors = ['#667eea', '#764ba2', '#f093fb', '#4facfe', '#43e97b', '#fa709a'];
            return colors[Math.floor(Math.random() * colors.length)];
        }

        // Search books
        function searchBooks() {
            if (!currentUser) {
                alert('Please sign in to search books');
                return;
            }

            const query = document.getElementById('searchInput').value.toLowerCase();
            if (!query) return;

            const filtered = allBooks.filter(book => 
                book.title.toLowerCase().includes(query) ||
                book.author.toLowerCase().includes(query) ||
                book.genre.toLowerCase().includes(query)
            );

            displayBooks(filtered);
            if (filtered.length === 0) {
                alert(`No books found matching '${query}'`);
            }
        }

        // Add to cart
        function addToCart(bookId) {
            const book = allBooks.find(b => b.id === bookId);
            if (!book) return;

            const existingItem = cart.find(item => item.book.id === bookId);
            if (existingItem) {
                existingItem.quantity++;
            } else {
                cart.push({ book, quantity: 1 });
            }

            saveCart();
            updateCartUI();
            alert(`'${book.title}' added to cart!`);
        }

        // Update cart UI
        function updateCartUI() {
            document.getElementById('cartCount').textContent = cart.reduce((sum, item) => sum + item.quantity, 0);
            
            const cartItems = document.getElementById('cartItems');
            cartItems.innerHTML = '';
            
            let total = 0;
            cart.forEach(item => {
                const itemTotal = item.book.price * item.quantity;
                total += itemTotal;
                
                cartItems.innerHTML += `
                    <div class="cart-item">
                        <strong>${item.book.title}</strong>
                        <p style="color: #666; font-size: 12px;">${item.book.author}</p>
                        <p>Quantity: ${item.quantity} × ₹${item.book.price} = ₹${itemTotal}</p>
                    </div>
                `;
            });
            
            document.getElementById('cartTotal').textContent = total.toFixed(2);
        }

        // Toggle cart
        function toggleCart() {
            document.getElementById('cartSidebar').classList.toggle('active');
        }

        // Checkout
        function checkout() {
            if (!currentUser) {
                alert('Please sign in to checkout');
                return;
            }
            
            if (cart.length === 0) {
                alert('Your cart is empty');
                return;
            }

            const total = cart.reduce((sum, item) => sum + (item.book.price * item.quantity), 0);
            if (confirm(`Confirm order for ₹${total.toFixed(2)}?`)) {
                alert('Order placed successfully! Thank you for your purchase!');
                cart = [];
                saveCart();
                updateCartUI();
                toggleCart();
            }
        }

        // Show login modal
        function showLogin() {
            closeModal();
            document.getElementById('loginModal').classList.add('active');
        }

        // Show register modal
        function showRegister() {
            closeModal();
            document.getElementById('registerModal').classList.add('active');
        }

        // Close modal
        function closeModal() {
            document.querySelectorAll('.modal').forEach(modal => {
                modal.classList.remove('active');
            });
        }

        // Handle login
        function handleLogin() {
            const username = document.getElementById('loginUsername').value.trim();
            const password = document.getElementById('loginPassword').value.trim();

            if (!username || !password) {
                alert('Please enter both username and password');
                return;
            }

            // Simple demo authentication
            const users = JSON.parse(localStorage.getItem('users') || '{}');
            if (users[username] && users[username].password === password) {
                currentUser = { username };
                localStorage.setItem('currentUser', JSON.stringify(currentUser));
                closeModal();
                showLoggedInView();
                alert(`Welcome back, ${username}!`);
            } else {
                alert('Invalid username or password. Try: demo/demo123');
            }
        }

        // Handle registration
        function handleRegister() {
            const username = document.getElementById('regUsername').value.trim();
            const email = document.getElementById('regEmail').value.trim();
            const password = document.getElementById('regPassword').value.trim();

            if (!username || !email || !password) {
                alert('Please fill in all fields');
                return;
            }

            if (password.length < 6) {
                alert('Password must be at least 6 characters');
                return;
            }

            const users = JSON.parse(localStorage.getItem('users') || '{}');
            if (users[username]) {
                alert('Username already exists');
                return;
            }

            users[username] = { password, email };
            localStorage.setItem('users', JSON.stringify(users));
            
            alert('Account created successfully! Please sign in.');
            closeModal();
            showLogin();
        }

        // Logout
        function logout() {
            if (confirm('Are you sure you want to logout?')) {
                currentUser = null;
                localStorage.removeItem('currentUser');
                cart = [];
                saveCart();
                updateCartUI();
                showGuestView();
            }
        }

        // Show home
        function showHome() {
            if (currentUser) {
                displayBooks(allBooks);
                document.getElementById('searchInput').value = '';
            }
        }

        // Show AI Insights
        function showAIInsights() {
            if (!currentUser) {
                alert('Please sign in to view AI insights');
                return;
            }
            alert('🧠 AI Insights Dashboard\n\nPersonalized recommendations based on your browsing history and preferences.\n\n📊 Features:\n• Content-based filtering\n• Collaborative recommendations\n• Trending books analysis\n• Price optimization\n\n(Full dashboard coming soon!)');
        }

        // Save cart to localStorage
        function saveCart() {
            localStorage.setItem('cart', JSON.stringify(cart));
        }

        // Load cart from localStorage
        function loadCart() {
            const saved = localStorage.getItem('cart');
            if (saved) {
                cart = JSON.parse(saved);
                updateCartUI();
            }
        }

        // Initialize on load
        init();

        // Search on Enter key
        document.getElementById('searchInput').addEventListener('keypress', (e) => {
            if (e.key === 'Enter') searchBooks();
        });

        // Close modals on background click
        document.querySelectorAll('.modal').forEach(modal => {
            modal.addEventListener('click', (e) => {
                if (e.target === modal) closeModal();
            });
        });
    </script>
</body>
</html>
