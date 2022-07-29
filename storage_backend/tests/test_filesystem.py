# Copyright 2017 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
import os

from odoo.exceptions import AccessError

from .common import Common, GenericStoreCase

ADAPTER_PATH = (
    "odoo.addons.storage_backend.components.filesystem_adapter.FileSystemStorageBackend"
)
class FileSystemCase(Common, GenericStoreCase):

    def test_move_files(self):
        backend = self.backend.sudo()
        base_dir = backend._get_adapter()._basedir()
        expected = [base_dir + "/" + self.filename]
        destination_path = os.path.join(base_dir, "destination")
        self._test_move_files(
            backend, ADAPTER_PATH, self.filename, destination_path, expected
        )


class FileSystemDemoUserAccessCase(Common):
    def _add_access_right_to_user(self):
        # We do not give the access to demo user
        # all test should raise an error
        pass

    def test_cannot_add_file(self):
        with self.assertRaises(AccessError):
            self.backend._add_b64_data(
                self.filename, self.filedata, mimetype=u"text/plain"
            )

    def test_cannot_list_file(self):
        with self.assertRaises(AccessError):
            self.backend._list()

    def test_cannot_read_file(self):
        with self.assertRaises(AccessError):
            self.backend._get_b64_data(self.filename)

    def test_cannot_delete_file(self):
        with self.assertRaises(AccessError):
            self.backend._delete(self.filename)
