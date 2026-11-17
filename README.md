# makefun-ai-judge-rich-01

[![ai-judge-rich-01](https://make.fun/badge/ai-judge-rich-01.svg)](https://make.fun/bounty/ai-judge-rich-01)
[![rank](https://make.fun/badge/ai-judge-rich-01/duchuAz/makefun-ai-judge-rich-01/rank.svg)](https://make.fun/bounty/ai-judge-rich-01)
[![reward](https://make.fun/badge/ai-judge-rich-01/duchuAz/makefun-ai-judge-rich-01/reward.svg)](https://make.fun/bounty/ai-judge-rich-01)

A deterministic Python 3.13 entry for the **ai-judge-rich-01** bounty on
[make.fun](https://make.fun/bounty/ai-judge-rich-01). It writes one plain-text
30-day money plan to `entry.txt` using only the standard library.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

This writes `out/entry.txt` as UTF-8 with no extra bytes. The same bytes are
written on every run.

## License

MIT. See [LICENSE](LICENSE).
