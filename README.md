# CSS-plus-md

### Add CSS framework classes to html produced from markdown

The aim of this program is to add CSS classes to a html document produced from
markdown. The html can then be incorporated into a website with the same
asthetics.

Requirements:
    1. BeautifulSoup4
    2. A html file to parse
    3. A csv file that specifies the classes to add

Basic operation:
    1. Read in CSS class data (from a spreadsheet / CSV)
    2. Read in html
    3. Parse
    4. Save html to new file (the program won't overwrite an existing file)

Possible features:
    - TOC options?
    - Method for removing any classes in a html file so that html produced by
      Rmarkdown, for example, can then be modified.
        * Rmarkdown does javascript vodoo though
    - Add wrapping, for example, wapping each `<h1>` in a div
    - Build methods into a class
        - Instansiate
        - Add rules from csv method
        - Import file
        - (Import template)
        - Parse
        - Output file
