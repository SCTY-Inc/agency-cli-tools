"""Signal providers."""
from brand_os.signals.providers.google_news import fetch_google_news
from brand_os.signals.providers.web import fetch_web_signals

__all__ = ["fetch_google_news", "fetch_web_signals"]
