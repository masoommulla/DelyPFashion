import re

css_path = r"d:\00 ProjectsOnline\Restaurants\DelypFashion\css\style.css"

with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# 1. Restore .main-nav.mobile-active to the original non-fullscreen version
# I added body.menu-open and changed .main-nav.mobile-active
menu_pattern = re.compile(r"body\.menu-open\s*\{\s*overflow:\s*hidden;\s*\}\s*\.main-nav\.mobile-active\s*\{.*?\}", re.DOTALL)
original_menu_css = """
.main-nav.mobile-active {
  display: flex;
  flex-direction: column;
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  background: var(--white);
  padding: 20px;
  border-bottom: 1px solid var(--line);
  box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);
  z-index: 200;
}
"""
css = menu_pattern.sub(original_menu_css.strip(), css)

# 2. Remove the /* Mobile Responsive Overrides */ block completely
mobile_override_pattern = re.compile(r"/\* Mobile Responsive Overrides \*/\s*@media \(max-width: 759px\) \{.*?\}\s*", re.DOTALL)
css = mobile_override_pattern.sub("\n", css)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

# Now JS
js_path = r"d:\00 ProjectsOnline\Restaurants\DelypFashion\js\script.js"
with open(js_path, "r", encoding="utf-8") as f:
    js = f.read()

js_pattern = re.compile(r"// Mobile Menu Toggle.*?\}\s*\}\s*// Category", re.DOTALL)
original_js = """// Mobile Menu Toggle
  const burgerBtn = document.querySelector('.burger');
  const mainNav = document.querySelector('.main-nav');

  if (burgerBtn && mainNav) {
    burgerBtn.addEventListener('click', () => {
      mainNav.classList.toggle('mobile-active');
    });
  }

  // Category"""
js = js_pattern.sub(original_js, js)

with open(js_path, "w", encoding="utf-8") as f:
    f.write(js)

print("Restored CSS and JS to exact state before mobile work started.")
