# Super Reply (超级回复)

> A fast, elegant quick-phrase manager for Windows. Press `Alt+V` to paste your most-used text snippets instantly.

## ✨ Features

- **Unlimited Groups** — tree-structured groups with nesting support
- **Quick Paste** — global hotkey (`Alt+V` by default) to pop up a phrase panel at cursor
- **Auto-fit Layout** — auto mode resizes the popup to show all phrases without scrolling, using multi-column when needed
- **Dark / Light / Follow-system** — three theme modes built-in
- **Import / Export** — JSON backup for migration and sync
- **Keyboard & Mouse Hotkeys** — customizable shortcuts

## 🚀 Quick Start

1. Download `SuperReply.exe` from [Releases](../../releases)
2. Double-click to run (appears in system tray)
3. Press `Alt+V` to open the phrase popup
4. Right-click groups → **Add Phrase** to create your own snippets

## 🛠 Build from Source

```bash
git clone https://github.com/yourname/super-reply.git
cd super-reply
pip install -r requirements.txt
python main.py
```

Build EXE:
```bash
pyinstaller --onedir --windowed --clean --name "SuperReply" main.py
```

## 📁 Project Structure

```
super-reply/
├── main.py              # Entry point
├── src/
│   ├── db/              # SQLite schema & models
│   ├── gui/             # PyQt5 UI components
│   ├── hotkey/          # Global hotkey manager
│   └── locale.py        # i18n (zh/en/jp)
├── Contact Information/ # Author contact image
└── requirements.txt
```

## 🎯 Default Hotkey

`Alt+V` — customizable in settings.

## 🌐 Languages

- 中文 (default)
- English
- 日本語

Language can be switched in Settings.

## 👤 Author

**执简**

Contact: see Help → About in the app.

## 📄 License

MIT
