# 🚀 SprintCore

**SprintCore** is an AI-powered CLI tool that converts Product Requirement Documents (PRDs) into structured agile artifacts — Epics, Stories, and Subtasks — using AI.

Built for Engineers, Product Managers, and Team Leads to speed up Sprint Planning.

---

## 🛠 Features

- 🧠 PRD → Epic/Story/Subtask generation via AI
- 📤 Export to `.json`, `.yaml`, or `.md`
- 🧪 Supports mock mode for local dev/testing
- 🔌 Ready for Jira integration (Linear support coming soon)
- ✨ Designed for extension (clustering, deduplication, planning, etc.)

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

👉 [Join the waitlist](https://sprintcore.ai)

---

## 📦 Installation

```bash
git clone https://github.com/spicewoodlabs/sprintcore.git
cd sprintcore
pip install .
cp example/.env.example example/.env
```

---

## 📦 Add OPENAI_API_KEY

Add `OPENAI_API_KEY=sk_...` in `.env`

--

## 🚀 Usage

### Basic

```bash
sprintcore create-story  --input sprintcore/examples/prd/prd-flight-booking.md --output stories.yaml --prompt prompt.txt
```

### With Mock Mode

```bash
sprintcore create-story  --input sprintcore/examples/prd/prd-flight-booking.md --output stories.yaml --prompt prompt.txt --mock
```

---

## 🔐 Environment Setup

Create a `.env` file in the repo root:

```env
OPENAI_API_KEY=sk-...
```

---

## 🧪 Run Tests

```bash
pytest sprintcore/tests
```

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
