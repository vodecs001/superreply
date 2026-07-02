"""
Super Reply — 快捷短语管理器
启动: python main.py
管理员运行可获得全局热键支持
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtCore import Qt

from src.gui.main_window import MainWindow
from src.gui.popup_window import PopupWindow
from src.hotkey.manager import HotkeyManager
from src.db.models import get_setting
from src.locale import t


def main():
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    app.setApplicationName("SuperReply")
    # 设置应用图标
    icon_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(sys.argv[0]))), "icon", "icon.png")
    if os.path.exists(icon_path):
        from PyQt5.QtGui import QIcon
        app.setWindowIcon(QIcon(icon_path))

    # 主窗口（管理界面）
    window = MainWindow()

    # 快捷键弹窗
    popup = PopupWindow()

    # 托盘
    tray = QSystemTrayIcon()
    tray.setToolTip(t("tray_tooltip"))
    tray.setIcon(app.style().standardIcon(app.style().SP_FileDialogListView))

    tray_menu = QMenu()
    show_action = QAction(f"📋 {t('menu_show')}", tray_menu)
    show_action.triggered.connect(window.toggle_visible)
    tray_menu.addAction(show_action)
    tray_menu.addSeparator()
    quit_action = QAction(f"🚪 {t('menu_quit')}", tray_menu)
    quit_action.triggered.connect(app.quit)
    tray_menu.addAction(quit_action)
    tray.setContextMenu(tray_menu)
    tray.activated.connect(lambda r: window.toggle_visible()
                           if r == QSystemTrayIcon.DoubleClick else None)
    tray.show()

    # 全局热键 → 弹出快捷窗
    hotkey_str = get_setting("hotkey", "Alt+V")
    hotkey = HotkeyManager(hotkey_str, window)
    hotkey.hotkey_triggered.connect(lambda: popup.show_at_cursor())
    hotkey.start()

    # 管理窗口快捷键变化时重新注册
    def on_hotkey_changed(new_hotkey: str):
        hotkey.update_hotkey(new_hotkey)

    window.set_hotkey_callback(on_hotkey_changed)

    if "--minimized" not in sys.argv:
        window.show()

    exit_code = app.exec_()
    hotkey.stop()
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
