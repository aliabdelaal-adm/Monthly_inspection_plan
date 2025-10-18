# 🎯 Smart Inspection Planner - Quick Reference

## Access
**Main Site → System Services Management → Data Management → Smart Planning Tool (🎯✨)**

## Key Features

### ⚡ Instant Updates
- No manual JSON file uploads needed
- Changes reflect immediately in the main site
- Direct GitHub API integration

### 🎯 Smart Priority System

| Priority | Criteria | Color |
|----------|----------|-------|
| 🔴 **High** | Never inspected OR >30 days since last inspection | Red border |
| 🟡 **Medium** | 14-30 days since last inspection | Yellow border |
| 🟢 **Low** | <14 days since last inspection | Green border |

### 🚫 Smart Filtering Rules

1. **No Same-Day Duplicates**
   - Shop cannot be assigned to multiple inspectors on the same day
   
2. **7-Day Cooldown Period**
   - Same inspector cannot inspect the same shop within 7 days

## Quick Workflow

```
1. Login with GitHub Token
   ↓
2. Select: Inspector → Date → Shift → Area
   ↓
3. View filtered shops (sorted by priority)
   ↓
4. Click shops to select
   ↓
5. Review preview
   ↓
6. Save → Updates instantly!
```

## Statistics Display

| Stat | Description |
|------|-------------|
| **Total Shops** | All shops in selected area |
| **Available Shops** | After smart filtering |
| **High Priority** | Shops needing urgent inspection |
| **Selected Shops** | Shops you've chosen |

## Priority Score Calculation

```javascript
Score = Date Points + Activity Points

Date Points:
- Never inspected: +100
- >30 days: +80
- 21-30 days: +60
- 14-21 days: +40
- <14 days: +20

Activity Points:
- Requires registration: +30
```

## Visual Indicators

| Element | Meaning |
|---------|---------|
| Left border color | Priority level |
| Green background | Selected shop |
| Hover effect | Interactive/clickable |
| Badge (top-left) | Priority label |

## Troubleshooting

| Problem | Solution |
|---------|----------|
| No shops displayed | Check all dropdowns are selected |
| All shops filtered | Try different date or inspector |
| Save failed | Verify GitHub token permissions |

## Security Notes

✅ Token stored locally (localStorage)  
✅ HTTPS encrypted requests  
✅ Confirmation before saving  
✅ No sensitive data in URLs  

## Technical Details

- **API**: GitHub REST API v3
- **File Updated**: `plan-data.json`
- **Language**: Pure JavaScript (no dependencies)
- **Responsive**: Works on desktop and mobile

---

**Version**: 1.0.0  
**Developer**: Dr. Ali Abdelaal  
**Date**: October 2025
