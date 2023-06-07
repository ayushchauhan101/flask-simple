## render template and request handling

### Create a Form to take input and render the output via separate html file:

- index.html : Renders the form and takes input
- greet.html : Renders the output

---

### Using block to render the same block of codes wherever called

- creates a block of code **layout.html** that will be copied everywhere without the hassle of typing the same HTML tags

```
{% block wrapper %}
{% endblock %}
```

- call wrapper (user given name of block) anywhere to emulate the same html tags again and again

```
{extends "layout.html"}
------
your html tags
------
{% block wrapper %}
{% endblock %}
```

_To prevent restarting the app again and again to see the changes:_

```
flask run --debug
```
