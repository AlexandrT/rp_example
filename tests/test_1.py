import requests
import pytest
import logging


logger = logging.getLogger('public_api')


class TestExample:
    def setup_class(cls):
        logger.info('=================================================================')

    def teardown_class(cls):
        logger.info('-----------------------------------------------------------------')

    def setup_method(self, method):
        logger.info('==================TEST STARTED==================')
        logger.info(f"{self.__doc__} {method.__doc__}")

    def teardown_method(self, method):
        logger.info('------------------TEST FINISHED------------------')

    @pytest.mark.parametrize(
        "expected",
        [
            1,
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12
        ]
    )
    def test_ok(self, expected):
        '''example'''
        req = requests.get('https://cat-fact.herokuapp.com/facts')

        assert req.status_code == expected

