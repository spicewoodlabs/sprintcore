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
pip install -e .
```

---

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

- [x] PRD to Stories CLI
- [x] Parse messy, unstructured PRDs (Google Docs, Notion, Markdown)
- [x] Generate clean stories with subtasks, labels, estimates
- [x] Story clustering by similarity
- [x] Duplicate story detection
- [x] Create Jira story using natural language prompt
- [x] Create Jira subtasks using natural language prompt
- [x] Upload stories in bulk
- [ ] Linear integration
- [ ] Slack integration
- [ ] Sprint planning agent
- [ ] Automated story updates based on git commits and PRs
- [ ] Automated story updates based on standup notes
- [ ] Automated story updates based on standup voice recordings
- [ ] Get info from Jira/Linear using natural language
- [ ] Create Jira Boards, Jira Sprints using natural language
- [x] Capture standup notes (Slack, meetings) and update the right stories
- [x] Auto-generate standup summaries based on team activity
- [x] Maintain sprint health without manual intervention
- [x] Flags stories that are missing key requirements and UI mocks
- [x] Clarifies requirements from PM
---

## 📝 License

MIT © Spicewood Labs LLC.
