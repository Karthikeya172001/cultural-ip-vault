{
    "app_name": "Cultural IP Vault",
    "panels": [
        {
            "type": "nft_creator",
            "id": "panel_nft_creator",
            "config": {
                "name": "Cultural Artifact",
                "symbol": "CULTIP",
                "metadata_uri": "ipfs://example-metadata-uri"
            },
            "position": {
                "x": 100,
                "y": 100
            }
        },
        {
            "type": "nft_reader",
            "id": "panel_nft_reader",
            "config": {
                "contract_address": "andromeda1xyz...mock",
                "read_fields": [
                    "name",
                    "symbol",
                    "owner",
                    "tokenURI"
                ]
            },
            "position": {
                "x": 400,
                "y": 100
            }
        }
    ],
    "metadata": {
        "created_by": "Karthikeya172001",
        "created_at": "2025-08-06",
        "description": "Sample app to demonstrate NFT creation and metadata retrieval"
    }
}