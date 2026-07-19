import os
import glob
import re

# 1. Create js/main.js
js_content = """
document.addEventListener("DOMContentLoaded", function() {
  const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.15
  };

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  const elements = document.querySelectorAll('.animate-on-scroll');
  elements.forEach(el => observer.observe(el));
});
"""

js_dir = r"d:\00 ProjectsOnline\Restaurants\DelypFashion\js"
os.makedirs(js_dir, exist_ok=True)
with open(os.path.join(js_dir, "main.js"), "w", encoding="utf-8") as f:
    f.write(js_content)

# 2. Append CSS
css_append = """
/* =========================================
   ANIMATIONS & MICRO-INTERACTIONS
   ========================================= */
.animate-on-scroll {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.8s cubic-bezier(0.16, 1, 0.3, 1), transform 0.8s cubic-bezier(0.16, 1, 0.3, 1);
  will-change: opacity, transform;
}
.animate-on-scroll.visible {
  opacity: 1;
  transform: translateY(0);
}

/* Stagger delays for grids */
.product-card:nth-child(1), .blog-card:nth-child(1), .category-card:nth-child(1) { transition-delay: 0.05s; }
.product-card:nth-child(2), .blog-card:nth-child(2), .category-card:nth-child(2) { transition-delay: 0.15s; }
.product-card:nth-child(3), .blog-card:nth-child(3), .category-card:nth-child(3) { transition-delay: 0.25s; }
.product-card:nth-child(4), .blog-card:nth-child(4), .category-card:nth-child(4) { transition-delay: 0.35s; }
.product-card:nth-child(5), .blog-card:nth-child(5) { transition-delay: 0.45s; }
.product-card:nth-child(6), .blog-card:nth-child(6) { transition-delay: 0.55s; }
.product-card:nth-child(7), .blog-card:nth-child(7) { transition-delay: 0.65s; }
.product-card:nth-child(8), .blog-card:nth-child(8) { transition-delay: 0.75s; }

/* Enhanced Micro-Interactions */
.btn-primary, .contact-btn, .shop-now-btn {
  transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.3s;
}
.btn-primary:hover, .contact-btn:hover, .shop-now-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}
"""
css_path = r"d:\00 ProjectsOnline\Restaurants\DelypFashion\css\style.css"
with open(css_path, "a", encoding="utf-8") as f:
    f.write(css_append)

# 3. Update HTML files
base_dir = r"d:\00 ProjectsOnline\Restaurants\DelypFashion"
html_files = glob.glob(os.path.join(base_dir, "*.html")) + glob.glob(os.path.join(base_dir, "pages", "*.html"))

targets = [
    'class="section-pad"', 
    'class="section-pad ',
    'class="product-card"', 
    'class="blog-card"',
    'class="category-card"',
    'class="hub-content-block"',
    'class="page-header"',
    'class="about-hero"',
    'class="our-story"',
    'class="core-values"',
    'class="materials-craft"',
    'class="newsletter-section"'
]

for file in html_files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # Add the script just before </body>
    if file.endswith("index.html"):
        script_tag = '<script src="js/main.js"></script>\n</body>'
    else:
        script_tag = '<script src="../js/main.js"></script>\n</body>'
        
    if "main.js" not in content:
        content = content.replace("</body>", script_tag)

    # Inject .animate-on-scroll class
    for t in targets:
        # e.g., class="product-card" -> class="product-card animate-on-scroll"
        new_t = t.replace('"', ' animate-on-scroll"')
        # Handle cases where there is already an animate-on-scroll class
        if "animate-on-scroll" not in new_t:
             continue # safety
        # Make sure not to double add
        content = content.replace(new_t, t) # Revert if already there
        content = content.replace(t, new_t)
        
    with open(file, "w", encoding="utf-8") as f:
        f.write(content)

print("Animations added successfully!")
