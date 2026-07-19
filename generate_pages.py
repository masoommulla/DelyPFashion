import os

header_template = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Delyo Fashion</title>
<link rel="stylesheet" href="../css/style.css">
</head>
<body>

<header class="site-header">
  <div class="logo">
    <a href="../index.html" style="text-decoration:none;">
      <span class="l1">DELYO</span><span class="l2">FASHION</span>
    </a>
  </div>

  <nav class="main-nav">
    <a href="../index.html">Home</a>
    <a href="about.html">About us</a>
    <a href="product.html">Product</a>
    <a href="blog.html">Blog</a>
  </nav>

  <div class="header-actions">
    <button class="icon-btn" aria-label="Notifications">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 8a6 6 0 0 0-12 0c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 0 1-3.46 0"/></svg>
    </button>
    <button class="icon-btn" aria-label="Cart">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="21" r="1"/><circle cx="20" cy="21" r="1"/><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"/></svg>
    </button>
    <span class="divider"></span>
    <button class="contact-btn">
      Contact us
      <span class="arrow-circle">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17 17 7"/><path d="M8 7h9v9"/></svg>
      </span>
    </button>
    <button class="burger" aria-label="Menu">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
    </button>
  </div>
</header>
"""

footer_template = """
<section class="newsletter-section">
  <div class="newsletter-container">
    <div class="newsletter-content">
      <h2>Join the Club & Get 15% Off</h2>
      <p>Subscribe to our newsletter for exclusive offers, new arrivals, and insider only discounts.</p>
      <form class="newsletter-form">
        <input type="email" placeholder="Enter your email address" required>
        <button type="submit">Subscribe</button>
      </form>
    </div>
  </div>
</section>

<footer class="site-footer">
  <div class="footer-container">
    <div class="footer-col brand-col">
      <div class="logo footer-logo">
        <span class="l1">DELYO</span><span class="l2">FASHION</span>
      </div>
      <p>Elevating everyday style with premium quality, sustainable materials, and timeless design.</p>
      <div class="social-links">
        <a href="#" aria-label="Instagram"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg></a>
        <a href="#" aria-label="Twitter"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path></svg></a>
        <a href="#" aria-label="Facebook"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg></a>
      </div>
    </div>
    
    <div class="footer-col">
      <h4>Quick Links</h4>
      <a href="product.html">Shop Collection</a>
      <a href="about.html">About Us</a>
      <a href="blog.html">The Journal</a>
      <a href="contact.html">Contact Us</a>
    </div>

    <div class="footer-col">
      <h4>Customer Care</h4>
      <a href="faq.html">FAQ</a>
      <a href="shipping.html">Shipping & Returns</a>
      <a href="size-guide.html">Size Guide</a>
      <a href="track-order.html">Track Order</a>
    </div>

    <div class="footer-col">
      <h4>Legal</h4>
      <a href="privacy.html">Privacy Policy</a>
      <a href="terms.html">Terms of Service</a>
      <a href="cookie.html">Cookie Policy</a>
    </div>
  </div>
  <div class="footer-bottom">
    <p>&copy; 2026 Delyo Fashion. All rights reserved.</p>
    <div class="payment-methods">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="1" y="4" width="22" height="16" rx="2" ry="2"></rect><line x1="1" y1="10" x2="23" y2="10"></line></svg>
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M16 8h-6a2 2 0 1 0 0 4h4a2 2 0 1 1 0 4H8"></path><path d="M12 18V6"></path></svg>
    </div>
  </div>
</footer>

</body>
</html>
"""

pages = [
    {
        "filename": "contact.html",
        "title": "Contact Us",
        "main": """
