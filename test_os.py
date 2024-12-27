import unittest

class TestOS(unittest.TestCase):
    def test_taskbar(self):
        from taskbar import Taskbar
        taskbar = Taskbar()
        self.assertEqual(taskbar.position, "top")
        self.assertEqual(taskbar.start_button, "Launcher")

    def test_app_store(self):
        from app_store import AppStore
        app_store = AppStore()
        self.assertEqual(len(app_store.apps), 0)

    def test_command_interface(self):
        from command_interface import CommandInterface
        command_interface = CommandInterface()
        command_interface.install_app("Example App")
        self.assertIn("Example App", command_interface.installed_apps)

if __name__ == "__main__":
    unittest.main()
  
