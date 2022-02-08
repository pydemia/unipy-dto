
# from ..unipy_dto.api import Settings
from unipy_dto.config.base import JsonConfig, EnvConfig, DotEnvConfig
from pydantic import Extra
from autologging import logged
from unittest import TestCase, mock, main
import os
from pprint import pprint


class Test_LoadConfig(TestCase):

    def setUp(self):
        config = JsonConfig()
        self.assertEqual(config.Config.allow_mutation, False)
        pprint(config.dict())
        self.config = config

    def test_if_attr_is_mutable(self):
        print(self.config.app_name)
        self.assertEqual(self.config.app_name, "JsonConfig")

        # Raise 'TypeError' if 'setter' is called
        # when 'allow_mutation' is set as 'False'.
        with self.assertRaises(TypeError):
            self.config.app_name = "JSON"
            print(self.config.app_name)
    
    def test_validator(self):
        cpu_spec = self.config.cpu_spec
        print(cpu_spec)
        self.assertGreaterEqual(
            cpu_spec.cpu_max, cpu_spec.cpu_min
        )
        # with self.assertWarns()
        self.config.cpu_spec.cpu_max = self.config.cpu_spec.cpu_min - 1
        print(cpu_spec.cpu_max)

    def tearDown(self):
        pass


if __name__ == "__main__":
    main()
