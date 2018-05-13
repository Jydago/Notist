# Good to know stuff
- Template in flask enables you to send variables into a template when using `render_template` in python code. This can then be referenced in the HTML code using `{{__variable_name__}}`
- Static assets are served using a route in the python code. See `send_asset(filename)` in __python_server.py__ for example