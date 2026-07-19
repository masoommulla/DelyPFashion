import re

html_path = r"d:\00 ProjectsOnline\Restaurants\DelypFashion\index.html"
css_path = r"d:\00 ProjectsOnline\Restaurants\DelypFashion\css\style.css"
js_path = r"d:\00 ProjectsOnline\Restaurants\DelypFashion\js\script.js"

# 1. Update HTML
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Add carousel buttons to the products header
header_pattern = re.compile(r'(<div class="products-head">\s*<h2 class="section-title">Our <span class="accent">Product</span></h2>)')
replacement_html = r'''\1
    <div class="mobile-nav-btn">
      <button class="nav-prev"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 18l-6-6 6-6"/></svg></button>
      <button class="nav-next"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18l6-6-6-6"/></svg></button>
    </div>'''
html = header_pattern.sub(replacement_html, html)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

# 2. Update CSS
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

new_css = '''
/* Desktop hiding for carousel arrows */
@media (min-width: 760px) {
  .mobile-nav-btn { display: none !important; }
}

/* Mobile Responsive Overrides for Product Carousel */
@media (max-width: 759px) {
  .products-head {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
  }
  .mobile-nav-btn {
    display: flex;
    gap: 8px;
  }
  .mobile-nav-btn button {
    background: var(--gray-bg);
    border: 1px solid var(--line);
    border-radius: 50%;
    width: 36px;
    height: 36px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
  }
  .mobile-nav-btn button svg {
    width: 16px;
    height: 16px;
  }
  
  .product-grid {
    display: grid !important;
    grid-template-rows: repeat(2, 1fr) !important;
    grid-auto-flow: column !important;
    grid-auto-columns: calc(50% - 6px) !important; /* 2 items visible */
    gap: 12px !important;
    overflow-x: auto !important;
    scroll-snap-type: x mandatory !important;
    scrollbar-width: none !important; /* Firefox */
    padding-bottom: 8px;
  }
  .product-grid::-webkit-scrollbar {
    display: none !important; /* Safari/Chrome */
  }
  .product-card {
    scroll-snap-align: start !important;
    height: auto !important;
  }
  .product-thumb {
    border-radius: 12px !important;
    aspect-ratio: 3/4 !important;
    margin-bottom: 8px !important;
  }
  .product-name {
    font-size: 11px !important;
  }
  .product-price {
    font-size: 12px !important;
  }
}
'''

css += new_css

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

# 3. Update JS
with open(js_path, "r", encoding="utf-8") as f:
    js = f.read()

new_js = '''
  // Mobile Product Carousel Navigation
  const prevBtn = document.querySelector('.nav-prev');
  const nextBtn = document.querySelector('.nav-next');
  const productGrid = document.querySelector('.product-grid');

  if (prevBtn && nextBtn && productGrid) {
    prevBtn.addEventListener('click', () => {
      // scroll by one column width roughly
      const cardWidth = productGrid.querySelector('.product-card').offsetWidth;
      productGrid.scrollBy({ left: -(cardWidth + 12), behavior: 'smooth' });
    });
    
    nextBtn.addEventListener('click', () => {
      const cardWidth = productGrid.querySelector('.product-card').offsetWidth;
      productGrid.scrollBy({ left: cardWidth + 12, behavior: 'smooth' });
    });
  }
});
'''

# We want to insert the JS right before the final `});` in script.js, assuming it's wrapped in DOMContentLoaded
js = js.replace('});', new_js)

with open(js_path, "w", encoding="utf-8") as f:
    f.write(js)

print("Updates applied successfully.")
