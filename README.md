# Baby Tools Shop - E-Commerce Application

## Table of Contents

1. [Description](#description)
2. [Quickstart](#quickstart)
3. [Usage](#usage)
4. [Technologies](#technologies)
5. [Project Structure](#project-structure)
6. [Configuration](#configuration)
7. [Development](#development)
8. [Screenshots](#screenshots)

## Description

The Baby Tools Shop is a comprehensive e-commerce web application built with Django, specifically designed for selling baby tools and accessories. This repository contains a fully containerized Django application that provides essential e-commerce functionality including:

- **User Management**: Registration, login, and authentication system
- **Product Catalog**: Browse and view detailed product information
- **Category Filtering**: Filter products by categories for easy navigation
- **Responsive Design**: Modern and user-friendly interface
- **Admin Panel**: Django admin interface for content management

The primary purpose of this repository is to provide a production-ready, containerized e-commerce solution that can be easily deployed and scaled in any Docker-compatible environment.

## Quickstart

### Prerequisites

- Docker installed on your system
- Git for cloning the repository
- Port 8025 available on your machine

### Quick Setup

1. **Clone the repository**:
   ```bash
   git clone git@github.com:Developer-Akademie-GmbH/baby-tools-shop.git
   cd baby-tools-shop
   ```

2. **Build and run the Docker container**:
   ```bash
   docker build -t baby-tools-shop .
   docker run -p 8025:8025 baby-tools-shop
   ```

3. **Access the application**:
   Open your browser and navigate to `http://localhost:8025`

The application will be running with a pre-configured SQLite database and all necessary migrations applied automatically.

**Important:** After first startup, create an admin user to access the management interface:
```bash
docker exec -it baby-shop bash
python manage.py createsuperuser
exit
```

## Usage

### Docker Deployment

#### Building the Container

```bash
# Build the Docker image
docker build -t baby-tools-shop .
```

#### Running the Container

```bash
# Run with default settings
docker run -p 8025:8025 baby-tools-shop

# Run with custom environment variables
docker run -p 8025:8025 \
  -e DJANGO_SECRET_KEY="your-secret-key-here" \
  -e DJANGO_DEBUG="False" \
  baby-tools-shop

# Run in detached mode
docker run -d -p 8025:8025 --name baby-shop baby-tools-shop
```

#### Docker Compose (Optional)

Create a `docker-compose.yml` file for easier management:

```yaml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "8025:8025"
    environment:
      - DJANGO_SECRET_KEY=your-production-secret-key
      - DJANGO_DEBUG=False
    volumes:
      - media_volume:/app/media
volumes:
  media_volume:
```

### Environment Variables

The application supports the following environment variables for configuration:

| Variable | Default Value | Description |
|----------|---------------|-------------|
| `DJANGO_SECRET_KEY` | Auto-generated insecure key | Django secret key for production |
| `DJANGO_DEBUG` | `True` | Enable/disable Django debug mode |
| `PORT` | `8025` | Port on which the application runs |

### Production Deployment

For production deployment, ensure you:

1. **Set a secure secret key**:
   ```bash
   export DJANGO_SECRET_KEY="your-very-secure-secret-key"
   ```

2. **Disable debug mode**:
   ```bash
   export DJANGO_DEBUG="False"
   ```

3. **Use persistent volumes for media files**:
   ```bash
   docker run -p 8025:8025 \
     -v /host/media:/app/media \
     -e DJANGO_SECRET_KEY="your-secret-key" \
     -e DJANGO_DEBUG="False" \
     baby-tools-shop
   ```

### Database Management

The application uses SQLite by default. Database migrations are automatically applied during container startup. To create a superuser for admin access:

```bash
# Execute into running container
docker exec -it baby-shop bash

# Create superuser
python manage.py createsuperuser
```

**Example superuser creation:**
```bash
Username (leave blank to use 'appuser'): admin
Email address: admin@babyshop.com
Password: [enter secure password]
Password (again): [repeat password]
Superuser created successfully.
```

### Admin Panel

Access the Django admin panel at `http://localhost:8025/admin` (or `http:///<your_ip_adress>:8025/admin` for live deployment) with superuser credentials to:
- **Add/edit products**: Create and manage baby tools inventory
- **Manage categories**: Organize products into logical groups
- **View user accounts**: Monitor registered customers
- **Configure site settings**: Customize application behavior

**Admin Interface Features:**
- Fully localized German interface
- Product image upload and management
- Category-based product organization
- User registration and authentication management
- Content moderation capabilities

## Technologies

- **Python 3.9**: Programming language
- **Django 4.0.2**: Web framework
- **SQLite**: Database (default)
- **Docker**: Containerization
- **Pillow**: Image processing
- **HTML/CSS/JavaScript**: Frontend technologies

## Project Structure

```
baby-tools-shop/
├── babyshop_app/                 # Main Django application
│   ├── babyshop/                 # Project configuration
│   │   ├── settings.py           # Django settings
│   │   ├── urls.py               # Main URL configuration
│   │   └── wsgi.py               # WSGI configuration
│   ├── products/                 # Products application
│   │   ├── models.py             # Product and Category models
│   │   ├── views.py              # Product views
│   │   ├── urls.py               # Product URLs
│   │   └── migrations/           # Database migrations
│   ├── users/                    # User management application
│   │   ├── models.py             # User models
│   │   ├── views.py              # Authentication views
│   │   ├── forms.py              # User forms
│   │   └── urls.py               # User URLs
│   ├── templates/                # HTML templates
│   └── manage.py                 # Django management script
├── project_images/               # Application screenshots
├── Dockerfile                    # Container definition
├── requirements.txt              # Python dependencies
├── .gitignore                    # Git ignore rules
└── README.md                     # This file
└── Baby-Tools-Shop-Checked.pdf   # Checklist
```

## Configuration

### Django Settings

Key configuration files and their purposes:

- **`babyshop/settings.py`**: Main Django configuration
- **`babyshop/urls.py`**: URL routing configuration
- **Application URLs**: Each app has its own `urls.py` for specific routing

### Customization Options

1. **Database Configuration**: Modify `DATABASES` setting in `settings.py` to use PostgreSQL or MySQL
2. **Static Files**: Configure `STATIC_ROOT` and `STATIC_URL` for production static file serving
3. **Media Files**: Adjust `MEDIA_ROOT` and `MEDIA_URL` for file upload handling
4. **Security Settings**: Update `SECRET_KEY`, `ALLOWED_HOSTS`, and security middleware

### Adding New Products

Products can be added through:
1. Django admin panel (`/admin`)
2. Django shell (`python manage.py shell`)
3. Custom management commands
4. API endpoints (if implemented)

## Development

### Local Development Without Docker

1. **Setup virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations**:
   ```bash
   cd babyshop_app
   python manage.py migrate
   ```

4. **Start development server**:
   ```bash
   python manage.py runserver 8025
   ```

### Adding New Features

1. Create new Django apps: `python manage.py startapp newapp`
2. Add to `INSTALLED_APPS` in settings.py
3. Create models, views, and templates
4. Update URL configurations
5. Run migrations: `python manage.py makemigrations` and `python manage.py migrate`

## Screenshots

### Home Page with Login
![Home Page with Login](project_images/capture_20220323080815407.jpg)

### Home Page with Product Filter
![Home Page with Filter](project_images/capture_20220323080840305.jpg)

### Product Detail Page
![Product Detail Page](project_images/capture_20220323080934541.jpg)

### Home Page (Not Logged In)
![Home Page No Login](project_images/capture_20220323080953570.jpg)

### User Registration Page
![Register Page](project_images/capture_20220323081016022.jpg)

### User Login Page
![Login Page](project_images/capture_20220323081044867.jpg)

---


**Features:**
- ✅ Fully containerized Django application
- ✅ German language interface
- ✅ Responsive design with Bootstrap
- ✅ User authentication and registration
- ✅ Product catalog with categories
- ✅ Admin panel for content management
- ✅ Production-ready deployment

---

**Note**: This application is designed for educational and demonstration purposes. For production use, additional security measures, performance optimizations, and comprehensive testing should be implemented.