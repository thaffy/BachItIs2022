import urllib.request
with urllib.request.urlopen('https://vg.no') as f:
    html = f.read().decode('utf-8')

f = open("htmlRequest.txt", "w")
f.write(html)
f.close()

