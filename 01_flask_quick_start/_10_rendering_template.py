from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)


if __name__ == '__main__':
    app.run(debug=True)

"""
Rendering Templates
--------------------

Generating HTML from within Python is not fun, and actually 
pretty cumbersome because you have to do the HTML escaping 
on your own to keep the application secure. 

Because of that Flask configures the `Jinja2` template 
engine for you automatically.

Templates can be used to generate any type of text file. 

For web applications, you'll primarily be generating HTML 
pages, but you can also generate markdown, plain text for 
emails, and anything else.

For a reference to HTML, CSS, and other web APIs, use the 
MDN Web Docs. https://developer.mozilla.org/

To render a template you can use the `render_template()` method. 
All you have to do is provide the name of the template and the 
variables you want to pass to the template engine as keyword 
arguments. Here's a simple example of how to render a template:


IMPORTANT: 


Flask will look for templates in the templates/ folder. 

- if your application is a module, this folder is next to 
that module, 

/application.py
/templates
    /hello.html

- if it's a package it's actually inside your package:
/application
    /__init__.py
    /templates
        /hello.html



For templates you can use the full power of Jinja2 templates. 
Head over to the official Jinja2 Template Documentation for 
more information. https://jinja.palletsprojects.com/templates/

Here is an example template:

----
<!doctype html >
<title > Hello from Flask < /title >
{ % if person % }
<h1 > Hello {{person}}!< /h1 >
{ % else % }
<h1 > Hello, World!< /h1 >
{ % endif % }
----

Inside templates you also have access to the 'config', 'request', 
'session' and 'g' [1] objects as well as the 'url_for()' and 
'get_flashed_messages()' functions.


Templates are especially useful if inheritance is used. If you
 want to know how that works, see Template Inheritance.
 https://flask.palletsprojects.com/en/3.0.x/patterns/templateinheritance/ 
 

Basically template inheritance makes it possible to keep certain 
elements on each page (like header, navigation and footer).

Automatic escaping is enabled, so if 'person' contains HTML it will 
be escaped automatically. If you can trust a variable and you know 
that it will be safe HTML (for example because it came from a module 
that converts wiki markup to HTML) you can mark it as safe by using 
the Markup class or by using the '|safe' filter in the template. 
Head over to the Jinja 2 documentation for more examples.



Here is a basic introduction to how the 'Markup' class works:

---

>>>from markupsafe import Markup
>>>Markup('<strong>Hello %s!</strong>') % '<blink>hacker</blink>'
Markup('<strong>Hello &lt;blink&gt;hacker&lt;/blink&gt;!</strong>')

>>>Markup.escape('<blink>hacker</blink>')
Markup('&lt;blink&gt;hacker&lt;/blink&gt;')

>>>Markup('<em>Marked up</em> &raquo; HTML').striptags()
'Marked up » HTML'

Changelog
----------
Changed in version 0.5: Autoescaping is no longer enabled for 
all templates. The following extensions for templates trigger 
autoescaping: .html, .htm, .xml, .xhtml. Templates loaded from 
a string will have autoescaping disabled.


[1]: Unsure what that 'g' object is ? 
It's something in which you can store information for your own 
needs. See the documentation for flask.g and Using SQLite 3 with Flask.
https://flask.palletsprojects.com/en/3.0.x/patterns/sqlite3/

"""
