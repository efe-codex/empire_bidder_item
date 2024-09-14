# Empire Bidding Bot

**Use at Your Own Risk**

This bot automatically bids on Empire for items you've specified.

---

## Table of Contents

1. [Installation](#installation)
2. [Enter Price Data](#enter-price-data)
3. [Configure Settings](#configure-settings)
4. [Run the Client](#run-the-client)
5. [How It Works](#how-it-works)
6. [Support & Appreciation](#support--appreciation)

---

## Installation

### 0. Download Files and Install Dependencies

Download the project files, install Python, and then install the required modules as described in [HOW TO INSTALL](HOWTOINSTALL.md).

---

## Enter Price Data

### 1. Edit Item Prices

Open `items_editor.py` to edit the `items.json` file. Add items by full name like:
- "Glock-18 | Water Elemental (Battle-Scarred)"
- "★ Flip Knife | Doppler (Factory New)"

---

## Configure Settings

### 2. Update Configuration

Edit the `config.json` file to match your desired settings. Below is a sample configuration:

```json
{
    "empireapi": "",              // Your API key
    "domain": "csgoempire.tv",    // Use .com or another domain
    "local_excel": false,         // Track bought items locally (ensure Excel is closed)
    "online_excel": false,        // Use online Excel tracking
    "sheet_file_name": "",
    "sheet_id": "",
    "bid_timer": 3.5              // Time between bids
}
```

---

## Run the Client

### 3. Start Bidding

Once you've updated the `config.json`, run the client to start bidding.

---

## How It Works

You enter the item names and their maximum prices. The bot will bid on these items until the specified price is reached.

---

## Support & Appreciation

If you find this project helpful, a +rep on my [CSGO profile](https://csgo-rep.com/profile/76561198822180159) would be greatly appreciated!

If you'd like to tip, any contribution is welcome:

- **BTC:** `bc1qc2r2up4ejy38smzjexnvqsss2wru4cry6499al`
- **ETH:** `0xCd1817B35982CEaD471951606A040ea815D5DcD0`
- **TRX (TRON):** `TENCbtD3yqPJMhwPBLcLKZQSLAyGFgV7et`
- **LTC:** `ltc1qsz0lrn9myt5sxymr8vnrwa059shqlsj3anpupg`
- **POLYGON:** `0xCd1817B35982CEaD471951606A040ea815D5DcD0`
- **BNB:** `0xCd1817B35982CEaD471951606A040ea815D5DcD0`

Thank you for your support!

---