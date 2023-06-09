## Create a form and render via jinja template engine:

- Create a form to accept two data : name & sport
- Create an empty python dictionary and save each time the form is submitted

- Pass the created dictionary to the target HTML file.
- User jinja templating and correct syntax to iterate throught each instance

[Learn more about jinja](https://jinja.palletsprojects.com/en/3.0.x/templates/)

---

### Add data validation

Always try to implement as much data validation and integrity check, both on client as well as server side.

- Create your own set of options in the backend i.e. all_sports in app.py
- Render your defined sets of options to be selecred only
- Check and stop empty or undefined data from submitting