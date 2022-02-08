
# from ..unipy_dto.api import Settings
from unipy_dto.config.base import JsonConfig, EnvConfig, DotEnvConfig
from pydantic import Extra
from autologging import logged
from unittest import TestCase, mock, main
import os
from pprint import pprint


class Test_LoadConfig(TestCase):

    def test_load_from_json(self):
        config = JsonConfig()
        self.assertIsInstance(config, JsonConfig)
        # Is extra values Allowed?
        self.assertEqual(config.Config.extra, Extra.allow)
        # Is editing values Allowed?
        self.assertEqual(config.Config.allow_mutation, False)
        # Printout given values
        print("JSON:")
        pprint(config.dict())

    @mock.patch.dict(os.environ,
        {
            "OS_DIST": "linux",
            "cpu_spec__cpu_min": "0.9",
            "cpu_spec__cpu_max": "0.5"
        }
    )
    def test_load_from_env(self):
        config = EnvConfig()
        self.assertIsInstance(config, EnvConfig)
        # Is extra values Allowed?
        self.assertEqual(config.Config.extra, Extra.allow)
        # Is editing values Allowed?
        self.assertEqual(config.Config.allow_mutation, True)
        # Printout given values
        print("ENV:")
        pprint(config.dict())

    def test_load_From_dotenv(self):
        config = DotEnvConfig()
        self.assertIsInstance(config, DotEnvConfig)
        # Is extra values Allowed?
        self.assertEqual(config.Config.extra, Extra.allow)
        # Is editing values Allowed?
        self.assertEqual(config.Config.allow_mutation, False)
        # Printout given values
        print("DOTENV:")
        pprint(config.dict())


if __name__ == "__main__":
    main()
