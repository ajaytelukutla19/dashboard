1.Create project folder

mkdir customer_api_web
cd customer_api_web
Add the files above to their respective paths.

2.Install dependencies

pip install -r requirements.txt
Run the server

3.python run.py
4.Test endpoints:

GET http://localhost:5000/customers?page=1&limit=5

GET http://localhost:5000/customers/1

