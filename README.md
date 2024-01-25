# Django Cryptocurrency API

This Django project is designed to manage information about cryptocurrencies. It includes models for storing cryptocurrency data, functionality to update data from a cryptocurrency API, and views to display a list of cryptocurrencies and details of a specific cryptocurrency.

## Check it out!

[Cryptocurrency API deployed to DigitalOcean](http://139.59.213.207/cryptocurrencies/)

## Get started

### ⚙️ _Installation_

1. **Clone the repository**:

   ```bash
   git clone https://github.com/YuliaHladyshkevych/cryptocurrency_api.git
   cd cryptocurrency_api
   
2. If you are using PyCharm - it may propose you automatically create venv for your project and install requirements in it, but if not:
   ```bash
   python -m venv venv
   venv\Scripts\activate (on Windows)
   source venv/bin/activate (on macOS)
3. You can open the project in IDE and configure .env file using .env.sample file 
as an example.

   
4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
5. **Apply database migrations:**
   ```bash
   python manage.py migrate
6. **Start the development server:**
   ```bash
   python manage.py runserver

7. **Access the application:**
   Open a web browser and go tohttp://localhost:8000/ 

   The API also is accessible at http://139.59.213.207/cryptocurrencies/

## Features

- **Cryptocurrency Model:** The project includes a robust Cryptocurrency model to store essential information about cryptocurrencies, including name, symbol, current price, market cap, rank, and an image for the logo.
- **API Integration:** The project integrates with the CoinMarketCap API to fetch real-time data about cryptocurrencies, including their current prices, market caps, ranks, and logos.
- **Image Handling and Automatic Deletion:** Cryptocurrency logos are stored as image files, and the project includes a function (cryptocurrency_logo_file_path) to determine the file path for each logo. Utilizes a signal (pre_delete) to automatically delete associated image files when a Cryptocurrency object is deleted.
- **Pagination:** Implements pagination for the list view to enhance user experience, with a default page size of 10 items.


## Preview
![img.png](img.png)