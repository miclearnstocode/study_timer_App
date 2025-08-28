# Expose Flask Blueprints instead of Tkinter classes
from .user_routes import user_bp
from .timer_routes import timer_bp

__all__ = ["user_bp", "timer_bp"]
