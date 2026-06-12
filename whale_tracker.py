# Install data visualization libraries if needed
!pip install web3 matplotlib seaborn

import matplotlib.pyplot as plt
import seaborn as sns
from web3 import Web3

# 🔑 PASTE YOUR ALCHEMY HTTPS ENDPOINT URL INSIDE THE QUOTES BELOW:
ALCHEMY_URL = "https://alchemy.com"

def run_data_pipeline():
    # Connect to the Ethereum Node
    w3 = Web3(Web3.HTTPProvider(ALCHEMY_URL))
    
    if not w3.is_connected():
        print("❌ Connection error. Please verify your Alchemy link.")
        return

    print("📡 PIPELINE ACTIVE: Fetching block details...")
    
    # Target the block you successfully analyzed
    target_block = 25300762
    block = w3.eth.get_block(target_block, full_transactions=True)
    transactions = block.get('transactions', [])
    
    print(f"📊 Processing {len(transactions)} transactions from Block #{target_block}...\n")
    
    # Data storage arrays for analytics
    all_values_eth = []
    whale_values = []
    WHALE_THRESHOLD = 0.01
    
    # Process transactions
    for tx in transactions:
        eth_value = float(w3.from_wei(tx['value'], 'ether'))
        all_values_eth.append(eth_value)
        
        if eth_value >= WHALE_THRESHOLD:
            whale_values.append(eth_value)
            
    print(f"✅ ANALYSIS COMPLETE: Isolated {len(whale_values)} whale transfers.")
    
    # --- VISUALIZATION LAYER ---
    print("🎨 Generating data visualization chart...")
    
    # Set professional style aesthetics
    sns.set_theme(style="darkgrid")
    plt.figure(figsize=(10, 6))
    
    # Create a distribution plot for whale transactions
    # Limiting x-axis slightly so extreme outlier 'whales' don't skew the chart view
    plot_data = [v for v in whale_values if v <= 2.0] 
    
    sns.histplot(plot_data, bins=20, kde=True, color="#627EEA", edgecolor="white")
    
    # Labels and Titles
    plt.title(f"Distribution of High-Value Transfers (Block #{target_block})", fontsize=14, fontweight='bold', pad=15)
    plt.xlabel("Transaction Value (ETH)", fontsize=12, labelpad=10)
    plt.ylabel("Number of Concurrent Transactions", fontsize=12, labelpad=10)
    
    # Add an indicator line for our threshold
    plt.axvline(x=WHALE_THRESHOLD, color='#FF4A4A', linestyle='--', linewidth=1.5, label=f'Whale Threshold ({WHALE_THRESHOLD} ETH)')
    plt.legend()
    
    # Save the chart as a image file for your portfolio
    plt.savefig('blockchain_whale_distribution.png', dpi=300, bbox_inches='tight')
    print("💾 SUCCESS: Chart saved locally as 'blockchain_whale_distribution.png'!")
    plt.show()

# Execute the pipeline
run_data_pipeline()
