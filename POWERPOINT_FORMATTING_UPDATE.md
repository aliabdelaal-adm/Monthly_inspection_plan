# PowerPoint Report Formatting Update

## Overview
This update aligns all PowerPoint report generation with the design and formatting standards established in `sea-world.pptx`.

## Changes Made

### 1. RTL (Right-to-Left) Text Direction
- Updated all text elements to use proper RTL formatting
- Changed individual text elements from `rtlMode: true` to `rtl: true`
- Maintained presentation-level RTL setting: `pptx.rtlMode = true`

### 2. Files Updated
- `index.html` - Shelter inspection reports PowerPoint generation (17 RTL updates)
- `index13.html` - Group inspection reports PowerPoint generation (21 RTL updates)

### 3. Formatting Specifications (Matching sea-world.pptx)

#### Title Slide
- Main title: 54pt, Bold, Centered, RTL
- Subtitle: 24pt, Centered, RTL
- Date: 20pt, Centered, RTL
- Background color: FF9800 (Orange)
- Header decoration: 4A90E2 (Blue)

#### Report Summary Slide
- Header: 36pt, Bold, Centered, White text, RTL
- Header background: FF9800 (Orange)
- Table font size: 20pt
- Table alignment: Right (RTL)
- Column widths: [6, 3] inches
- Row height: 0.42 inches
- Cell margins: 0.1 inches (top/bottom)

#### Checklist Slide
- Header: 36pt, Bold, Centered, White text, RTL
- Header background: 4A90E2 (Blue)
- Table font size: 18pt
- Table alignment: Right (RTL)
- Column widths: [3, 6] inches
- Row height: 0.38 inches
- Cell margins: 0.1 inches (top/bottom)

#### Notes & Recommendations Slide
- Header: 36pt, Bold, Centered, White text, RTL
- Header background: F39C12 (Accent Orange)
- Section titles: 24pt, Bold, Right-aligned, RTL
- Content text: 18pt, Right-aligned, RTL

#### Photos Slide
- Header: 32pt, Bold, Centered, White text, RTL
- Header background: 27AE60 (Green)
- Photo captions: 16pt, Bold, Centered, RTL

#### Final Summary Slide
- Title: 48pt, Bold, Centered, White text, RTL
- Subtitle: 24pt, Italic, Centered, White text, RTL
- Background: 27AE60 (Green)

### 4. Theme Colors
```javascript
const themeColors = {
    primary: '4A90E2',      // Blue
    secondary: 'ff9800',    // Orange
    accent: 'F39C12',       // Accent Orange
    success: '27AE60',      // Green
    warning: 'E74C3C',      // Red
    dark: '2C3E50',         // Dark Gray
    light: 'ECF0F1'         // Light Gray
};
```

## Technical Details

### RTL Property Usage
The correct RTL property for PptxGenJS text elements is `rtl: true`, not `rtlMode: true`.
- `pptx.rtlMode = true` - Sets presentation-level RTL (correct)
- `rtl: true` - Sets individual text element RTL (correct)
- `rtlMode: true` - Incorrect for text elements (was changed)

### Table Configuration
Tables use the following properties to ensure proper RTL alignment:
```javascript
slide.addTable(rows, {
    fontSize: 20,           // Font size in points
    fontFace: 'Arial',      // Font family
    align: 'right',         // Text alignment (RTL)
    valign: 'middle',       // Vertical alignment
    margin: 0.1,            // Cell margins in inches
    rowH: 0.42,             // Row height in inches
    colW: [6, 3],          // Column widths in inches
    border: { pt: 2, color: '...' },
    fill: { color: '...' }
});
```

## Verification

All formatting has been verified against the `sea-world.pptx` template:
- ✅ Font sizes match
- ✅ Colors match exactly
- ✅ Table dimensions match
- ✅ Row heights match
- ✅ Cell margins match
- ✅ RTL text direction properly set
- ✅ All text alignment correct

## Testing

To test the updated PowerPoint generation:
1. Open `index.html` or `index13.html` in a browser
2. Create or load sample reports
3. Click the PowerPoint export button
4. Verify the generated PPTX file has:
   - Proper RTL text direction
   - Correct formatting and layout
   - Colors matching the template
   - Professional appearance

## Files Affected
- `index.html` - Shelter inspection reports
- `index13.html` - Group inspection reports
- `sea-world.pptx` - Reference template (unchanged)
- `POWERPOINT_FORMATTING_UPDATE.md` - This documentation

## Compatibility
- PptxGenJS version: 3.12.0
- Browser support: All modern browsers
- No breaking changes to existing functionality
