import webbrowser as wb 

urls = [
    'g1.globo.com',
    'github.com',
    'gmail.com'
]

for url in urls:
    wb.open_new_tab(url)
