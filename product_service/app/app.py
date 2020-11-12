import setup
import add_products
from dotenv import load_dotenv

app = setup.create_app()
load_dotenv(dotenv_path='../.env')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
