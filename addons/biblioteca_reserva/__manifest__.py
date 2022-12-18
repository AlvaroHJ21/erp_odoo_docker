{
    "name": "Biblioteca Reserva",
    'author': 'Grupo 5',
    'category':'Extra Tools',
    'version': '1.0.0',
    "depends": ["base"],
    "summary": "Un sistema inteligente de gestión de bibliotecas.",
    "description": """
        El propósito de un sistema de gestión de bibliotecas es operar una biblioteca con eficiencia y a costos reducidos. Las actividades de la biblioteca incluyen la compra de libros, la catalogación, la indexación de libros, el registro de libros en circulación y la verificación de existencias, que cuando se realizan mediante un software automatizado eliminan la necesidad de un trabajo manual repetitivo y minimizan las posibilidades de errores.
    """,
    "data": [
        "security/ir.model.access.csv",
        "views/books.xml",
        "views/book_items.xml",
        "views/libraries.xml",
        "views/members.xml",
        "views/reservations.xml",
        "views/menu.xml",
    ],
    'installable': True,
    'application': True,
    'auto-install': False
}
