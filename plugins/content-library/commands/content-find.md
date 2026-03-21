# /content-find

Search the Content Library for existing copy or assets matching your query. Always check the library before creating new content.

## How to Invoke

**Find copy by type or channel:**
```
/content-find meta ad copy
/content-find email welcome series
/content-find landing page copy spring launch
/content-find google RSA headlines
```

**Find copy by campaign:**
```
/content-find campaign:2026-03-spring-launch
/content-find campaign:evergreen
```

**Find copy by tag or attribute:**
```
/content-find before-after hook
/content-find social proof urgent
/content-find high-performer
```

**Find assets:**
```
/content-find assets lifestyle photography
/content-find assets video 9x16
/content-find assets product shots white background
/content-find assets approved-for-paid-media
```

**Find both copy and assets:**
```
/content-find spring launch
/content-find [keyword] --all
```

## What You Get

A formatted list of all matching items:
- Copy: title, ID, type, channel, campaign, status, preview text, file path, tags
- Assets: name, ID, type, format, dimensions, license status, description, file path
- Status flags: ✅ Approved / 🔄 In review / ⏸ Paused / ❌ Retired (retired items flagged but not recommended)

## Tips

- Use broad terms first, then narrow down
- Tag searches are powerful: `high-performer`, `untested`, `fatigued`
- License expiry and model release issues are flagged automatically
- If nothing is found, the library will say so — only then should new content be created
