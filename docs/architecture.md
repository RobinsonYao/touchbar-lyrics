# System Architecture

Apple Music

↓

Player Layer

↓

Lyric Provider

↓

LRC Parser

↓

Sync Engine

↓

Output Layer

↓

Terminal / BetterTouchTool / Touch Bar

---

Module Dependency

main.py

↓

player.py

↓

lyric_provider.py

↓

lrc_parser.py

↓

sync_engine.py

↓

btt_output.py

Output Layer

Purpose:
Decouple lyric rendering from lyric engine.

Interfaces:
    OutputBase.send(text)

Implementations:
    TerminalOutput
    TouchBarOutput (future)
    MenuBarOutput (future)
    DesktopOutput (future)

Dependency Direction:

runtime
    ↓
OutputBase
    ↓
TerminalOutput / TouchBarOutput