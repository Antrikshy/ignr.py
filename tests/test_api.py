"""Tests for ignr.api (no network: API.request is stubbed)."""

import unittest

from ignr.api import API


def make_api(response):
    api = API(None)
    api.request = lambda url="/": response
    return api


class TestGetTemplateList(unittest.TestCase):
    def test_strips_whitespace_and_drops_empties(self):
        api = make_api("python, django\nmacos, windows\n")
        self.assertEqual(
            api.get_template_list(), ["python", "django", "macos", "windows"]
        )

    def test_valid_tech_is_accepted(self):
        # 'django' is valid even though the raw list separates
        # entries with ", ". Must not raise ValueError.
        api = API(None)

        def fake_request(url="/"):
            if url == "/api/list":
                return "python, django"
            return "### Django ###\n*.pyc\n"

        api.request = fake_request
        self.assertEqual(api.get_gitignore(["django"]), "### Django ###\n*.pyc\n")

    def test_unknown_tech_still_rejected(self):
        api = make_api("python, django")
        with self.assertRaises(ValueError):
            api.get_gitignore(["cobol"])


if __name__ == "__main__":
    unittest.main()
