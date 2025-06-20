"""A client library for accessing Field Manager Data API"""

from .auth import TokenManager, authenticate, get_prod_client, get_test_client
from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
    "authenticate",
    "get_test_client",
    "get_prod_client",
    "TokenManager",
)
