import stripe

from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_product(paid_course):
    """Создает продукт в страйпе."""
    stripe_product = stripe.Product.create(name="paid_course")
    return stripe_product


def create_stripe_price(amount, paid_course):
    """Создает цену в страйпе."""
    stripe_price = stripe.Price.create(
        currency="rub",
        unit_amount=int(float(amount) * 100),
        product_data={"name": paid_course},
    )
    return stripe_price


def create_stripe_session(stripe_price):
    """Создает сессию на оплату в страйпе."""
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": stripe_price.get("id"), "quantity": 1}],
        mode="payment",
    )
    return session.get("id"), session.get("url")
