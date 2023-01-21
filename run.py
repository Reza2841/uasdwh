from app import app
from app.Controllers import predikController

if __name__ == '__main__':
    app.run(host="localhost", port=3000, debug=True)
