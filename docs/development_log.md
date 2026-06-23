## 2026-06-23

### Touch Bar 集成完成

完成内容：

1. PyObjC 环境搭建
2. NSTouchBar 调用验证
3. Touch Bar Hello World 测试
4. 动态文本更新测试
5. Apple Music 实时歌词显示
6. 歌曲切换自动重载
7. 歌词缓存机制验证

关键成果：

实现 Apple Music → 网易云歌词 → Touch Bar 的完整链路。

项目达到首个可运行版本。

版本定义：

V1.0-alpha

2026-06-23

Key findings:

NSTouchBar depends on KeyWindow.

orderOut() destroys TouchBar ownership.

NSApplicationActivationPolicyProhibited suppresses TouchBar.

Accessory mode works.

Ghost Window selected for V1.x.

V1.1-B2-D1

完成 Menubar 动态菜单控制。

新增：

- Collapse TouchBar
- Expand TouchBar

实现：

EXPANDED ⇄ COLLAPSED

状态机。

MenuActions 独立负责菜单回调。

MenuApp 负责状态切换。

TouchBar 与 Menubar 共用 AppState。