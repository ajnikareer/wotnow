"""Gemini structured-output contracts. Kept simple (no defaults, no dict fields) for SDK schema conversion."""
from __future__ import annotations

from pydantic import BaseModel, Field


class RubricItem(BaseModel):
    point: str = Field(description="One key action the learner should mention, under 12 words")
    note: str = Field(description="Why it matters, one short sentence")
    weight: int = Field(description="Points 5-50; all weights should sum to 100")
    critical: bool = Field(description="True if missing it could cause harm")
    card: str = Field(description="Fact card id this point comes from, e.g. FIRE-012")


class ScenarioDraft(BaseModel):
    title: str = Field(description="3-6 word title")
    body: str = Field(description="The situation, 45-90 words, present tense, no question")
    question: str = Field(description="One question ending with '?', e.g. 'What should Maya do?'")
    scene_emojis: list[str] = Field(description="Exactly 3 emojis illustrating the scene")
    scene_bubble: str = Field(description="A short tempting-but-wrong line someone says, max 6 words")
    rubric: list[RubricItem] = Field(description="3-5 rubric items")
    dangerous_actions: list[str] = Field(description="1-4 harmful things a learner might suggest; may be empty")
    model_answer: str = Field(description="An ideal answer in 2-3 sentences")


class OptionDraft(BaseModel):
    text: str = Field(description="Answer option, under 14 words")


class PollDraft(BaseModel):
    title: str
    body: str = Field(description="Situation in 15-40 words")
    question: str = Field(description="Ends with '?'")
    options: list[OptionDraft] = Field(description="Exactly 4 options")
    correct_index: int = Field(description="0-3, index of the best option")
    explanation: str = Field(description="Why, 1-3 sentences, grounded in the fact cards")


class MythDraft(BaseModel):
    title: str
    statement: str = Field(description="A claim in quotes-style, 8-20 words")
    answer: str = Field(description="'myth' or 'fact'")
    explanation: str = Field(description="1-3 sentences")


class ScamDraft(BaseModel):
    title: str
    sender: str = Field(description="Realistic sender id or masked number, e.g. '+91 98•••• 4417' or 'VM-BNKUPD'")
    text: str = Field(description="The message, 20-45 words")
    answer: str = Field(description="'scam' or 'legit'")
    explanation: str


class QuizQuestionDraft(BaseModel):
    text: str
    options: list[OptionDraft] = Field(description="Exactly 4 options")
    correct_index: int
    explanation: str


class QuizDraft(BaseModel):
    title: str = Field(description="Catchy 2-4 word quiz title")
    questions: list[QuizQuestionDraft] = Field(description="Exactly 5 questions")


class JudgeOut(BaseModel):
    hits: list[str] = Field(description="Ids of rubric items the answer covers (by meaning)")
    dangerous: bool
    dangerous_reason: str = Field(description="Empty string if not dangerous")
    feedback: str = Field(description="2 short sentences: praise what's right, explain the most important miss")


class ModerationOut(BaseModel):
    label: str = Field(description="one of: ok, off_topic, abusive, personal_info, unsafe_advice")
    reason: str


class AlertDraft(BaseModel):
    title: str = Field(description="Under 8 words, e.g. 'Hot and hazy in Pune today'")
    body: str = Field(description="1-2 friendly sentences for students")
    steps: list[str] = Field(description="Exactly 3 short actions a student can do today, each under 9 words")
    step_emojis: list[str] = Field(description="Exactly 3 emojis, one per step")


class StartersOut(BaseModel):
    starters: list[str] = Field(description="Exactly 3 short conversation starters for a parent")
