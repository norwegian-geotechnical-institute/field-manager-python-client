import sys
import types
import unittest
from unittest.mock import patch


keycloak_module = types.ModuleType("keycloak")
keycloak_module.KeycloakOpenID = object
sys.modules.setdefault("keycloak", keycloak_module)

from field_manager_python_client import auth


class ServiceAccountAuthTests(unittest.TestCase):
    def test_service_account_rejects_device_code_client_id(self):
        with self.assertRaisesRegex(ValueError, "shared device-code client"):
            auth.get_service_account_client(
                environment="test",
                client_id=auth.ENVIRONMENTS["test"]["KEYCLOAK_DEVICE_CLIENT_ID"],
                client_secret="secret",
            )

    def test_service_account_uses_dedicated_client_id(self):
        class DummyKeycloakOpenID:
            def __init__(self, **kwargs):
                self.kwargs = kwargs

            def token(self, grant_type):
                self.grant_type = grant_type
                return {"access_token": "token"}

        instances = []

        def create_keycloak(**kwargs):
            instance = DummyKeycloakOpenID(**kwargs)
            instances.append(instance)
            return instance

        with patch.object(auth, "KeycloakOpenID", create_keycloak):
            client = auth.get_service_account_client(
                environment="test",
                client_id="dedicated-client",
                client_secret="secret",
            )

        self.assertEqual(client.token, "token")
        self.assertEqual(instances[0].grant_type, "client_credentials")
        self.assertEqual(instances[0].kwargs["client_id"], "dedicated-client")
        self.assertEqual(instances[0].kwargs["client_secret_key"], "secret")

    def test_service_account_uses_service_account_env_var(self):
        class DummyKeycloakOpenID:
            def __init__(self, **kwargs):
                self.kwargs = kwargs

            def token(self, grant_type):
                return {"access_token": "token"}

        instances = []

        def create_keycloak(**kwargs):
            instance = DummyKeycloakOpenID(**kwargs)
            instances.append(instance)
            return instance

        with (
            patch.object(auth, "KeycloakOpenID", create_keycloak),
            patch.dict(
                "os.environ",
                {
                    "KEYCLOAK_SERVICE_ACCOUNT_CLIENT_ID": "service-account-client",
                    "KEYCLOAK_CLIENT_SECRET": "secret",
                },
            ),
        ):
            auth.get_service_account_client(environment="test")

        self.assertEqual(instances[0].kwargs["client_id"], "service-account-client")


if __name__ == "__main__":
    unittest.main()
