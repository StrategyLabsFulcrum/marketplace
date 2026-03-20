# Create Rule

Step-by-step guided rule creation for message handling. Can be triggered standalone or from within a triage session when the user says "rule" or "create rule" on a specific message.

## Entry Points

### From Triage (contextual)
When the user selects `rule` on a specific message during triage, pre-populate the rule builder with that message's sender, subject, and patterns.

> "Let's create a rule based on this email from [Sender]. I'll walk you through it."

### Standalone
When the user runs `/create-rule` directly:

> "Let's create a new message rule. I'll walk you through each step."

---

## Step 1: What Triggers This Rule?

> "What should trigger this rule? Pick one or combine multiple:"

### Sender-Based
> - **Specific sender:** "Messages from [email address / phone number]"
> - **Domain:** "Emails from anyone @[domain.com]"
> - **Sender type:** "Emails from mailing lists / newsletters / no-reply addresses"
> - **Platform:** "Only from [Email / Slack / iMessage / All]"
> - **New senders:** "First-time senders not in my contacts"

If from triage context, pre-fill:
> "Trigger: Emails from [sender's email]. Want to broaden to all emails from @[domain]?"

### Content-Based
> - **Subject contains:** [keywords or phrases]
> - **Body contains:** [keywords or phrases]
> - **Has attachments:** Yes / No / Specific types (.pdf, .xlsx, etc.)
> - **Thread length:** More than [X] messages

### Timing-Based
> - **Received during:** [time window] (e.g., 8 PM - 7 AM for quiet hours)
> - **Day of week:** [specific days]
> - **Recurring:** "Every email from this sender" vs. "Just this week"

### Behavior-Based
> - **I've junked this sender [X]+ times:** Auto-junk after threshold
> - **No reply from me after [X] days:** Follow-up reminder
> - **I sent an email and got no reply in [X] days:** Stale follow-up

### Combine Triggers
> "Want to combine triggers? For example: 'Emails from @linkedin.com that contain notification in the subject'"
>
> Current trigger(s):
> 1. [trigger 1]
> 2. [add another?]

---

## Step 2: What Should Happen?

> "When this rule triggers, what should I do? Pick one or chain multiple actions:"

### Categorization
> - **Categorize as:** 🔴 RESPOND / 🟡 FYI / 🗑️ JUNK / 🔕 UNSUBSCRIBE
> - **Escalate to HIGH:** Always treat as urgent

### Organization
> - **Label as:** [label name] (create new or use existing)
> - **Mark as:** Read / Starred / Important
> - **Archive:** Move out of inbox, keep in All Mail
> - **Delete:** Move to trash

### Routing
> - **Forward to:** [email address] — with or without a note
> - **Delegate to:** [person's name] — draft a forwarding email for approval
> - **Auto-draft reply using:** [template or instructions]

### Task Management
> - **Create a task:** With priority [HIGH / MED / LOW]
> - **Create a reminder in:** [time period]
> - **Add to follow-up queue:** Check back in [X] days

### Visibility
> - **Snooze until:** [time / day] — hide until then, resurface in triage
> - **Bundle into digest:** Group with similar messages, show as one item in weekly digest
> - **Skip triage:** Process silently, never show in batches

### Chain Actions
> "Want to chain multiple actions? For example: 'Label as Finance AND forward to bookkeeper AND mark read'"
>
> Current action(s):
> 1. [action 1]
> 2. [add another?]

---

## Step 3: Any Exceptions?

> "Should this rule have exceptions — situations where it should NOT apply?"

### Common Exceptions
> - **VIP override:** "Don't apply if sender is on my VIP list"
> - **Keyword override:** "Don't apply if subject contains [keywords]" (e.g., "urgent", "action required")
> - **Thread override:** "Don't apply if I'm already in the conversation"
> - **Attachment override:** "Don't apply if there's an attachment"
> - **Time override:** "Only apply during [time window]"
> - **No exceptions:** "Apply this rule every time, no exceptions"

---

## Step 4: Review & Name the Rule

Present the complete rule for review:

```
📋 NEW RULE — Ready for Review

NAME: [Auto-suggested based on trigger + action]
(e.g., "Auto-junk LinkedIn notifications", "Forward invoices to bookkeeper")

TRIGGER:
├── Sender: @linkedin.com
└── Subject contains: "notification"

ACTION:
├── Categorize as: 🗑️ JUNK
└── Delete automatically

EXCEPTIONS:
└── Don't apply if sender is on VIP list

STATUS: Active (will start applying immediately)
```

> "Does this look right?"
> - **Activate** — Save and start applying immediately
> - **Edit** — Go back and change a step
> - **Test first** — Run against your last 30 days of email to see what it would have caught
> - **Save as draft** — Save but don't activate yet

---

## Step 5: Test Run (optional)

If the user wants to test before activating:

> "Testing rule against your last 30 days of email..."
>
> "This rule would have matched **23 messages:**
> - 18 LinkedIn notification emails
> - 3 LinkedIn InMail notifications
> - 2 LinkedIn job alert emails
>
> **False positives (0):** No messages that shouldn't have been caught.
>
> Looks clean. Activate? [Yes / Edit / Cancel]"

If false positives are found:
> "**Possible false positive:** This rule would have caught an email from [Name] at LinkedIn
> (a real recruiter message, not a notification). Want to add an exception?"

---

## Step 6: Save & Confirm

After activation:

1. Append the rule to `inbox-command-center/rules.md`
2. Confirm:
   > "✅ Rule created: **[Rule Name]**
   > Active immediately. I'll apply it to all future triages.
   >
   > You can edit or pause this rule anytime — say 'show my rules' or 'edit [rule name]'."

---

## Rule Management Commands

At any time, the user can manage existing rules:

### View Rules
> "Show my rules" / "What rules do I have?"

Present all active rules:
```
📋 ACTIVE RULES ([X] total)

1. Auto-junk LinkedIn notifications
   Trigger: @linkedin.com + "notification"
   Action: 🗑️ JUNK → Delete
   Triggered: 47 times | Last: today
   [Edit] [Pause] [Delete]

2. Forward invoices to Stephen
   Trigger: Subject contains "invoice" or "receipt"
   Action: Forward to stephen@grifco.com + Label "Finance"
   Triggered: 12 times | Last: 3 days ago
   [Edit] [Pause] [Delete]

3. VIP Priority
   Trigger: Sender on VIP list
   Action: Always 🔴 RESPOND
   Triggered: 89 times | Last: today
   [Edit] [Pause] [Delete]

[+ Create New Rule]
```

### Edit a Rule
> "Edit the LinkedIn rule" / "Change the invoice forwarding rule"

Re-open the rule builder with current values pre-filled. Walk through each step, showing current value and asking if they want to change.

### Pause/Resume
> "Pause the quiet hours rule" / "Resume the LinkedIn rule"

Toggle the rule's status between Active and Paused. Paused rules are skipped during triage.

### Delete
> "Delete the [rule name] rule"

Confirm before deleting:
> "Delete **Auto-junk LinkedIn notifications**? This has triggered 47 times. [Confirm / Cancel]"

### View Suggestions
> "Show rule suggestions" / "Any new rule ideas?"

Present pending learned suggestions from `inbox-command-center/rule-suggestions.md`:
> "Based on your recent triages, here are some rules I'd suggest:
> 1. [suggestion] — [Enable / Dismiss]
> 2. [suggestion] — [Enable / Dismiss]"
