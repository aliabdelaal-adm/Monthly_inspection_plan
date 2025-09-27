# Bell Notifications System Documentation

## Overview
The enhanced bell notifications system allows all inspectors to create, read, update, and delete notifications that are automatically synchronized across all users.

## Features

### ✅ For All Users (No Developer Restrictions)
- **Add Notifications**: Create new notifications with automatic timestamping
- **Edit Notifications**: Click on any notification to edit it inline
- **Delete Notifications**: Remove notifications with confirmation dialog
- **View All Notifications**: See all notifications with metadata (author, timestamp)

### 🔄 Automatic Synchronization
- Changes are saved to `plan-data.json`
- Auto-push script monitors file changes and pushes to Git
- All inspectors receive updates automatically through Git sync

## How to Use

### Adding a Notification
1. Click the bell icon (🔔) in the top-right corner
2. Type your notification in the "إضافة إشعار جديد" text area
3. Click "➕ إضافة إشعار" button
4. Notification is automatically saved and synchronized

### Editing a Notification
1. Open the bell notifications modal
2. Click on any existing notification text
3. Edit the text in the textarea that appears
4. Click "✅ حفظ" to save or "❌ إلغاء" to cancel

### Deleting a Notification
1. Click the "🗑️ حذف" button next to any notification
2. Confirm deletion in the popup dialog
3. Notification is removed and changes are synchronized

## Data Structure

### In `plan-data.json`:
```json
{
  "bellNotes": {
    "infoText": "Header text for notifications",
    "notes": "Legacy text area content",
    "notifications": [
      {
        "id": "unique_id",
        "text": "Notification content",
        "timestamp": "2025-09-27T17:00:00.000Z",
        "author": "Inspector name",
        "lastModified": "2025-09-27T17:30:00.000Z"
      }
    ]
  }
}
```

## Technical Implementation

### Key Functions
- `showBellModal()`: Opens notification modal
- `addNewNotification()`: Creates new notifications
- `editNotification(index)`: Enables editing mode
- `saveNotificationEdit(index)`: Saves changes
- `deleteNotification(index)`: Removes notifications
- `displayNotificationsList()`: Renders notification list

### Auto-Synchronization
The existing `auto_push_on_change.py` script monitors `plan-data.json` for changes:
- Detects file modifications automatically
- Commits changes to Git with auto-generated messages
- Pushes to remote repository for distribution
- All inspectors receive updates through Git pull/sync

## Benefits

1. **Universal Access**: All inspectors can manage notifications
2. **Real-time Updates**: Changes sync automatically across all users
3. **Rich Metadata**: Shows who created/modified each notification and when
4. **Safe Operations**: Confirmation dialogs prevent accidental deletions
5. **Backward Compatible**: Legacy textarea still available
6. **User-Friendly**: Intuitive click-to-edit interface

## Setup Requirements

For auto-synchronization to work:
1. `auto_push_on_change.py` should be running
2. Git repository should be properly configured
3. `watchdog` Python package should be installed: `pip install watchdog`

## Troubleshooting

- **Notifications not syncing**: Check if auto-push script is running
- **Changes not saving**: Verify `plan-data.json` file permissions
- **Modal not opening**: Check for JavaScript errors in browser console