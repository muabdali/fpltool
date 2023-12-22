async def handle_response(message: str) -> str:
    f_message = message.lower()
    
    if f_message == 'foo':
        return "bar"
    
    if f_message == 'solanke-goals':
        return str(6)
    
    # If the command is !solanke_goals
    if f_message == '!solanke_goals':
        print("3")
        return "6"
    
    return ""  # Return an empty string if no matching condition is met
