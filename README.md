# devops-bitrix

## Installation Setup

- Visit this page and download: `https://www.bitrix24.com/self-hosted/download.php`
- Unzip and put it into `bitrix/www/` from root directory
- Run the following command from the root directory
- Or 
```bash
wget https://www.bitrixsoft.com/download/files/portal/en_bitrix24_encode.zip
unzip -d bitrix/www en_bitrix24_encode.zip
```
- Then from the root directory
```bash

# To start everything
docker compose up -d # detach mode

# To stop all the containers
docker compose down

# Or to start from scratch 
docker compose down -v

```

