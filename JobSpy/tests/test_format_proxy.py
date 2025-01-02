import unittest

from src.jobspy.scrapers.utils import RotatingProxySession


class TestProxyFormatter(unittest.TestCase):
    def test_http_proxy_with_only_http(self):
        proxy = "http://example.com:8080"
        expected = {"http": "http://example.com:8080"}
        result = RotatingProxySession.format_proxy(proxy, only_http=True)
        self.assertEqual(result, expected)

    def test_http_proxy_with_https(self):
        proxy = "http://example.com:8080"
        expected = {"http": "http://example.com:8080", "https": "http://example.com:8080"}
        result = RotatingProxySession.format_proxy(proxy, only_http=False)
        self.assertEqual(result, expected)

    def test_https_proxy_with_only_http(self):
        proxy = "https://example.com:8080"
        expected = {"http": "https://example.com:8080"}
        result = RotatingProxySession.format_proxy(proxy, only_http=True)
        self.assertEqual(result, expected)

    def test_https_proxy_with_https(self):
        proxy = "https://example.com:8080"
        expected = {"http": "https://example.com:8080", "https": "https://example.com:8080"}
        result = RotatingProxySession.format_proxy(proxy, only_http=False)
        self.assertEqual(result, expected)

    def test_plain_proxy_with_only_http(self):
        proxy = "example.com:8080"
        expected = {"http": "http://example.com:8080"}
        result = RotatingProxySession.format_proxy(proxy, only_http=True)
        self.assertEqual(result, expected)

    def test_plain_proxy_with_https(self):
        proxy = "example.com:8080"
        expected = {"http": "http://example.com:8080", "https": "http://example.com:8080"}
        result = RotatingProxySession.format_proxy(proxy, only_http=False)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
