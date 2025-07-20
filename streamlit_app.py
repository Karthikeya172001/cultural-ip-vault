import streamlit as st
from PIL import Image
import random
import time

st.set_page_config(page_title="🎨 Cultural IP Vault", layout="centered")

st.markdown("# 🎨 Cultural IP Vault")
st.markdown("Preserving & Tokenizing Traditional Art with AI + Blockchain (aOS)")

# Tabs for clean UI
tab1, tab2 = st.tabs(["Upload Art", "Mint Preview & Royalties"])

with tab1:
    st.header("🖼️ Upload Traditional Artwork")
    uploaded_file = st.file_uploader("Choose an image of cultural art", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Artwork", use_column_width=True)

        with st.spinner("🧠 Generating cultural metadata using AI..."):
            time.sleep(2)
            # Simulated metadata
            metadata = {
                "Art Form": "Kalamkari",
                "Region": "Andhra Pradesh, India",
                "Theme": "Epics & Nature Motifs",
                "Artist": "Lakshmi Devi (Simulated)",
                "Cultural Significance": "Used in storytelling rituals and temple art",
            }

        st.success("✅ Metadata generated!")
        for key, value in metadata.items():
            st.write(f"**{key}**: {value}")

        st.session_state.metadata = metadata
        st.session_state.art_uploaded = True

with tab2:
    if st.session_state.get("art_uploaded"):
        st.header("🔗 Mint Preview")
        if st.button("🚀 Simulate Mint NFT on aOS"):
            token_id = f"0x{random.randint(1000, 9999):04x}"
            st.success(f"NFT Minted! Token ID: `{token_id}` (Simulated via CW721 ADO)")

            st.subheader("💰 Royalty Distribution (via Conditional Splitter ADO)")
            st.write("""
            - 👩‍🎨 50% to Original Artist  
            - 🏛️ 30% to Local Cultural Trust  
            - 🌐 20% to Global Cultural IP Fund
            """)

            st.markdown("---")
            st.subheader("🌍 Simulated aOS Marketplace Publishing")
            st.button("📤 Publish NFT (Placeholder)")

    else:
        st.info("Please upload art and generate metadata in the first tab.")