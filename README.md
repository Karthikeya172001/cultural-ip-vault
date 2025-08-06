# 🎭 Cultural IP Vault

Preserving & Tokenizing Traditional Art using AI + Blockchain (aOS)

This project is built for the **Andromeda Hackathon – Data Retrieval Task**, combining the power of the **App Builder** (aOS) and a **Python frontend** for a complete simulation of minting cultural NFTs.

---

## 📂 What's Included

| File                      | Description                                                |
|---------------------------|------------------------------------------------------------|
| `cultural-ip-vault.flex`  | Exported App Builder file (.flex) for NFT + Reader Panel   |
| `app.py`                  | Streamlit app for uploading cultural artwork + minting NFT |
| `screenshot.png` (opt)    | UI preview screenshot                                      |

---

## 🎨 Features

### 🔧 aOS Builder (via `.flex` file)
- NFT Creation Panel (CW721 ADO)
- Metadata Reader Panel (displays name, symbol, owner, tokenURI)

### 🧠 Streamlit App
- Upload traditional cultural artwork
- Simulated AI-generated metadata (Art form, Region, Artist, Significance)
- Simulated NFT Minting using CW721 ADO logic
- Simulated Royalty Distribution using Conditional Splitter ADO
- Placeholder: Publish to aOS Marketplace

---

## 🚀 How to Run the Frontend

If you'd like to test the simulation locally, run:

```bash
pip install streamlit pillow
streamlit run app.py
