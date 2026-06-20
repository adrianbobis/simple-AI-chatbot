const input = document.getElementById("messageInput");

const button = document.getElementById("sendButton");

const chatWindow = document.getElementById("chatWindow");

button.onclick = sendMessage;

input.addEventListener("keypress", function (event) {
  if (event.key === "Enter") {
    sendMessage();
  }
});

async function sendMessage() {
  const message = input.value.trim();

  if (!message) return;

  addMessage(message, "user");

  input.value = "";

  addMessage("Analyzing...", "bot", "loading");

  try {
    const player = getSelectedPlayer();

    const result = await sendChatRequest(message, player);

    removeLoading();

    addMessage(result.answer, "bot");
  } catch (error) {
    removeLoading();

    addMessage("Server connection error.", "bot");
  }
}

function addMessage(text, sender, extra = "") {
  const div = document.createElement("div");

  div.className = `message ${sender} ${extra}`;

  div.innerHTML = `
        <div class="bubble">
            ${text}
        </div>
    `;

  chatWindow.appendChild(div);

  chatWindow.scrollTop = chatWindow.scrollHeight;
}

function removeLoading() {
  const loading = document.querySelector(".loading");

  if (loading) {
    loading.remove();
  }
}
