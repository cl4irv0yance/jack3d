import os
import sys
import webbrowser

if len(sys.argv) != 2:
    print('\n[+] Description: %s can quickly verify if a web page is vulnerable to clickjacking' % __file__)
    print('[+] Usage: python %s <url>\n' % __file__)
    exit(0)

url = sys.argv[1]

html = '''
<html>
    <head>
        <title>Clickjacking Test Page</title>
    </head>

    <body>
        <h1>Clickjacking Test Results</h1>
        <h2>Target: <a href="%s">%s</a></h2>
        <h3>If you see the target website rendered below, it is <font color="red">VULNERABLE</font>.</h3>
        <iframe width="1280" height="900" src="%s" style="border: 2px solid red;"></iframe>
        <iframe style="position: absolute; left: 20px; top: 250px; opacity: 0.8; background: AliceBlue; font-weight: bold;" src="cj-attacker.html"></iframe>
    </body>
</html>
''' % (url, url, url)

# Modified cj-attacker.html to include an alert
html2 = '''
<html>
    <body>
        <div style="opacity: 1.0; left: 10px; top: 50px; background: PapayaWhip; font-weight: bold;">
            <center>
                <a href="#" onclick="alert('You have been clickjacked!');">CLICK ME TO TEST ALERT</a>
                <br>(normally invisible)
            </center>
        </div>
    </body>
</html>
'''

cjt = os.path.abspath('cj-target.html')
cja = os.path.abspath('cj-attacker.html')
localurl = 'file://' + cjt

with open(cjt, 'w') as t, open(cja, 'w') as a:
    t.write(html)
    a.write(html2)

webbrowser.open(localurl)

print('\n[+] Test Complete!')
