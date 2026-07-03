# Super Reply (超级回复)

> A fast, elegant quick-phrase manager for Windows. Press `Alt+V` to paste your saved text snippets into any application.

## Features

- **2-level group tree** — root groups + one level of sub-groups, with count badges
- **Quick paste** — global hotkey (`Alt+V` default) opens a phrase panel at cursor position
- **Auto-fit layout** — auto mode resizes the panel to show all phrases without scrolling. When phrases exceed vertical space, they flow into multiple columns
- **Dark / Light / Follow-system** — 3 theme modes, switchable from the toolbar
- **Import / Export** — JSON backup for migration between devices
- **Customizable hotkeys** — supports single keys (F1~F12) and combos (Ctrl+Alt+X)
- **Phrase management** — add/edit/delete/pin phrases via right-click on groups

## Quick Start

1. Download `SuperReply.exe` from [Releases](../../releases)
2. Double-click to run (tray icon in system tray)
3. Press `Alt+V` to open the phrase popup
4. Right-click a group → **Add Phrase** to create your first snippet
5. Click any phrase to paste it into the active application

## How It Works

**Management Window** — where you organize groups and phrases:
- Left panel: group tree (right-click to create/manage groups)
- Right panel: phrase list (double-click to edit)
- Toolbar: theme switch, import/export, settings, about

**Popup Window** — activated by hotkey, appears at cursor:
- Left: group tree (hover to switch groups)
- Right: phrase list (click to paste)
- Click outside or press ESC to dismiss

## Build from Source

```bash
pip install -r requirements.txt
python main.py
```

To create standalone EXE:
```bash
pyinstaller --onefile --windowed --name "SuperReply" --icon=icon/icon.png main.py
```

## Project Structure

```
├── main.py              # Entry point
├── src/
│   ├── db/              # SQLite schema & CRUD
│   ├── gui/             # PyQt5 UI (main window, popup, phrase list, group tree, themes)
│   ├── hotkey/          # Global hotkey via Windows RegisterHotKey API
│   └── locale.py        # i18n (zh/en/jp)
├── Contact_Information/ # Author contact images
└── requirements.txt
```

## Default Hotkey

`Alt+V` — customizable in Settings → Hotkey.

## Languages

- 中文 (default)
- English
- 日本語

## Author

**执简** — see Help → About in the app.

## License

MIT