<main class="utility-page section-pad">
  <div class="page-header">
    <h1 class="page-title">Contact <span class="accent">Us</span></h1>
    <p>We're here to help. Reach out to our team with any questions.</p>
  </div>
  <div class="contact-grid">
    <div class="contact-info">
      <h3>Get in Touch</h3>
      <p><strong>Email:</strong> support@delyofashion.com</p>
      <p><strong>Phone:</strong> +1 (555) 123-4567</p>
      <p><strong>Address:</strong><br>123 Fashion Ave, Suite 400<br>New York, NY 10001</p>
      <div class="map-placeholder">
        <span>Interactive Map</span>
      </div>
    </div>
    <div class="contact-form-container">
      <h3>Send a Message</h3>
      <form class="utility-form">
        <div class="form-group">
          <label>Name</label>
          <input type="text" placeholder="Your name">
        </div>
        <div class="form-group">
          <label>Email</label>
          <input type="email" placeholder="Your email">
        </div>
        <div class="form-group">
          <label>Message</label>
          <textarea rows="5" placeholder="How can we help?"></textarea>
        </div>
        <button type="button" class="btn-primary">Submit</button>
      </form>
    </div>
  </div>
</main>
"""
    },
    {
        "filename": "faq.html",
        "title": "FAQ",
        "main": """
<main class="utility-page section-pad">
  <div class="page-header">
    <h1 class="page-title">Frequently Asked <span class="accent">Questions</span></h1>
  </div>
  <div class="content-block">
    <h3>Shipping & Delivery</h3>
    <p><strong>How long does shipping take?</strong><br>Standard shipping takes 3-5 business days. Express shipping takes 1-2 business days.</p>
    <p><strong>Do you ship internationally?</strong><br>Yes, we ship to most countries worldwide. International shipping rates apply.</p>
    
    <h3>Returns & Exchanges</h3>
    <p><strong>What is your return policy?</strong><br>You have 30 days from the date of delivery to return unworn items.</p>
    <p><strong>How do I start a return?</strong><br>Visit our returns portal or contact our support team.</p>
  </div>
</main>
"""
    },
    {
        "filename": "shipping.html",
        "title": "Shipping & Returns",
        "main": """
<main class="utility-page section-pad">
  <div class="page-header">
    <h1 class="page-title">Shipping & <span class="accent">Returns</span></h1>
  </div>
  <div class="content-block">
    <h3>Shipping Information</h3>
    <p>All orders are processed within 1-2 business days. Orders are not shipped or delivered on weekends or holidays.</p>
    <p>If we are experiencing a high volume of orders, shipments may be delayed by a few days. Please allow additional days in transit for delivery.</p>
    
    <h3>Return Policy</h3>
    <p>We accept returns up to 30 days after delivery, if the item is unused and in its original condition, and we will refund the full order amount minus the shipping costs for the return.</p>
    <p>In the event that your order arrives damaged in any way, please email us as soon as possible with your order number and a photo of the item's condition.</p>
  </div>
</main>
"""
    },
    {
        "filename": "size-guide.html",
        "title": "Size Guide",
        "main": """
<main class="utility-page section-pad">
  <div class="page-header">
    <h1 class="page-title">Size <span class="accent">Guide</span></h1>
    <p>Find your perfect fit.</p>
  </div>
  <div class="content-block">
    <h3>Men's Tops</h3>
    <table class="utility-table">
      <thead>
        <tr><th>Size</th><th>Chest (in)</th><th>Waist (in)</th></tr>
      </thead>
      <tbody>
        <tr><td>S</td><td>34-36</td><td>28-30</td></tr>
        <tr><td>M</td><td>38-40</td><td>32-34</td></tr>
        <tr><td>L</td><td>42-44</td><td>36-38</td></tr>
        <tr><td>XL</td><td>46-48</td><td>40-42</td></tr>
      </tbody>
    </table>
    
    <h3 style="margin-top: 40px;">Women's Tops</h3>
    <table class="utility-table">
      <thead>
        <tr><th>Size</th><th>Bust (in)</th><th>Waist (in)</th></tr>
      </thead>
      <tbody>
        <tr><td>XS</td><td>32-33</td><td>24-25</td></tr>
        <tr><td>S</td><td>34-35</td><td>26-27</td></tr>
        <tr><td>M</td><td>36-37</td><td>28-29</td></tr>
        <tr><td>L</td><td>38-39</td><td>30-31</td></tr>
      </tbody>
    </table>
  </div>
