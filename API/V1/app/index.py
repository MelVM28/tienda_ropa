from .controllers.usuarios   import usuarios_bp
from .controllers.marcas     import marcas_bp
from .controllers.prendas    import prendas_bp
from .controllers.ventas     import ventas_bp
from .controllers.reportes   import reportes_bp

def register_routes(app):
    app.register_blueprint(usuarios_bp)
    app.register_blueprint(marcas_bp)
    app.register_blueprint(prendas_bp)
    app.register_blueprint(ventas_bp)
    app.register_blueprint(reportes_bp)
