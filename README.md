# 🚀 SprintCore

**SprintCore** is an AI-powered CLI tool that does a lot of things 

1. Converts Product Requirement Documents (PRDs) into structured agile artifacts — Epics, Stories, and Subtasks — using AI.

2. Suggest bug fixes based on your code using AI

Built for Engineers, Product Managers, and Team Leads to speed up Sprint Planning.

---

## 🛠 PRD -> Story 
- 🧠 PRD → Epic/Story/Subtask generation via AI
- 📤 Export to `.json`, `.yaml`, or `.md`
- 🧪 Supports mock mode for local dev/testing
- 🔌 Ready for Jira integration (Linear support coming soon)
- ✨ Designed for extension (clustering, deduplication, planning, etc.)

## 🛠 Bug Report -> Code 
- 📤 Just describe your bug and AI will suggest the fix in seconds
- 🧠 Index code base locally
- 📤 Uses local vector DB
- 🔌 Ready for Jira/Linear (Paid feature)

---

## 💼 Paid Version (Coming Soon)
- 🧭 Unstructured Slack Messages -> Structured Tasks in Jira/Linear
- 📊 Unstructured Notes -> Structured Tasks in Jira/Linear
- 🔁 Standup notes -> Story updates
- 🔁 Git commit  -> Story point updates
- 🧭 Full web dashboard with team access
- 🔁 Story deduplication + clustering
- 📊 Sprint velocity tracking
- 🔗 Deep integrations with Jira, Linear, GitHub
- ✅ Priority support and model configuration
- 🔁 Bugfix Jira/Linear integration

👉 [Join the waitlist](https://sprintcore.ai)

---

## 📦 Installation

`$ git clone https://github.com/spicewoodlabs/sprintcore.git`

`$ cd sprintcore`

`$ cp .env.example .env`

`$ pip install --no-cache-dir --upgrade --force-reinstall sprintcore`



---

## 📦 Add OPENAI_API_KEY

Add `OPENAI_API_KEY=sk_...` in `.env`

--
## 📦 Add ANTHROPIC_API_KEY (for bug-fix agent)

Add `ANTHROPIC_API_KEY=sk_...` in `.env`

--

## 🚀 Usage:: PRD -> Story 

`$ sprintcore create-story  --input sprintcore/examples/prd/prd-flight-booking.md --output stories.yaml --prompt prompt.txt`

---
## 🚀 Usage:: Bug Report -> Bug fix

### Step 1: Index your codebase/git repo. 
This is a one time step unless you add moee code. Run the following command from the root directory to index your repo. Pass the source code repo in the `--source` parameter. Make sure to not index `node_modules` or other directories. Provide the full path and not the relative path

#### NextJS

`$ sprintcore index-code --lang nextjs --source-code /Users/myuser/code-examples/tsx/ [--index INDEX]`

#### Javascript

`$ sprintcore index-code --lang js --source-code /Users/myuser/code-examples/tsx/ [--index INDEX]`

## Step 2: Query the index (Optional)
Query the index to find top k matching documents 


`$ sprintcore bug-fix --bug_description "post title is not appearing on the page" --mode query`


### Step 3: Get code fix recommendations from AI


`$ sprintcore bug-fix  --bug_description "post title is not appearing on the page" --mode fix_code`

---

## 📌 Roadmap

- [x] PRD to Stories CLI - Open Source - Free
- [x] Parse messy, unstructured PRDs (Google Docs, Notion, Markdown) - Open Source - Free
- [x] Generate clean stories with subtasks, labels, estimates - Open Source - Free with limitations
- [x] Slick UI - Paid
- [x] Jira/Linear Copilot - Paid
- [x] Story clustering by similarity - Paid
- [x] Duplicate story detection  - Paid
- [x] Create Jira story using natural language prompt - Paid
- [x] Create Jira subtasks using natural language prompt - Paid
- [x] Upload stories in bulk - Paid
- [x] Jira integration - Paid
- [ ] Linear integration - Paid
- [ ] Slack integration - Paid
- [ ] Sprint planning agent - Paid
- [ ] Automated story updates based on git commits and PRs - Paid
- [ ] Automated story updates based on standup notes - Paid
- [ ] Automated story updates based on standup voice recordings - Paid
- [ ] Get info from Jira/Linear using natural language - Paid
- [ ] Create Jira Boards, Jira Sprints using natural language - Paid
- [ ] Capture standup notes (Slack, meetings) and update the right stories - Paid
- [ ] Auto-generate standup summaries based on team activity - Paid
- [ ] Maintain sprint health without manual intervention - Paid
- [ ] Flags stories that are missing key requirements and UI mocks - Paid
- [ ] Clarifies requirements from PM - Paid

---

## 📝 License

MIT © Spicewood Labs LLC.
