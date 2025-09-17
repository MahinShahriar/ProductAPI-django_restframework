# ProductAPI - Django REST Framework

A simple product catalog API built with Django, Django REST Framework, JWT Authentication, Redis, and PostgreSQL.  
This project demonstrates basic CRUD operations for products, seller registration & authentication, and JWT-based authorization.

---

## Features

- **Product Catalog**
  - List, detail, create, update, and delete products
  - Filter products by seller
- **Seller Authentication**
  - Seller registration
  - Login with JWT token issuance
  - Seller dashboard endpoint
- **JWT Authentication**
  - Secure endpoints for product management
  - Session and JWT token support
- **PostgreSQL Backend**
  - Robust relational data storage

---

## Technologies Used

- Python
- Django
- Django REST Framework
- JWT Authentication (`rest_framework_simplejwt`)
- Redis (for caching)
- PostgreSQL

---

## Getting Started

### Prerequisites

- Python 3.8+
- PostgreSQL
- Redis (optional, for caching)
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/MahinShahriar/ProductAPI-django_restframework.git
   cd ProductAPI-django_restframework
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure PostgreSQL**
   - Create a database named `django_api` and a user `django_user` with password `django123`.
   - Update credentials in `django_api/settings.py` if needed.

5. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (optional, for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

---

## API Endpoints

### Product Endpoints

| Method | Endpoint                | Description                            | Auth Required |
|--------|-------------------------|----------------------------------------|--------------|
| GET    | `/product/list/`        | List all products                      | No           |
| GET    | `/product/<id>`         | Get product details                    | No           |
| POST   | `/product/create/`      | Create a new product                   | Yes          |
| PUT    | `/product/update/<id>`  | Update a product                       | Yes          |
| DELETE | `/product/delete/<id>`  | Delete a product                       | Yes          |
| GET    | `/product/seller/<id>`  | List products for a specific seller    | No           |

### Seller Endpoints

| Method | Endpoint            | Description                        | Auth Required |
|--------|---------------------|------------------------------------|--------------|
| POST   | `/signup`           | Seller registration                | No           |
| POST   | `/login`            | Seller login (returns JWT tokens)  | No           |
| GET    | `/dashboard`        | Seller dashboard                   | Yes          |

### JWT Endpoints

| Method | Endpoint                   | Description                      |
|--------|----------------------------|----------------------------------|
| POST   | `/api/token/`              | Get JWT token                    |
| POST   | `/api/token/refresh/`      | Refresh JWT token                |

---

## Example Usage

### Register Seller

```http
POST /signup
{
  "username": "seller01",
  "email": "seller01@example.com",
  "password": "mypassword"
}
```

### Login Seller

```http
POST /login
{
  "username": "seller01",
  "password": "mypassword"
}
```
_Response includes JWT access and refresh tokens._

### Create Product (Authenticated)

```http
POST /product/create/
Authorization: Bearer <your-jwt-token>
{
  "name": "Sample Product",
  "price": 100,
  "description": "A cool product.",
  "catalogue": "t-shirt"
}
```

---

## Caching (Redis) [Optional]

To enable caching, install and run Redis, then configure in your `settings.py`:

```python
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
```

You can use Django's cache API to optimize expensive queries.

---

## Running Tests

*(If implemented)*

```bash
python manage.py test
```

---

## Project Structure

```
django_api/
    settings.py
    urls.py
    wsgi.py
    asgi.py
product_catalog/
    models.py
    views.py
    serializer.py
    urls.py
manage.py
requirements.txt
```

---

## License

This project is licensed under the MIT License.

---

## Contact

For issues or feature requests, please use the [GitHub Issues](https://github.com/MahinShahriar/ProductAPI-django_restframework/issues) page.
