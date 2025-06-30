from app import create_app
from main import app


app = create_app()
if __name__ == "__main__":
    app.run(debug=True)