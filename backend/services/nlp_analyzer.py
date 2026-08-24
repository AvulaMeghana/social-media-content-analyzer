import re
from textblob import TextBlob
import textstat


def analyze_content(text: str) -> dict:
    """
    Analyze social media content using basic NLP techniques.
    """

    text = text.strip()

    if not text:
        return {
            "error": "No text provided for analysis."
        }

    # -------------------------
    # Basic text statistics
    # -------------------------

    words = re.findall(r"\b[\w'-]+\b", text)
    word_count = len(words)

    sentences = re.split(r"[.!?]+", text)
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    sentence_count = len(sentences)

    # -------------------------
    # Sentiment analysis
    # -------------------------

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.1:
        sentiment = "Positive"
    elif polarity < -0.1:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    # -------------------------
    # Hashtag extraction
    # -------------------------

    hashtags = re.findall(r"#\w+", text)

    # -------------------------
    # CTA detection
    # -------------------------

    cta_phrases = [
        "buy now",
        "shop now",
        "learn more",
        "try now",
        "try it",
        "click here",
        "sign up",
        "get started",
        "comment below",
        "share your thoughts",
        "tell us",
        "let us know",
        "follow us"
    ]

    text_lower = text.lower()

    detected_ctas = [
        phrase for phrase in cta_phrases
        if phrase in text_lower
    ]

    has_cta = len(detected_ctas) > 0

    # -------------------------
    # Keyword extraction
    # -------------------------

    stop_words = {
        "the", "a", "an", "and", "or", "but",
        "is", "are", "was", "were", "to", "of",
        "in", "on", "for", "with", "this", "that",
        "it", "our", "we", "you", "your", "today"
    }

    keyword_candidates = [
        word.lower()
        for word in words
        if len(word) > 3
        and word.lower() not in stop_words
        and not word.startswith("#")
    ]

    frequency = {}

    for word in keyword_candidates:
        frequency[word] = frequency.get(word, 0) + 1

    keywords = sorted(
        frequency,
        key=frequency.get,
        reverse=True
    )[:10]

    # -------------------------
    # Readability
    # -------------------------

    try:
        readability_score = round(
            textstat.flesch_reading_ease(text),
            2
        )
    except Exception:
        readability_score = None

    # -------------------------
    # Suggestions
    # -------------------------

    suggestions = []

    if word_count > 100:
        suggestions.append(
            "Consider making the post shorter and more concise."
        )

    if word_count < 5:
        suggestions.append(
            "Add more useful or engaging information to the post."
        )

    if not has_cta:
        suggestions.append(
            "Add a clear call-to-action such as 'Learn more', "
            "'Try now', or 'Share your thoughts'."
        )

    if len(hashtags) == 0:
        suggestions.append(
            "Consider adding 2-4 relevant hashtags."
        )
    elif len(hashtags) > 8:
        suggestions.append(
            "Consider reducing the number of hashtags."
        )

    if polarity < -0.3:
        suggestions.append(
            "Consider using a more positive or constructive tone."
        )

    if readability_score is not None and readability_score < 40:
        suggestions.append(
            "Simplify the language to improve readability."
        )

    if not suggestions:
        suggestions.append(
            "The post has a good basic structure. "
            "Consider testing different hooks and calls-to-action."
        )

    # -------------------------
    # Engagement score
    # -------------------------

    score = 50

    if polarity > 0:
        score += 10

    if has_cta:
        score += 15

    if 1 <= len(hashtags) <= 5:
        score += 10

    if 10 <= word_count <= 80:
        score += 10

    if "?" in text:
        score += 5

    score = min(score, 100)

    return {
        "word_count": word_count,
        "sentence_count": sentence_count,
        "sentiment": sentiment,
        "sentiment_polarity": round(polarity, 2),
        "hashtags": hashtags,
        "keywords": keywords,
        "call_to_action": {
            "present": has_cta,
            "detected": detected_ctas
        },
        "readability_score": readability_score,
        "engagement_score": score,
        "suggestions": suggestions
    }