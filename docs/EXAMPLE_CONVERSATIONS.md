# 💬 Example Conversations with VickyBot

This guide shows what kinds of conversations the chatbot handles and how it responds. Use these as reference for testing!

---

## 🎯 Greeting & Introduction

**User:** "Hello! Who are you?"

**VickyBot:** 👋 Hey! I'm VickyBot, an AI agent representing Vicky Kumar. I have his complete profile — work experience, technical skills, projects, competitive programming achievements, and contact info.

You can ask me about:
• His current role and work experience
• Technical skills and tech stack
• Personal projects and GitHub repos
• Competitive programming achievements
• Education and background
• How to contact Vicky

What would you like to know?

---

## 💼 Company-Specific Questions

**User:** "Tell me about Eka.Care"

**VickyBot:** 🏥 Backend Developer at Eka.Care (Nov 2024 – Present) in Bangalore.

I've been architecting and implementing a centralized OAuth2 + OpenID Connect authentication platform that powers Eka.Care's EMR, PHR, Scribe, and partner-facing products. Also built the entire Scribe platform backend for doctor dictation and patient consultations.

Tech Stack: Go, Python, Django, AWS

Key Achievements:
• Built full OAuth2/OIDC provider supporting Login with Google, Apple, and other identity providers
• Designed an Auth Console for managing OAuth clients, API keys, scopes, and access policies
• Created AWS Lambda Authorizers integrated with API Gateway for secure request authentication
• Implemented CloudFront Functions for dynamic redirects and login flows
• Architected an event-driven voice-to-text pipeline using AWS SNS, SQS, S3, Lambda
• Optimized end-to-end audio processing latency from 20 seconds to 5-10 seconds per consultation
• Contributed to 40%+ month-over-month growth in daily Scribe consultations
• Led integrations with major healthcare clients like Medanta, Cliniik, and NIC (Government of India)

---

**User:** "What did you do at Deeptek.AI?"

**VickyBot:** 🏗️ Software Engineer at Deeptek.AI (Nov 2022 – Nov 2024) in Pune, Maharashtra

Worked on medical imaging and radiology reporting systems for 1000+ hospitals across India and APAC.

Tech Stack: Java, Spring Boot, MySQL

Key Achievements:
• Architected GCP data migration strategy reducing cloud infrastructure costs by 65%
• Integrated open-source medical imaging viewer saving $300K+ annually in licensing fees
• Led monolith to microservices migration improving system performance by 40%
• Built radiology reporting system with LLM integration reducing radiologist reporting time by 50%
• Developed 50+ REST APIs supporting radiology workflows
• Optimized bulk DICOM processing enabling throughput of 10K+ images per minute
• Implemented async data export handling 100K+ medical records with 60% faster DB queries
• Deployed voice dictation system across 100+ hospitals in India and APAC region

---

## 🛠️ Technical Skills Questions

**User:** "What's your tech stack?"

**VickyBot:** I'm a polyglot backend engineer with expertise across multiple domains:

**Languages:** Go, Python, Java, C++, JavaScript
**Frameworks:** Spring Boot, Django, Go-Gin, React
**Databases:** MySQL, MongoDB, DynamoDB, BigQuery, Elasticsearch
**Cloud & DevOps:** AWS (EC2, S3, Lambda, API Gateway, CloudFront, SNS, SQS), GCP, Docker, CI/CD, Git
**Specialized Tools:** REST APIs, Microservices, OAuth 2.0, OpenID Connect, MCP, NewRelic, Redash

**Real Examples of Tech Usage:**
• Go + Gin + AWS at Eka.Care for building authentication platforms
• Java + Spring Boot + MySQL at Deeptek for medical imaging APIs
• Python + Django at Celebal for data pipelines with PySpark
• React for frontend work in personal projects

---

**User:** "Do you know Kubernetes?"

**VickyBot:** Kubernetes isn't explicitly in my resume, but I work with Docker extensively and have strong microservices and cloud infrastructure experience. At Deeptek, I led a monolith-to-microservices migration improving performance by 40%, which involved containerization and orchestration patterns.

If Kubernetes-specific experience matters for your role, I'm definitely capable of picking it up quickly given my Cloud/DevOps background! 🚀

---

## 🚀 Projects

**User:** "Show me your projects"

**VickyBot:** 💻 I've built three main projects:

┌─ Medical AI Health Assessment (2025)
├─ Tech: Claude AI API, Python, Django, React, JavaScript
├─ GitHub: https://github.com/vickykumar
└─ Built a web application integrating Claude AI for dynamic health assessment questionnaires. Generates personalized medical insights and automated medical summaries with diagnosis, medications, and recommendations. Designed to optimize OPD efficiency and improve patient-doctor interaction workflows.

┌─ Generic Webhook Dispatch System (2025)
├─ Tech: GoLang, AWS SQS, SNS, Lambda, REST APIs
├─ GitHub: https://github.com/vickykumar
└─ Designed and implemented a generic webhook backend microservice in Go supporting event delivery across multiple protocols. Enables clients to register webhooks for HTTP/HTTPS, AWS SQS, SNS, and Lambda invocations. Built with async dispatch architecture using Go routines for high reliability and scalability.

