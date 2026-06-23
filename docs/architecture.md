# Architecture

## 系统架构

Apple Music

↓

player.py

↓

netease_provider.py

↓

cache_manager.py

↓

lrc_parser.py

↓

sync_engine.py

↓

touchbar_output.py

↓

MacBook Touch Bar

---

## 模块说明

### player.py

负责获取 Apple Music 当前播放信息。

输出：

* 歌曲名
* 歌手
* 时长
* 当前播放位置

---

### netease_provider.py

负责：

* 搜索歌曲
* 最佳匹配
* 下载歌词

---

### cache_manager.py

负责：

* 歌词缓存
* 缓存读取
* 缓存保存

---

### lrc_parser.py

负责：

* LRC解析
* 时间轴生成

---

### sync_engine.py

负责：

* 根据播放时间查找当前歌词

---

### touchbar_output.py

负责：

* Touch Bar 初始化
* 歌词显示
* Touch Bar 更新

---

### realtime_player.py

系统运行主循环。

职责：

* 歌曲切换检测
* 歌词加载
* 同步调度
* 输出调度
