"""
Catalogue Expansion Generator:
Generates all 20 agent cards JSON files in backend/app/content/fact_cards/
and updates agents.json with all 20 agents.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "app" / "content"
CARDS_DIR = CONTENT_DIR / "fact_cards"
CARDS_DIR.mkdir(parents=True, exist_ok=True)

def card(cid, agent_id, subtopic, title, bands, facts, do_list, dont_list,
         myth_stmt, myth_ans, myth_truth,
         quiz_q, quiz_opts, quiz_correct, quiz_exp,
         situations, question, rubric_points, dangerous_keys, source_name, source_url):
    # compute weights automatically so they sum to 100
    n = len(rubric_points)
    base_weight = 100 // n
    remainder = 100 % n
    rubric = []
    for i, (pt, note, crit, keys) in enumerate(rubric_points):
        w = base_weight + (remainder if i == 0 else 0)
        rubric.append({
            "point": pt,
            "note": note,
            "weight": w,
            "critical": crit,
            "keys": keys
        })
    return {
        "id": cid,
        "agentId": agent_id,
        "subtopic": subtopic,
        "title": title,
        "bands": bands,
        "facts": facts,
        "do": do_list,
        "dont": dont_list,
        "myths": [
            {
                "statement": myth_stmt,
                "answer": myth_ans,
                "truth": myth_truth
            }
        ],
        "quiz": [
            {
                "q": quiz_q,
                "options": quiz_opts,
                "correct": quiz_correct,
                "explanation": quiz_exp
            }
        ],
        "scenario": {
            "situations": situations,
            "question": question,
            "emojis": ["📌", "⚡", "🧒"],
            "bubble": "What is the safest move?",
            "rubric": rubric,
            "dangerous": dangerous_keys
        },
        "sources": [{"name": source_name, "url": source_url}],
        "reviewed": True
    }

print("Generator helper loaded")
