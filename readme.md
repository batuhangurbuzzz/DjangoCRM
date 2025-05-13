# DjangoCRM

## 🇹🇷 Türkçe Açıklama

**DjangoCRM**, müşteri ilişkileri yönetimi (CRM) amacıyla geliştirilmiş, modüler ve genişletilebilir bir Django tabanlı web uygulamasıdır. Bu proje, modern web geliştirme standartlarına uygun olarak yapılandırılmıştır ve güçlü bir veritabanı altyapısıyla desteklenmektedir.

### 🚀 Özellikler

- Django 5.2.1 ile geliştirilmiş sağlam altyapı
- Ortam değişkenleri ile güvenli yapılandırma (`django-environ`)
- MySQL veritabanı desteği (MySQL Connector, mysqlclient, PyMySQL)
- Ölçeklenebilir ve esnek yapı
- Geliştirici dostu proje yapısı

### 🛠️ Kullanılan Teknolojiler

| Teknoloji              | Sürüm     | Açıklama |
|------------------------|-----------|----------|
| Python                 | 3.12+     | Proje geliştirme dili |
| Django                 | 5.2.1     | Web uygulama çatısı |
| django-environ         | 0.12.0    | Ortam değişkenlerini yönetmek için |
| mysql-connector-python | 9.3.0     | MySQL bağlantısı için resmi kütüphane |
| mysqlclient            | 2.2.7     | Django’nun MySQL ile çalışması için önerilen sürücü |
| PyMySQL                | 1.1.1     | Alternatif bir MySQL istemcisi |
| sqlparse               | 0.5.3     | SQL ayrıştırma için |
| tzdata                 | 2025.2    | Zaman dilimi verisi |
| asgiref                | 3.8.1     | Django ASGI uyumluluğu için |

> Not: `mysql`, `mysql-connector` gibi bazı paketler genellikle `mysql-connector-python` yerine önerilmez. Gereksiz olanları ileride temizleyebilirsiniz.

### 🔧 Kurulum

1. **Proje deposunu klonlayın**:

```bash
git clone https://github.com/kullanici_adi/DjangoCRM.git
cd DjangoCRM
```

2. **Sanal ortam oluşturun ve etkinleştirin**:

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

3. **Bağımlılıkları yükleyin**:

```bash
pip install -r requirements.txt
```

4. **Ortam değişkenlerini ayarlayın**:

Proje kök dizinine `.env` dosyası oluşturun ve en az şu satırı ekleyin:

```env
SECRET_KEY=django-insecure-xyz123...
DEBUG=True
```

5. **Veritabanını oluşturun ve migrasyonları uygulayın**:

```bash
python manage.py migrate
```

6. **Geliştirme sunucusunu başlatın**:

```bash
python manage.py runserver
```

---

## 🇬🇧 English Description

**DjangoCRM** is a modular and extensible CRM (Customer Relationship Management) web application built with Django. Designed for modern development practices, it provides a secure and scalable backend architecture powered by MySQL.

### 🚀 Features

- Robust backend built with Django 5.2.1
- Secure configuration via environment variables (`django-environ`)
- MySQL database support (MySQL Connector, mysqlclient, PyMySQL)
- Scalable and flexible architecture
- Developer-friendly structure

### 🛠️ Technologies Used

| Technology             | Version   | Description |
|------------------------|-----------|-------------|
| Python                 | 3.12+     | Programming language |
| Django                 | 5.2.1     | Web framework |
| django-environ         | 0.12.0    | Environment variable management |
| mysql-connector-python | 9.3.0     | Official MySQL connector |
| mysqlclient            | 2.2.7     | Recommended driver for Django with MySQL |
| PyMySQL                | 1.1.1     | Alternative MySQL client |
| sqlparse               | 0.5.3     | SQL parsing tool |
| tzdata                 | 2025.2    | Timezone data |
| asgiref                | 3.8.1     | ASGI support for Django |

> Note: Packages like `mysql` and `mysql-connector` are generally not recommended over `mysql-connector-python`. You may consider cleaning them up in the future.

### 🔧 Setup

1. **Clone the repository**:

```bash
git clone https://github.com/your_username/DjangoCRM.git
cd DjangoCRM
```

2. **Create and activate a virtual environment**:

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

4. **Configure environment variables**:

Create a `.env` file in the project root directory with at least the following:

```env
SECRET_KEY=django-insecure-xyz123...
DEBUG=True
```

5. **Apply migrations**:

```bash
python manage.py migrate
```

6. **Start the development server**:

```bash
python manage.py runserver
```

---

## 📄 License

This project is developed for personal use. A detailed license will be added later.
