with open('index.html', 'r') as f:
    content = f.read()

# Add the nav scroll script before </head>
nav_script = '''    <script>
      const nav = document.getElementById('main-nav');
      window.addEventListener('scroll', () => {
        if (window.scrollY > 100) {
          nav.style.background = 'rgba(5, 5, 5, 0.95)';
          nav.style.backdropFilter = 'blur(10px)';
          nav.style.boxShadow = '0 4px 30px rgba(0, 0, 0, 0.5)';
        } else {
          nav.style.background = 'transparent';
          nav.style.backdropFilter = 'none';
          nav.style.boxShadow = 'none';
        }
      });
    </script>
  </head>'''

content = content.replace('  </head>', nav_script)

with open('index.html', 'w') as f:
    f.write(content)

print("Done")
