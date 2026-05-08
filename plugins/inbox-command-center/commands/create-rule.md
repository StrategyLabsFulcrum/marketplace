# Create Rule

Step-by-step guided rule creation for message handling. Can be triggered standalone or from within a triage session when the user says "rule" or "create rule" on a specific message.

In v1.4, every rule has three dimensions: **type** (delete / prioritize / folder / organize), **stakes** (low_stakes / high_stakes), and **scope** (per-inbox or global). The wizard collects all three plus the trigger and action.

## Entry Points

### From Triage (contextual)

When user types `rule` on a message during triage, prefill the rule wizard with context from that message:
- Suggested **trigger**: sender (most common) or subject pattern
- Suggested **type**: based on message category (delete/prioritize/folder/organize)
- Suggested **stakes**: per default-by-action table (see SKILL.md Rules Engine)
- Suggested **scope**: current inbox alias

Show prefilled values and ask user to confirm or override each.

### Standalone

User says: "create a rule" / "make a rule" / "I want to set up a rule"

Walk through Steps 1-6 from a blank slate.

## Step 1: What Triggers This Rule?

Ask what should match. Multiple trigger types can combine.

### Sender-Based

```
[ ] Specific email address (e.g., bryan@dieselpowerproducts.com)
[ ] Domain (e.g., @strategylabs.us)
[ ] Sender pattern (e.g., contains "noreply")
[ ] Multiple senders (comma-separated list)
```

### Content-Based

```
[ ] Subject contains: [keywords]
[ ] Subject matches pattern: [regex]
[ ] Body contains: [keywords]
[ ] Has attachment / specific attachment type
```

### Timing-Based

```
[ ] Received during quiet hours (e.g., 9pm-7am)
[ ] Older than [N] days unread
[ ] No reply after [N] days (for sent emails)
```

### Behavior-Based

```
[ ] Sender flagged as junk [N]+ times
[ ] User has trashed similar emails [N]+ times
[ ] User has replied to this sender within [time]
[ ] First-time sender (not in contacts.md)
```

### Combine triggers

```
Combine multiple triggers?

  [ ] Match ALL conditions (AND)
  [ ] Match ANY condition (OR)
  [ ] Single condition only (default)
```

## Step 2: What Should Happen?

Choose the action. Each action implies a default `Type` and `Stakes` (shown inline). User can override stakes if they want.

### Delete actions

```
[ ] Move to trash (recoverable)              → Type: delete | Stakes: low (default)
[ ] Permanent delete                         → Type: delete | Stakes: high (default — irreversible)
[ ] Auto-junk + create unsubscribe attempt   → Type: delete | Stakes: low (default)
```

### Prioritization actions

```
[ ] Categorize as: 🔴 RESPOND / 🟡 FYI / 🗑️ JUNK / 🔕 UNSUBSCRIBE
[ ] Mark as: read / starred
[ ] Escalate to 🔴 HIGH priority
[ ] Mark sender as VIP (adds [VIP] tag in contacts.md)
                                              → Type: prioritize | Stakes: low (default)
```

### Organization actions

```
[ ] Add label / category: [name]              → Type: organize | Stakes: low (default)
[ ] Auto-archive (remove from INBOX)          → Type: organize | Stakes: low (default)
[ ] Bundle into digest: [digest name]         → Type: organize | Stakes: low (default)
```

### Folder routing

```
Move to folder:
[ ] Low Priority
[ ] Newsletters
[ ] Receipts & Orders
[ ] Finance
[ ] Automated/Bot
[ ] Pending Review
[ ] Delegated
[ ] Custom folder: [name]                     → Type: folder | Stakes: low (default)
```

The skill creates the underlying Gmail label or Outlook subfolder automatically (synthetic abstraction — see SKILL.md Folder Rules).

### Reply / forward actions

```
[ ] Auto-draft using template                 → Type: organize | Stakes: low (drafts only)
[ ] Auto-reply with template                  → Type: organize | Stakes: high (default — sends)
[ ] Auto-forward to [email]                   → Type: organize | Stakes: high (default — touches another human)
```

### Task management

```
[ ] Add to todos.md (priority [HIGH/MED/LOW])
[ ] Add sender to followups.md
[ ] Create reminder in [time] via [channel]
                                              → Type: organize | Stakes: low (default)
```

### Snooze

```
[ ] Snooze until [time/condition]             → Type: prioritize | Stakes: low (default)
```

### Chain actions

```
Combine multiple actions on a match?

  [ ] Yes, chain actions
       → User picks 2+ actions; they execute in order
  [ ] Single action only
```

## Step 2b: Stakes (confirm or override)

Based on the chosen action, the wizard suggests a default stakes level. Show user:

```
Suggested stakes: [low_stakes / high_stakes]

  Low stakes  — Auto-applies silently after approval. Logged to session log.
                Examples: archive, label, trash, mark-read, route to folder.

  High stakes — Always confirms with you per-instance, even after rule
                approval. Examples: permanent delete, auto-reply, auto-forward.

  [ ] Use suggested ([X])
  [ ] Override to other ([Y])
```

If user overrides high → low for an inherently risky action (auto-reply, permanent delete), warn:
> "⚠️ This action sends or destroys data. Setting it to low_stakes means it'll execute without per-instance confirmation. Are you sure?"

## Step 2c: Scope

```
Step 2c — Scope

Apply this rule to:

  [ ] All inboxes (global)
       → Useful when the rule is about a person or pattern that
         crosses inboxes (VIP escalation, urgency keywords).
       
  [ ] Just this inbox: [current alias] (per-inbox, recommended default)
       → Useful when the rule reflects a per-account preference
         (e.g., "newsletters in personal go to Newsletters, but in
         uno-mas they're already filtered").

  [ ] Specific inboxes: [pick 2+]
       → Apply to a subset of your inboxes (rare).
```

