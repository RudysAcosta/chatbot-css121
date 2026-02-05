<template>
  <div class="page">
    <header class="hero">
      <div class="hero-inner">
        <p class="tag">CSC 121 · Essex County College</p>
        <h1>Simple Chatbot</h1>
        <p class="lead">
          A small university project built with Python, Flask, and Vue.
        </p>
      </div>
    </header>

    <main class="main">
      <section class="card chat">
        <div class="chat-header">
          <h2>Chat</h2>
          <p>Ask about the weather, a joke, or say hello.</p>
        </div>

        <div class="chat-body" ref="chatBody">
          <div
            v-for="(msg, i) in messages"
            :key="i"
            :class="['bubble', msg.role]"
          >
            <span class="label">{{ msg.roleLabel }}:</span>
            <span class="text">{{ msg.text }}</span>
          </div>

          <div v-if="isLoading" class="bubble bot">
            <span class="label">Bot:</span>
            <span class="text">Typing...</span>
          </div>
        </div>

        <form class="chat-input" @submit.prevent="sendMessage">
          <input
            v-model="input"
            type="text"
            placeholder="Type your message..."
            autocomplete="off"
          />
          <button type="submit" :disabled="!input.trim() || isLoading">
            Send
          </button>
        </form>
      </section>
    </main>
  </div>
</template>

<script setup>
import { onMounted, nextTick, ref } from "vue";

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:5000/chat";
const API_KEY = import.meta.env.VITE_API_KEY || "";

const input = ref("");
const isLoading = ref(false);
const chatBody = ref(null);

const messages = ref([
  {
    role: "bot",
    roleLabel: "Bot",
    text: "Hello! I am your chatbot. How can I assist you today?",
  },
]);

const scrollToBottom = async () => {
  await nextTick();
  if (chatBody.value) {
    chatBody.value.scrollTop = chatBody.value.scrollHeight;
  }
};

const sendMessage = async () => {
  const text = input.value.trim();
  if (!text) return;

  messages.value.push({ role: "user", roleLabel: "You", text });
  input.value = "";
  isLoading.value = true;
  await scrollToBottom();

  try {
    const res = await fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "x-api-key": API_KEY,
      },
      body: JSON.stringify({ message: text }),
    });

    const data = await res.json();
    messages.value.push({
      role: "bot",
      roleLabel: "Bot",
      text: data.response || data.error || "No response from server.",
    });
  } catch (err) {
    messages.value.push({
      role: "bot",
      roleLabel: "Bot",
      text: "Error: Could not reach the API.",
    });
  } finally {
    isLoading.value = false;
    await scrollToBottom();
  }
};

onMounted(scrollToBottom);
</script>
