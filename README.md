# pairwise-vfr-cfr-timebase

## 领域

游戏、图形与多媒体

## 主题

VFR 视频转恒定帧率

## 说明

时间戳有理数化、显示序重建、运动感知丢帧。

初始状态下 `av/vfr_cfr.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