</main>
"""
    },
    {
        "filename": "track-order.html",
        "title": "Track Order",
        "main": """
<main class="utility-page section-pad">
  <div class="page-header">
    <h1 class="page-title">Track <span class="accent">Order</span></h1>
    <p>Enter your order details below to check the current status.</p>
  </div>
  <div class="contact-form-container" style="max-width: 500px; margin: 0 auto;">
    <form class="utility-form">
      <div class="form-group">
        <label>Order Number</label>
        <input type="text" placeholder="e.g. #DF123456">
      </div>
      <div class="form-group">
        <label>Email Address</label>
        <input type="email" placeholder="Email used for the order">
      </div>
      <button type="button" class="btn-primary" style="width: 100%;">Track Package</button>
    </form>
  </div>
</main>
"""
    },
    {
        "filename": "privacy.html",
        "title": "Privacy Policy",
        "main": """
<main class="utility-page section-pad">
  <div class="page-header">
    <h1 class="page-title">Privacy <span class="accent">Policy</span></h1>
    <p>Last updated: July 2026</p>
  </div>
  <div class="content-block legal-text">
    <h3>1. Information We Collect</h3>
    <p>We collect information you provide directly to us, such as when you create or modify your account, request on-demand services, contact customer support, or otherwise communicate with us.</p>
    <h3>2. Use of Information</h3>
    <p>We may use the information we collect about you to provide, maintain, and improve our services, including to facilitate payments, send receipts, and provide products and services you request.</p>
    <h3>3. Sharing of Information</h3>
    <p>We will not share your personal information with third parties without your consent, except in the specific circumstances described in this policy.</p>
  </div>
</main>
"""
    },
    {
        "filename": "terms.html",
        "title": "Terms of Service",
        "main": """
<main class="utility-page section-pad">
  <div class="page-header">
    <h1 class="page-title">Terms of <span class="accent">Service</span></h1>
    <p>Last updated: July 2026</p>
  </div>
  <div class="content-block legal-text">
    <h3>1. Agreement to Terms</h3>
    <p>By accessing our website, you agree to be bound by these Terms of Service and all applicable laws and regulations.</p>
    <h3>2. Intellectual Property</h3>
    <p>The Service and its original content, features, and functionality are and will remain the exclusive property of Delyo Fashion and its licensors.</p>
    <h3>3. Termination</h3>
    <p>We may terminate or suspend access to our Service immediately, without prior notice or liability, for any reason whatsoever.</p>
  </div>
</main>
"""
    },
    {
        "filename": "cookie.html",
        "title": "Cookie Policy",
        "main": """
<main class="utility-page section-pad">
  <div class="page-header">
    <h1 class="page-title">Cookie <span class="accent">Policy</span></h1>
    <p>Last updated: July 2026</p>
  </div>
  <div class="content-block legal-text">
    <h3>1. What Are Cookies</h3>
    <p>Cookies are small files stored on your device that hold a modest amount of data specific to a particular client and website, and can be accessed either by the web server or the client computer.</p>
    <h3>2. How We Use Cookies</h3>
    <p>We use cookies to understand and save user's preferences for future visits and compile aggregate data about site traffic and site interactions in order to offer better site experiences.</p>
    <h3>3. Managing Cookies</h3>
    <p>You can choose to have your computer warn you each time a cookie is being sent, or you can choose to turn off all cookies through your browser settings.</p>
  </div>
</main>
"""
    }
]

target_dir = r"d:\00 ProjectsOnline\Restaurants\DelypFashion\pages"
os.makedirs(target_dir, exist_ok=True)

for p in pages:
    content = header_template.replace("{title}", p["title"]) + p["main"] + footer_template
    filepath = os.path.join(target_dir, p["filename"])
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
        
print("Successfully generated 8 pages.")
