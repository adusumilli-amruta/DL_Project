css = '''
<style>
/* Full page background */
body {
    background: linear-gradient(to right, #6a11cb, #2575fc); /* Add gradient background */
    background-attachment: fixed; /* Keeps the background static while scrolling */
    color: white;
    margin: 0;
    padding: 0;
    font-family: 'Arial', sans-serif;
}

/* Header with shadow effect */
.chat-header {
    text-align: center;
    padding: 20px;
    font-size: 2rem;
    font-weight: bold;
    color: white;
    background: rgba(0, 0, 0, 0.8);
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.3);
}

/* Chat history container with translucent effect */
.chat-history {
    max-height: 60vh;
    overflow-y: auto;
    padding: 20px;
    margin: 20px auto;
    width: 85%;
    background: rgba(255, 255, 255, 0.1); /* Translucent effect */
    border-radius: 12px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

/* Chat bubbles */
.chat-message {
    display: flex;
    align-items: flex-start;
    margin-bottom: 15px;
}

/* Align user and bot messages */
.chat-message.user {
    flex-direction: row-reverse;
}

.chat-message.user .message {
    background: linear-gradient(135deg, #6a11cb, #2575fc);
    color: white;
}

.chat-message.bot .message {
    background: rgba(255, 255, 255, 0.8); /* Light translucent bot message */
    color: #333;
}

/* Avatar styling */
.chat-message .avatar {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    overflow: hidden;
    margin: 0 10px;
    display: flex;
    justify-content: center;
    align-items: center;
    background: #f0f0f0;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.chat-message .avatar img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

/* Message bubble */
.chat-message .message {
    padding: 15px;
    border-radius: 18px;
    max-width: 70%;
    font-size: 0.95rem;
    line-height: 1.4;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
}

/* Input container */
.input-container {
    position: sticky;
    bottom: 0;
    padding: 15px 20px;
    background: rgba(0, 0, 0, 0.9);
    box-shadow: 0px -2px 4px rgba(0, 0, 0, 0.3);
}

.input-container input {
    width: calc(100% - 100px);
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 25px;
    outline: none;
    margin-right: 10px;
    font-size: 1rem;
}

.input-container input:focus {
    border-color: #6a11cb;
}

.input-container button {
    background: linear-gradient(135deg, #6a11cb, #2575fc);
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 25px;
    font-size: 1rem;
    cursor: pointer;
    transition: background 0.3s ease;
}

.input-container button:hover {
    background: linear-gradient(135deg, #2575fc, #6a11cb);
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://cdn-icons-png.flaticon.com/512/4712/4712104.png" alt="Bot Avatar">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://cdn-icons-png.flaticon.com/512/706/706830.png" alt="User Avatar">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''
