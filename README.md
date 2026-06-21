import streamlit as st
import google.generativeai as genai
import requests
from io import BytesIO
from PIL import Image

# --- 1. ऐप का सुंदर हेडर और थीम सेट करना ---
st.set_page_config(page_title="विवेक का सुपर AI", page_icon="🤖", layout="centered")

# मुख्य टाइटल (जो सबसे ऊपर चमकेगा)
st.title("🤖 विवेक का अपना दो-इन-वन AI ऐप")
st.markdown("---") # एक पतली सुंदर लाइन

# --- 2. तुम्हारी जेमिनी API की चाबी और नया मॉडल (2.5) ---
GOOGLE_API_KEY =

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash') # एकदम नया मॉडल जो एरर नहीं देगा!

# --- 3. साइडबार मेनू (Menu) ---
st.sidebar.image("https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=500", use_container_width=True)
st.sidebar.title("⚙️ मेनु")
option = st.sidebar.radio("आपको क्या करना है?", ["💬 AI से सवाल पूछें", "🎨 AI से फोटो बनवाएँ"])

# --- फीचर 1: सवाल-जवाब (Chat Room) ---
if option == "💬 AI से सवाल पूछें":
    st.subheader("💬 चैट रूम (Chat with AI)")
    user_question = st.text_input("अपना सवाल यहाँ टाइप करें (जैसे: बनाना शेक की रेसिपी):")
    
    if st.button("✨ जवाब ढूँढो", type="primary"): # नीले रंग का सुंदर बटन
        if user_question:
            with st.spinner("🧠 AI सोच रहा है, कृपया थोड़ा रुकें..."):
                try:
                    response = model.generate_content(user_question)
                    st.success("💡 AI का जवाब:")
                    st.info(response.text) # सुंदर बॉक्स में जवाब
                except Exception as e:
                    st.error(f"❌ गड़बड़ हुई: {e}")
        else:
            st.warning("⚠️ भाई, पहले कुछ टाइप तो करो!")

# --- फीचर 2: फोटो जनरेटर (Image Generator) ---
elif option == "🎨 AI से फोटो बनवाएँ":
    st.subheader("🎨 मैजिक फोटो जनरेटर")
    image_prompt = st.text_input("कैसी फोटो चाहिए? विस्तार से लिखें (जैसे: चेस खेलता हुआ रोबोट):")
    
    if st.button("🚀 फोटो बनाओ", type="primary"):
        if image_prompt:
            with st.spinner("🎨 AI पेंटिंग बना रहा है..."):
                try:
                    encoded_prompt = requests.utils.quote(image_prompt)
                    image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}"
                    
                    response = requests.get(image_url)
                    if response.status_code == 200:
                        img = Image.open(BytesIO(response.content))
                        
                        # ऐप की स्क्रीन पर बड़ी और सुंदर फोटो दिखाना
                        st.image(img, caption=f"आपकी कल्पना: {image_prompt}", use_container_width=True)
                        
                        # डाउनलोड बटन ताकि दोस्त गैलरी में सेव कर सकें
                        buf = BytesIO()
                        img.save(buf, format="JPEG")
                        byte_im = buf.getvalue()
                        st.download_button(label="📥 फोटो डाउनलोड करें", data=byte_im, file_name="vivek_ai_image.jpg", mime="image/jpeg")
                    else:
                        st.error("❌ फोटो नहीं बन पाई।")
                except Exception as e:
                    st.error(f"❌ दिक्कत आई: {e}")
        else:
            st.warning("⚠️ कृपया पहले बताएं कि कैसी फोटो बनानी है!")
