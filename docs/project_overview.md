# TouchBar Lyrics

## Project Goal

为 macOS Apple Music 提供实时同步歌词显示。

系统通过读取 Apple Music 当前播放状态，获取歌曲对应歌词，并根据播放进度实时同步显示。

初期输出到终端。

后期支持：

* BetterTouchTool
* Touch Bar
* 菜单栏歌词
* 双语歌词
* 本地缓存

---

## MVP

Apple Music

↓

读取歌曲信息

↓

获取歌词

↓

同步歌词

↓

终端显示

---

## Core Modules

### Player Layer

负责获取：

* Song Name
* Artist
* Album
* Position
* State

### Lyric Provider Layer

负责：

* 网易云歌词
* QQ音乐歌词

### LRC Parser Layer

负责：

* LRC解析
* 时间轴建立

### Sync Engine

负责：

* 歌词同步

### Output Layer

负责：

* Terminal
* BetterTouchTool
* Touch Bar

---

## Development Stages

V0.1

Apple Music 信息读取

V0.2

歌词获取

V0.3

歌词同步

V0.4

Touch Bar 输出

V1.0

完整产品
