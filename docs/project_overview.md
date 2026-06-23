# TouchBar Lyrics

## 项目简介

TouchBar Lyrics 是一个运行于 macOS 的实时歌词显示工具。

程序自动读取 Apple Music 当前播放歌曲，通过网易云音乐接口搜索并获取歌词，完成歌词解析、缓存与同步，并最终在 MacBook Touch Bar 上实时显示歌词。

项目目标是在不修改 Apple Music 的前提下，为 Touch Bar 提供类似原生播放器的实时歌词体验。

---

## 当前功能

### 歌曲识别

* 自动获取 Apple Music 当前播放歌曲
* 获取歌曲名称
* 获取歌手名称
* 获取歌曲时长

### 歌词匹配

* 网易云音乐搜索
* 歌名匹配
* 歌手匹配
* 时长匹配

### 歌词处理

* 下载 LRC 歌词
* LRC 解析
* 时间轴生成
* 实时歌词同步

### 本地缓存

* 歌词自动缓存
* 缓存优先读取
* 减少网络请求

### Touch Bar 输出

* 实时歌词显示
* 自动随歌曲切换
* 自动同步当前播放进度

---

## 技术栈

* Python 3.11
* PyObjC
* AppleScript
* Apple Music
* NetEase Music API

---

## 当前状态

V1.0-alpha

核心功能已完成验证，可正常运行。
