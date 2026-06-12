# Ethereum Real-Time Enterprise Data Pipeline

A production-ready Python data pipeline that interfaces with the Ethereum Mainnet via an enterprise Alchemy RPC node. This system captures live cryptographic block payloads, decodes transaction arrays, and applies conditional filters to track high-value asset movements in real-time.

## 🚀 Features
- **Live Node Synchronization**: Establishes secure, stateful connections to distributed ledger infrastructure.
- **Payload Unpacking**: Parses raw, nested block receipts containing over 700+ concurrent transactions.
- **Whale Alert System**: Implements high-speed conditional filtering to isolate micro-transactions from macro-asset transfers.

## 🛠️ Tech Stack
- **Language**: Python 3
- **Network Interface**: Web3.py (Enterprise Blockchain Layer)
- **Infrastructure Provider**: Alchemy RPC Node Gateway

## 💻 Code Architecture
The core pipeline connects to the Mainnet gateway, downloads target blocks, and iterates through individual transactions to compute live network statistics:

```python
# Core logic snippet
block = w3.eth.get_block(target_block, full_transactions=True)
for tx in block.get('transactions', []):
    eth_value = w3.from_wei(tx['value'], 'ether')
    if eth_value >= WHALE_THRESHOLD_ETH:
        # Trigger real-time alert pipeline
```

## 📊 Live Execution Output
```text
📡 SCANNER ACTIVE: Monitoring the Ethereum network...
🔍 Found 731 active transactions inside Block #25300762
🚨 ALERT: Whale Movement Detected!
   💰 Value: 0.2010 ETH
📊 SCAN COMPLETE: Found 62 transactions larger than 0.01 ETH.
```

## 🔒 Security Compliance
- Uses environment variables for API key isolation.
- Zero hardcoded production secrets in version control.
