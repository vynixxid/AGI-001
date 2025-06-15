const chatBox = document.getElementById("chatBox");
const userInput = document.getElementById("userInput");

function sendMessage() {
  const input = userInput.value.trim();
  if (!input) return;

  // Tampilkan pertanyaan pengguna
  const userEntry = document.createElement("div");
  userEntry.className = "chat-entry user";
  userEntry.textContent = input;
  chatBox.appendChild(userEntry);

  // Jawaban AI (dummy)
  const aiEntry = document.createElement("div");
  aiEntry.className = "chat-entry ai";
  aiEntry.textContent = generateAIResponse(input);
  chatBox.appendChild(aiEntry);

  userInput.value = "";
  chatBox.scrollTop = chatBox.scrollHeight;
}

function generateAIResponse(input) {
  // Simulasi jawaban pintar
  return `Ini adalah respons dari BabyAGI untuk: "${input}"`;
}

userInput.addEventListener("keydown", function (e) {
  if (e.key === "Enter") sendMessage();
});
