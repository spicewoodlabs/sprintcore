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
sprintcore prd2story --input path/to/prd.md --output sprint.yaml
```

### With Mock Mode

```bash
sprintcore prd2story --input path/to/prd.md --output mock.json --mock
```

---

## 🔐 Environment Setup

Create a `.env` file in the repo root:

```env
OPENAI_API_KEY=sk-...
JIRA_URL=https://yourcompany.atlassian.net
JIRA_USER=you@example.com
JIRA_TOKEN=your_token
JIRA_PROJECT=ENG
```

---

## 🧪 Run Tests

```bash
pytest sprintcore/tests
```

---

## 📌 Roadmap

- [x] PRD to Stories CLI
- [ ] Story clustering by similarity
- [ ] Duplicate story detection
- [ ] Linear integration
- [ ] Sprint planning agent

---

## 📝 License

MIT © [Your Name]
