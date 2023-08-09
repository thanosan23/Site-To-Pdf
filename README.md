# Site to PDF
Converts a website to PDF

## Usage
Run the docker container:
```
docker build -t site-to-pdf .
docker run -p 8080:8080 -d --rm --name site-to-web site-to-web
```

To convert a url to a pdf, go to your browser and go to `localhost:8080`. Go to the `convert/` route and set the URL argument to the URL:
```
http://localhost:8080/convert?url=<enter url here>
```

This will open up a PDF. You can download the PDF or print the PDF!
