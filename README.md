## render template and request handling

### Create a simple flask server to send request via pre built template

---

An HTML file named index.html must be added to templates directory

> always use templates as the name of the directory to avoid errors

The flask server serches and serves a webpage via index.html using render_template from **flask library.**

---

Get a request from the url and render via the webpage using request from the **flask library.**

### Steps include :

- Enter the following URl or use any name in place of Tom

```
http://localhost:5000/?name=Tom
```

- Add the following code around the placeholder variable:

```
Hello, {{name}}
```

_this {{}} is the Jinja templating that comes with Flask_

- Run the flask server:

```
flask run
```

- You will see result like:

```
Hello, Tom
```

_Now the flask server is responding to the user input and serving via HTML template._
