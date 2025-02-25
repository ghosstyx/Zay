# Zay

**Zay** is a modern e-commerce web application built using Django, providing a robust platform for online shopping and order management.

## Features

- **Product Catalog**: Browse a wide variety of products with detailed descriptions.
- **Shopping Cart**: Add, update, and remove items from your cart with ease.
- **Order Placement**: Seamlessly place orders and provide delivery details.
- **Admin Panel**: Manage products, categories, and orders through the Django admin interface.

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/ghosstyx/Zay.git
   cd Zay
2. **Set up a virtual environment**:    
   ```bash
    python -m venv env
   source env/bin/activate  # For Windows: env\Scripts\activate

3. **Install dependencies:**:
   ```bash
   pip install -r requirements.txt

4. **Apply database migrations**:
    ```bash
   python manage.py migrate

5. **Run the development server**:
    ```bash
   python manage.py runserver


## Usage

- **Home Page**: Browse featured products.
- **Product Details**: View detailed information about each product.
- **Shopping Cart**: Add products to your cart and review your selections.
- **Checkout**: Provide shipping details and confirm your order
