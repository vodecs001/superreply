# 超级回复 (Super Reply)

> 一款快速、优雅的 Windows 快捷短语管理工具。按下 `Alt+V`，即可在任意软件中快速粘贴常用语。

## ✨ 功能特色

- **无限分组** — 树形结构，支持无限嵌套子分组
- **快捷粘贴** — 全局快捷键（默认 `Alt+V`）在光标处弹出短语面板
- **自适应布局** — 自动模式根据内容调整窗口大小，无滚动条，短语多时自动分列
- **深色 / 浅色 / 跟随系统** — 三种主题模式自由切换
- **导入 / 导出** — JSON 格式备份，方便迁移和同步
- **键盘 / 鼠标快捷键** — 支持自定义组合键

## 🚀 快速开始

1. 从 [Releases](../../releases) 下载 `SuperReply.exe`
2. 双击运行（自动进入系统托盘）
3. 按 `Alt+V` 呼出短语窗口
4. 右键分组 → **添加短语** 创建自己的常用语

## 🛠 从源码构建

```bash
git clone https://github.com/yourname/super-reply.git
cd super-reply
pip install -r requirements.txt
python main.py
```

打包 EXE：
```bash
pyinstaller --onedir --windowed --clean --name "SuperReply" main.py
```

## 📁 项目结构

```
super-reply/
├── main.py              # 入口文件
├── src/
│   ├── db/              # SQLite 数据库层
│   ├── gui/             # PyQt5 界面组件
│   ├── hotkey/          # 全局热键管理
│   └── locale.py        # 多语言支持 (中/英/日)
├── Contact Information/ # 作者联系方式图片
└── requirements.txt
```

## 🎯 默认快捷键

`Alt+V` — 可在设置中自定义。

## 👤 作者

**执简**

联系方式请查看软件中帮助 → 关于作者。

## 📄 许可证

MIT
