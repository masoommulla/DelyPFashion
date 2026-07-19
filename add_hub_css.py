import os

new_css = """
/* =========================================
   HUB LAYOUT (Customer Care & Legal)
   ========================================= */
.hub-page {
  padding: 60px 20px 100px;
  background: var(--white);
  max-width: 1200px;
  margin: 0 auto;
}
.hub-header {
  text-align: center;
  margin-bottom: 60px;
  padding-bottom: 40px;
  border-bottom: 1px solid var(--line);
}
.hub-header h1 {
  font-family: var(--font-display);
  font-size: clamp(32px, 5vw, 48px);
  margin-bottom: 16px;
}
.hub-header p {
  color: var(--ink-soft);
  font-size: 18px;
}
.hub-layout {
  display: flex;
  flex-direction: column;
  gap: 60px;
}
@media (min-width: 900px) {
  .hub-layout {
    flex-direction: row;
    align-items: flex-start;
  }
}
.hub-sidebar {
  flex: 0 0 250px;
  position: sticky;
  top: 100px;
}
.hub-sidebar h4 {
  font-size: 14px;
  text-transform: uppercase;
  letter-spacing: 1px;
  color: var(--ink-soft);
  margin-bottom: 16px;
}
.hub-nav {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-bottom: 40px;
}
.hub-nav a {
  text-decoration: none;
  color: var(--ink-soft);
  font-size: 16px;
  font-weight: 500;
  padding: 8px 0;
  transition: color 0.2s;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.hub-nav a:hover {
  color: var(--ink);
}
.hub-nav a.active {
  color: var(--ink);
  font-weight: 700;
}
.hub-nav a.active::after {
  content: "→";
}
.hub-content {
  flex: 1;
  max-width: 800px;
}
.hub-content h2 {
  font-size: 32px;
  margin-bottom: 32px;
  font-family: var(--font-display);
}
.hub-content-block {
  margin-bottom: 40px;
}
.hub-content-block h3 {
  font-size: 20px;
  margin-bottom: 16px;
  color: var(--ink);
}
.hub-content-block p {
  font-size: 16px;
  line-height: 1.8;
  color: var(--ink-soft);
  margin-bottom: 20px;
}
"""

with open(r"d:\00 ProjectsOnline\Restaurants\DelypFashion\css\style.css", "a", encoding="utf-8") as f:
    f.write(new_css)

print("Appended hub CSS.")
