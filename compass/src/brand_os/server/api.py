"""FastAPI server (optional)."""
from __future__ import annotations


def create_app():
    """Create FastAPI application.

    Requires: fastapi, uvicorn optional dependencies
    """
    try:
        from fastapi import FastAPI
    except ImportError:
        raise ImportError("fastapi required. Install with: pip install brand-os[server]")

    app = FastAPI(
        title="brandos",
        description="Brand operations API",
        version="0.1.0",
    )

    # Health check
    @app.get("/health")
    async def health():
        return {"status": "ok"}

    # TODO: Add routes for each module
    # - /persona/*
    # - /intel/*
    # - /signals/*
    # - /plan/*
    # - /produce/*
    # - /eval/*
    # - /publish/*
    # - /monitor/*

    return app


def run_server(host: str = "127.0.0.1", port: int = 8000):
    """Run the API server."""
    try:
        import uvicorn
    except ImportError:
        raise ImportError("uvicorn required. Install with: pip install brand-os[server]")

    app = create_app()
    uvicorn.run(app, host=host, port=port)