┌─ Student Monitoring System with Facial Recognition (2022)
├─ Tech: MySQL, Python, Django, JavaScript, OpenCV
├─ GitHub: https://github.com/vickykumar
└─ Multi-role system with class management, assignment distribution, and automated attendance tracking using facial recognition. Includes manual override capability, scheduled email notifications, and comprehensive student management with enrollment tracking and progress reporting.

---

**User:** "Tell me more about the Webhook Dispatch System"

**VickyBot:** 🔄 Great question! This project showcases my expertise in building scalable, event-driven backend systems.

**What It Does:**
A generic webhook microservice that lets clients register and trigger webhooks to multiple endpoints. Instead of directly calling endpoints, the service queues events and processes them asynchronously for reliability.

**Architecture Highlights:**
• **Async Dispatch**: Built with Go routines and channels for concurrent processing
• **Multiple Protocols**: Supports HTTP/HTTPS, AWS SQS, SNS, and Lambda invocations
• **Secure APIs**: Client credentials (client ID + secret) for webhook triggering
• **Decoupled**: Separates request ingestion from delivery execution
• **Scalable**: Worker-based consumers process events in parallel

**Why It Matters:**
Demonstrates understanding of:
✓ Event-driven architecture
✓ Asynchronous processing
✓ Go concurrency patterns
✓ AWS services integration
✓ System reliability and scalability

Perfect for roles involving microservices, real-time data pipelines, or event streaming! 📊

---

## 🏆 Competitive Programming

**User:** "What are your competitive programming achievements?"

**VickyBot:** 🏆 I'm an active competitive programmer across multiple platforms:

**LeetCode:** 1850+ rating with 1500+ problems solved
**CodeChef:** 4-star rating (1800+) with 600+ problems solved
**HackerRank:** 5-star rating with 400+ problems solved

**Notable Achievements:**
• Rank 64 out of 1078 in HackerRank Celebrate Pride 2021
• Rank 44 out of 31K in CodeChef March Challenge 2021
• Consistently ranked in top 300 competitive programmers

These achievements reflect my strong foundation in **data structures, algorithms, system design, and problem-solving** — all critical for backend engineering!

---

## 📚 Education

**User:** "What's your educational background?"

**VickyBot:** 🎓 Bachelor of Science in Computer Science
Government Engineering College Ajmer (2018 – 2022)
GPA: 8.79/10

Higher Secondary Certificate
Bihar Board of Education (2016 – 2018)
Percentage: 74%

---

## 📬 Contact Information

**User:** "How can I contact Vicky?"

**VickyBot:** 📞 Here are all the ways to reach me:

**Email:** vickykr26941@gmail.com
**Phone:** +91-8709459003
**LinkedIn:** https://linkedin.com/in/vickykumar
**GitHub:** https://github.com/vickykumar

Feel free to reach out on any of these channels! Always happy to chat about backend engineering, system design, or AI/LLM projects. 🚀

---

## 🔗 GitHub Integration

**User:** "What are your latest GitHub repositories?"

**VickyBot:** 📊 Here's my GitHub activity:

**Profile Stats:**
Public Repos: 25+ | Followers: 120+ | Bio: Backend Engineer | Go, Python, Java

**Top Repositories:**
• portfolio-agent [Python] ⭐ 45 — AI-powered portfolio chatbot with Groq LLaMA (https://github.com/vickykumar/portfolio-agent)
• webhook-dispatch [Go] ⭐ 32 — Generic webhook backend microservice (https://github.com/vickykumar/webhook-dispatch)
• medical-ai-health [Python] ⭐ 28 — Health assessment with Claude AI (https://github.com/vickykumar/medical-ai-health)
• radiology-apis [Java] ⭐ 18 — REST APIs for medical imaging (https://github.com/vickykumar/radiology-apis)

[And more on my GitHub profile!]

---

## ❓ Off-Topic Questions

**User:** "What's your favorite movie?"

**VickyBot:** 😄 I'm here to help you learn about Vicky's portfolio! I don't have personal preferences, but I can definitely tell you about:

• His work experience and achievements
• Technical skills and projects
• Competitive programming stats
• Education and background
• How to contact him

What would you like to know? 🚀

---

## 🎓 How to Use These Examples

1. **Copy questions verbatim** to test the bot
2. **Paraphrase** to see how well it generalizes (e.g., "What did you build at Eka.Care?" instead of company name)
3. **Ask follow-ups** to test conversation context
4. **Try edge cases** like typos or vague questions

The bot should handle variations gracefully! If responses are off, check:
- ✓ `data/portfolio_data.json` has correct information
- ✓ GROQ_API_KEY is valid
- ✓ System prompt in `agent.py` is up-to-date

---

## 🎯 Pro Tips for Better Responses

1. **Be Specific:** "Tell me about Eka.Care" → Better than "Current job?"
2. **Ask for Details:** "Tell me more about..." → Triggers deeper explanations
3. **Ask for Comparisons:** "How did Deeptek differ from Eka.Care?" → Cross-company context
4. **Ask for Examples:** "Give me an example of using Go" → Real-world usage
5. **Use Natural Language:** The bot understands conversational queries, not just keyword matching

---

**Enjoy your conversations with VickyBot! 🤖💬**
