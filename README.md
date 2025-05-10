Product Recommender System - Django
===================================
This is a simple Django-based product recommender system that provides APIs to manage products, place orders, and
recommend products frequently bought together. Designed as a coding challenge for Pragma, the project is structured
to be scalable, testable, and extensible.

Features
--------
- Product CRUD APIs
- Order CRUD APIs
- API to create orders using product IDs
- API to recommend frequently bought-together products
- Seed scripts to populate fake products and orders
- Built with Django and Django REST Framework
- 
Recommendation Logic
--------------------
The system tracks which products are frequently ordered together. When a product ID is provided, it searches all past
orders containing that product and finds other products that appear in those orders. The top co-occurring products are
returned as recommendations.

Project Structure
-----------------
recommender/
 products/
 models.py
 views.py
 api.py
 serializers.py
 management/commands/populate_products.py
 orders/
 models.py
 views.py
 api.py
 serializers.py
 management/commands/populate_orders.py
 recommender/ (main project)
 settings.py
 urls.py
 manage.py
 requirements.txt
 
Requirements
------------
- Python 3.8+
- pip (Python package manager)
- (Optional) Docker
Setup Instructions
------------------
1. Clone the repository
 git clone https://github.com/yourusername/product-recommender.git
 cd product-recommender
2. Create a virtual environment and activate it
 python -m venv env
 source env/bin/activate # On Windows: env\Scripts\activate
3. Install dependencies
 pip install -r requirements.txt
4. Apply database migrations
 python manage.py makemigrations
 python manage.py migrate
5. Populate test data
 python manage.py populate_products
 python manage.py populate_orders

Running the Application
-----------------------
python manage.py runserver
API will be accessible at http://localhost:8000/api/

API Endpoints
-------------
| Endpoint | Method | Description |
|----------------------------------|------------|-----------------------------------------------|
| /api/products/ | GET, POST | List/Create Products |
| /api/products/<id>/ | GET, PUT, DELETE | Retrieve/Update/Delete a Product |
| /api/orders/ | GET, POST | List/Create Orders |
| /api/orders/<id>/ | GET, PUT, DELETE | Retrieve/Update/Delete an Order |
| /api/create-order/ | POST | Create an order with a list of product IDs |
| /api/recommend/?product_id=<id> | GET | Recommend frequently bought-together products |

Example API Usage
-----------------
Create an Order:
POST /api/create-order/
 {
 "product_ids": [1, 2, 3]
 }
Get Recommendations:
GET /api/recommend/?product_id=2
 [
 {
 "id": 5,
 "name": "Product 5",
 "category": "Electronics",
 "price": 199.99,
 "description": "Description for Product 5"
 },
 ...
 ]
 
Optional: Docker Setup
----------------------
1. Build and run with Docker
 docker build -t recommender-app .
 docker run -p 8000:8000 recommender-app
Optional: Dashboard (Bonus)
--------------------------
To reset the database:
 rm db.sqlite3
 python manage.py migrate
 python manage.py populate_products
 python manage.py populate_orders

-------
By: Bhoomika P Shetty
Email: bhoomikapshetty352@gmail.com 
GitHub: https://github.com/bhoomikashetty-123/
