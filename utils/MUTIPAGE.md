### Multi-page app

Can be created using dcc.Location and dcc.Link or Dash page

html.Div(dcc.Link('Dashboard', href=dash.page_registry['pages.analytics']['path']))

#### There are three basic steps for creating a multi-page app with Dash Pages:

1. Create individual .py files for each page in your app, and put them in a /pages directory.

2. In each of these page files:

 * Add a dash.register_page(__name__), which tells Dash that this is a page in your app.
* Define the page's content within a variable called layout or a function called layout that returns the content.

3. In your main app file, app.py:

* When declaring your app, set use_pages to True: app = Dash(__name__, use_pages=True)
* Add dash.page_container in your app layout where you want the page content to be displayed when a user visits one of the app's page paths.


#### Questions
Dynamically Create a Layout for Multi-Page App Validation (app.validation)
Circular Imports (not to clear)