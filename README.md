<<<<<<< HEAD
# 🤖 Adikhi AI — Business Intelligence Chatbot

Built with Python · Powered by Claude (Anthropic)

---

## 📁 Project Files

```
adikhi_ai/
├── chatbot.py          ← AI core (Claude API + memory)
├── app.py              ← Flask web server
├── terminal.py         ← Terminal-only version
├── requirements.txt    ← Python packages
├── .env.example        ← Copy to .env + add API key
└── templates/
    └── index.html      ← Web chat UI
```

---

## ⚡ Setup (3 Steps)

```bash
# Step 1: Install packages
pip install -r requirements.txt

# Step 2: Add your API key
cp .env.example .env
# Edit .env → paste your key from console.anthropic.com

# Step 3: Run
python app.py       ← Web UI at http://localhost:5000
python terminal.py  ← Terminal mode
```

---

## 💡 What Adikhi AI Can Do

| Domain              | Examples                                      |
|---------------------|-----------------------------------------------|
| 💼 Sales            | Conversion rate, cold outreach, closing deals  |
| 🛒 E-Commerce       | Product listings, Shopify tips, fulfillment    |
| 📣 Marketing        | SEO, email campaigns, social media strategy    |
| 💰 Finance          | Cash flow, fundraising, unit economics         |
| 👥 HR               | Hiring, onboarding, team management            |
| 🚀 Startups         | MVP, go-to-market, product-market fit          |
| 🤝 Customer Success | Churn reduction, NPS, loyalty programs         |
| ⚙️  Operations      | Workflow, SOPs, vendor management              |

---

## 🖥 Terminal Commands

```
/reset    Start fresh conversation
/save     Save chat to .txt + .json
/stats    View session stats
/topics   Show all business topics
/clear    Clear screen
/help     Show help menu
/quit     Exit
```

---

## 🌐 Web API

| Method | Endpoint    | Action              |
|--------|-------------|---------------------|
| POST   | /api/chat   | Send message        |
| POST   | /api/reset  | Reset conversation  |
| POST   | /api/save   | Save chat to files  |
| GET    | /api/stats  | Session statistics  |

---

## 🚀 Deploy

**Railway:** `railway login && railway up`  
**Render:** Connect GitHub → Python → `python app.py`  
**Heroku:** Add `Procfile` with `web: python app.py`
=======
# adikhi-ai
>>>>>>> e3830280c0233c5f6d2961637d866804cbd98462
