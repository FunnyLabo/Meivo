import application

app = application.create_app()
print(app.url_map)
app.run()