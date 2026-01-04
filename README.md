# 🩺 AI Doctor – Medical Chatbot with Vision & Voice

An intelligent **AI-powered Medical Chatbot** that can **see, listen, and respond**. This project demonstrates how to build a personalized **AI Doctor voice assistant** using cutting-edge **open-source multimodal AI models** for medical question answering, image analysis, and voice interaction.

The system combines **vision**, **speech**, and **text-based reasoning** to provide informative and context-aware medical responses.

---

## 🚀 Features

* 🧠 **Medical Question Answering** using a large language model
* 👁️ **Image Understanding (Vision)** for analyzing medical images or symptoms
* 🎙️ **Voice Input Support** using speech-to-text
* 🗣️ **Conversational Responses** in natural language
* 🌐 **Web-based Interface** for easy interaction
* 📄 **Multi-modal Support** (Text + Image + Voice)

---

## 🛠️ Technologies Used

### 🤖 AI Models

* **Meta Llama 3 Vision 90B**

  * Multimodal LLM for advanced image and text understanding
* **Whisper (OpenAI)**

  * High-accuracy speech-to-text conversion

### 💻 Backend & Frameworks

* **Python**
* **FastAPI / Flask** (API layer)
* **Gradio** (Web UI for chatbot interaction)

### 📦 Supporting Libraries

* OpenCV / PIL (Image processing)
* NumPy
* Torch / Transformers
* Speech Recognition utilities

---

## 📌 How It Works

1. **User Input**

   * Text query, voice input, or medical image upload

2. **Speech Processing (Optional)**

   * Voice input is converted to text using **Whisper**

3. **Vision + Language Processing**

   * Images and text are processed by **Meta Llama 3 Vision 90B**

4. **Medical Response Generation**

   * The AI analyzes the input and generates a contextual medical response

5. **Chatbot Output**

   * Response is displayed via a web interface (and can be extended to voice output)

---

## 📂 Project Structure

```
AI_Doctor_Chatbot/
│
├── app.py / gradio_app.py        # Main application
├── brain_of_the_doctor.py        
├── voice_of_the patient.py             
├── README.md                     # Project documentation
└── assets/                       # Sample images / audio files
|__ voice_Of_the_doctor.py
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/ai-doctor-chatbot.git
cd ai-doctor-chatbot
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
python gradio_app.py
```

The chatbot will launch in your browser.

---

## ⚠️ Medical Disclaimer

> This AI Doctor chatbot is **for educational and informational purposes only**.
> It is **not a substitute for professional medical advice, diagnosis, or treatment**.
> Always consult a qualified healthcare professional for medical concerns.






