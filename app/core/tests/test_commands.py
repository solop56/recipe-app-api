"""
Test custom Django management commands.
"""
from unittest.mock import patch

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase
from psycopg2 import OperationalError as Psycopg20pError


@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """Test commands."""
    def test_wait_for_db_ready(self, patched_checked):
        """Testing for database if database is ready."""
        patched_checked.return_value = True
        call_command('wait_for_db')
        patched_checked.assert_called_once_with(databases=['default'])

    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_checked):
        """Testing for database if database when getting OperationalError."""
        patched_checked.side_effect = [Psycopg20pError] * 2 +  \
                                      [OperationalError] * 3 + [True]
        call_command('wait_for_db')
        self.assertEqual(patched_checked.call_count, 6)
        patched_checked.assert_called_with(databases=['default'])
