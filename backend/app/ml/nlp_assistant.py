class NLPAssistant:
    def __init__(self):
        # Placeholder for LangChain / Llama.cpp / RAG setup
        pass

    def chat(self, user_query: str, history: list, financial_context: dict):
        """
        Simulate an LLM response using simple intent matching for now.
        Production will use a localized LLM with RAG pipeline.
        """
        query = user_query.lower()
        savings = financial_context.get("savings", 0)
        
        # Check if history implies ongoing context
        if len(history) > 1 and "trip" in query:
             return "Since we were just talking about your finances, a trip might set you back. I still advise building the emergency fund first!"
        
        if "laptop" in query or "trip" in query or "afford" in query:
            if savings > 50000:
                return "Based on your current savings of ₹" + str(savings) + ", you can afford this. However, it's recommended to save up for 2 more months to avoid dipping into your emergency fund."
            else:
                return "Your current savings are ₹" + str(savings) + ". It's better to postpone this purchase and focus on building your emergency fund first."
        
        if "reduce expenses" in query:
            return "Looking at your breakdown, you are spending heavily on Shopping. Try setting a strict limit for non-essential purchases this month."
            
        return "I am FinVerse AI, your personal financial advisor. I am still learning how to process complex queries, but I can help you analyze your budget, anomalies, and goals!"

nlp_assistant = NLPAssistant()
