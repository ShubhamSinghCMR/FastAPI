import fastapi
import uvicorn

api = fastapi.FastAPI()

@api.get('/')
def home_page():
    body = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome Page</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                margin: 0;
                padding: 0;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
            }
            h1 {
                color: #4CAF50;
            }
            p {
                color: #555;
            }
            a {
                color: #007BFF;
                text-decoration: none;
            }
            a:hover {
                text-decoration: underline;
            }
            .container {
                text-align: center;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
                background-color: white;
                width: 50%;
                max-width: 800px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to FastAPI Home Page</h1>
            <p>This is a simple FastAPI application designed to show a friendly welcome page.</p>
        </div>
    </body>
    </html>
    """
    return fastapi.responses.HTMLResponse(
        content=body   
    )

uvicorn.run(api)