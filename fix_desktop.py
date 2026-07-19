import re

css_path = r"d:\00 ProjectsOnline\Restaurants\DelypFashion\css\style.css"

with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# 1. Remove the broken category-grid block I added at the end (around line 1523)
# It starts with:
# .category-grid{
#   display:grid;
#   gap:8px;
#   grid-template-columns:repeat(4,1fr);
# }
# And ends before .blog-grid {

broken_cat_grid_pattern = re.compile(
    r"\.category-grid\{\s*display:grid;\s*gap:8px;\s*grid-template-columns:repeat\(4,1fr\);\s*\}.*?(?=\.blog-grid \{)", 
    re.DOTALL
)

css = broken_cat_grid_pattern.sub("", css)


# 2. Fix .product-grid base to what it should be:
broken_prod_grid_pattern = re.compile(
    r"\.product-grid\{\s*display:grid;\s*grid-template-columns:repeat\(4,1fr\);\s*gap:12px;\s*margin-bottom:56px;\s*\}\s*@media \(max-width: 759px\) \{.*?\}.*?@media \(min-width:1024px\)\{\s*\.product-grid\{\s*grid-template-columns:repeat\(4,1fr\);\s*gap:40px 20px;\s*\}\s*\}",
    re.DOTALL
)

restored_prod_grid = """
.product-grid{
  display:grid;
  grid-template-columns:1fr;
  gap:32px;
  margin-bottom:56px;
}
@media (min-width:600px){
  .product-grid{ grid-template-columns:repeat(2,1fr); gap:24px; }
}
@media (min-width:1024px){
  .product-grid{ grid-template-columns:repeat(4,1fr); gap:40px 20px;}
}
"""

css = broken_prod_grid_pattern.sub(restored_prod_grid.strip() + "\n", css)


# 3. Add proper mobile-only overrides for BOTH grids without touching desktop
mobile_overrides = """
/* Mobile Responsive Overrides */
@media (max-width: 759px) {
  /* Category Grid (Landing Page) */
  .category-grid {
    grid-template-columns: repeat(3, 1fr) !important;
    gap: 8px !important;
  }
  .category-card {
    border-radius: 12px;
    height: 120px !important;
  }
  .category-card.tall {
    height: 120px !important; /* Stop it from taking 2 rows on mobile */
  }
  .category-card h3 {
    font-size: 10px !important;
    bottom: 8px !important;
    left: 8px !important;
  }
  
  /* Product Grid (Landing Page) */
  .product-grid {
    grid-template-columns: repeat(4, 1fr) !important;
    gap: 8px !important;
  }
  .product-thumb {
    border-radius: 8px !important;
    margin-bottom: 8px !important;
  }
  .fav-btn {
    width: 20px !important;
    height: 20px !important;
    top: 4px !important;
    right: 4px !important;
  }
  .fav-btn svg { width: 10px !important; height: 10px !important; }
  .product-name { font-size: 9px !important; line-height: 1.2 !important; }
  .product-price { font-size: 10px !important; }
  .product-info { gap: 4px !important; }
}
"""

css += mobile_overrides

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

print("Desktop restored and Mobile overrides appended.")
