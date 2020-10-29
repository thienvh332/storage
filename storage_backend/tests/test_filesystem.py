# Copyright 2017 Akretion (http://www.akretion.com).
# @author Sébastien BEAU <sebastien.beau@akretion.com>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
import os

from odoo.exceptions import AccessError

from .common import CommonCase, BackendStorageTestMixin


ADAPTER_PATH = (
    "odoo.addons.storage_backend.components.filesystem_adapter.FileSystemStorageBackend"
)


class FileSystemCase(CommonCase, BackendStorageTestMixin):

    def test_setting_and_getting_data_from_root(self):
        self._test_setting_and_getting_data_from_root()

    def test_setting_and_getting_data_from_dir(self):
        self._test_setting_and_getting_data_from_dir()

    def test_move_files(self):
        backend = self.backend.sudo()
        base_dir = backend._get_adapter()._basedir()
        expected = [base_dir + "/" + self.filename]
        destination_path = os.path.join(base_dir, "destination")
        self._test_move_files(
            backend, ADAPTER_PATH, self.filename, destination_path, expected
        )


class FileSystemDemoUserAccessCase(CommonCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.backend = cls.backend.sudo(cls.demo_user)

    def test_cannot_add_file(self):
        with self.assertRaises(AccessError):
            self.backend.add(
                self.filename, self.filedata, mimetype="text/plain", binary=False
            )

    def test_cannot_list_file(self):
        with self.assertRaises(AccessError):
            self.backend.list_files()

    def test_cannot_read_file(self):
        with self.assertRaises(AccessError):
            self.backend.get(self.filename, binary=False)

    def test_cannot_delete_file(self):
        with self.assertRaises(AccessError):
            self.backend._delete(self.filename)
