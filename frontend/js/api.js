const API_URL = "http://localhost:8000/chat";

async function sendChatRequest(message, selectedPlayer) {
  const response = await fetch(API_URL, {
    method: "POST",

    headers: {
      "Content-Type": "application/json",
    },

    body: JSON.stringify({
      message: message,

      selected_player: selectedPlayer,
    }),
  });

  return await response.json();
}
