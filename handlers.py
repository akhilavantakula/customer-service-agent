from rag import search_knowledge_base

def handle_technical(inquiry):
    return search_knowledge_base(inquiry)

def handle_feature(inquiry):
    return "Thank you for your suggestion! We've logged your feature request."

def handle_sales(inquiry):
    return "Thanks for your interest! Our sales team will contact you shortly."

def handle_escalation(inquiry):
    return "We're escalating your request to our support team."