VIP-related rules (sender-is-VIP triggers) auto-default to global with no override option — they're inherently global per the rules engine.

## Step 3: Any Exceptions?

```
Step 3 — Exceptions

Should this rule NOT apply when:

  [ ] Sender is a VIP (recommended for delete/junk rules)
  [ ] Subject contains override keyword: [e.g., "urgent"]
  [ ] Sender is in your contacts.md
  [ ] Email is part of a thread you've already replied to
  [ ] (No exceptions)
```

Exceptions are checked before the rule's main action runs.

## Step 4: Review and Name the Rule

Show the complete rule preview:

```
Step 4 — Review Rule

Name: [Auto-archive ESPN newsletters]   ← user can edit

  Type:    delete
  Stakes:  low_stakes
  Scope:   per-inbox: personal

  Trigger:
    - Sender: notifications@espn.com

  Action:
    - Move to Trash

  Exceptions:
    - (none)

  Status: Active

Save this rule?
  [ ] Save and activate
  [ ] Save and pause (don't apply yet)
  [ ] Edit something
  [ ] Cancel
```

If user picks "Edit something", show numbered fields they can edit by saying e.g. "edit trigger" or "edit stakes".

## Step 5: Test Run (optional)

```
Step 5 — Test Run (Optional)

Run this rule against the last [N] days of email to see what it
would have caught? Doesn't make any actual changes.

  [ ] Yes, test against last 7 days
  [ ] Yes, test against last 30 days
  [ ] Skip — just save it
```

If yes:
1. Query messages from the test period using rule's trigger
2. Apply scope filter (which inbox(es))
3. Show count and a few sample matches:
   ```
   Test results — last 7 days:
   
   Rule would have matched [N] messages in [inbox(es)]:
     - 2026-05-05 — notifications@espn.com — "Tonight's MLB scores"
     - 2026-05-04 — notifications@espn.com — "Trade deadline rumors"
     - 2026-05-02 — notifications@espn.com — "NBA finals preview"
     ...
   
   Action that would have run: Move to Trash
   
   Looks right? [Save and activate / Edit / Cancel]
   ```

## Step 6: Save and Confirm

On save:

1. Append to `~/Inbox Command Center/rules.md` with full rule structure (Type, Stakes, Scope, Status, Trigger, Action, Exceptions, Created date, Last triggered = null, Times triggered = 0)

2. If folder routing rule with new folder: create the underlying Gmail label or Outlook subfolder. Update `.meta.json.connected_inboxes[i].folders_enabled[]`.

3. Log to session log:
   ```
   **HH:MM** — Rule created: [Name] (type=[X], stakes=[Y], scope=[Z])
   ```

4. Confirm:
   ```
   ✓ Rule saved: [Name]
   
   It will apply on your next triage. To pause/edit/delete anytime,
   open ~/Inbox Command Center/rules.md or say "show my rules".
   ```

5. If from triage context: return to the next message in the batch.

---

## Rule Management Commands

### View Rules

User says: "show my rules" / "list rules" / "what rules do I have"

Read `rules.md`. Group by scope:

```
RULES — [N] active, [M] paused

GLOBAL ([X])
─────────
  • [Name] — Type: [X] | Stakes: [Y] | Triggered [Z] times
  • ...

PER-INBOX: personal ([X])
────────────────────────
  • [Name] — Type: [X] | Stakes: [Y] | Triggered [Z] times
  • ...

PER-INBOX: uno-mas ([X])
───────────────────────
  • ...

PAUSED ([M])
──────────
  • [Name] — paused [date]

[Edit a rule] [Delete a rule] [View pending suggestions]
```

### Edit a Rule

User says: "edit rule [name]" or picks from the list.

Walk through the same steps as creation, prefilled with current values. User can change any field (Type, Stakes, Scope, Trigger, Action, Exceptions, Status, Name).

### Pause / Resume

```
"pause rule [name]"   →  Set Status: Paused. Rule stops applying.
"resume rule [name]"  →  Set Status: Active.
```

### Delete

```
"delete rule [name]" → Confirm: "Delete '[name]' permanently? [Yes / No]"
On confirm: remove from rules.md. Log: "Rule deleted: [name]".
```

If the rule was tied to a folder (Type: folder), ask whether to also remove the folder from the inbox or keep it for manual use.

### View Suggestions

User says: "show rule suggestions" / "what rules do you suggest" / "review pending rules"

Read `rules-review-queue.md`. Walk user through each (one at a time):

```
Pending rule [1 of N]:

  Type:    [X]
  Stakes:  [Y]
  Scope:   [Z]
  
  Trigger: [description]
  Action:  [description]
  
  Why I'm suggesting this: [pattern reasoning]

  [Approve] [Modify and approve] [Reject] [Skip for now]
```

For each:
- **Approve** → save to `rules.md`, remove from queue, log to session log
- **Modify** → enter edit flow with prefilled values
- **Reject** → remove from queue, log "Rejected: [reason]"
- **Skip** → leave in queue for next review

After last suggestion: update `.meta.json.last_rule_review = today`.

---

## Notes for the skill

- **Default stakes by action type** — see SKILL.md Rules Engine. Always show the suggested default before asking user to confirm/override.
- **Default scope is per-inbox** — global is a deliberate choice. VIP-related rules are the only inherent globals.
- **Auto-create folders silently** — when a folder rule references a folder not yet enabled in the target inbox, just create it
- **Show diff on rule edits** — if user edits an existing rule, show before/after on the changed fields
- **Append, don't rewrite** — when saving a new rule, append to rules.md without disturbing existing rules' formatting
- **Log every rule action** — created, edited, paused, resumed, deleted — all to session log
