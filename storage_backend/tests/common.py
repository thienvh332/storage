# Copyright 2017 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import base64

from unittest import mock

from odoo.addons.component.tests.common import TransactionComponentCase


class GenericStoreCase(object):
    def _test_setting_and_getting_data(self):
        # Check that the directory is empty
        files = self.backend.list_files()
        self.assertNotIn(self.filename, files)

        # Add a new file
        self.backend.add(
            self.filename, self.filedata, mimetype=u"text/plain", binary=False
        )

        # Check that the file exist
        files = self.backend.list_files()
        self.assertIn(self.filename, files)

        # Retrieve the file added
        data = self.backend.get(self.filename, binary=False)
        self.assertEqual(data, self.filedata)

        # Delete the file
        self.backend.delete(self.filename)
        files = self.backend.list_files()
        self.assertNotIn(self.filename, files)

    def test_setting_and_getting_data_from_root(self):
        self._test_setting_and_getting_data()

    def test_setting_and_getting_data_from_dir(self):
        self.backend.directory_path = self.case_with_subdirectory
        self._test_setting_and_getting_data()
    def _test_move_files(
        self,
        backend,
        adapter_dotted_path,
        filename,
        destination_path,
        expected_filepaths,
    ):
        with mock.patch(adapter_dotted_path + ".move_files") as mocked:
            mocked.return_value = expected_filepaths
            res = backend.move_files(filename, destination_path)
            self.assertEqual(sorted(res), sorted(expected_filepaths))


class Common(TransactionComponentCase):
    def _add_access_right_to_user(self):
        self.user.write({"groups_id": [(4, self.env.ref("base.group_system").id)]})

    def setUp(self):
        super(Common, self).setUp()
        self.user = self.env.ref("base.user_demo")
        self._add_access_right_to_user()
        self.env = self.env(user=self.user)
        self.backend = self.env.ref("storage_backend.default_storage_backend")
        self.filedata = base64.b64encode(b"This is a simple file")
        self.filename = "test_file.txt"
        self.case_with_subdirectory = "subdirectory/here"
