from unittest import TestCase
from unittest.mock import patch

from gutenberg_http import logic


class MetadataTests(TestCase):
    @patch.object(logic, 'get_metadata')
    def test_is_cached(self, mock_get_metadata):
        logic.metadata(fields='title', text_id=123)
        logic.metadata(fields='title', text_id=123)
        self.assertEqual(mock_get_metadata.call_count, 1)

        logic.metadata(fields='author', text_id=123)
        self.assertEqual(mock_get_metadata.call_count, 2)

        logic.metadata(fields='author', text_id=456)
        self.assertEqual(mock_get_metadata.call_count, 3)


class BodyTests(TestCase):
    @patch.object(logic, 'load_etext')
    def test_is_cached(self, mock_load_etext):
        logic.body(text_id=123)
        logic.body(text_id=123)
        self.assertEqual(mock_load_etext.call_count, 1)

        logic.body(text_id=456)
        self.assertEqual(mock_load_etext.call_count, 2)


class SearchTests(TestCase):
    @patch.object(logic, 'get_etexts')
    def test_is_cached(self, mock_get_etexts):
        logic.search('title eq Moby Dick')
        logic.search('title eq Moby Dick')
        self.assertEqual(mock_get_etexts.call_count, 1)

        logic.search('title eq The Jungle Book')
        self.assertEqual(mock_get_etexts.call_count, 2)