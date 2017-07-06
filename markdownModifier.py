"""
The aim of this program is to add CSS classes to a html document produced from
markdown. The html can then be incorporated into a website with the same
asthetics.

NOTE: Markdown may not produce every html tag

Requirements:
    1. BeautifulSoup4
    2. A html file to parse
    3. A csv file that specifies the classes to add

Basic operation:
    1. Read in CSS class data (from a spreadsheet / CSV)
    2. Read in html
    3. Parse
    4. Save html to new file (the program won't overwrite an existing file)

TODO:
    - !! TOC styling !!
    - Method for removing any classes in a html file so that html produced by
      Rmarkdown, for example, can then be modified.
        * Rmarkdown does javascript vodoo though
    - Add wrapping, for example, wapping each <h1> in a div
    - Build methods into a class
        - Instansiate
        - Add rules from csv method
        - Import file
        - (Import template)
        - Parse
        - Output file

    - Add methods that can deal with nested structures
        - e.g. adding a class to <p> only if it is inside a <li>
"""

from bs4 import BeautifulSoup

def loadHTML(path_to_file):
    html = ""
    with open(path_to_file, mode='r') as f:
        for line in f:
            html += line
        f.close()
    return html

tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'em', 'strong', 'del', 'br',
        'a', 'img', 'table', 'thead', 'tbody', 'tr', 'td', 'ul', 'ol', 'li',
        'pre', 'code', 'blockquote', 'hr']

def removeTagClassValues(html, tag):
    soup = BeautifulSoup(html, 'lxml')
    tag = soup.find_all(tag)
    if tag != None:
        for j in tag:
            del j['class']
    return str(soup)

def removeAllTagClassValues(html):
    tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'em', 'strong', 'del', 'br',
            'a', 'img', 'table', 'thead', 'tbody', 'tr', 'td', 'ul', 'ol', 'li',
            'pre', 'code', 'blockquote', 'hr']
    html = html
    for i in tags:
        html = removeTagClassValues(html, i)
    return html

def toHTML(html, path_to_file):
    with open(path_to_file, mode='x') as f:
        print(html, file=f)
        f.close()

def loadTagAttributes(path_to_file):
    """
    Input : csv file
    Output: Dictionary of html tag attributes
    """
    attribute_dictionay = {}
    with open(path_to_file, mode='r') as f:
        for line in f:
            line_data = line.replace('\n', '').split(sep=",")
            if line_data[1] != '':
                attribute_dictionay[line_data[0]] = line_data[1]
        f.close()
    return attribute_dictionay

def addClassValue(html_text, html_tag, class_value):
    soup = BeautifulSoup(html_text, 'lxml')
    tag  = soup.find_all(html_tag)
    for i in tag:
        i['class'] = class_value
    return str(soup)

def addAllClassValues(html, class_dict):
    html = html
    for i in class_dict:
        html = addClassValue(html, i, class_dict[i])
    return html

x = loadTagAttributes('htmlTagClasses.csv')

test = loadHTML('arduino.html')

test = addAllClassValues(test, x)

toHTML(test, "test_check.html")
