import glob

footer_old = """
    <div class="footer-col">
      <h4>Quick Links</h4>
      <a href="product.html">Shop Collection</a>
      <a href="about.html">About Us</a>
      <a href="blog.html">The Journal</a>
      <a href="#">Contact Us</a>
    </div>

    <div class="footer-col">
      <h4>Customer Care</h4>
      <a href="#">FAQ</a>
      <a href="#">Shipping & Returns</a>
      <a href="#">Size Guide</a>
      <a href="#">Track Order</a>
    </div>

    <div class="footer-col">
      <h4>Legal</h4>
      <a href="#">Privacy Policy</a>
      <a href="#">Terms of Service</a>
      <a href="#">Cookie Policy</a>
    </div>
"""

footer_new = """
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
"""

for file in ["d:/00 ProjectsOnline/Restaurants/DelypFashion/pages/about.html", "d:/00 ProjectsOnline/Restaurants/DelypFashion/pages/product.html", "d:/00 ProjectsOnline/Restaurants/DelypFashion/pages/blog.html"]:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace(footer_old.strip(), footer_new.strip())
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Updated footers in about, product, and blog html files.")
