# Security and Safety Policy

## Responsible AI & Content Grounding
wotnow is an AI-powered social learning network built for students. Because safety topics are consequential, our platform enforces strict architectural safeguards:
- **100% Fact-Grounded:** All educational scenarios, challenges, and facts are checked against reviewed fact cards (derived from NDMA, St John Ambulance, Tele-MANAS, POCSO, and statutory public safety frameworks).
- **Two-Agent Safety Pipeline:** Educational content is drafted by specialized domain agents and must pass a second, strict `safety_reviewer` agent before being published. Unverified or ambiguous drafts are automatically rejected.
- **Guardrail Plugin:** All student inputs pass through real-time PII scrubbing and prompt-injection defense before reaching language models. Model outputs are scanned to block medication dosages, medical diagnoses, external URLs, and inappropriate themes.
- **Not Medical or Emergency Advice:** wotnow does not provide clinical or emergency services. In a real emergency, users are instructed to call emergency responders (**112** in India or national equivalents).

## Reporting a Vulnerability
If you discover a security vulnerability or safety concern in wotnow:
1. Please email **ajnikareer@gmail.com** with details of the issue.
2. Include steps to reproduce and any relevant context.
3. We take all responsible disclosures seriously and will respond promptly.