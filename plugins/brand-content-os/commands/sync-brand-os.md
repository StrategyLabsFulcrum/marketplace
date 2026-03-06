---
description: Sync brand knowledge files between local filesystem and Fast.io workspace
allowed-tools: Read, Write, Edit, Glob, Grep, AskUserQuestion, mcp__72a6dfc4-2caa-4b8c-b086-b5e5ba5e5355__storage, mcp__72a6dfc4-2caa-4b8c-b086-b5e5ba5e5355__upload, mcp__72a6dfc4-2caa-4b8c-b086-b5e5ba5e5355__workspace, mcp__72a6dfc4-2caa-4b8c-b086-b5e5ba5e5355__auth
argument-hint: "<pull|push|status>"
---

# Sync Brand OS — Fast.io File Synchronization

Sync brand knowledge files between the local `brand-os/` directory and a Fast.io workspace. This enables team collaboration — multiple people can read and update the same brand files across different machines and sessions.

## Before Starting

1. **Read configuration**: Look for `.brand-os-config.md` in the working directory (the same directory that contains `brand-os/`).

2. **If no config file found**: Inform the user that sync is not configured. Offer two options:
   - Run `/new-brand-setup` to create brand files and configure storage
   - Create a config file now by asking for the Fast.io workspace ID

3. **If `mode` is `local`**: Inform the user that sync is disabled because storage is set to local-only. Ask if they'd like to switch to Fast.io mode. If yes, ask for the workspace ID and update the config file.

4. **If `mode` is `fast.io`**: Proceed with the sync operation.

## Argument Routing

Check `$ARGUMENTS` for the sync direction:

- If `pull` — go to Pull Workflow
- If `push` — go to Push Workflow
- If `status` — go to Status Workflow
- If empty or unrecognized — ask the user: "Which direction would you like to sync?" with options: Pull (Fast.io → local), Push (local → Fast.io), Status (show sync state)

## Pull Workflow (Fast.io → Local)

Pull brand knowledge files from Fast.io to the local `brand-os/` directory.

1. **Authenticate**: Ensure the Fast.io session is active. If not authenticated, use `auth pkce-login` to initiate browser-based login and guide the user through the approval flow.

2. **List remote files**: Use `storage list` to list files in the Fast.io workspace's `brand-os/` folder (using the `workspace_id` from the config).

3. **Handle missing remote folder**: If the `brand-os/` folder doesn't exist on Fast.io, inform the user: "No brand-os/ folder found in the Fast.io workspace '[workspace_name]'. Would you like to push your local files up instead?" If yes, switch to the Push Workflow.

4. **Fetch each file**: For each of the expected brand files (brand-foundations.md, voice-guidelines.md, content-pillars.md, key-messages.md, platform-config.md, system-prompt.md):
   - Use `storage read-content` to fetch the file content from Fast.io
   - Write the content to the local `brand-os/` directory using the `Write` tool
   - If a file exists on Fast.io but not locally, create it
   - If a file exists locally but not on Fast.io, leave the local file as-is and note it

5. **Create local directory**: If `brand-os/` doesn't exist locally, create it before writing files.

6. **Update timestamp**: Edit `.brand-os-config.md` to update `last_pull` with the current ISO 8601 timestamp.

7. **Report**: "[X] brand files pulled from Fast.io workspace '[workspace_name]'." List which files were updated. Note any files that exist locally but not on Fast.io.

## Push Workflow (Local → Fast.io)

Upload local brand knowledge files to the Fast.io workspace.

1. **Authenticate**: Same as Pull — ensure session is active.

2. **Check local files**: Use `Glob` to find all markdown files in the local `brand-os/` directory. If the directory is empty or doesn't exist, inform the user and suggest running `/new-brand-setup` first.

3. **Upload each file**: For each markdown file in `brand-os/`:
   - Read the local file content using `Read`
   - Upload to the Fast.io workspace's `brand-os/` folder using `upload text-file`
   - If the file already exists on Fast.io, this creates a new version automatically

4. **Handle missing remote folder**: If the `brand-os/` folder doesn't exist on Fast.io yet, create it (the upload tool will handle this, or use `storage create-folder` if needed).

5. **Update timestamp**: Edit `.brand-os-config.md` to update `last_push` with the current ISO 8601 timestamp.

6. **Report**: "[X] brand files pushed to Fast.io workspace '[workspace_name]'." List which files were uploaded.

## Status Workflow

Display the current sync state without changing any files.

1. **Read config**: Display the following from `.brand-os-config.md`:
   - Storage mode (`local` or `fast.io`)
   - Fast.io workspace name and ID (if applicable)
   - Last pull timestamp and how long ago (e.g., "2 hours ago", "3 days ago")
   - Last push timestamp and how long ago
   - `auto_pull_on_start` setting

2. **List local files**: Show all files in the local `brand-os/` directory with their last-modified dates.

3. **Stale sync warning**: If `last_pull` is older than 24 hours or missing, suggest: "Your local files may be out of date. Run `/sync-brand-os pull` to fetch the latest from Fast.io."

## Error Handling

| Scenario | Behavior |
|----------|----------|
| No `.brand-os-config.md` found | Inform user. Offer to create one (ask for workspace ID) or suggest `/new-brand-setup`. |
| `mode` is `local` | Inform user sync is disabled. Offer to switch to `fast.io` mode. |
| Fast.io authentication fails | Trigger `auth pkce-login` flow. Guide user to open the URL in their browser, approve access, and paste back the authorization code. |
| Fast.io workspace not found | Report error with the workspace ID from the config. Suggest checking that the ID is correct in `.brand-os-config.md`. |
| `brand-os/` folder doesn't exist on Fast.io | For pull: offer to push local files up instead. For push: create the folder and upload. |
| `brand-os/` folder doesn't exist locally | For pull: create it and write files. For push: inform user and suggest `/new-brand-setup`. |
| Network failure during sync | Report which files succeeded and which failed. Do NOT update the last_pull/last_push timestamps if any files failed. Suggest retrying. |
