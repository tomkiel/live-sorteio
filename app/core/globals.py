from dynaconf import settings
from flask import request


def init_app(app):
    @app.context_processor
    def inject_globals():
      return {
        "app_name": settings.get("APP_NAME") or "[DEV_MOD] - FALAFEL",
        "app_url": settings.get("APP_URL") if settings.get("APP_ENV") == "production" else request.url_root,
        "app_env": settings.get("APP_ENV") or "development",
        "app_version": settings.get("APP_VERSION")
    }