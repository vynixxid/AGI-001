function speak(text) {
  const synth = window.speechSynthesis;
  const voice = synth.getVoices().find(v => v.name.includes("Google UK English Female"));
  const utter = new SpeechSynthesisUtterance(text);
  utter.voice = voice;
  utter.pitch = 1.8; // Suara lebih tinggi seperti bayi
  utter.rate = 1.4;
  synth.speak(utter);
}
