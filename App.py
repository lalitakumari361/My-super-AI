import streamlit as st
import google.generativeai as genai

# ऐप का नाम और सुंदर लुक
st.set_page_config(page_title="विवेक का सुपर AI", page_icon="🤖")
st.title("🤖 विवेक का सुपर AI ऐप")

# स्ट्रीमलिट की सुरक्षित तिजोरी (Secrets) से API की उठाना
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except Exception as e:
    st.error("ओहो! स्ट्रीमलिट की तिजोरी में API Key नहीं मिली। कृपया उसे Advanced Settings में डालें।")

# टाइप करने के लिए बॉक्स (Input Box)
user_input = st.text_input("यहाँ श्याम (AI) से कुछ भी पूछो विवेक भाई:", placeholder="जैसे: एक मजेदार पहेली सुनाओ!")

# जब तुम कुछ टाइप करोगे और एंटर दबाोगे
if user_input:
    with st.spinner("श्याम सोच रहा है... 🧠"):
        try:
            # गूगल के जेमिनी सर्वर से बात करना
            model = genai.GenerativeModel("gemini-pro")
            response = model.generate_content(user_input)
            
            # एआई का जवाब दिखाना
            st.success("🤖 श्याम का जवाब:")
            st.write(response.text)
        except Exception as e:
            st.error(f"सर्वर से बात करने में कुछ दिक्कत आई: {e}")
