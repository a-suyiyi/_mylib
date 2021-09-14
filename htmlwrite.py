def html(*text):
    a=open('d:/game.html','w+')
    b=''
    for i in text:
        b=b+i
    a.write(
       '<html>\n'+b+'</html>')
    a.close()
def head(*t):
    a=''
    for i in t:
        a+=i
    return '<head>\n'+a+'</head>\n'
def body(*t):
    a=''
    for i in t:
        a+=i
    return '<body>\n'+a+'</body>\n'
def table(*t):
    a=''
    for i in t:
        a+=i
    return '<table>\n'+a+'</table>\n'
def tr(*t):
    a=''
    for i in t:
        a+=i
    return '<tr>\n'+a+'</tr>\n'
def td(t):
    return '<td>'+t+'</td>'
def p(t):
    return '<p>'+t+'</p>\n'
def a(url,t):
    return '<a herf="'+str(url)+'">'+str(t)+'</a>\n'
def enter():
    return '<hr/>\n'
def line():
    return '<br/>\n'
def b(t):
    return '<b>'+t+'</b>\n'
def i(t):
    return '<i>'+t+'</i>\n'
def ins(t):
    return '<ins>'+t+'</ins>\n'
def delete(t):
    return '<del>'+t+'</del>\n'
def sub(t):
    return '<sub>'+t+'</sub>\n'
