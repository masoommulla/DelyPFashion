import os
import glob
import re

base_dir = r"d:\00 ProjectsOnline\Restaurants\DelypFashion"
html_files = glob.glob(os.path.join(base_dir, "*.html")) + glob.glob(os.path.join(base_dir, "pages", "*.html"))

# Regex to match the broken class attributes:
# class= animate-on-scroll"SOMETHING animate-on-scroll"
# We want to turn it back into class="SOMETHING"
broken_class_pattern = re.compile(r'class=\s*animate-on-scroll"([^"]*?)\s*animate-on-scroll"')

for file in html_files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Fix the broken HTML classes
    # e.g., class= animate-on-scroll"category-card animate-on-scroll" -> class="category-card"
    # Also in case there are multiple spaces or slightly different ones, we will just globally replace the exact broken strings:
    
    # Let's just do targeted string replacements for the targets I used in add_animations.py:
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
    
    for t in targets:
        # What did it become?
        # t = class="product-card"
        # t.replace('"', ' animate-on-scroll"') -> class= animate-on-scroll"product-card animate-on-scroll"
        broken_t = t.replace('"', ' animate-on-scroll"')
        content = content.replace(broken_t, t)
        
        # Also let's fix if there was any valid class="something animate-on-scroll" and remove the animation class just in case
        content = content.replace(' animate-on-scroll"', '"')

    # 2. Remove the main.js script tag I added
    content = content.replace('<script src="js/main.js"></script>\n', '')
    content = content.replace('<script src="../js/main.js"></script>\n', '')

    with open(file, "w", encoding="utf-8") as f:
        f.write(content)

print("HTML files successfully repaired and animations completely removed.")
