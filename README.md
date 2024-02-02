
# FastAPI-Django-App

## [TR]

### FastAPI
- Sürücüleri listeler ve filtreleyebilir.
- SQLAlchemy ile ORM yapısı içermektedir.
- Veritabanı bağlantısı için ".env" içerisindeki URL_DATABASE bilgisine ve TABLE_NAME bilgisine ihtiyaç duymaktadır.
- 1 Endpoint'e sahiptir, sadece GET isteklerine izin verilir.
    - /fetch_drivers

### Django
- FastAPI'den gelen bilgileri görselleştirir.
- Basit bir html tablo yapısına ve filtrelemesine sahiptir.
- .env içerisindeki FASTAPI_URL bilgisine ihtiyaç duymaktadır.
- 2 Endpoint'e sahiptir, GET isteklerine ve formdan gelen POST isteğine izin verilir.
    - '/' -> 'hello world'
    - '/drivers' sürücüleri listeler.

### Nasıl Çalışır?
1. ```pip install -r requirements.txt```
2. Database ve tablo bilgilerini '.env' dosyasına yazın.
3. FastAPI "." dizininde ```uvicorn app.main:app --reload --port 8001``` komutu ile çalıştırılabilir.
4. FastAPI URL bilgisini '.env' dosyasına yazın.
3. Django "." dizininde ```python .\django_gui\manage.py runserver``` komutu ile çalıştırılabilir.

### Django HMTL Görüntüsü için
screenshots klasörüne bakabilirsiniz.

## [EN]

###FastAPI
- Lists drivers and can filter them.
- Contains ORM structure with SQLAlchemy.
- It requires URL_DATABASE information and TABLE_NAME information in ".env" for database connection.
- It has 1 Endpoint, only GET requests are allowed.
     - /fetch_drivers

### Django
- Visualizes information from FastAPI.
- It has a simple HTML table structure and filtering.
- It requires FASTAPI_URL information in .env.
- It has 2 Endpoints, GET requests and POST request from the form are allowed.
     - '/' -> 'hello world'
     - '/drivers' lists drivers.

### How does it work?
1. ```pip install -r requirements.txt```
2. Write the database and table information to the '.env' file.
3. For FastAPI; It can be run in this directory(".") with the command ```uvicorn app.main:app --reload --port 8001```.
4. Write the FastAPI URL information to the '.env' file.
5. For Django; It can be run in this directory(".") with the command ```python .\django_gui\manage.py runserver```.

### For Django HMTL Image
You can look in the screenshots folder.